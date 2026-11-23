---
title: "Using RawFish"
---

<a id="using&#45;rawfish"></a>

This walkthrough is for developers with the actual RawFish reference\-prototype checkout\. It covers local startup, model and memory configuration, one complete Creator session and shutdown\. For editable source, use [the repository setup](/rawfish/prototype#build-and-test); [the runbook](/rawfish/runbook) holds authentication and integration checks, and [architecture](/rawfish/architecture) explains the implementation\. The [rebuild contract](/rawfish/rebuild-target) describes the planned replacement\.

Work through a fictional creator announcement: enter the scenario, save a cohort setting, check the model and read a generated report\. Keep the run so you can compare it with a revised announcement\.

In this prototype, Creator's Simulate step records completion without running agents\. Generate report makes a separate model call to write the report\. Policy lanes use a different runner\. The [fresh rebuild](/rawfish/rebuild-target) is planned and there is no hosted service\.

<Danger>

**Your input can reach the model provider\.** Use nonconfidential material suitable for that provider\. Preview and simulation can send it there\.

</Danger>

## Start the local stack {#start-the-retained-local-stack}

<Info>

**Start from the RawFish checkout\.** You need that checkout, Make, Python 3, Docker with Compose v2 and a running Docker daemon, plus native Ollama\.

</Info>

If you need to work on the source first, see the [developer setup](/rawfish/prototype#build-and-test)\.

From the checkout's root:

```sh
make init
```

This creates `.env.local` and refuses to overwrite an existing file\. Open it and replace `NEO4J_PASSWORD` and `SECRET_KEY`; use at least 32 characters for the secret\. Check the model names and embedding dimension against the models you intend to run\. [Configure the prototype's services](#configure-the-services) explains those choices and the different host and container addresses\.

Start the stack, then inspect it:

```sh
make up
make status
```

The first start can download models and images and build the application\. The recipe runs Ollama on the host and RawFish and Neo4j in Docker\. It probes the model's structured JSON responses, which report generation needs\. If the probe fails, resolve the named model, endpoint or response\-format error before continuing\.

Open `http://localhost:3000/` in your browser to reach Launch\. The backend health endpoint is `http://localhost:5001/health`; use `make logs` to investigate a service that is not ready\. Check the individual health results even if startup prints its final banner\.

This recipe disables authentication and binds ports to loopback\. For changes to authentication or network exposure, use the [developer runbook](/rawfish/runbook#authentication-changes-are-a-developer-deployment-concern)\.

## Configure the services {#configure-the-services}

Configure the model that reads your scenario and writes its report, then choose how the prototype stores the world graph\. In Creator, choosing a model changes report generation\. The Simulate step still records completion without running agents\. Create the settings file in [local startup](#start-the-retained-local-stack) before applying these examples\.

## Choose the model that receives the input {#choose-the-model-that-receives-the-input}

For native Ollama on the host:

```env
RAWFISH_LLM_PROVIDER_MODE=local_ollama
RAWFISH_LLM_MODEL=qwen3-coder:30b
RAWFISH_LLM_BASE_URL=http://localhost:11434/v1
```

For another local server with an OpenAI\-compatible API:

```env
RAWFISH_LLM_PROVIDER_MODE=local_openai_compatible
RAWFISH_LLM_MODEL=qwen2.5:7b
RAWFISH_LLM_BASE_URL=http://localhost:8000/v1
```

Neither local mode needs an external provider key\. Replace the model name with one your server provides and your machine can run\. The examples do not install models\. Preflight checks availability and the structured responses report generation needs\.

To use an external provider instead:

```env
RAWFISH_LLM_PROVIDER_MODE=external
RAWFISH_LLM_PROVIDER=openai
RAWFISH_LLM_MODEL=gpt-4o-mini
RAWFISH_LLM_API_KEY=<provider-key>
RAWFISH_LLM_BASE_URL=https://api.openai.com/v1
RAWFISH_CONTAINER_LLM_BASE_URL=https://api.openai.com/v1
```

<Danger>

**External processing\.** Your input can leave the machine when you use an external provider\. Use only suitable, nonconfidential material\.

</Danger>

Preflight shows an estimated cost when the price is known, or `cost_unavailable` when it is not\.

The `make up` recipe still starts native Ollama and Neo4j and pulls its configured local models\. Changing the router mode does not remove those dependencies or convert the recipe into another deployment\.

## Distinguish the host address from the container address {#distinguish-the-host-address-from-the-container-address}

On the host, `localhost:11434` reaches native Ollama\. Inside a container, `localhost` points back to that container\. The local recipe therefore uses the host gateway:

| Caller | Default model address | Override in `.env.local` |
| --- | --- | --- |
| Host\-side RawFish probes | `http://localhost:11434/v1` | `RAWFISH_LLM_BASE_URL` |
| RawFish in Docker | `http://host.docker.internal:11434/v1` | `RAWFISH_CONTAINER_LLM_BASE_URL` |
| Graphiti in Docker | `http://host.docker.internal:11434/v1` | `RAWFISH_CONTAINER_OPENAI_BASE_URL` |

If you use another local server, set the address for each caller that needs it\. A successful host probe does not mean the container reaches the same service\.

<Info>

**Replace both local addresses\.** The host probes and Docker application have separate endpoint settings\. Changing only the provider and model leaves the local Ollama addresses in place\. Use the chosen provider’s address for both callers\. In a native source run that should use the provider’s default address, clear the stale `RAWFISH_LLM_BASE_URL` and any `LLM_BASE_URL` fallback instead\. The Docker recipe still needs its explicit container override because an empty value selects its local default\.

</Info>

## Choose the graph\-memory arrangement {#choose-the-graph-memory-arrangement}

For source development, `ZEP_MODE=mock` uses a deterministic in\-process store without Neo4j\. Graphiti mode uses Neo4j and its own model, embedding and reranking clients\. These are separate from the RawFish provider router\.

A host\-side Graphiti configuration is:

```env
ZEP_MODE=graphiti
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=<local-password>
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_API_KEY=local-graphiti-key
OPENAI_MODEL=qwen3-coder:30b
OPENAI_EMBEDDING_MODEL=nomic-embed-text
OPENAI_EMBEDDING_DIM=768
OPENAI_RERANKING_MODEL=qwen3-coder:30b
```

The `OPENAI_*` names belong to Graphiti's client; the shown address is local\. Match the embedding dimension to the model you use\. The prototype's locked Neo4j dependency falls outside Graphiti's declared supported range, so Graphiti mode remains experimental\.

The Docker recipe fixes `ZEP_MODE=graphiti` and uses `bolt://neo4j:7687` inside its network\. Setting `ZEP_MODE=mock` in the host file does not switch that recipe to mock memory\. Developers changing this setup can follow the [configuration reference](/rawfish/runbook#configuration-sources-and-caller-boundaries)\.

## Follow the failure to the dependency {#follow-the-failure-to-the-dependency}

| Symptom | Check |
| --- | --- |
| `missing_external_key` | Supply the key for the chosen external provider, or choose a local mode\. |
| Local model request times out | Confirm the server is running, the model is installed and this caller uses the right address\. |
| Graphiti unavailable | Check Neo4j and Graphiti's model, embedding and reranking settings\. A working RawFish model call tests a different client\. |
| API requests return 401 | In an auth\-enabled source build, match the frontend and backend keys\. See the [authentication reference](/rawfish/runbook#authentication-changes-are-a-developer-deployment-concern)\. |
| Scale guard blocks launch | Review ensemble size, stakeholders and rounds before increasing the cap\. |

<Danger>

**The browser key does not protect a shared service\.** In a source build, the frontend's `VITE_API_KEY` is included in the JavaScript delivered to the browser\. Matching it to the backend key makes prototype requests work; it does not authenticate separate people\. The local recipe exposes its ports only on loopback\. It does not supply sign\-in or separate users' data for a shared service\.

</Danger>

When the services are ready, continue with [choosing the lane](#choose-the-lane-and-keep-the-draft-in-view)\.

## Choose the lane and keep the draft in view {#choose-the-lane-and-keep-the-draft-in-view}

Launch offers **Creator**, **Internal policy** and **Public policy**\. Each supplies different scenario fields, groups and report questions\. Use Internal policy for workplace changes and Public policy for civic decisions\. Choose **Creator** and **Paste** for this walkthrough\.

The other source markers, `cached`, `live` and `graph`, do not connect an upload, cache, feed or graph import\. Start with pasted text\. Drafts stay in page memory until a run is created: reloading or opening the draft address elsewhere loses the text and returns to Launch\. Changing lanes after saving requires a new run\.

The cockpit keeps draft text out of URLs and refuses links that carry it, but it cannot remove text you have already copied into an address or browser history\.

## Continue through the six cockpit steps {#continue-through-the-six-cockpit-steps}

Paste this fictional announcement on Launch:

```text
Our channel is replacing its weekly long-form explainer with short daily clips next month. The full archive stays available, but new explainers stop. We have a fixed production budget and want newcomers to understand the work without losing the depth regular viewers value.

Stress question: where does this announcement leave viewers unsure what they will receive?
Assumptions: regular viewers value the explanations; newcomers need a shorter entrance; the team cannot produce both formats daily.
Success: viewers can distinguish the new clips from the archive and find the explanation behind a clip.
Failure modes: regular viewers read the change as abandonment; a newcomer sees an excerpt without its qualification.
What could change a view: a clear route to the longer explanation and an honest account of what production will stop.
```

Choose **preview parse** to inspect the suggested title, question and cohorts, then **Draft scenario**\. **parse seed** in Scenario parses the current text again\. This prototype provides one text area and a cohort plan, so keep the full scenario text alongside your run\.

1. **Scenario:** check **Stress question**, choose **paste** under **Source posture**, then **Build the world** to open Build\.
2. **Build:** choose **Build the world** again to create and prepare the saved run\. A run identifier and world panel should appear\. Here the graph shows the run and its configured stakeholder cohorts joined by `TESTS_AGAINST` relationships; it is not a world or influence network inferred from the source\. Inspect those settings, then choose **Tune cohorts**\.
3. **Cohorts:** inspect the groups and save a configuration change using the next section before launch\.
4. **Preflight:** check provider mode, model and address, then **refresh preflight**\. Review readiness, scale, token estimate, latency and available external cost\. Choose **Launch swarm** when ready\.
5. **Simulate:** follow status and the console\. Creator completes through its deterministic marker\. If the run halts, inspect the error; **duplicate as draft** makes an editable copy\. There is no Stop control\.
6. **Findings:** after completion, open **Read** and choose **Generate report** if none is loaded\. Wait for the background job, then inspect the tagged claims\. Simulation completion and report generation are separate steps\.

The initial cohorts are **Long\-time fans**, **Gen\-Z skeptics** and **Casual viewers**\. These are authored archetypes rather than measured audience groups\. For this example, look for ambiguity about what happens to the clips, archive and future explainers\.

## Save a configuration or create a variant {#save-a-configuration-or-create-a-variant}

Before launch, select **Long\-time fans**\. Change **Sentiment bias** from `0` to `-0.2`, then choose **Save patch**\. Wait for the settings hash to refresh without an error\. The cockpit prepares the run again after a saved edit; refresh preflight before launching\.

The workbench also shows activity, influence and active hours, plus opinion\-drift controls in policy lanes\. Values carry origin text, such as your input, a lane default, a prior or a random draw\. An origin tells you where a value came from, not whether it measures a real population\. The cockpit has no per\-field lock control\.

<Note>

**A saved setting is not an executed experiment\.** For Creator, this saves the changed setting in configuration and completion metadata\. The report prompt does not use that setting, so it is not a sentiment experiment\.

</Note>

**Reseed variant** increments the seed and records the old and new settings in lineage\. It changes and prepares the same run; it does not create a second executable run or report\. Save any field edits first because the seed\-only request does not include them\. Both controls freeze after launch\. Separate variant runs are part of the rebuild design\.

## Read what the run actually supports {#read-what-the-run-actually-supports}

Findings offers **Read**, **Ask** and **Analysis**; the last uses `mode=data` in saved\-run addresses\. [Read the findings](/rawfish/using#read-what-the-run-actually-supports) explains the claim labels\.

Creator’s report proposes reactions without an executed conversation behind them, even when a claim is labelled “simulated observation”\. Check those proposals against the announcement, then take unresolved questions to actual viewers\. A generated quotation is not testimony\.

If report generation fails validation, keep the error and model choice together when diagnosing it\. A successful model call does not necessarily produce a valid report\.

## Compare settings before comparing reactions {#compare-settings-before-comparing-reactions}

Open **Analysis**, then **Compare** and **refresh compare**\. After reseeding, it compares the latest settings with their parent snapshot\. **stat diffs** counts changes\. The **present**, **missing** and **corrupted** buckets reflect settings subjects; they do not establish that two valid reports were compared\.

To compare announcement text, start a second run from Launch\. Keep the first draft and question, but replace “new explainers stop” with “one new long\-form explainer will remain each month; daily clips replace the other weekly editions\.” Align the provider, cohorts and other settings\. Keep both run identifiers and valid reports\.

Read the reports side by side\. Does the monthly explanation change the proposed concern about abandonment? Does ambiguity about the archive remain? This is a manual comparison of separate scenarios, not an automatic paired experiment\. Wording can vary between model calls, and a missing or invalid report leaves the comparison incomplete\. Neither result estimates how many real viewers share a concern\.

## Return to a saved run and finish locally {#return-to-a-saved-run-and-finish-locally}

Launch's **Past runs** list remembers saved run identifiers in this browser\. Opening one loads its lane and phase from the backend\. There is no dedicated Share control\. A saved address carries run identity and cockpit state; it grants no access by itself\. An unsaved draft address does not preserve or transfer the draft text\.

Stop the stack when finished:

```sh
make down
```

This preserves container data and leaves native Ollama running\.

<Danger>

**Purging removes saved data\.** `make purge` removes named volumes, including graph and runner\-state data\. Use it only for a deliberate reset after saving anything you need\.

</Danger>

The prototype does not provide full sensitivity analysis, a counterfactual editor, live action labels or hosted multi\-user use\. Continue with [interpreting the findings](#read-what-the-run-actually-supports) or the [planned workflow](/rawfish/rebuild-target)\.
