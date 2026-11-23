---
title: "frontend/src/cockpit/runStore.js"
noindex: true
---

```js
/* ==========================================================================
   runStore — the cockpit's single state owner (boards 02/04/07).

   One run per cockpit. The store owns the run lifecycle (create → prepare →
   start, idempotency-keyed, retry-safe), the statistical workbench with its
   dirty-hash gate, preflight, findings (read · ask · data) and the overlay
   trail. Steps are layout-only components that inject this store.
   ========================================================================== */

import { computed, nextTick, reactive, ref, watch } from 'vue'
import {
  chatWithSimulationReport,
  compareSimulations,
  createSimulation,
  evaluatePreflight,
  findSimulationStatus,
  generateSimulationReport,
  getReportGenerationJob,
  getCatalog,
  getSimulationGraph,
  getSimulationReport,
  getSimulationStatus,
  getStatisticalConfig,
  getStatisticalLineage,
  getStatisticalVariants,
  getStatisticalManifest,
  listUseCases,
  parseScenarioSeed,
  patchStatisticalConfig,
  prepareSimulation,
  reseedStatisticalConfig,
  runSensitivity,
  startSimulation
} from '../api/useCases.js'
import { preferredGraphFromPayloads, manifestGraph } from './graphAdapter.js'
import { readDraft, setDraft } from './draftStore.js'
import {
  findLaneManifest,
  getLaneManifest,
  laneIds,
  laneIdsFromManifests,
  laneManifests,
  laneManifestsFromIndex,
  mergeLaneManifest
} from './manifestRegistry.js'
import { cockpitTimeline } from './monitorAdapter.js'
import { collectEvidenceRefs, collectReportClaims, validityFlagsMap as buildValidityFlagsMap } from './reportAdapter.js'

export const RUN_STORE_KEY = 'rawfish:run-store'

/* The six steps (board 04). Findings carries read | ask | data modes. */
export const SPEC_STEPS = [
  { id: 'scenario', num: '01', label: 'Scenario' },
  { id: 'build', num: '02', label: 'Build' },
  { id: 'cohorts', num: '03', label: 'Cohorts' },
  { id: 'preflight', num: '04', label: 'Preflight' },
  { id: 'simulate', num: '05', label: 'Simulate' },
  { id: 'findings', num: '06', label: 'Findings' }
]

export const FINDINGS_MODES = ['read', 'ask', 'data']

/* Phase words are fixed vocabulary (board 12): draft · prepared · running ·
   halted · complete · reported. Backend phases map onto them; halted is an
   interruption, not a phase. */
export function displayPhase (backendPhase, hasRun) {
  if (!hasRun) return 'draft'
  const map = {
    created: 'draft',
    prepared: 'prepared',
    starting: 'running',
    running: 'running',
    failed: 'halted',
    completed: 'complete',
    reported: 'reported'
  }
  return map[backendPhase] || backendPhase || 'draft'
}

const RUN_INDEX_KEY = 'rawfish.runs'

export function createRunStore (props, router, route) {
  let localDraft = props.runId ? null : readDraft()
  let createdFromDraftRunId = null
  /* ------------------------------------------------------------------ lane */
  const discoveredLaneManifests = ref(laneManifests)
  const registeredLaneIds = computed(() => laneIdsFromManifests(discoveredLaneManifests.value))
  const selectedLaneId = ref(props.runId ? null : (localDraft?.lane || props.lane || registeredLaneIds.value[0] || laneIds[0] || null))
  const backendCatalog = ref(null)
  const catalogError = ref('')

  const manifest = computed(() => {
    const indexed = selectedLaneId.value
      ? discoveredLaneManifests.value.find(lane => lane?.lane_id === selectedLaneId.value) || null
      : null
    const staticManifest = indexed || (selectedLaneId.value ? getLaneManifest(selectedLaneId.value) : null)
    return mergeLaneManifest(selectedLaneId.value, backendCatalog.value?.lane_manifest || staticManifest)
  })

  /* ------------------------------------------------------------------- run */
  const activeRunId = computed(() => props.runId || null)
  const statusPayload = ref(null)
  const lifecycleError = ref('')
  const isHydrating = ref(false)
  const isBusy = ref(false)
  const statusPollTimer = ref(null)

  const backendPhase = computed(() => (
    statusPayload.value?.phase || statusPayload.value?.status || (activeRunId.value ? 'unknown' : null)
  ))
  const phase = computed(() => displayPhase(backendPhase.value, Boolean(activeRunId.value)))
  const isStreaming = computed(() => ['starting', 'running'].includes(backendPhase.value))
  const isHalted = computed(() => backendPhase.value === 'failed')
  const isFrozen = computed(() => (
    ['starting', 'running', 'failed', 'completed', 'reported'].includes(backendPhase.value)
  ))
  const frozenReason = 'recipe frozen · duplicate as draft to edit'

  /* -------------------------------------------------------------- scenario */
  const scenarioText = ref(localDraft?.text || '')
  const sourceModes = [
    { id: 'paste', label: 'paste' },
    { id: 'cached', label: 'cached' },
    { id: 'live', label: 'live marker' },
    { id: 'graph', label: 'prepared graph' }
  ]
  const sourceMode = ref(localDraft?.source || 'paste')
  const scenarioParse = ref(localDraft?.preview || null)
  const parseLoading = ref(false)
  const parseError = ref('')

  /* ----------------------------------------------------------- statistical */
  const statisticalPayload = ref(null)
  const statisticalConfig = ref(null)
  const statisticalSettings = reactive({})
  const statisticalError = ref('')
  const statisticalVariantsPayload = ref(null)
  const statisticalLineagePayload = ref(null)
  const statisticalDirty = ref(false)
  const statisticalSaveLoading = ref(false)
  const statisticalReseedLoading = ref(false)
  const statisticalVariantError = ref('')
  const selectedCohortId = ref('')

  /* ------------------------------------------------------------- preflight */
  const preflight = reactive({ ensemble_n: 5, rounds: 16 })
  const provider = reactive({
    mode: findLaneManifest(props.lane || registeredLaneIds.value[0] || laneIds[0])?.default_provider?.mode || 'local_ollama',
    model: findLaneManifest(props.lane || registeredLaneIds.value[0] || laneIds[0])?.default_provider?.model || 'qwen3-coder:30b',
    provider: '',
    base_url: '',
    probe_provider: true
  })
  const preflightLoading = ref(false)
  const preflightPayload = ref(null)
  const preflightError = ref('')

  /* ------------------------------------------------------------------ graph */
  const graphPayload = ref(null)
  const graphError = ref('')

  /* --------------------------------------------------------------- findings */
  const reportPayload = ref(null)
  const reportError = ref('')
  const reportNotice = ref('')
  const askInput = ref('')
  const askHistory = ref([])
  const askError = ref('')
  const askSending = ref(false)
  const analysisComparePayload = ref(null)
  const analysisError = ref('')
  const analysisLoading = ref(false)
  const sensitivityPayload = ref(null)
  const sensitivityError = ref('')
  const sensitivityLoading = ref(false)

  /* ---------------------------------------------------------------- console */
  const consoleManual = ref(null) // null = auto (open only while streaming)

  /* ---------------------------------------------------------------- derived */
  const cohorts = computed(() => {
    const list = (manifest.value?.cohorts || [])
      .map((cohort, index) => ({
        id: String(cohort.id || `cohort_${index + 1}`),
        label: cohort.label || cohort.name || `Cohort ${index + 1}`,
        shortLabel: cohort.short_label || cohort.shortLabel || `C${index + 1}`
      }))
      .filter(cohort => cohort.id)
    return list.length ? list : [{ id: 'cohort_1', label: 'Cohort 1', shortLabel: 'C1' }]
  })
  const selectedCohort = computed(() => (
    cohorts.value.find(cohort => cohort.id === selectedCohortId.value) || cohorts.value[0] || null
  ))
  const stakeholderCount = computed(() => Math.max(1, manifest.value?.cohorts?.length || 1))

  const statisticalFields = computed(() => (
    statisticalPayload.value?.manifest?.fields || statisticalPayload.value?.fields || []
  ))
  /* Run SCALE belongs to Preflight (which owns ensemble, rounds and launch cost);
     rendering it again in Cohorts would be two controls for one concept.
     Sampling identity (seed, salts, priors, drift profile) stays with
     Cohorts; scale fields stay out of the Workbench display. */
  const PREFLIGHT_OWNED_FIELDS = new Set(['run.ensemble_n', 'run.drift_horizon_rounds'])
  const runStatisticalFields = computed(() => statisticalFields.value.filter(field => (
    !isCohortScopedField(field) && !PREFLIGHT_OWNED_FIELDS.has(field.id)
  )))
  const cohortStatisticalFields = computed(() => statisticalFields.value.filter(field => isCohortScopedField(field)))

  const persistedStatisticalHash = computed(() => (
    statisticalConfig.value?.statistical_settings_hash ||
    statisticalPayload.value?.default_config?.statistical_settings_hash ||
    ''
  ))
  const statisticalHash = computed(() => (
    statisticalDirty.value && persistedStatisticalHash.value
      ? `${persistedStatisticalHash.value} · edited`
      : persistedStatisticalHash.value
  ))
  const shortHash = computed(() => {
    if (!statisticalHash.value) return 'settings draft'
    return statisticalHash.value.length > 26
      ? `${statisticalHash.value.slice(0, 20)}…${statisticalDirty.value ? ' · edited' : ''}`
      : statisticalHash.value
  })

  const scaleProduct = computed(() => preflight.ensemble_n * stakeholderCount.value * preflight.rounds)
  const costPreflight = computed(() => manifest.value?.eval_instruments?.cost_preflight || {})
  const scaleCap = computed(() => preflightPayload.value?.scale_cap || costPreflight.value.budget_cap || 500)
  const preflightScaleProduct = computed(() => preflightPayload.value?.scale_product || scaleProduct.value)
  const tokenEstimate = computed(() => preflightPayload.value?.token_estimate || scaleProduct.value * 150)
  const providerReadiness = computed(() => {
    const readiness = preflightPayload.value?.provider_readiness
    if (!readiness) return preflightLoading.value ? 'checking' : 'not checked'
    return readiness.ready ? readiness.status : `${readiness.status}${readiness.reason ? ` · ${readiness.reason}` : ''}`
  })
  const latencyCopy = computed(() => (
    preflightPayload.value?.estimated_latency_ms == null
      ? 'not measured'
      : `${preflightPayload.value.estimated_latency_ms} ms`
  ))
  const costCopy = computed(() => formatCost(preflightPayload.value?.estimated_external_cost))
  const budgetCopy = computed(() => formatBudgetStatus(preflightPayload.value?.external_budget_status))

  const runGraphSource = computed(() => (
    preferredGraphFromPayloads(
      [graphPayload.value, 'graph'],
      [statusPayload.value, 'status'],
      [reportPayload.value, 'report']
    ) || manifestGraph(manifest.value, activeRunId.value, backendPhase.value, statisticalHash.value)
  ))
  const runGraphData = computed(() => runGraphSource.value?.graphData || null)
  const worldExists = computed(() => Boolean(activeRunId.value && (
    runGraphData.value?.nodes?.length ||
    isStreaming.value ||
    ['created', 'prepared', 'completed', 'reported', 'unknown'].includes(backendPhase.value)
  )))
  const graphStats = computed(() => {
    const nodes = Array.isArray(runGraphData.value?.nodes) ? runGraphData.value.nodes.length : 0
    const edges = Array.isArray(runGraphData.value?.edges) ? runGraphData.value.edges.length : 0
    const schemaTypes = new Set(
      (runGraphData.value?.nodes || []).flatMap(node => node.labels || [])
    ).size
    return { nodes, edges, schemaTypes }
  })

  const reportClaims = computed(() => collectReportClaims(reportPayload.value, manifest.value))
  const evidenceItems = computed(() => collectEvidenceRefs(reportPayload.value))
  const validityFlags = computed(() => buildValidityFlagsMap(reportPayload.value))
  const canGenerateReport = computed(() => backendPhase.value === 'completed')
  const reportGateReason = computed(() => {
    if (!activeRunId.value) return 'needs a completed run'
    if (canGenerateReport.value) return ''
    const byPhase = {
      created: 'needs a launched run — launch from preflight',
      prepared: 'needs a launched run — launch from preflight',
      starting: 'report unlocks when the run completes',
      running: 'report unlocks when the run completes',
      failed: 'run halted — findings need a completed run',
      reported: 'a report already exists — refresh it instead',
      unknown: 'waiting for lifecycle status'
    }
    return byPhase[backendPhase.value] || `report unavailable while ${phase.value}`
  })
  const canAsk = computed(() => Boolean(activeRunId.value && selectedLaneId.value && reportPayload.value))

  const statisticalVariants = computed(() => (
    Array.isArray(statisticalVariantsPayload.value?.variants) ? statisticalVariantsPayload.value.variants : []
  ))
  const statisticalLineage = computed(() => (
    Array.isArray(statisticalLineagePayload.value?.lineage) ? statisticalLineagePayload.value.lineage : []
  ))
  const latestVariant = computed(() => (
    [...statisticalVariants.value].reverse().find(variant => variant?.variant_id && variant.variant_id !== 'base') || null
  ))
  const compareDiffCount = computed(() => (
    Array.isArray(analysisComparePayload.value?.statistical_diff)
      ? analysisComparePayload.value.statistical_diff.length
      : 0
  ))

  const readiness = computed(() => [
    { id: 'question', label: 'stress question', ok: scenarioText.value.trim().length > 0 },
    { id: 'cohorts', label: `cohorts · ${stakeholderCount.value}`, ok: (manifest.value?.cohorts?.length || 0) > 0 },
    { id: 'catalog', label: 'backend catalog', ok: Boolean(backendCatalog.value) }
  ])

  const canEditWorkbench = computed(() => Boolean(
    activeRunId.value && selectedLaneId.value && statisticalFields.value.length && !isFrozen.value
  ))
  const workbenchGateReason = computed(() => {
    if (!activeRunId.value) return 'needs a built world — build creates the run'
    if (isStreaming.value) return 'run in progress — settings are frozen'
    if (isHalted.value) return 'run halted — duplicate as draft to edit'
    if (['completed', 'reported'].includes(backendPhase.value)) return 'run finished — fork a variant from findings · data'
    if (!statisticalFields.value.length) return 'no statistical manifest for this lane'
    return ''
  })

  /* ------------------------------------------------------- step permission */
  const currentStep = computed(() => {
    if (SPEC_STEPS.some(step => step.id === props.step)) return props.step
    return activeRunId.value ? 'simulate' : 'scenario'
  })
  const findingsMode = computed(() => (FINDINGS_MODES.includes(props.mode) ? props.mode : 'read'))

  function stepGateReason (stepId) {
    /* Reasons are complete clauses placed at the thing they explain
       (board 12) — each step names its OWN gate; no cascading. */
    if (stepId === 'scenario') return ''
    if (stepId === 'build') {
      return scenarioText.value.trim() ? '' : 'opens once the question parses'
    }
    if (['cohorts', 'preflight'].includes(stepId)) {
      if (!activeRunId.value) return stepId === 'cohorts' ? 'needs a built world' : 'needs cohorts'
      return ''
    }
    if (stepId === 'simulate') {
      if (!activeRunId.value) return 'launch from preflight'
      return ''
    }
    if (stepId === 'findings') {
      if (reportPayload.value) return ''
      if (['completed', 'reported'].includes(backendPhase.value)) return ''
      return 'no artifacts yet'
    }
    return ''
  }

  function stepDone (stepId) {
    if (stepId === 'scenario') return Boolean(scenarioText.value.trim())
    if (stepId === 'build') return Boolean(activeRunId.value)
    if (stepId === 'cohorts') return Boolean(activeRunId.value && statisticalConfig.value)
    if (stepId === 'preflight') return ['starting', 'running', 'failed', 'completed', 'reported'].includes(backendPhase.value)
    if (stepId === 'simulate') return ['completed', 'reported'].includes(backendPhase.value)
    if (stepId === 'findings') return backendPhase.value === 'reported'
    return false
  }

  const spineItems = computed(() => SPEC_STEPS.map(step => {
    const reason = stepGateReason(step.id)
    let state = 'reachable'
    if (reason) state = 'locked'
    if (stepDone(step.id)) state = 'done'
    if (step.id === currentStep.value) state = 'active'
    /* halted is an interruption, not a phase — the spine shows it on
       Simulate regardless of where the operator is (board 07) */
    if (step.id === 'simulate' && isHalted.value) state = 'halted'
    return { ...step, state, reason }
  }))

  /* ------------------------------------------------------------- navigation */
  function routeQuery (overrides = {}) {
    const query = {
      step: currentStep.value,
      ...(currentStep.value === 'findings' ? { mode: findingsMode.value } : {}),
      ...(activeRunId.value
        ? {}
        : {
            lane: selectedLaneId.value || undefined
          }),
      ...overrides
    }
    for (const key of Object.keys(query)) {
      if (query[key] === undefined || query[key] === null || query[key] === '') delete query[key]
    }
    return query
  }

  function goStep (stepId, mode = null) {
    if (stepGateReason(stepId)) return
    router.push({
      path: activeRunId.value ? `/run/${activeRunId.value}` : '/run',
      query: routeQuery({
        step: stepId,
        mode: stepId === 'findings' ? (mode || findingsMode.value) : undefined
      })
    })
  }

  function duplicateAsDraft () {
    setDraft({
      lane: selectedLaneId.value,
      text: scenarioText.value.trim(),
      source: 'paste',
      preview: null
    })
    router.push({
      path: '/run',
      query: {
        step: 'scenario',
        lane: selectedLaneId.value || undefined
      }
    })
  }

  /* ------------------------------------------------------------ overlay O1/O2 */
  const overlayTrail = ref([])
  const summonerEl = ref(null)

  const overlay = computed(() => {
    const top = overlayTrail.value[overlayTrail.value.length - 1]
    if (!top) return null
    return parseOverlayHash(top.hash)
  })

  function parseOverlayHash (hash) {
    const match = /^(claim|act|evidence|node|agent|cohort):(.+)$/.exec(hash || '')
    if (!match) return null
    let [, kind, rest] = match
    let facet = ''
    if (rest.includes('/')) {
      const parts = rest.split('/')
      rest = parts[0]
      facet = parts[1] || ''
    }
    return { kind, id: decodeURIComponent(rest), facet, hash }
  }

  function overlayLabel (hash) {
    const parsed = parseOverlayHash(hash)
    if (!parsed) return hash
    if (parsed.kind === 'claim') return `claim ${parsed.id}`
    return `${parsed.kind} ${parsed.id}`
  }

  function summon (hash, event = null) {
    if (typeof document !== 'undefined') {
      summonerEl.value = event?.currentTarget || document.activeElement || null
    }
    if (overlayTrail.value[overlayTrail.value.length - 1]?.hash === hash) return
    overlayTrail.value = [...overlayTrail.value, { hash, label: overlayLabel(hash) }]
    router.push({ query: route.query, hash: `#${hash}` })
  }

  function popOverlay () {
    if (!overlayTrail.value.length) return
    const next = overlayTrail.value.slice(0, -1)
    overlayTrail.value = next
    const top = next[next.length - 1]
    router.replace({ query: route.query, hash: top ? `#${top.hash}` : '' })
    if (!top) flashSummoner()
  }

  function dismissOverlays () {
    if (!overlayTrail.value.length) return
    overlayTrail.value = []
    router.replace({ query: route.query, hash: '' })
    flashSummoner()
  }

  function flashSummoner () {
    const el = summonerEl.value
    if (!el || typeof el.classList === 'undefined' || !el.isConnected) return
    el.classList.remove('rf-flash')
    void el.offsetWidth
    el.classList.add('rf-flash')
    if (typeof el.focus === 'function') el.focus({ preventScroll: true })
  }

  watch(() => route.hash, hash => {
    const clean = (hash || '').replace(/^#/, '')
    const top = overlayTrail.value[overlayTrail.value.length - 1]?.hash || ''
    if (clean === top) return
    if (!clean) {
      if (overlayTrail.value.length) {
        overlayTrail.value = []
        flashSummoner()
      }
      return
    }
    const prev = overlayTrail.value[overlayTrail.value.length - 2]?.hash || ''
    if (clean === prev) {
      overlayTrail.value = overlayTrail.value.slice(0, -1)
      return
    }
    if (!parseOverlayHash(clean)) return
    overlayTrail.value = [...overlayTrail.value, { hash: clean, label: overlayLabel(clean) }]
  }, { immediate: true })

  /* ---------------------------------------------------------------- console */
  const timeline = computed(() => {
    const order = ['created', 'prepared', 'starting', 'running', 'completed', 'reported']
    const index = order.indexOf(backendPhase.value)
    const progress = order.map((id, i) => ({
      id,
      label: displayPhase(id, true),
      active: id === backendPhase.value,
      done: index >= 0 && i < index
    }))
    return cockpitTimeline(progress, statusPayload.value, reportPayload.value)
  })

  const consoleLogs = computed(() => {
    if (!activeRunId.value) return []
    return timeline.value.map((event, index) => ({
      id: event.id || `event-${index}`,
      time: '',
      tag: event.source,
      msg: event.copy,
      kind: consoleKind(event.severity),
      severity: event.severity
    }))
  })

  const consoleLine = computed(() => {
    if (!activeRunId.value) return 'idle · no run attached'
    const firstError = firstOf(statusPayload.value?.errors)
    const lines = {
      created: 'draft · recipe editable · edits reset readiness',
      prepared: 'graph ready · awaiting launch',
      starting: 'starting · runner attaching',
      running: lastRunEvent() || 'running · rounds committing',
      failed: `halted · ${firstError || 'see log'} — duplicate as draft to retry`,
      completed: 'rounds done · report can be generated from findings',
      reported: 'artifacts hashed · replay available from findings',
      unknown: 'hydrating run status'
    }
    return lines[backendPhase.value] || `${phase.value} · run ${activeRunId.value}`
  })

  const consoleDot = computed(() => {
    if (isHalted.value) return 'danger'
    if (isStreaming.value || backendPhase.value === 'completed') return 'live'
    return 'idle'
  })

  const consoleOpen = computed(() => {
    if (consoleManual.value !== null) return consoleManual.value
    return isStreaming.value || isHalted.value
  })

  function toggleConsole () {
    consoleManual.value = !consoleOpen.value
  }

  function lastRunEvent () {
    const events = statusPayload.value?.monitor_events
    if (!Array.isArray(events) || !events.length) return ''
    const last = events[events.length - 1]
    const copy = typeof last === 'string' ? last : (last?.message || last?.copy || '')
    return copy ? `running · ${copy}` : ''
  }

  function consoleKind (severity) {
    if (['error', 'warning'].includes(severity)) return 'danger'
    if (['active', 'claim', 'evidence'].includes(severity)) return 'accent'
    return 'default'
  }

  const contextLine = computed(() => ({
    lane: manifest.value?.lane_id || selectedLaneId.value || 'lane',
    phase: phase.value,
    env: 'graphiti'
  }))

  /* ------------------------------------------------------------- lifecycles */
  async function boot () {
    await loadLaneIndex()
    if (activeRunId.value) {
      await hydrateRun()
    } else if (selectedLaneId.value) {
      await loadCatalog(selectedLaneId.value)
      await loadStatisticalManifestForLane(selectedLaneId.value)
      if (currentStep.value === 'preflight') await refreshPreflight({ silent: true })
    }
    schedulePolling()
  }

  function teardown () {
    stopPolling()
  }

  async function loadLaneIndex () {
    try {
      const index = await listUseCases()
      discoveredLaneManifests.value = laneManifestsFromIndex(index)
    } catch (_error) {
      discoveredLaneManifests.value = laneManifests
    }
    if (!activeRunId.value && !selectedLaneId.value) {
      selectedLaneId.value = props.lane || registeredLaneIds.value[0] || laneIds[0] || null
    }
  }

  async function loadCatalog (laneId) {
    catalogError.value = ''
    try {
      const catalog = await getCatalog(laneId)
      if (selectedLaneId.value === laneId) backendCatalog.value = catalog
    } catch (error) {
      catalogError.value = formatError(error, `catalog unavailable for ${laneId} — start the backend, then retry`)
    }
  }

  async function loadStatisticalManifestForLane (laneId) {
    statisticalError.value = ''
    try {
      const payload = await getStatisticalManifest(laneId)
      if (selectedLaneId.value !== laneId) return
      statisticalPayload.value = payload
      applyStatisticalSettings(payload.default_config?.settings || {})
      statisticalConfig.value = payload.default_config || null
    } catch (error) {
      statisticalPayload.value = null
      statisticalConfig.value = null
      clearStatisticalSettings()
      statisticalError.value = formatError(error, `statistical manifest unavailable for ${laneId}`)
    }
  }

  async function loadStatisticalConfigForRun (laneId, simulationId) {
    statisticalError.value = ''
    try {
      const config = await getStatisticalConfig(laneId, simulationId)
      statisticalConfig.value = config
      applyStatisticalSettings(config.settings || {})
    } catch (error) {
      statisticalError.value = formatError(error, 'statistical config unavailable for this run')
    }
  }

  async function hydrateRun () {
    if (!activeRunId.value) return
    if (!registeredLaneIds.value.length) await loadLaneIndex()
    isHydrating.value = true
    lifecycleError.value = ''
    reportPayload.value = null
    clearAsk()
    backendCatalog.value = null
    try {
      const result = await findSimulationStatus(activeRunId.value, registeredLaneIds.value, null)
      if (!result?.laneId || !result?.status) {
        selectedLaneId.value = null
        statusPayload.value = null
        lifecycleError.value = `run ${activeRunId.value} was not found in any registered lane`
        return
      }
      selectedLaneId.value = result.laneId
      statusPayload.value = result.status
      await loadCatalog(result.laneId)
      await loadGraph({ silent: true })
      await loadStatisticalManifestForLane(result.laneId)
      await loadStatisticalConfigForRun(result.laneId, activeRunId.value)
      if (currentStep.value === 'cohorts') await loadWorkbenchArtifacts({ silent: true })
      if (currentStep.value === 'findings') {
        await loadReport({ silent: true })
        if (findingsMode.value === 'data') await loadAnalysisArtifacts({ silent: true })
      }
    } catch (error) {
      selectedLaneId.value = null
      statusPayload.value = null
      lifecycleError.value = formatError(error, `run ${activeRunId.value} could not be hydrated`)
    } finally {
      isHydrating.value = false
    }
  }

  /* -------------------------------------------------------- scenario parse */
  async function parseSeed () {
    const seed = scenarioText.value.trim()
    if (!seed || parseLoading.value || !selectedLaneId.value) return
    parseLoading.value = true
    parseError.value = ''
    try {
      const parsed = await parseScenarioSeed(selectedLaneId.value, {
        seed_text: seed,
        stress_question: seed,
        ...parseIdentity(selectedLaneId.value)
      })
      scenarioParse.value = {
        lane_id: selectedLaneId.value,
        source_mode: sourceMode.value,
        parse_source: parsed.parse_source || 'unknown',
        parser: parsed.parser || 'unknown',
        scenario_draft: parsed.scenario_draft || {}
      }
    } catch (error) {
      parseError.value = formatError(error, 'scenario parse failed')
    } finally {
      parseLoading.value = false
    }
  }

  function parseIdentity (laneId) {
    if (laneId === 'creator') return { persona: 'video_creator' }
    if (laneId === 'internal_policy') return { persona: 'policy', scope: 'internal_org' }
    if (laneId === 'public_policy') return { persona: 'policy', scope: 'public_policy' }
    return { persona: laneId }
  }

  /* ------------------------------------------------------------ build */
  async function buildWorld () {
    if (!selectedLaneId.value || isBusy.value) return
    isBusy.value = true
    lifecycleError.value = ''
    try {
      await ensurePreparedRun({ routeStep: 'build' })
    } catch (error) {
      lifecycleError.value = formatError(error, 'world build failed — see console')
    } finally {
      isBusy.value = false
    }
  }

  async function ensurePreparedRun ({ routeStep = null } = {}) {
    if (!selectedLaneId.value) throw new Error('no lane selected')
    const laneId = selectedLaneId.value
    let simulationId = activeRunId.value
    let currentPhase = backendPhase.value

    if (!simulationId) {
      const createPayload = buildCreatePayload()
      const created = await createSimulation(laneId, createPayload, idKey('create', 'draft', createPayload))
      simulationId = created.simulation_id
      createdFromDraftRunId = simulationId
      currentPhase = created.phase || created.status || 'created'
      statusPayload.value = created
      rememberRun(simulationId, laneId)
    }
    if (!simulationId) throw new Error('create did not return a simulation id')

    if (!['prepared', 'starting', 'running', 'completed', 'reported'].includes(currentPhase)) {
      const prepared = await prepareSimulation(laneId, simulationId, idKey('prepare', simulationId))
      currentPhase = prepared.phase || prepared.status || 'prepared'
      statusPayload.value = { ...(statusPayload.value || {}), ...prepared }
    }

    await loadGraphFor(laneId, simulationId, { silent: true })
    if (routeStep && simulationId !== activeRunId.value) {
      await router.push({ path: `/run/${simulationId}`, query: { step: routeStep } })
    }
    return { laneId, simulationId, phase: currentPhase }
  }

  function rememberRun (simulationId, laneId) {
    try {
      const seen = JSON.parse(localStorage.getItem(RUN_INDEX_KEY) || '[]')
        .filter(item => item && item.id !== simulationId)
      seen.unshift({ id: simulationId, lane: laneId, ts: Date.now() })
      localStorage.setItem(RUN_INDEX_KEY, JSON.stringify(seen.slice(0, 24)))
    } catch { /* private mode — the index is a convenience, not a record */ }
  }

  function buildCreatePayload () {
    return {
      scenario: buildScenarioPayload(),
      source_context: sourceContextPayload(),
      provider: providerPayload(),
      preflight_meter: preflightPayload.value || undefined,
      statistical_settings: statisticalFields.value.length ? { ...statisticalSettings } : undefined
    }
  }

  /* -------------------------------------------------------- preflight */
  async function refreshPreflight ({ silent = false, probeProvider = provider.probe_provider } = {}) {
    if (!selectedLaneId.value) return
    preflightLoading.value = true
    if (!silent) preflightError.value = ''
    try {
      preflightPayload.value = await evaluatePreflight(selectedLaneId.value, {
        scenario: buildScenarioPayload(),
        source_context: sourceContextPayload(),
        stakeholders: stakeholderCount.value,
        rounds: preflight.rounds,
        ensemble_n: preflight.ensemble_n,
        provider: providerPayload(),
        probe_provider: Boolean(probeProvider)
      })
      preflightError.value = ''
    } catch (error) {
      preflightPayload.value = null
      preflightError.value = formatError(error, 'preflight failed against the backend')
    } finally {
      preflightLoading.value = false
    }
  }

  const launchGateReason = computed(() => {
    if (isBusy.value || preflightLoading.value) return ''
    if (!scenarioText.value.trim()) return 'paste a draft first'
    if (activeRunId.value && !['created', 'prepared', 'unknown'].includes(backendPhase.value)) {
      return `launch is locked while ${phase.value} — findings owns completed runs`
    }
    if (preflightError.value) return 'resolve the preflight error, then launch'
    return ''
  })

  async function launchRun () {
    if (!selectedLaneId.value || isBusy.value) return
    isBusy.value = true
    lifecycleError.value = ''
    try {
      await refreshPreflight({ silent: true, probeProvider: true })
      if (!preflightPayload.value) throw new Error('preflight did not return a payload')
      if (preflightPayload.value.scale_ok === false) {
        throw new Error('scale guard refused this run — reduce N, cohorts, or rounds')
      }
      if (preflightPayload.value.provider_readiness?.ready === false) {
        throw new Error(preflightPayload.value.provider_readiness.reason || 'provider is not ready')
      }
      const { laneId, simulationId, phase: bootPhase } = await ensurePreparedRun()
      if (bootPhase !== 'prepared') {
        throw new Error(`start requires a prepared run; current phase is ${bootPhase}`)
      }
      const started = await startSimulation(laneId, simulationId, idKey('start', simulationId))
      statusPayload.value = started
      await router.push({ path: `/run/${simulationId}`, query: { step: 'simulate' } })
    } catch (error) {
      lifecycleError.value = formatError(error, 'launch failed — see console')
    } finally {
      isBusy.value = false
    }
  }

  /* ----------------------------------------------------------- status/graph */
  async function refreshStatus ({ silent = false } = {}) {
    if (!activeRunId.value || !selectedLaneId.value) return
    if (!silent) lifecycleError.value = ''
    try {
      statusPayload.value = await getSimulationStatus(selectedLaneId.value, activeRunId.value)
      await loadGraph({ silent: true })
      lifecycleError.value = ''
    } catch (error) {
      lifecycleError.value = formatError(error, 'status refresh failed')
    }
  }

  async function loadGraph ({ silent = false } = {}) {
    if (!activeRunId.value || !selectedLaneId.value) return
    await loadGraphFor(selectedLaneId.value, activeRunId.value, { silent })
  }

  async function loadGraphFor (laneId, simulationId, { silent = false } = {}) {
    if (!laneId || !simulationId) return
    if (!silent) graphError.value = ''
    try {
      graphPayload.value = await getSimulationGraph(laneId, simulationId)
      graphError.value = ''
    } catch (error) {
      graphPayload.value = null
      graphError.value = formatError(error, 'live run graph unavailable — showing the manifest fallback')
    }
  }

  async function refreshStage () {
    if (!activeRunId.value || !selectedLaneId.value) return
    await refreshStatus({ silent: true })
    await loadGraph()
    if (currentStep.value === 'findings') await loadReport({ silent: true })
  }

  function stopPolling () {
    if (statusPollTimer.value) {
      window.clearTimeout(statusPollTimer.value)
      statusPollTimer.value = null
    }
  }

  function schedulePolling () {
    stopPolling()
    if (!activeRunId.value || !selectedLaneId.value || !isStreaming.value) return
    statusPollTimer.value = window.setTimeout(async () => {
      statusPollTimer.value = null
      await refreshStatus({ silent: true })
      schedulePolling()
    }, 2500)
  }

  /* ------------------------------------------------------------- workbench */
  function clearStatisticalSettings () {
    for (const key of Object.keys(statisticalSettings)) delete statisticalSettings[key]
  }

  function applyStatisticalSettings (settings) {
    clearStatisticalSettings()
    for (const [key, value] of Object.entries(settings || {})) {
      statisticalSettings[key] = cloneValue(value)
    }
    statisticalDirty.value = false
    syncPreflightFromSettings()
  }

  function syncPreflightFromSettings () {
    const ensembleN = settingValue('run.ensemble_n')
    const rounds = settingValue('run.drift_horizon_rounds')
    if (Number.isFinite(Number(ensembleN))) preflight.ensemble_n = Number(ensembleN)
    if (Number.isFinite(Number(rounds))) preflight.rounds = Number(rounds)
  }

  function settingValue (fieldId, fallback = undefined) {
    if (Object.prototype.hasOwnProperty.call(statisticalSettings, fieldId)) return statisticalSettings[fieldId]
    return fallback
  }

  function fieldValue (field) {
    const cohortValue = cohortScopedValue(statisticalSettings, field)
    if (cohortValue !== undefined) return cohortValue
    const value = settingValue(field.id)
    if (value !== undefined) return value
    return cloneValue(field.default)
  }

  function fieldValueForCohort (field, cohortId) {
    if (!field) return undefined
    const cohortValue = cohortScopedValue(statisticalSettings, field, cohortId)
    if (cohortValue !== undefined) return cohortValue
    const baseValue = cohortScopedValue(statisticalConfig.value?.settings || {}, field, cohortId)
    if (baseValue !== undefined) return baseValue
    const value = settingValue(field.id)
    return value !== undefined ? value : cloneValue(field.default)
  }

  function setFieldValue (field, value) {
    const canonicalId = field.id
    if (cohortScopedPathInfo(canonicalId)) {
      setCohortScopedValue(canonicalId, value)
      statisticalDirty.value = true
      return
    }
    statisticalSettings[canonicalId] = cloneValue(value)
    if (canonicalId === 'run.ensemble_n') preflight.ensemble_n = Number(value) || preflight.ensemble_n
    if (canonicalId === 'run.drift_horizon_rounds') preflight.rounds = Number(value) || preflight.rounds
    statisticalDirty.value = true
  }

  function toggleArrayValue (field, value) {
    const current = Array.isArray(fieldValue(field)) ? [...fieldValue(field)] : []
    const index = current.indexOf(value)
    if (index >= 0) current.splice(index, 1)
    else current.push(value)
    if (field.control === 'active_hours_grid') current.sort((a, b) => a - b)
    setFieldValue(field, current)
  }

  function setObjectValue (field, key, value) {
    setFieldValue(field, { ...fieldValue(field), [key]: value })
  }

  function isCohortScopedField (field) {
    return Boolean(cohortScopedPathInfo(field.id))
  }

  function cohortScopedPathInfo (canonical) {
    const map = {
      'cohort.active_hours': { section: 'statistical', name: 'active_hours' },
      'cohort.activity_level': { section: 'statistical', name: 'activity_level' },
      'cohort.posts_per_hour': { section: 'statistical', name: 'posts_per_hour' },
      'cohort.comments_per_hour': { section: 'statistical', name: 'comments_per_hour' },
      'cohort.sentiment_bias': { section: 'statistical', name: 'sentiment_bias' },
      'cohort.influence_weight': { section: 'statistical', name: 'influence_weight' },
      'cohort.priors.attached_priors_id': { section: 'priors', name: 'bundle_id' },
      'cohort.drift.axis': { section: 'drift', name: 'axis' },
      'variant.counterfactual_axis': { section: 'drift', name: 'counterfactual_axis' },
      'variant.sensitivity_metric': { section: 'drift', name: 'sensitivity_metric' },
      'manifest.uncertainty_band': { section: 'drift', name: 'uncertainty_band' }
    }
    return map[canonical] || null
  }

  function encodePointerToken (value) {
    return String(value).replace(/~/g, '~0').replace(/\//g, '~1')
  }

  function cohortScopedValue (settings, field, cohortId = selectedCohort.value?.id) {
    const info = cohortScopedPathInfo(field.id)
    if (!info || !cohortId || !settings?.cohorts || typeof settings.cohorts !== 'object') return undefined
    const value = settings.cohorts?.[cohortId]?.[info.section]?.[info.name]
    return value === undefined ? undefined : cloneValue(value)
  }

  function setCohortScopedValue (canonicalId, value, cohortId = selectedCohort.value?.id) {
    const info = cohortScopedPathInfo(canonicalId)
    if (!info || !cohortId) return
    const current = statisticalSettings.cohorts && typeof statisticalSettings.cohorts === 'object'
      ? cloneValue(statisticalSettings.cohorts)
      : {}
    current[cohortId] = current[cohortId] || {}
    current[cohortId][info.section] = current[cohortId][info.section] || {}
    current[cohortId][info.section][info.name] = cloneValue(value)
    statisticalSettings.cohorts = current
    delete statisticalSettings[canonicalId]
  }

  function buildPatchOps () {
    const baseSettings = statisticalConfig.value?.settings || {}
    return statisticalFields.value.flatMap(field => {
      if (isCohortScopedField(field)) {
        return cohorts.value.map(cohort => cohort.id).flatMap(cohortId => {
          const paths = patchPathsForField(field, cohortId)
          if (!paths.length) return []
          const nextValue = baseValueForField(statisticalSettings, field, cohortId)
          const previousValue = baseValueForField(baseSettings, field, cohortId)
          if (JSON.stringify(nextValue) === JSON.stringify(previousValue)) return []
          return paths.map(path => ({ op: 'replace', path, value: cloneValue(nextValue) }))
        })
      }
      const paths = patchPathsForField(field)
      if (!paths.length) return []
      const nextValue = fieldValue(field)
      const previousValue = baseValueForField(baseSettings, field)
      if (JSON.stringify(nextValue) === JSON.stringify(previousValue)) return []
      return paths.map(path => ({ op: 'replace', path, value: cloneValue(nextValue) }))
    })
  }

  function baseValueForField (settings, field, cohortId = selectedCohort.value?.id) {
    const cohortValue = cohortScopedValue(settings, field, cohortId)
    if (cohortValue !== undefined) return cohortValue
    if (Object.prototype.hasOwnProperty.call(settings, field.id)) return settings[field.id]
    return field.default
  }

  function patchPathsForField (field, cohortId = selectedCohort.value?.id) {
    const map = {
      'run.run_seed': '/run/run_seed',
      'run.ensemble_n': '/run/ensemble_n',
      'run.drift_horizon_rounds': '/run/drift_horizon_rounds'
    }
    if (field.id === 'run.persona_salts') return ['/run/persona_salts']
    if (map[field.id]) return [map[field.id]]
    const info = cohortScopedPathInfo(field.id)
    if (!info) return []
    return cohortId ? [`/cohorts/${encodePointerToken(cohortId)}/${info.section}/${info.name}`] : []
  }

  async function saveWorkbenchPatch () {
    if (!canEditWorkbench.value || statisticalSaveLoading.value) return
    const ops = buildPatchOps()
    if (!ops.length) {
      statisticalVariantError.value = 'no settings have changed'
      return
    }
    statisticalSaveLoading.value = true
    statisticalVariantError.value = ''
    try {
      const result = await patchStatisticalConfig(
        selectedLaneId.value,
        activeRunId.value,
        ops,
        persistedStatisticalHash.value,
        idKey('statistical-patch', activeRunId.value, { expected_hash: persistedStatisticalHash.value, ops })
      )
      statisticalConfig.value = {
        ...(statisticalConfig.value || {}),
        ...result,
        settings: result?.settings || { ...statisticalSettings }
      }
      applyStatisticalSettings(statisticalConfig.value.settings || {})
      await reprepareAfterEdit()
      await loadWorkbenchArtifacts({ silent: true })
    } catch (error) {
      statisticalVariantError.value = formatError(error, 'workbench patch endpoint unavailable')
    } finally {
      statisticalSaveLoading.value = false
    }
  }

  async function reseedWorkbench () {
    if (!canEditWorkbench.value || statisticalReseedLoading.value) return
    statisticalReseedLoading.value = true
    statisticalVariantError.value = ''
    try {
      const fallbackSeed = defaultSeedForRun()
      const currentSeed = Number(settingValue('run.run_seed', fallbackSeed))
      const reseedPayload = {
        seed: Number.isFinite(currentSeed) ? currentSeed + 1 : fallbackSeed + 1,
        reason: 'operator_reseed'
      }
      const result = await reseedStatisticalConfig(
        selectedLaneId.value,
        activeRunId.value,
        reseedPayload,
        null,
        idKey('statistical-reseed', activeRunId.value, reseedPayload)
      )
      const config = result?.config || result
      if (config?.settings) {
        statisticalConfig.value = config
        applyStatisticalSettings(config.settings)
      }
      await reprepareAfterEdit()
      await loadWorkbenchArtifacts({ silent: true })
    } catch (error) {
      statisticalVariantError.value = formatError(error, 'workbench reseed endpoint unavailable')
    } finally {
      statisticalReseedLoading.value = false
    }
  }

  /* editing while prepared resets readiness honestly (dirty-hash gate) */
  async function reprepareAfterEdit () {
    if (!activeRunId.value || !selectedLaneId.value || backendPhase.value !== 'prepared') return
    const prepared = await prepareSimulation(
      selectedLaneId.value,
      activeRunId.value,
      idKey('prepare', activeRunId.value, {
        statistical_settings_hash: statisticalConfig.value?.statistical_settings_hash || statisticalHash.value
      })
    )
    statusPayload.value = { ...(statusPayload.value || {}), ...prepared }
    await loadGraph({ silent: true })
  }

  async function loadWorkbenchArtifacts ({ silent = false } = {}) {
    if (!activeRunId.value || !selectedLaneId.value) return
    if (!silent) statisticalVariantError.value = ''
    try {
      statisticalLineagePayload.value = await getStatisticalLineage(selectedLaneId.value, activeRunId.value)
    } catch (error) {
      statisticalLineagePayload.value = null
      statisticalVariantError.value = formatError(error, 'statistical lineage endpoint unavailable')
    }
    try {
      statisticalVariantsPayload.value = await getStatisticalVariants(selectedLaneId.value, activeRunId.value, 'statistical')
    } catch (error) {
      statisticalVariantsPayload.value = null
      statisticalVariantError.value = formatError(error, 'statistical variants endpoint unavailable')
    }
  }

  /* -------------------------------------------------------------- findings */
  async function generateReport () {
    if (!activeRunId.value || !selectedLaneId.value) return
    if (!canGenerateReport.value) {
      reportError.value = reportGateReason.value
      return
    }
    isBusy.value = true
    reportError.value = ''
    try {
      const result = await generateSimulationReport(selectedLaneId.value, activeRunId.value, idKey('report', activeRunId.value))
      if (result?.job_id && result?.status !== 'succeeded') {
        reportNotice.value = 'report generation is running in the background'
        await waitForReportJob(result.job_id)
      }
      await refreshStatus({ silent: true })
      await loadReport()
    } catch (error) {
      reportError.value = formatError(error, 'report generation failed')
    } finally {
      isBusy.value = false
    }
  }

  async function waitForReportJob (jobId) {
    const maxAttempts = 90
    for (let attempt = 0; attempt < maxAttempts; attempt += 1) {
      const job = await getReportGenerationJob(selectedLaneId.value, activeRunId.value, jobId)
      if (job?.status === 'succeeded') return job
      if (job?.status === 'failed') {
        throw new Error(job.response?.error?.message || job.response?.error || 'report generation job failed')
      }
      await sleep(1000)
    }
    throw new Error('report generation job did not finish before the cockpit timeout')
  }

  async function loadReport ({ silent = false } = {}) {
    if (!activeRunId.value || !selectedLaneId.value) return
    if (!silent) {
      reportError.value = ''
      reportNotice.value = ''
    }
    try {
      reportPayload.value = await getSimulationReport(selectedLaneId.value, activeRunId.value)
      reportNotice.value = ''
    } catch (error) {
      reportPayload.value = null
      if (error?.code === 'REPORT_NOT_READY') {
        reportNotice.value = 'report is not ready yet for this run'
        return
      }
      reportError.value = formatError(error, 'report load failed')
    }
  }

  async function sendAsk (messageOverride = null) {
    if (!canAsk.value || askSending.value) return
    const message = String(messageOverride || askInput.value).trim()
    if (!message) return
    const nextHistory = [...askHistory.value, { role: 'user', content: message }]
    askHistory.value = nextHistory
    if (!messageOverride) askInput.value = ''
    askError.value = ''
    askSending.value = true
    try {
      const chatPayload = { message, chat_history: nextHistory.slice(0, -1) }
      const response = await chatWithSimulationReport(
        selectedLaneId.value,
        activeRunId.value,
        message,
        nextHistory.slice(0, -1),
        idKey('report-chat', activeRunId.value, chatPayload)
      )
      askHistory.value = [
        ...nextHistory,
        { role: 'assistant', content: response?.response || 'the report agent returned an empty response' }
      ]
    } catch (error) {
      askHistory.value = nextHistory.slice(0, -1)
      if (!messageOverride) askInput.value = message
      askError.value = formatError(error, 'report agent chat failed')
    } finally {
      askSending.value = false
    }
  }

  function clearAsk () {
    askInput.value = ''
    askHistory.value = []
    askError.value = ''
    askSending.value = false
  }

  async function loadAnalysisArtifacts ({ silent = false } = {}) {
    if (!activeRunId.value || !selectedLaneId.value || analysisLoading.value) return
    analysisLoading.value = true
    if (!silent) analysisError.value = ''
    try {
      await loadWorkbenchArtifacts({ silent: true })
      if (latestVariant.value) {
        analysisComparePayload.value = await compareSimulations(
          selectedLaneId.value,
          {
            base_run_id: activeRunId.value,
            variant_run_id: latestVariant.value.variant_id,
            axes: ['statistical', 'findings']
          },
          idKey('compare', activeRunId.value, {
            variant_run_id: latestVariant.value.variant_id,
            axes: ['statistical', 'findings']
          })
        )
      } else {
        analysisComparePayload.value = null
      }
      analysisError.value = ''
    } catch (error) {
      analysisComparePayload.value = null
      analysisError.value = formatError(error, 'compare artifacts unavailable')
    } finally {
      analysisLoading.value = false
    }
  }

  async function runSensitivitySweep () {
    if (!activeRunId.value || !selectedLaneId.value || sensitivityLoading.value) return
    sensitivityLoading.value = true
    sensitivityError.value = ''
    try {
      sensitivityPayload.value = await runSensitivity(
        selectedLaneId.value,
        activeRunId.value,
        { axes: ['statistical'] },
        idKey('sensitivity', activeRunId.value)
      )
    } catch (error) {
      sensitivityPayload.value = null
      sensitivityError.value = error?.code === 'CAPABILITY_UNSUPPORTED'
        ? 'this lane does not run real-ensemble sensitivity'
        : formatError(error, 'sensitivity endpoint unavailable')
    } finally {
      sensitivityLoading.value = false
    }
  }

  /* --------------------------------------------------------------- payloads */
  function providerPayload () {
    return {
      mode: provider.mode,
      model: provider.model,
      provider: provider.provider || undefined,
      base_url: provider.base_url || undefined
    }
  }

  function sourceContextPayload () {
    const source = sourceModes.find(option => option.id === sourceMode.value) || sourceModes[0]
    const connectorCapabilities = Array.isArray(manifest.value?.connector_capabilities)
      ? manifest.value.connector_capabilities
      : []
    const payload = {
      mode: source.id,
      label: source.label,
      items: [
        { id: 'seed', label: scenarioText.value.trim() ? 'operator seed' : 'seed pending', status: `${scenarioText.value.trim().length} chars` },
        { id: 'cohorts', label: 'cohort priors', status: `${cohorts.value.length} cohorts` },
        { id: 'provider', label: 'provider', status: `${provider.mode} · ${provider.model || 'model pending'}` }
      ],
      connectors: connectorCapabilities.map((connector, index) => ({
        id: connector.id || connector.connector_id || connector.name || `connector_${index + 1}`,
        label: connector.label || connector.name || connector.id || `Connector ${index + 1}`,
        state: connector.enabled === false ? 'declared_disabled' : 'declared'
      }))
    }
    if (scenarioParse.value) {
      payload.parse_provenance = {
        source: scenarioParse.value.parse_source || 'unknown',
        parser: scenarioParse.value.parser || 'unknown'
      }
    }
    return payload
  }

  function buildScenarioPayload () {
    const seed = scenarioText.value.trim() || 'Untitled RawFish scenario'
    const title = seed.split(/\s+/).slice(0, 10).join(' ') || 'RawFish scenario'
    const summary = seed.length > 180 ? `${seed.slice(0, 177)}...` : seed
    const parsedDraft = normalizedParsedDraft()
    if (selectedLaneId.value === 'creator') {
      return mergeScenarioDraft({
        persona: firstPersonaId('video_creator'),
        title,
        summary,
        seed_text: seed,
        stress_question: seed,
        stakeholders: buildCreatorStakeholders(),
        assumptions: ['Operator-provided seed is the source of truth.'],
        success_criteria: ['Identify likely audience failure modes before launch.'],
        failure_modes_to_watch: ['Misread cohort incentives', 'Overconfident positive reaction']
      }, parsedDraft)
    }
    return mergeScenarioDraft({
      title,
      summary,
      seed_text: seed,
      stress_question: seed,
      stakeholders: buildPolicyStakeholders(),
      assumptions: ['Operator-provided seed is the source of truth.'],
      success_criteria: ['Identify adoption, legitimacy, and implementation risks.'],
      failure_modes_to_watch: ['Low trust', 'Ambiguous accountability', 'Uneven burden']
    }, parsedDraft)
  }

  function normalizedParsedDraft () {
    const draft = scenarioParse.value?.scenario_draft
    if (!draft || typeof draft !== 'object' || Array.isArray(draft)) return null
    return draft
  }

  function mergeScenarioDraft (base, parsedDraft) {
    if (!parsedDraft) return base
    const merged = { ...base }
    for (const field of ['persona', 'scope', 'title', 'summary', 'seed_text', 'stress_question']) {
      if (typeof parsedDraft[field] === 'string' && parsedDraft[field].trim()) merged[field] = parsedDraft[field].trim()
    }
    for (const field of ['stakeholders', 'assumptions', 'success_criteria', 'failure_modes_to_watch']) {
      if (Array.isArray(parsedDraft[field]) && parsedDraft[field].length) merged[field] = parsedDraft[field]
    }
    return merged
  }

  function firstPersonaId (fallback) {
    return backendCatalog.value?.personas?.[0]?.persona_id || fallback
  }

  function segmentTypeForPersonaScope (persona, scope, fallback) {
    const flat = backendCatalog.value?.segment_types_by_persona
    const normalizedScope = scope === '' || scope === 'null' ? null : scope
    const candidateKeys = [
      normalizedScope ? `${persona}:${normalizedScope}` : persona,
      normalizedScope ? `${persona}:${selectedLaneId.value}` : null,
      persona
    ].filter(Boolean)
    if (flat && typeof flat === 'object') {
      for (const key of candidateKeys) {
        const allowed = flat[key]
        if (Array.isArray(allowed) && allowed.length) return allowed[0]
      }
    }
    const row = (backendCatalog.value?.personas || []).find(candidate => (
      (candidate?.persona_id || candidate?.persona) === persona
    ))
    const scopes = row?.segment_types_by_scope || {}
    const scopeKeys = normalizedScope ? [normalizedScope, selectedLaneId.value] : ['null', '', null]
    for (const key of scopeKeys) {
      const allowed = scopes[key]
      if (Array.isArray(allowed) && allowed.length) return allowed[0]
    }
    return fallback
  }

  function buildCreatorStakeholders () {
    return (manifest.value?.cohorts || [{ id: 'audience', label: 'Audience' }]).map((cohort, index) => ({
      segment_id: cohort.id || `cohort_${index + 1}`,
      name: cohort.label || `Cohort ${index + 1}`,
      type: index === 0
        ? segmentTypeForPersonaScope(firstPersonaId('video_creator'), null, 'loyal_subscriber')
        : 'casual_viewer',
      what_changes_their_mind: ['clear evidence', 'trusted context'],
      notes: 'Generated from cockpit seed.'
    }))
  }

  function buildPolicyStakeholders () {
    const fallbackType = selectedLaneId.value === 'public_policy' ? 'citizen_segment' : 'employee_cohort'
    const segmentType = segmentTypeForPersonaScope('policy', null, fallbackType)
    return (manifest.value?.cohorts || [{ id: 'stakeholder', label: 'Stakeholder' }]).map((cohort, index) => ({
      segment_id: cohort.id || `stakeholder_${index + 1}`,
      name: cohort.label || `Stakeholder ${index + 1}`,
      type: segmentType,
      interests: ['clarity', 'fairness'],
      incentives: ['avoid unnecessary risk'],
      constraints: ['limited information'],
      likely_support_reasons: ['clear benefit'],
      likely_opposition_reasons: ['implementation uncertainty'],
      information_channels: ['internal update'],
      influence_level: 3,
      vulnerability_level: 3,
      compliance_propensity: 3,
      trust_level: 3,
      mobilization_capacity: 2,
      what_changes_their_mind: ['clear evidence', 'credible implementation owner'],
      notes: 'Generated from cockpit seed.'
    }))
  }

  /* ------------------------------------------------------------- id / utils */
  function idKey (phaseName, simulationId = 'draft', payload = null) {
    const lane = selectedLaneId.value || 'unknown'
    return `rawfish-${phaseName}-${lane}-${simulationId}-${hashString(stableStringify(payload || {}))}`
  }

  function stableStringify (value) {
    if (value === null || typeof value !== 'object') return JSON.stringify(value)
    if (Array.isArray(value)) return `[${value.map(item => stableStringify(item)).join(',')}]`
    return `{${Object.keys(value).sort().map(key => (
      `${JSON.stringify(key)}:${stableStringify(value[key])}`
    )).join(',')}}`
  }

  function hashString (value) {
    let hash = 2166136261
    for (let index = 0; index < value.length; index += 1) {
      hash ^= value.charCodeAt(index)
      hash = Math.imul(hash, 16777619)
    }
    return (hash >>> 0).toString(36)
  }

  function defaultSeedForRun () {
    return parseInt(hashString(`${selectedLaneId.value || 'unknown'}:${activeRunId.value || 'draft'}`), 36) % 1000000
  }

  function cloneValue (value) {
    if (Array.isArray(value)) return [...value]
    if (value && typeof value === 'object') return { ...value }
    return value
  }

  function sleep (ms) {
    return new Promise(resolve => window.setTimeout(resolve, ms))
  }

  function firstOf (list) {
    if (!Array.isArray(list) || !list.length) return ''
    const entry = list[0]
    return typeof entry === 'string' ? entry : (entry?.message || entry?.copy || '')
  }

  function formatCost (cost) {
    if (provider.mode !== 'external') return 'local runtime only'
    if (!preflightPayload.value) return 'not checked'
    if (!cost) return 'cost unavailable'
    if (typeof cost.amount === 'number') return `${cost.currency || 'USD'} ${cost.amount.toFixed(4)}`
    if (typeof cost.estimated_cost_usd === 'number') return `$${cost.estimated_cost_usd.toFixed(4)}`
    return cost.status || cost.reason || 'cost unavailable'
  }

  function formatBudgetStatus (budget) {
    if (provider.mode !== 'external') return 'not applicable'
    if (!preflightPayload.value) return 'not checked'
    if (!budget) return 'not provided'
    if (budget.warning) {
      const amount = typeof budget.amount === 'number' ? ` ${budget.currency || 'USD'} ${budget.amount.toFixed(4)}` : ''
      return `${budget.status || 'warning'}${amount}`
    }
    return budget.status || 'ok'
  }

  function impactCopy (field) {
    const hint = field?.impact_hint
    if (typeof hint === 'string') return hint
    if (hint && typeof hint === 'object') return hint.summary || hint.copy || hint.description || hint.effect || field.description
    return field?.description || ''
  }

  function fieldProvenance (field) {
    const fromConfig = statisticalConfig.value?.provenance_per_field?.[field.id]
    const sources = Array.isArray(field.provenance) ? field.provenance : []
    return [...new Set([fromConfig, ...sources].filter(Boolean))].slice(0, 3)
  }

  function formatError (error, fallback) {
    return error?.message || fallback
  }

  /* ---------------------------------------------------------------- watchers */
  watch(activeRunId, runId => {
    if (runId && runId === createdFromDraftRunId) {
      if (localDraft && readDraft() === localDraft) setDraft(null)
      localDraft = null
      return
    }
    localDraft = runId ? null : readDraft()
    scenarioText.value = localDraft?.text || ''
    scenarioParse.value = localDraft?.preview || null
    sourceMode.value = localDraft?.source || 'paste'
  })

  watch([scenarioText, scenarioParse, sourceMode], ([text, preview, source]) => {
    if (!activeRunId.value && localDraft && readDraft() === localDraft) {
      Object.assign(localDraft, { text, preview, source })
    }
  })

  watch(cohorts, list => {
    if (!list.length) {
      selectedCohortId.value = ''
      return
    }
    if (!list.some(cohort => cohort.id === selectedCohortId.value)) {
      selectedCohortId.value = list[0].id
    }
  }, { immediate: true })

  watch(() => [props.runId, props.lane], async () => {
    await loadLaneIndex()
    if (activeRunId.value) {
      await hydrateRun()
      schedulePolling()
      return
    }
    stopPolling()
    selectedLaneId.value = localDraft?.lane || props.lane || registeredLaneIds.value[0] || laneIds[0] || null
    backendCatalog.value = null
    statusPayload.value = null
    reportPayload.value = null
    clearAsk()
    if (selectedLaneId.value) {
      await loadCatalog(selectedLaneId.value)
      await loadStatisticalManifestForLane(selectedLaneId.value)
    }
  })

  watch(() => [activeRunId.value, selectedLaneId.value, backendPhase.value], () => {
    schedulePolling()
  })

  watch([currentStep, findingsMode], async () => {
    await nextTick()
    if (currentStep.value === 'cohorts' && activeRunId.value && selectedLaneId.value) {
      await loadWorkbenchArtifacts({ silent: true })
    }
    if (currentStep.value === 'preflight' && selectedLaneId.value) {
      await refreshPreflight({ silent: true })
    }
    if (activeRunId.value && selectedLaneId.value && ['simulate', 'findings'].includes(currentStep.value)) {
      await refreshStatus({ silent: true })
    }
    if (activeRunId.value && selectedLaneId.value && currentStep.value === 'findings') {
      await loadReport({ silent: true })
      if (findingsMode.value === 'data') await loadAnalysisArtifacts({ silent: true })
    }
  })

  watch(() => manifest.value?.lane_id, () => {
    const defaults = manifest.value?.default_provider
    if (!defaults) return
    provider.mode = defaults.mode || provider.mode
    provider.model = defaults.model || provider.model
  })

  return {
    /* identity */
    SPEC_STEPS,
    manifest,
    selectedLaneId,
    backendCatalog,
    catalogError,
    /* run */
    activeRunId,
    statusPayload,
    backendPhase,
    phase,
    isStreaming,
    isHalted,
    isFrozen,
    frozenReason,
    isHydrating,
    isBusy,
    lifecycleError,
    /* scenario */
    scenarioText,
    sourceModes,
    sourceMode,
    scenarioParse,
    parseLoading,
    parseError,
    parseSeed,
    readiness,
    /* steps */
    currentStep,
    findingsMode,
    spineItems,
    stepGateReason,
    goStep,
    duplicateAsDraft,
    /* build */
    buildWorld,
    worldExists,
    graphStats,
    runGraphSource,
    runGraphData,
    graphError,
    refreshStage,
    /* cohorts / workbench */
    cohorts,
    selectedCohortId,
    selectedCohort,
    statisticalFields,
    runStatisticalFields,
    cohortStatisticalFields,
    statisticalError,
    statisticalDirty,
    statisticalHash,
    shortHash,
    statisticalVariants,
    statisticalLineage,
    statisticalVariantError,
    statisticalSaveLoading,
    statisticalReseedLoading,
    canEditWorkbench,
    workbenchGateReason,
    fieldValue,
    fieldValueForCohort,
    setFieldValue,
    toggleArrayValue,
    setObjectValue,
    isCohortScopedField,
    impactCopy,
    fieldProvenance,
    saveWorkbenchPatch,
    reseedWorkbench,
    /* preflight */
    preflight,
    provider,
    preflightLoading,
    preflightPayload,
    preflightError,
    refreshPreflight,
    stakeholderCount,
    scaleCap,
    preflightScaleProduct,
    tokenEstimate,
    providerReadiness,
    latencyCopy,
    costCopy,
    budgetCopy,
    launchGateReason,
    launchRun,
    /* simulate */
    timeline,
    refreshStatus,
    /* findings */
    reportPayload,
    reportError,
    reportNotice,
    reportClaims,
    evidenceItems,
    validityFlags,
    canGenerateReport,
    reportGateReason,
    generateReport,
    loadReport,
    askInput,
    askHistory,
    askError,
    askSending,
    canAsk,
    sendAsk,
    analysisComparePayload,
    analysisError,
    analysisLoading,
    loadAnalysisArtifacts,
    compareDiffCount,
    latestVariant,
    sensitivityPayload,
    sensitivityError,
    sensitivityLoading,
    runSensitivitySweep,
    /* console */
    consoleLine,
    consoleDot,
    consoleOpen,
    consoleLogs,
    toggleConsole,
    contextLine,
    /* overlays */
    overlay,
    overlayTrail,
    summon,
    popOverlay,
    dismissOverlays,
    /* lifecycle */
    boot,
    teardown
  }
}
```
