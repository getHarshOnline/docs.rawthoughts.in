---
title: "Demo smoke"
---

<a id="demo&#45;smoke"></a>

Choose the mock smoke to check generic lane dispatch without model services\. Choose the local report smoke to exercise report generation, read\-back and chat with a real local model\. Neither executes a Creator agent swarm\.

Run commands from the repository root after [installing source dependencies](/rawfish/prototype#build-and-test)\.

## Check dispatch without a model server {#check-dispatch-without-a-model-server}

```sh
make smoke
```

`process/demo_smoke.py` needs neither Ollama nor Neo4j\. It checks every lane's catalog and required `lane_manifest`, Creator persona discovery, local preflight without external credentials and an external preflight that reports a missing key\. It creates, prepares, starts and polls a Creator run, then checks the saved provider and preflight snapshots\. It does not generate a report\.

A pass ends with:

```text
--- RAWFISH SMOKE: ALL CHECKS PASS ---
```

## Check a report with local Ollama {#check-a-report-with-local-ollama}

The report smoke loads the root `.env.local` when present\. Set its local endpoint and model, then start Ollama with that model available\.

<CodeGroup>

```sh Optional local report
make smoke-local-report
```

```sh Required local report
make smoke-local-report-required
```

</CodeGroup>

Both forms remove external provider keys from their process and check the local endpoint and model before running\. The optional form exits successfully with `SKIP` if the endpoint or model is absent\. The required form sets `RAWFISH_REQUIRE_LOCAL_REPORT_SMOKE=true` and fails instead; `make ci` uses this form\.

The script creates, prepares and starts Creator, generates a report with the local model, reads it back and asks it a question\. Creator's runner still supplies only a deterministic completion marker, and its report generator does not use the evidence catalog\. A pass checks this report path, not policy\-lane execution, round\-by\-round conversations or real\-world validity\.

[Process checks](/rawfish/source/process/README-md) explains the full `make ci` run\.

## Present the prototype accurately {#present-the-prototype-accurately}

Show how a scenario becomes saved configuration and a generated report, using nonconfidential material\. Say which runner you are demonstrating: Creator completes through a deterministic marker, then a model writes the report, and no agent interactions are shown\. A policy\-lane demo needs its own successful rehearsal\. Run `make ci` first, or `make demo-check` to rehearse against an already running stack\.

Follow the [six cockpit steps](/rawfish/using#continue-through-the-six-cockpit-steps), whichever model you use\. For an external provider, show readiness and the available cost before launch; an unknown price appears as `cost_unavailable`\. The local `make up` recipe still uses native Ollama and Neo4j, so changing the report provider alone does not remove them\. Compose fixes Graphiti memory, so setting `ZEP_MODE=mock` in a host file does not change it\. Generate the report only after completion, because the model call is a separate operation\.

In Findings, ask which concern comes from the scenario and which recorded action supports the proposed reaction\. On Creator there is no executed conversation behind that reaction\. End with the real question the operator could investigate, rather than presenting generated personas as testimony\.

There is no demo\-only cleanup command\. Blanket deletion can remove needed runs, and Docker volumes may hold data outside a host's `backend/data`, so save the reports and settings you need before a deliberate reset and use [normal shutdown](/rawfish/using#return-to-a-saved-run-and-finish-locally) to preserve data\.
