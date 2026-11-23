---
title: "Record reference"
---

<a id="record&#45;reference"></a>

Scope's planned records are grouped below by the operations they support\. These field sketches are inputs to the future published schemas, not wire formats callers may already use\. Each record still needs its exact schema, limits, canonicalisation and signature vectors, and fixtures in the owner manifest\. A callable operation also needs membership in that manifest's operation inventory, admission and qualification; publishing a schema creates no command\. [Contracts](/scope/engineering/contracts) explains each family's purpose, consumers and mode\-specific signing authority; the family pages define its behavior\.

Two parts of the declared contract set still lack field sketches here\. The standalone service\-output signer, `ScopeStandaloneOwnerSigningAuthorityV1`, has its required bindings and lifecycle on [Contracts](/scope/engineering/contracts)\. The four retrieval records have accepted meanings on [Retrieval](/scope/engineering/retrieval) but no final schema names or bodies\. Their completion remains part of [contract publication](/scope/engineering/contracts#one-manifest-generated-is-the-only-inventory); this reference does not make those records callable or fill their missing shapes by implication\.

Conventions in every sketch: a field ending in `?` is absent unless its state branch requires it, and `null`, empty strings and sentinel references are invalid; every `*_ref` travels with its `*_sha256`; arrays are bounded, sorted by their schema comparator and free of duplicates; every signed record's canonical digest is SHA\-256 over its RFC 8785 canonical form with the digest and signature members omitted\.

## Resolving context and recording its use {#resolving-context-and-recording-its-use}

[Fields and conventions](/scope/engineering/records/resolving-context-and-recording-its-use) for context requirements, resolve requests, signed bundles, exact reads, use reports and receipts\.

## Admission, trust and authority {#admission-trust-and-authority}

[Fields and conventions](/scope/engineering/records/admission-trust-and-authority) for caller grants, trust and recovery records, revocations, checkpoints and authority mutations\.

## Importing an owner snapshot {#importing-an-owner-snapshot}

[Fields and conventions](/scope/engineering/records/importing-an-owner-snapshot) for delegations, import admission, profiles, staged chunks and import receipts\.

## Execution episodes {#execution-episodes}

[Fields and conventions](/scope/engineering/records/execution-episodes) for the deferred episode open, handoff binding, expiry and revision records\.

## Research exports {#research-exports}

[Fields and conventions](/scope/engineering/records/research-exports) for research requests and the minimised evidence Scope returns\.

## Improvement proposals {#improvement-proposals}

[Fields and conventions](/scope/engineering/records/improvement-proposals) for cycle checkpoints, scoring and memory proposals, releases and equivalence evidence\.

Part of [Scope engineering](/scope/engineering)\.
