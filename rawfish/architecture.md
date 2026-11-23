---
title: "Architecture"
---

<a id="architecture"></a>

Follow a request through the prototype to see where to make a change\. The Flask API manages the shared lifecycle and calls a lane adapter to validate the scenario, prepare run files, start the runner and generate the report\. The Vue cockpit reads each lane's catalog and manifests\. Some payload builders still name the three existing lanes, so a new lane needs frontend changes too\.

[Using RawFish](/rawfish/using) leads to cockpit tasks\. The [rebuild contract](/rawfish/rebuild-target) describes the planned replacement\.

<a id="a&#45;lane&#45;uses&#45;manifests&#45;and&#45;an&#45;adapter&#45;plus&#45;current&#45;cockpit&#45;seams"></a>

## A lane supplies its meaning through an adapter {#a-lane-supplies-its-meaning-through-an-adapter}

A lane registers an adapter implementing the use\-case interface, a lane manifest, a statistical manifest and a cohort pack\. The catalog route returns the lane's personas together with its required `lane_manifest`, and the cockpit renders many scenario, cohort, report, timeline and control surfaces from those declarations\. A field that does not apply to a lane is omitted from its manifest rather than shown disabled\.

All lanes use `/` and `/run/:runId?` in the browser and `/api/sim/use-cases/<lane_id>/...` on the backend; there is no separate policy application or browser route\. Keep the stable ids `creator`, `internal_policy` and `public_policy` when tracing a request\. Each policy lane owns its adapter and manifest, and `policy_core` supplies identity helpers, though the current policy implementation still shares a policy\-scope mapping internally\. Run and report calls use RawFish's provider router; Graphiti has separate model, embedding and reranking clients\.

The [SimulationUseCase protocol](/rawfish/source/backend/app/simulation_platform/use_case-py) leaves scenario and report types to the lane\. Each adapter supplies the validation models and an `artifact_names` mapping from logical names to files inside a run directory\. The generic layer can find a report without assuming every lane writes the same filename\. Its `report_schema` enables schema validation on stored reads\. The `report_draft_schema` can limit model output to fields the model supplies, while the application adds the run ID and records which input produced the report\.

Adapters opt into shared report checks through `guardrail_capabilities`\. An adapter that already performs those checks internally declares that fact, so dispatch does not apply demotions and other side effects twice\. An unsupported optional capability raises `NotImplementedError`, which dispatch exposes as `501 CAPABILITY_UNSUPPORTED`\. This is different from a provider failure during a supported operation\. The [registry](/rawfish/source/backend/app/simulation_platform/registry-py) checks required member presence rather than call signatures; conformance tests still have to exercise behavior\. Its process\-wide singleton makes built\-in registration simple, but tests must restore registry state when they add temporary adapters\.

The cockpit also needs lane\-specific frontend integration\. Launch hard\-codes seed presets and parser identity by lane\. The run store repeats the parser\-identity mapping, chooses separate creator and policy scenario payload builders, and chooses a public\-policy or internal\-policy stakeholder fallback from the lane id\. A fourth genuinely distinct lane therefore needs changes and tests at those cockpit seams in addition to its manifests, cohort pack and adapter\. Follow [extending RawFish](/rawfish/contributing/lanes) for the adapter and frontend changes\. The rebuild aims to remove those lane\-id branches\.

## A run's lifecycle {#a-run-s-lifecycle}

In [the run store](/rawfish/source/frontend/src/cockpit/runStore-js), **Build the world** first creates the run, then prepares it and reads the graph\. Creation stores the lane, scenario, provider and statistical settings\. Preparation delegates ontology, persona and artifact work to the adapter\. The cockpit then navigates to the saved run identifier\. This separates an editable in\-memory draft from backend state; reopening the draft address cannot recover its text\.

Consider changing the creator cohort's sentiment before launch\. The workbench first changes local settings\. **Save patch** constructs JSON Patch operations and sends the last saved settings hash\. The backend takes the run lock, rejects `starting`, `running`, `completed` and `reported` phases, checks an expected hash when supplied, validates paths and values, then writes the configuration files and state\. A stale hash returns `409`\. A path the backend does not allow returns `422`\. The cockpit always sends a hash, but the API accepts a request without one\.

If the run was prepared, the edit marks it for preparation again\. The cockpit calls prepare with the changed hash before proceeding\. This matters because accepting a settings change alone does not regenerate the personas and artifacts consumed by execution\. Preflight then checks the selected provider and scale, and **Launch swarm** starts the prepared run through the runner adapter\. Status polling supplies progress; completion permits report generation\.

The runner implementation differs by lane\. The [creator adapter](/rawfish/source/backend/app/creator/adapter-py) does not start an agent subprocess: it writes `creator_deterministic_mock_v1` completion metadata containing the statistical settings and returns control to dispatch\. Its later report calls a model with the scenario, stress question, persona and segment identities/types\. It discards the evidence catalog and does not read cohort statistical settings, so it cannot explain observed interactions or the effect of changing those settings\. The policy adapters use the OASIS runner bridge and need their own execution tests\.

