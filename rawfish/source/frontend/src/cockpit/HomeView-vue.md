---
title: "frontend/src/cockpit/HomeView.vue"
noindex: true
---

```vue
<template>
  <!-- S0 · Home — start a stress test: paste a draft, pick a lane, start
       from a preset, bring a prepared graph — and every past run with its
       phase (board 04). The spine belongs to a run; home shows brand +
       context only. -->
  <main class="s0">
    <header class="rf-z1">
      <router-link class="rf-z1__brand" to="/">rawfish</router-link>
      <span class="rf-spine"></span>
      <span class="rf-z1__ctx">pre-mortem · graphiti · local</span>
    </header>

    <section class="s0__main">
      <div class="s0__hero">
        <RfLabel tone="accent">Pre-mortem simulation engine</RfLabel>
        <h1>What do you want to stress-test?</h1>
        <p class="dock-prose">Paste a draft. RawFish builds a knowledge-graph world from it, inhabits it with cohorts of agents, runs a costed swarm, and returns tagged, evidence-linked findings — a pre-mortem, never a prediction.</p>
      </div>

      <div class="s0__work">
        <RfPanel class="seedbox" title="Draft" flush>
          <template #meta>{{ seedChars }} chars · {{ parseState }}</template>
          <textarea
            v-model="seedText"
            rows="8"
            placeholder="We're shipping a rebrand next month. Worried long-time fans feel abandoned while we chase a younger audience…"
          ></textarea>
          <template #foot>
            <span class="chip-row" aria-label="Source posture">
              <RfChip
                v-for="source in sourceModes"
                :key="source.id"
                as="button"
                :variant="source.id === selectedSourceMode ? 'selected' : 'default'"
                @click="selectedSourceMode = source.id"
              >
                {{ source.label }}
              </RfChip>
            </span>
            <span class="spacer"></span>
            <RfButton
              role="quiet"
              :disabled="previewLoading || !seedText.trim()"
              @click="previewSeed"
            >
              {{ previewLoading ? 'parsing…' : 'preview parse →' }}
            </RfButton>
            <RfButton
              role="primary"
              :disabled="!seedText.trim()"
              reason="paste a draft first"
              @click="openLane(activeLane)"
            >
              Draft scenario →
            </RfButton>
          </template>
        </RfPanel>

        <aside class="lane-rail" aria-label="Lanes">
          <div class="rail-title">
            <RfLabel>Choose a lane</RfLabel>
            <span class="rf-meta">{{ catalogueLanes.length }} live</span>
          </div>
          <button
            v-for="lane in catalogueLanes"
            :key="lane.lane_id"
            type="button"
            :class="['rf-card', lane.lane_id === selectedLaneId ? 'rf-card--active' : null]"
            @click="selectLane(lane.lane_id)"
          >
            <span class="cohort-card__title">{{ lane.label }}</span>
            <span class="dock-prose">{{ lane.summary }}</span>
            <span class="rf-meta">{{ (lane.cohorts || []).length }} cohorts · {{ (lane.report_sections || []).length }} report sections</span>
          </button>
          <button
            type="button"
            :class="['rf-card', selectedSourceMode === 'graph' ? 'rf-card--active' : null]"
            @click="selectedSourceMode = 'graph'"
          >
            <span class="cohort-card__title">Bring a graph</span>
            <span class="rf-meta">prepared graph → same cockpit</span>
          </button>
        </aside>
      </div>

      <RfPanel v-if="preview || previewError" title="Parse preview" hairline>
        <template #meta>{{ preview ? `${preview.parse_source} · ${preview.parser}` : 'failed' }}</template>
        <RfLabelRow v-if="previewError" label="parse" :value="previewError" tone="danger" />
        <template v-else>
          <p class="claim__title">{{ previewTitle }}</p>
          <p class="dock-prose">{{ previewQuestion }}</p>
          <div class="chip-row">
            <RfChip v-for="cohort in previewCohorts" :key="cohort.id">{{ cohort.short_label || cohort.label }}</RfChip>
          </div>
        </template>
      </RfPanel>

      <section aria-label="Presets">
        <div class="rail-title">
          <RfLabel>Start from a preset</RfLabel>
          <span class="rf-meta">{{ seedPresets.length }} seeds · {{ selectedLaneLabel }}</span>
        </div>
        <hr data-content=" presets ">
        <div class="preset-list">
          <button
            v-for="preset in seedPresets"
            :key="preset"
            type="button"
            class="rf-card"
            @click="seedText = preset"
          >
            <span class="rf-meta">{{ activeLane }}</span>
            <span class="dock-prose">{{ preset }}</span>
          </button>
        </div>
      </section>

      <section v-if="recentRuns.length" aria-label="Past runs">
        <div class="rail-title">
          <RfLabel>Past runs</RfLabel>
          <span class="rf-meta">{{ recentRuns.length }} on this machine</span>
        </div>
        <hr data-content=" runs ">
        <div class="run-list">
          <button
            v-for="run in recentRuns"
            :key="run.id"
            type="button"
            class="rf-card"
            @click="openRun(run)"
          >
            <span class="run-card__id">{{ run.id }}</span>
            <span class="rf-meta">{{ run.lane }} · {{ run.phase || 'phase unknown' }}</span>
          </button>
        </div>
      </section>
    </section>
  </main>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { findSimulationStatus, listUseCases, parseScenarioSeed } from '../api/useCases.js'
import { laneManifests, laneIds, laneManifestsFromIndex } from './manifestRegistry.js'
import { displayPhase } from './runStore.js'
import { setDraft } from './draftStore.js'
import { RfButton, RfChip, RfLabel, RfLabelRow, RfPanel } from './primitives/index.js'

const router = useRouter()
const catalogueLanes = ref(laneManifests)
const selectedLaneId = ref(laneManifests[0]?.lane_id || 'creator')
const activeLane = computed(() => (
  catalogueLanes.value.some(lane => lane.lane_id === selectedLaneId.value)
    ? selectedLaneId.value
    : catalogueLanes.value[0]?.lane_id || 'creator'
))
const seedText = ref('')
const selectedSourceMode = ref('paste')
const preview = ref(null)
let previewInput = null
const previewError = ref('')
const previewLoading = ref(false)

const sourceModes = [
  { id: 'paste', label: 'paste' },
  { id: 'cached', label: 'cached' },
  { id: 'live', label: 'live marker' },
  { id: 'graph', label: 'prepared graph' }
]

const selectedLane = computed(() => catalogueLanes.value.find(lane => lane.lane_id === activeLane.value) || null)
const selectedLaneLabel = computed(() => selectedLane.value?.label || activeLane.value)
const seedChars = computed(() => seedText.value.trim().length)
const parseState = computed(() => {
  if (preview.value) return 'parsed'
  return seedChars.value > 0 ? 'parse-ready' : 'seed pending'
})
const previewCohorts = computed(() => (
  Array.isArray(selectedLane.value?.cohorts) && selectedLane.value.cohorts.length
    ? selectedLane.value.cohorts
    : []
))
const previewTitle = computed(() => {
  const draft = preview.value?.scenario_draft || {}
  return draft.title || draft.summary || seedText.value.trim().split(/\s+/).slice(0, 8).join(' ') || 'Scenario draft'
})
const previewQuestion = computed(() => (
  preview.value?.scenario_draft?.stress_question || seedText.value.trim() || 'Stress question pending.'
))
const seedPresets = computed(() => {
  const laneId = activeLane.value
  if (laneId === 'creator') {
    return [
      'Launch a controversial pricing change to long-time fans.',
      'Stress-test a public apology before posting.'
    ]
  }
  if (laneId === 'internal_policy') {
    return [
      'Roll out a return-to-office policy across uneven teams.',
      'Change promotion criteria with unclear manager incentives.'
    ]
  }
  return [
    'Announce a public-benefit policy with uncertain agency ownership.',
    'Open a consultation process after a contested infrastructure decision.'
  ]
})

const recentRuns = ref([])

onMounted(async () => {
  try {
    const index = await listUseCases()
    const backendLanes = laneManifestsFromIndex(index)
    if (backendLanes.length) catalogueLanes.value = backendLanes
    if (!catalogueLanes.value.some(lane => lane.lane_id === selectedLaneId.value)) {
      selectedLaneId.value = catalogueLanes.value[0]?.lane_id || 'creator'
    }
  } catch (_error) {
    catalogueLanes.value = laneManifests
  }
  await hydrateRecentRuns()
})

async function hydrateRecentRuns () {
  let stored = []
  try {
    stored = JSON.parse(localStorage.getItem('rawfish.runs') || '[]')
  } catch { stored = [] }
  if (!Array.isArray(stored) || !stored.length) return
  recentRuns.value = stored.slice(0, 8)
  const hydrated = await Promise.all(recentRuns.value.map(async run => {
    try {
      const found = await findSimulationStatus(run.id, laneIds, run.lane)
      const backendPhase = found?.status?.phase || found?.status?.status
      return { ...run, backendPhase, phase: backendPhase ? displayPhase(backendPhase, true) : run.phase }
    } catch {
      return run
    }
  }))
  recentRuns.value = hydrated
}

function openRun (run) {
  const step = ['completed', 'reported'].includes(run.backendPhase) ? 'findings' : 'simulate'
  router.push({
    path: `/run/${run.id}`,
    query: step === 'findings' ? { step, mode: 'read' } : { step }
  })
}

function selectLane (laneId) {
  selectedLaneId.value = laneId
  preview.value = null
  previewError.value = ''
}

async function previewSeed () {
  const seed = seedText.value.trim()
  if (!seed || previewLoading.value) return
  previewLoading.value = true
  previewError.value = ''
  const lane = activeLane.value
  const source = selectedSourceMode.value
  try {
    preview.value = await parseScenarioSeed(lane, {
      seed_text: seed,
      stress_question: seed,
      ...parseIdentity(lane)
    })
    previewInput = { seed, lane, source }
  } catch (error) {
    preview.value = null
    previewError.value = error?.message || 'scenario preview failed'
  } finally {
    previewLoading.value = false
  }
}

function openLane (laneId) {
  const text = seedText.value.trim()
  const source = selectedSourceMode.value
  const matchesPreview = previewInput?.seed === text && previewInput.lane === laneId && previewInput.source === source
  setDraft({
    lane: laneId,
    text,
    source,
    preview: matchesPreview && preview.value ? {
      lane_id: laneId,
      source_mode: source,
      parse_source: preview.value.parse_source || 'unknown',
      parser: preview.value.parser || 'unknown',
      scenario_draft: preview.value.scenario_draft || {}
    } : null
  })
  router.push({ path: '/run', query: { lane: laneId, step: 'scenario' } })
}

function parseIdentity (laneId) {
  if (laneId === 'creator') return { persona: 'video_creator' }
  if (laneId === 'internal_policy') return { persona: 'policy', scope: 'internal_org' }
  if (laneId === 'public_policy') return { persona: 'policy', scope: 'public_policy' }
  return { persona: laneId }
}
</script>
```
