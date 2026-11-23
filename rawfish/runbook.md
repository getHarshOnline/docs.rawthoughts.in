---
title: "RawFish runbook"
---

<a id="rawfish&#45;runbook"></a>

Use this reference when changing the prototype's services, authentication or API integration\. For an ordinary local session, follow the [startup and cockpit walkthrough](/rawfish/using); [service configuration](/rawfish/using#configure-the-services) covers the model and graph\-memory choices\.

## Browser and API contracts {#browser-and-api-contracts}

| Surface | Behavior |
| --- | --- |
| `/` on the frontend | Launch and lane selection |
| `/run` | Draft cockpit, with text held in page memory |
| `/run/<run_id>` | Saved cockpit; `step` selects a step and `mode=read`, `ask` or `data` selects Findings |
| `/api/sim/use-cases/<lane_id>/catalog` | Lane catalog, including its required `lane_manifest` |
| `/api/sim/use-cases/<lane_id>/evals/preflight_meter` | Scale and provider\-readiness result |

Lane ids are `creator`, `internal_policy` and `public_policy`\. The local recipe exposes frontend port 3000 and backend port 5001 on loopback\. It does not provide separate authenticated users\. The [architecture](/rawfish/architecture) explains current behavior; the [rebuild contract](/rawfish/rebuild-target) defines the intended replacement\.

## Configuration sources and caller boundaries {#configuration-sources-and-caller-boundaries}

[\.env\.local\.template](/rawfish/source/env-local-template) defines host settings for the Docker\-backed stack\. [docker\-compose\.local\.yml](/rawfish/source/docker-compose-local-yml) supplies container addresses and loopback ports\. [process/local\_stack\.sh](/rawfish/source/process/local_stack-sh) starts and stops services, acquires models and runs probes\. Some readiness failures only warn, so inspect the individual health results rather than relying on the final banner\.

The recipe runs native Ollama on the host and fixes Graphiti with Neo4j for memory\. Containers reach the host through a gateway\. Changing a host URL or `ZEP_MODE` alone does not change the corresponding container configuration\. Use `RAWFISH_CONTAINER_LLM_BASE_URL` for RawFish's container model address and `RAWFISH_CONTAINER_OPENAI_BASE_URL` for Graphiti's\.

RawFish's `RAWFISH_LLM_*` fields and Graphiti's `OPENAI_*` fields configure separate clients\. An adapter must preserve that separation\. An unknown external model price is `cost_unavailable`, not zero\.

## Authentication changes are a developer deployment concern {#authentication-changes-are-a-developer-deployment-concern}

The local Docker recipe fixes `AUTH_ENABLED=false` and exposes ports only on loopback\. An auth\-enabled source build requires:

- A random `SECRET_KEY` of at least 32 characters\.
- `AUTH_ENABLED=true`\.
- Matching `API_KEY` and `VITE_API_KEY` values\. With `FLASK_DEBUG=false`, the backend rejects the example placeholders\.

For source development, put the backend values in the root `.env` and the browser's `VITE_API_KEY` in `frontend/.env.local`\. Keep `VITE_API_KEY` in the root file too because backend startup validates it\. Restart Vite after changing its environment, or rebuild built frontend assets\. A stale browser key can return 401 while the health endpoint succeeds\.

<Warning>

**The browser key is public to its readers\.** `VITE_API_KEY` is embedded in JavaScript\. It enables prototype requests but does not identify a user or separate their data\. Shared operation needs sign\-in, per\-user data access and network protection that this prototype does not supply\.

</Warning>

Return to [choosing a lane](/rawfish/using#choose-the-lane-and-keep-the-draft-in-view) for cockpit use\.

## Deployment boundaries {#deployment-boundaries}

Run the production backend with one worker\. The existing `npm run backend:prod` command selects `gunicorn -w 1 --threads 8`; a different launcher must also keep `-w 1`\. The [simulation runner](/rawfish/assets/backend/app/services/simulation_runner.py) holds process handles, monitor threads and run state in process\-local maps\. Multiple workers can send status or stop requests to a process that does not own the run\. Extra threads do not remove that single\-worker requirement\.

The browser uses same\-origin `/api` requests by default\. If you set `VITE_API_BASE_URL` for a different API host, add that exact origin to `connect-src` in [frontend/index\.html](/rawfish/assets/frontend/index.html) before building the frontend\. Its current Content\-Security\-Policy permits `'self'` and `http://localhost:5001`; an unlisted origin is blocked by the browser even when the API is reachable\. Set the backend's `ALLOWED_ORIGINS` to the actual frontend origins\. Browser connection policy and the backend's origin allowlist are separate checks\.

Keep the OASIS runner's execution limits explicit\. The [settings template](/rawfish/assets/.env.example) selects these defaults:

- `OASIS_DEFAULT_MAX_ROUNDS=150` supplies the round limit when the caller gives no positive `max_rounds`\.
- `OASIS_MAX_ROUNDS_CAP=200` remains the hard ceiling even when the caller requests more rounds\.
- `OASIS_MAX_AGENTS_CAP=1000` rejects a run whose configured agent count exceeds the cap\.
- `OASIS_ROUND_TIMEOUT_SEC=600` sets the simulation scripts’ per\-round timeout in seconds\.
- `OASIS_RUN_TIMEOUT_SEC=7200` sets their total\-run timeout in seconds\.

The runner clamps calculated rounds to the selected limit and rejects excess agents\. These controls apply to the OASIS execution path; Creator's deterministic completion marker does not run an OASIS swarm\. They also remain separate from RawFish's ensemble × stakeholder\-segment × rounds scale guard\. Raising a limit increases permitted work and potential provider cost\.

## Check a change {#maintainer-qualification}

Run `make ci` from the repository root for the full local check\. Install and start local Ollama with the configured model first: the provider probe and required report smoke make real requests\.

| Command | Use it to check |
| --- | --- |
| `make hygiene-gates` | Source hygiene, type checks and encoded UI and product rules |
| `make closure-gates` | Drift from the prototype's route, manifest and workbench rules |
| `make smoke` | Generic dispatch with mock dependencies |
| `make probe-llm` | The local model's structured JSON response pattern |
| `make smoke-local-report-required` | Creator report generation, read\-back and chat with a local model |
| `make test-backend` | Backend pytest suites |
| `make test-frontend` | Frontend Vitest suites |
| `make build-frontend` | Frontend production build |
| `make test-browser` | Desktop and mobile Playwright smoke |

`make smoke` checks the generic dispatch path with mock dependencies\. `make smoke-local-report-required` checks that a real local model can generate a Creator report and respond in chat after the runner writes its completion marker\. For a change to policy execution or reports, run that lane's tests separately\.

## Diagnose a changed integration {#diagnose-a-changed-integration}

Follow the failing caller\. A host model probe can pass while a container uses an unreachable address\. A RawFish model call can pass while Graphiti's Neo4j, embedding or reranking client fails\.

The scale guard counts ensemble size, stakeholders and rounds\. Changing its cap or override changes which runs the application admits\. Source markers remain metadata; saved ids remain record identifiers\.

`make down` stops the local containers and preserves data\. The purge path removes named graph and runner\-state volumes\. Save needed reports and settings before a deliberate reset; use the [shutdown task](/rawfish/using#return-to-a-saved-run-and-finish-locally) for an ordinary session\.