The current reseed route also mutates that same run's configuration\. It appends a lineage event containing parent and changed settings, and the cockpit prepares the same run again\. The event is a settings variant, not another executed run\. The **Compare** panel compares its settings with the parent snapshot\. The backend fills its findings buckets from settings\-subject presence without loading both reports, so those buckets cannot establish report validity or an observed effect of reseeding\. Reseed uses the same refused\-phase set as patch\. Neither route includes `failed` in that set, so the backend phase check leaves a failed\-run mutation gap\. The cockpit additionally freezes failed runs and offers **duplicate as draft**; its frozen controls do not close that API gap\. Separate variant runs are a [rebuild target](/rawfish/rebuild-target)\.

Mutating routes wrapped in the idempotency helper accept `Idempotency-Key`: the same key and body reuse a response, while a changed body under that key is refused\. The cockpit derives keys from the operation, run and selected payload\. This prevents some accidental retries; it is not a transaction over the whole run\. Individual files use atomic replacement, but a later failure can leave the sequence partly written\. Report publication has the same boundary\.

## Models and memory {#models-and-memory}

Run and report model calls use the [provider router](/rawfish/assets/backend/app/simulation_platform/llm/router.py), whose current factory builds `RawFishLiteLLMClient` on LiteLLM\. The provider mode is `local_ollama`, `local_openai_compatible` or `external`, chosen for each run and kept with it; local modes need no external key\. This client requests a JSON object unless JSON mode is off, strips enclosing code fences and parses the response as an object\. The separate structured wrapper delegates to it because it advertises no strict JSON\-schema capability\. The audited client records model, mode, tokens, latency and phase into run metadata\. Graphiti has its own model and embedding configuration; router selection alone does not configure that separate client\.

Memory is chosen separately with `ZEP_MODE`\. The prototype memory interface finds entities of declared types, lists one type, sets the ontology, adds episodes, searches, and reads all nodes or all edges\.

- `mock`, the default, needs no service\. It keys entities from the scenario hash and cohort names, extracts by matching the ontology against seed text, and returns seeded search results\. Unsupported operations fail explicitly\.
- `graphiti` is an experimental local Neo4j profile\. The dependency lock pins Neo4j 5\.23\.0 for the simulation engine, below Graphiti’s declared minimum\. A lock that installs does not establish supported dependencies\.
- Hosted Zep is a deprecated experiment pinned at `zep-cloud` 3\.13\.0\. It warns on use and implements neither writes nor search\. Removing it remains a release proposal, not completed behavior\.

The [Graphiti adapter](/rawfish/assets/backend/app/seam/graphiti_store.py) creates its model, embedder and reranker independently, each with its own endpoint and model\. Selecting a local run provider does not configure them\. The intended local profile uses local OpenAI\-compatible endpoints for all three and Neo4j Community bound to loopback with a mandatory password\. Entity types must be typed models generated from the ontology; each episode needs a reference time; errors must remove credentials from connection strings\.

The prototype rejects OpenAI’s cloud host wherever it constructs the store\. Blocking that host does not prove endpoint confinement\. The selected release profile still needs tests for unexpected network access, telemetry with the switch off, unset and on, stored telemetry identifiers and concurrent group isolation\. Direct synchronous `add_episode` calls must expose failures and read each write back; a queued provider’s acknowledgment is not proof of ingestion\.

### Structured\-output handling {#structured-output-handling}

The active `RawFishLiteLLMClient` advertises `supports_json_schema=False`\. Its `_parse_json` strips enclosing Markdown fences, calls `json.loads` and rejects a non\-object response\. Both `loose` and `strict` JSON modes send `response_format={"type": "json_object"}`; `off` omits that request\. The client does not use the legacy prose extraction, malformed\-JSON repair or schema\-validation retry loop\. LiteLLM receives the configured generation timeout and transport retry count: the code defaults are 60 seconds and one retry, while the [environment template](/rawfish/assets/.env.example) selects 120 seconds and one retry\. A run using the template therefore differs from the code default\.

The retained [PolicyLLMClient](/rawfish/assets/backend/app/seam/llm_patches.py) has a different parsing path: strip fences, try strict JSON, decode an object or array embedded in prose, extract balanced braces, then remove control characters and trailing commas\. Final failure raises `LLMJSONParseError` with an excerpt capped at 500 characters, rather than logging the full response\. Its `strict` mode rethrows a failed JSON\-object request; `loose` can fall back to a second request without `response_format`; `off` starts with that second path\. Its own defaults are `LLM_TIMEOUT_SECONDS=60`, `LLM_MAX_RETRIES=2`, 8,192 tokens for ontology and 16,384 for reports\. Those settings do not describe the active router's implementation\.

