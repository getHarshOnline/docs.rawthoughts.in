---
title: "process/README.md"
noindex: true
---

````md
# Process gates and smoke checks

Use the process checks to find source-rule violations and exercise the prototype's dispatch and report paths. The pytest and Vitest suites run separately; they do not collect the scripts in this folder. Every command below starts at the repository root. [The rebuild contract](../docs/POLICY_PRODUCT_SPEC.md) describes requirements beyond the current prototype.

<a id="the-makefile-separates-the-signals"></a>

## Choose a check

```sh
make hygiene-gates   # every hygiene gate, plus git diff --check
make closure-gates   # the contract drift checker
make gates           # both of the above
make ci              # the gates, all test suites, the build, the smokes and the provider probe
```

`make gates` is the static layer: it says the tree follows the rules, not that the product works. `make ci` is the full local check, and it includes the mock smoke, the provider probe and the live local report smoke, which needs a local model installed.

| Signal | Command | What a pass means |
| --- | --- | --- |
| Hygiene gates | `make hygiene-gates` | The tree is tidy: skips are owned, types check, the design system holds, no drift from the product's names, routes or wording |
| Contract drift | `make closure-gates` | The workbench, run metadata, manifests, providers, routes, tokens and docs match the prototype rules encoded by `check_rawfish_closure_contract.py` |
| Both | `make gates` | Hygiene and contract drift together |
| Mock smoke | `make smoke` | The mock wire path works end to end; not a full test suite |
| Provider probe | `make probe-llm` | The configured model honours the JSON-mode call pattern the report generator uses |
| Live local smoke | `make smoke-local-report-required` | A creator run reaches report generation, read-back and chat using a local model after deterministic runner completion |
| Backend tests | `make test-backend` | The full backend pytest suite passes, with every skip disclosed |
| Frontend tests | `make test-frontend` | The Vitest suites for the cockpit, router, manifests, API client and utilities pass |
| Browser smoke | `make test-browser` | Playwright walks Launch, source, preflight, run, report and chat on desktop and mobile |
| Everything | `make ci` | All of the above |

<a id="the-hygiene-gates"></a>

## Diagnose a hygiene failure

`run_hygiene_gates.sh` runs two lists in turn, the Python gates and the shell gates, and runs every gate before it exits, so one pass shows every violation. It exits 1 if any gate failed. Run it directly with `bash process/run_hygiene_gates.sh`.

The Python gates:

- `check_rawfish_contract.py` fails when the tree drifts from the proof of concept's expected shape: extra browser routes, stale product strings or lane contracts, a missing lane or statistical manifest, a direct or default cloud provider, an unguarded report step, a provider path that fails open, or workbench settings that stop reaching the run's artifacts.
- `check_no_planning_terminology.py` scans the declared backend application, tests, scripts and manifests plus `frontend/src/` for direct citations of the retiring planning path and narrow orchestration markers in content or filenames. Filename matching is case-insensitive and its built-in fixtures cover the documented `W2_runner.py` and `test_annex11_pinning.py` shapes. Ordinary domain and code vocabulary such as `plan`, `planning`, `planner`, `plan_id` and an unnumbered state-machine `phase` is deliberately allowed.
- `check_no_predictor_language.py` fails when forecasting language appears in user-facing text: the README files, `package.json`, frontend source, `index.html`, locales, backend prompts, errors and persona vocabulary, and `docs/`. It matches word forms, not just exact words, and a few files that must quote the banned words to define them are allowlisted.
- `check_design_system_css.py` fails when product CSS bypasses the shared primitives: raw hex colours, shadows, negative letter-spacing, viewport-sized or raw pixel type.

The shell gates:

- `check_no_removed_api_surface.sh` fails when frontend source hard-codes an `/api/sim/*` URL, imports a removed policy API client, or declares a removed browser route.
- `check_docker_compose_loopback.sh` fails when `docker-compose.yml` binds the backend or frontend to anything but `127.0.0.1`, so the proof of concept is never published on a public interface by accident.
- `check_frontend_guard_usage.sh` fails when a Vue template or script calls a `computed(...)` ref as a function instead of reading its value.
- `check_no_transition_all.sh` fails when product CSS uses `transition: all`; motion names the properties it animates. Upstream files are allowlisted with a reason beside each.
- `check_ui_contract.sh` runs the ten interface gates, U1 to U10, described in [the UI contract](../docs/RAWFISH_UI_CONTRACT.md).
- `check_pyright.sh` runs `uv run --frozen pyright` over the backend and fails on any error. The expected result is zero errors and zero warnings.

<a id="the-contract-drift-checker"></a>

## Diagnose contract drift

`check_rawfish_closure_contract.py` runs through `make closure-gates`, not the hygiene script. It checks the prototype rules encoded in that script: the workbench's route shape, its patch and allowlist rules, the variant and compare surfaces, the statistical fields of run metadata, the richer manifest metadata, provider probe and budget warnings, the exact route list, hooks for removed routes, the self-hosted fonts and the accent token, and any runtime identifier carrying the upstream product's name. The checker enforces those encoded rules; it does not test every requirement in the rebuild contract.

<a id="any-single-gate-can-run-alone"></a>

## Run a single gate

```sh
python3 process/check_rawfish_contract.py
python3 process/check_no_planning_terminology.py
python3 process/check_no_predictor_language.py
python3 process/check_design_system_css.py
python3 process/check_rawfish_closure_contract.py
bash    process/check_no_removed_api_surface.sh
bash    process/check_docker_compose_loopback.sh
bash    process/check_frontend_guard_usage.sh
bash    process/check_no_transition_all.sh
bash    process/check_ui_contract.sh
bash    process/check_pyright.sh
```

Each gate exits 0 on a pass, 1 on a violation and 2 when a tool it needs is missing, such as ripgrep.

<a id="the-smoke-scripts-drive-real-routes"></a>

## Follow the smoke scripts

- `demo_smoke.py` is the mock smoke behind `make smoke`; it is described in [the demo smoke page](../docs/DEMO_SMOKE.md).
- `local_report_smoke.py` drives a creator run through create, prepare and its deterministic completion marker, then generates and reads back a report and asks it a question using a local model, behind `make smoke-local-report` and its required form. It does not establish creator agent execution or a policy-lane report.
- `probe_llm_json_mode.py` makes a real JSON-mode round trip in the same pattern the report generator uses, behind `make probe-llm`.
- `boot_smoke.sh` starts the backend and frontend, checks that the main routes answer, and shuts both down.
- `local_stack.sh` runs the full local stack (Ollama on the host, Neo4j and RawFish in Docker) behind `make up` and `make down`.

<a id="adding-a-gate"></a>

## Add a gate

Put a `check_<topic>.py` or `check_<topic>.sh` in this folder. A Python gate exposes `main() -> int` returning 0 or 1; a shell gate exits 0 or 1 itself. Add its path to `PY_GATES` or `SH_GATES` in `run_hygiene_gates.sh`, and describe what it fails on in the lists above.
````
