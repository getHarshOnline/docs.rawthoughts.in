---
title: "RawFish"
---

<a id="rawfish"></a>

RawFish rehearses what could follow from a decision before anyone commits to it, while it can still be changed: the problem is seeing where a decision could lead, and how it could go wrong, before it is made\. In RawThoughts' one system it asks the counterfactuals, what could follow if a direction were taken, and it is a local\-first simulation product\. This repository contains its reference prototype: a Flask backend, Vue cockpit, three decision lanes and model\-generated reports\. The rebuild's design has three callable layers, a swarm simulation, an intervention and counterfactual comparison, and the lanes that supply each domain's questions \([layers](/rawfish/rebuild-target/layers)\); this prototype is not layered that way\. It declares baseline, counterfactual and sensitivity variants and compares saved statistical settings; the comparison layer is not built and gets its own contract\. The product is planned for a fresh rebuild; this code provides examples and lessons rather than the rebuild's starting codebase\.

<Info>

**Creator does not run an agent swarm\.** Its runner writes a deterministic completion marker\. A separate model call generates report text without using the evidence catalog or cohort statistical settings\. Generated reactions are hypotheses, not observed audience behavior\.

</Info>

## Choose your next task {#choose-your-next-task}

- [Try the local prototype](/rawfish/using): Start the local stack, save a fictional creator announcement and generate a report with a model\.
- [Understand the architecture](/rawfish/architecture): Follow a run through lane dispatch, configuration, execution and report storage\.
- [Extend a lane](/rawfish/contributing/lanes): Implement an adapter and update the current cockpit's lane\-specific seams\.
- [Check a change](/rawfish/runbook#maintainer-qualification): Choose static checks, tests and model\-backed smoke checks for your change\.

## What the prototype includes {#what-the-prototype-includes}

The cockpit has six steps: Scenario, Build, Cohorts, Preflight, Simulate and Findings\. Creator, Internal policy and Public policy share the browser routes `/` and `/run/:runId?` and dispatch through `/api/sim/use-cases/<lane_id>/...`\. Findings contains Read, Ask and Analysis rather than separate report and chat pages\.

Lane catalogs carry a required `lane_manifest`\. The workbench stores statistical settings, while the provider router supports local Ollama, other local OpenAI\-compatible servers and explicitly configured external providers\. Graphiti uses separate model and memory settings\. Reports carry five claim labels and pass a language check during generation; those checks cannot establish that a generated claim is true\.

[Architecture](/rawfish/architecture) explains the current implementation\. The [rebuild contract](/rawfish/rebuild-target) separates the intended replacement from the prototype's behavior\.

## Build and test {#build-and-test}

To edit this checkout, install:

- Node\.js 20\.19 or later within 20\.x, or 22\.12 or later, matching Vite's supported range\.
- Python `>=3.11,<3.13` and `uv`\.
- Docker and native Ollama if you will use the Docker\-backed local stack\.

From the repository root:

```sh
npm run setup:all
```

Dependency installation does not need a model server\. For the Docker\-backed application, continue with the [local startup guide](/rawfish/using#start-the-retained-local-stack)\. It requires this repository's checkout\.

## Run it {#run-it}

Use two terminals to run editable source on loopback\.

1. **Configure the backend and browser key**
   
   Copy the root settings template if you do not already have `.env`:
   
   ```sh
   cp .env.example .env
   ```
   
   In `.env`, replace `SECRET_KEY` with a random value of at least 32 characters\. Replace `API_KEY` and set `VITE_API_KEY` to that same key\. The backend rejects placeholder keys\. Set `RAWFISH_LLM_BASE_URL` and `RAWFISH_LLM_MODEL` to an available model server and model\.
   
   Create `frontend/.env.local` with the same `VITE_API_KEY`\. The backend loads the root `.env`; Vite loads environment files under `frontend/`\. Restart Vite after changing its file\. See the [authentication reference](/rawfish/runbook#authentication-changes-are-a-developer-deployment-concern) before changing network exposure\.

2. **Start the backend**
   
   From the repository root:
   
   ```sh
   npm run backend
   ```
   
   The default backend port is 5001\.

3. **Start the frontend**
   
   In a second terminal, starting at the repository root:
   
   ```sh
   cd frontend
   npm exec -- vite --host 127.0.0.1
   ```
   
   Open `http://127.0.0.1:3000/`\. Vite forwards `/api` requests to the backend\. If the page loads but API requests fail, check that the backend is running and the browser key matches `API_KEY`\.

<Warning>

**The browser key is readable\.** Vite includes `VITE_API_KEY` in delivered JavaScript\. Matching it to the backend key enables prototype requests; it does not authenticate separate users\.

</Warning>

For a deployment change, read [worker count, API origins and execution limits](/rawfish/runbook#deployment-boundaries)\.

Continue with [the cockpit walkthrough](/rawfish/using#choose-the-lane-and-keep-the-draft-in-view)\. [Service configuration](/rawfish/using#configure-the-services) explains model choice and graph memory\.

## Choose a provider {#choose-a-provider}

Local modes need no external provider key\. External mode requires an explicit provider, model and key\. Preflight checks readiness and shows an estimated cost when the price is known\. An unknown price stays `cost_unavailable`\.

RawFish's provider router does not configure Graphiti's model, embedding or reranking clients\. Follow the [model and memory settings](/rawfish/using#configure-the-services) for the client you are changing\.

## Verify the configured checkout {#verify-the-configured-checkout}

The complete check makes real local\-model requests\. Start Ollama with the model selected by `RAWFISH_LLM_MODEL`, then run from the repository root:

```sh
make ci
```

This runs static gates, backend and frontend tests, the frontend build, desktop and mobile browser smoke, mock smoke, a provider probe and the required local report smoke\. The last two load the root `.env.local` when present and require local Ollama even if your application uses another provider\. They do not install or start the model\.

For a focused change, choose a check from [the runbook](/rawfish/runbook#maintainer-qualification)\. To see what the prototype actually produces, [follow the Creator example](/rawfish/using#read-what-the-run-actually-supports)\.

## Licence and attribution {#licence-and-attribution}

RawFish is a modified version of [MiroFish](https://github.com/666ghj/MiroFish), licensed under GNU AGPL\-3\.0\. The [LICENSE](/rawfish/source/LICENSE) is unchanged, and RawFish's modifications are AGPL\-3\.0\-or\-later as [LICENSE\-ADDITIONS\.md](/rawfish/source/LICENSE-ADDITIONS) states\. [CITATION\.cff](/rawfish/source/CITATION-cff) credits MiroFish and OASIS\. If you operate a modified version as a network service, AGPL section 13 requires a source offer to its users\.

Commercial use is permitted under the applicable licence\. Alternative terms for RawFish's own modifications and additions require a separate written agreement with RawThoughts Enterprises Private Limited, which can grant them only for material it is entitled to relicense and never for the upstream code; this repository grants none\. The self\-hosted Noto Sans and JetBrains Mono fonts keep their SIL Open Font License 1\.1 texts in `THIRD_PARTY_LICENSES`, as [NOTO\-SANS\-OFL](/rawfish/assets/THIRD_PARTY_LICENSES/NOTO-SANS-OFL) and [JETBRAINS\-MONO\-OFL](/rawfish/assets/THIRD_PARTY_LICENSES/JETBRAINS-MONO-OFL)\. See [NOTICE](/rawfish/assets/NOTICE) for ownership, [CITATION\.cff](/rawfish/source/CITATION-cff) for citation and [CONTRIBUTING\.md](/rawfish/source/CONTRIBUTING-md) for contribution requirements\. Outside contributions remain closed pending review of the [draft agreement](/rawfish/source/CLA-md) and a way to record acceptance\.