The [structured wrapper](/rawfish/assets/backend/app/simulation_platform/llm/structured_output.py) checks the wrapped client's capabilities\. With a schema, declared support and an exposed OpenAI client, it requests strict JSON\-schema output and retries validation failures up to its configured limit \(two by default\), feeding the validation error back to the model\. Provider or JSON\-decode failures fall back to the wrapped client's `chat_json`\. `PolicyLLMClient` can advertise that capability through `LLM_SUPPORTS_JSON_SCHEMA`; the current router does not\. The wrapper sums usage across its strict\-schema validation attempts, and the [audited client](/rawfish/assets/backend/app/simulation_platform/llm/audited.py) writes one entry per logical call with the reported tokens, model, mode, latency, phase and timestamp\. That aggregation does not establish accounting for unreported retries inside another provider client\. The Rust rebuild still needs its own implementation and checks\.

### Scale and configured defaults {#scale-and-configured-defaults}

The prototype's [pure scale guard](/rawfish/assets/backend/app/simulation_platform/scale_guard.py) multiplies ensemble size, stakeholder\-segment count and rounds, treating each factor as at least one\. Its [caps](/rawfish/assets/backend/app/simulation_platform/scale_caps.py) are 500 normally and 5,000 when the expensive tier is explicitly enabled\. This raises the ceiling rather than removing it\. The API's preflight and reseed snapshot in [use\_cases\.py](/rawfish/assets/backend/app/api/use_cases.py) and the [policy runner](/rawfish/assets/backend/app/services/policy/policy_runner_service.py) each evaluate the guard from their own resolved inputs\. They do not reuse one durable decision across the whole run\. The API's rough token estimate defaults to the scale product multiplied by 150; it is not a measured model rate\.

The rebuild must record one scale decision and reuse it at preflight, start, metadata, replay and receipt, as required by the [target verification cases](/rawfish/rebuild-target#detailed-verification-cases)\. Its token estimate must use a measured basis or say “No estimate yet”\. The prototype's configured agent\-and\-round defaults below are separate from the stakeholder\-segment count supplied to the guard; these settings alone do not establish which runner executes or whether the controls affect its behavior:

| Lane | Configured default | Mock\-profile default |
| --- | --- | --- |
| creator | 30 agents by 2 rounds | 12 by 2 |
| internal policy | 50 by 4 | 24 by 3 |
| public policy | 80 by 5 | 32 by 3 |

## Reports {#reports}

Report generation finds a completed run before calling the lane generator\. For policy reports, the model supplies claims and sections\. RawFish adds the run ID and input details, checks the claim labels and runs the language guard\. The draft schema keeps those application\-owned fields out of the model's response\. It cannot make a generated claim true\.

JSON, rendered Markdown, report metadata and lifecycle state are written in sequence\. The stored JSON route validates the adapter's schema but does not repeat the language guard or verify the recorded digest and embedded run identity\. It can return JSON written before a later publication step failed\. Keep generation errors and the run/report context when reading results\. HTTP 200 or file presence alone does not mean report publication completed\. The [product contract](/rawfish/rebuild-target) sets the rebuild requirements, and [guardrails](/rawfish/guardrails) describes the checks\.

The [findings task](/rawfish/using#read-what-the-run-actually-supports) shows how these limits affect a reader using the creator announcement example\.

<a id="how&#45;the&#45;repository&#45;is&#45;laid&#45;out"></a>

## Find the implementation boundary {#find-the-implementation-boundary}

| Path | What lives there |
| --- | --- |
| `backend/app/simulation_platform/` | the lane platform: the registry, run state and its state machine, the scale guard, idempotency, run locks, run metadata, guardrail hooks, the runner adapter and the provider router under `llm/` |
| `backend/app/policy_core/` | what the two policy lanes share: lane identity and scope context |
| `backend/app/creator/`, `internal_policy/`, `public_policy/` | one adapter per lane, with its catalog and defaults |
| `backend/app/api/` | the generic lane API, mounted at `/api/sim/use-cases/<lane_id>/...` |
| `backend/app/services/` | the engine services: profile generator, simulation configuration, runner and IPC |
| `backend/app/seam/` | the memory stores \(the deterministic mock and Graphiti\) behind one interface |
| `frontend/src/cockpit/` | the cockpit: shell, the six step views, the workbench field, overlays, primitives and the run store |
| `frontend/src/lanes/` | each lane's manifest |
| `frontend/src/styles/rawfish.css` | the token sheet, the only place colours, type roles and spacing are defined |
| `process/` | the process gates, described in that folder's README |
| `scenarios/`, `examples/` | scenario presets and example scenarios |

## Gates and tests {#gates-and-tests}

`make gates` checks source rules for routes, manifests, API clients, loopback ports, fonts, UI tokens and test\-skip records\. `make ci` also runs tests, builds and smoke checks\. Use [the runbook](/rawfish/runbook#maintainer-qualification) to choose between mock dispatch and model\-backed report checks\. Run a test that exercises new runtime behavior directly\.
