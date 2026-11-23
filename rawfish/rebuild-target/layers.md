---
title: "RawFish's layers"
---

<a id="rawfish&#45;s&#45;layers"></a>

RawFish's design lets another product ask for the part of a simulation its question needs\. The rebuild's design has three layers, each defined once: a swarm simulation, an intervention and counterfactual comparison, and the lanes\. The [rebuild contract](/rawfish/rebuild-target) does not define the layers yet, and the prototype in this repository is not layered this way, so read this page as the design and [architecture](/rawfish/architecture) for what the prototype does\.

## The swarm simulation runs a world {#the-swarm-simulation-runs-a-world}

In the design it takes a prepared world, built from the source material a request names with the scenario, cohorts and limits chosen for the run, and a seed schedule\. It returns a run: its state, artifacts, findings and the record of what the simulated agents did\. The agents are generated personas, so what they do generates hypotheses to investigate and says nothing about a real population\. Today the Creator lane runs no swarm: its runner writes a deterministic completion marker\.

## The intervention and counterfactual layer compares arms {#the-intervention-and-counterfactual-layer-compares-arms}

In the design it takes one declared thing to vary in the same simulated world, a baseline arm and one or more varied arms, and runs the arms on a shared seed schedule so that what differs between them is the declared change and not the draw of the dice\. It returns a contrast between the arms with its spread\. A contrast between arms is an intervention contrast and not an identified causal effect\. Today the prototype declares baseline, counterfactual and sensitivity variants, where a counterfactual variant names the base variant it differs from, and it has endpoints that compare saved statistical settings; the catalogue's analysis settings keep counterfactual analysis disabled\. The comparison layer is not built and gets its own contract; the rebuild contract's list of retired surfaces bars the prototype's retired counterfactual handlers from returning, and the layer is a separate operation\.

## The lanes supply a domain's questions {#the-lanes-supply-a-domain-s-questions}

A lane supplies a domain's questions, cohorts, scenario fields, report sections and caveats; the domains are such as a creator announcement, an internal policy or a public policy\. In the design a lane never reimplements the comparison, and the comparison never reimplements the swarm, so each mechanism has one home and one set of checks\. Today three lanes register through manifests and adapters, and a fourth needs cockpit changes as well; [Extending RawFish](/rawfish/contributing/lanes) shows how\.

## What a caller supplies and receives {#what-a-caller-supplies-and-receives}

In the design a caller asks at the layer its question needs, through an SDK or API, the command line or an agent protocol, and none of these exists yet\. The caller supplies a request that names its inputs and its limits: what the evidence is allowed to support, the budget and what happens if an input or provider becomes unavailable\. A change to an existing run names the revision it expects, so an old request cannot overwrite newer work\. The caller receives references to the run, its state, artifacts, findings, evaluations and the record of a cancellation\. A run, an arm, a claim and a finding are each addressable, so a caller can refer to one on its own, for example a planning tool that tries a direction beside another, or a work record that links a rehearsal to the proposal it tested\. Today the cockpit supplies an expected hash for saving a settings patch, but the backend accepts patches without it\.

## Components a host renders {#components-a-host-renders}

In the design RawFish serves components with the descriptors that say how to render them, and the host surface renders them: a run, a cohort, a claim with its evidence or a comparison of two arms can appear as a card in a chat or another host, with the same fields, staleness and access filtering\. The standalone cockpit is a composition of those components\. Today the cockpit is one Vue application\.
