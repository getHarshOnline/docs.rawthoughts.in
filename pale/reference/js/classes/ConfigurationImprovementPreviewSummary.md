---
title: "Class: ConfigurationImprovementPreviewSummary"
---

<a id="class&#45;configurationimprovementpreviewsummary"></a>

Complete owned summary with exact API bytes and separately typed coordinates\.

Counts follow \[`api::PortableWorkspaceComparison`\]'s complete disjoint
impact partition\. This value carries no source bytes or effect authority\.

## Accessors {#accessors}

### affectedCount {#affectedcount}

#### Get Signature {#get-signature}

```ts
get affectedCount(): number;
```

Number of affected subjects in the complete impact partition\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### baselinePrincipalUniverseDigest {#baselineprincipaluniversedigest}

#### Get Signature {#get-signature-1}

```ts
get baselinePrincipalUniverseDigest(): string;
```

Baseline admitted\-universe identity\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### baselineWorkspaceAdmissionEvidenceDigest {#baselineworkspaceadmissionevidencedigest}

#### Get Signature {#get-signature-2}

```ts
get baselineWorkspaceAdmissionEvidenceDigest(): string;
```

Baseline admission\-evidence frontier\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### baselineWorkspaceSemanticIrDigest {#baselineworkspacesemanticirdigest}

#### Get Signature {#get-signature-3}

```ts
get baselineWorkspaceSemanticIrDigest(): string;
```

Baseline workspace semantic\-IR identity\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidateCompositionPlanDigest {#candidatecompositionplandigest}

#### Get Signature {#get-signature-4}

```ts
get candidateCompositionPlanDigest(): string;
```

Candidate composition\-proof identity\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidateInstanceDigest {#candidateinstancedigest}

#### Get Signature {#get-signature-5}

```ts
get candidateInstanceDigest(): string;
```

Candidate private instance identity, not readiness\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidatePackageSemanticIrDigest {#candidatepackagesemanticirdigest}

#### Get Signature {#get-signature-6}

```ts
get candidatePackageSemanticIrDigest(): string;
```

Candidate admitted Package semantic identity\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidatePrincipalUniverseDigest {#candidateprincipaluniversedigest}

#### Get Signature {#get-signature-7}

```ts
get candidatePrincipalUniverseDigest(): string;
```

Candidate admitted\-universe identity\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidateProfileDigest {#candidateprofiledigest}

#### Get Signature {#get-signature-8}

```ts
get candidateProfileDigest(): string;
```

Candidate effective\-profile identity\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidateSelectedTopologyDigest {#candidateselectedtopologydigest}

#### Get Signature {#get-signature-9}

```ts
get candidateSelectedTopologyDigest(): string;
```

Candidate selected topology identity\.

<Heading level={5} id="returns&#45;9" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidateWorkspaceAdmissionEvidenceDigest {#candidateworkspaceadmissionevidencedigest}

#### Get Signature {#get-signature-10}

```ts
get candidateWorkspaceAdmissionEvidenceDigest(): string;
```

Candidate admission\-evidence frontier\.

<Heading level={5} id="returns&#45;10" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidateWorkspaceSemanticIrDigest {#candidateworkspacesemanticirdigest}

#### Get Signature {#get-signature-11}

```ts
get candidateWorkspaceSemanticIrDigest(): string;
```

Candidate workspace semantic\-IR identity\.

<Heading level={5} id="returns&#45;11" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature-12}

```ts
get canonicalBytes(): Buffer;
```

Exact API\-owned canonical bytes, not a Node serialization\.

<Heading level={5} id="returns&#45;12" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### changeRootCount {#changerootcount}

#### Get Signature {#get-signature-13}

```ts
get changeRootCount(): number;
```

Number of exact change roots\.

<Heading level={5} id="returns&#45;13" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### compositionPlanChange {#compositionplanchange}

#### Get Signature {#get-signature-14}

```ts
get compositionPlanChange(): ConfigurationImprovementCoordinateChange;
```

Composition\-proof transition\.

<Heading level={5} id="returns&#45;14" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementCoordinateChange`](/pale/reference/js/interfaces/ConfigurationImprovementCoordinateChange)

-----

### compositionPlanDigest {#compositionplandigest}

#### Get Signature {#get-signature-15}

```ts
get compositionPlanDigest(): string;
```

Baseline composition\-proof identity\.

<Heading level={5} id="returns&#45;15" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### derivationReceiptDigest {#derivationreceiptdigest}

#### Get Signature {#get-signature-16}

```ts
get derivationReceiptDigest(): string;
```

Exact derivation receipt identity\.

<Heading level={5} id="returns&#45;16" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### executionWorkspaceId {#executionworkspaceid}

#### Get Signature {#get-signature-17}

```ts
get executionWorkspaceId(): string;
```

Selected execution workspace\.

<Heading level={5} id="returns&#45;17" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### instanceChange {#instancechange}

#### Get Signature {#get-signature-18}

```ts
get instanceChange(): ConfigurationImprovementCoordinateChange;
```

Private instance transition, independent of native realization\.

<Heading level={5} id="returns&#45;18" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementCoordinateChange`](/pale/reference/js/interfaces/ConfigurationImprovementCoordinateChange)

-----

### instanceDigest {#instancedigest}

#### Get Signature {#get-signature-19}

```ts
get instanceDigest(): string;
```

Baseline private instance identity, not readiness\.

<Heading level={5} id="returns&#45;19" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### packageSemanticIrChange {#packagesemanticirchange}

#### Get Signature {#get-signature-20}

```ts
get packageSemanticIrChange(): ConfigurationImprovementCoordinateChange;
```

Admitted Package semantic transition\.

<Heading level={5} id="returns&#45;20" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementCoordinateChange`](/pale/reference/js/interfaces/ConfigurationImprovementCoordinateChange)

-----

### packageSemanticIrDigest {#packagesemanticirdigest}

#### Get Signature {#get-signature-21}

```ts
get packageSemanticIrDigest(): string;
```

Baseline admitted Package semantic identity\.

<Heading level={5} id="returns&#45;21" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### profileChange {#profilechange}

#### Get Signature {#get-signature-22}

```ts
get profileChange(): ConfigurationImprovementCoordinateChange;
```

Portable profile transition\.

<Heading level={5} id="returns&#45;22" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementCoordinateChange`](/pale/reference/js/interfaces/ConfigurationImprovementCoordinateChange)

-----

### profileDigest {#profiledigest}

#### Get Signature {#get-signature-23}

```ts
get profileDigest(): string;
```

Baseline effective\-profile identity\.

<Heading level={5} id="returns&#45;23" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### projectId {#projectid}

#### Get Signature {#get-signature-24}

```ts
get projectId(): string;
```

Selected project\.

<Heading level={5} id="returns&#45;24" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### selectedTopologyChange {#selectedtopologychange}

#### Get Signature {#get-signature-25}

```ts
get selectedTopologyChange(): ConfigurationImprovementCoordinateChange;
```

Selected topology transition\.

<Heading level={5} id="returns&#45;25" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementCoordinateChange`](/pale/reference/js/interfaces/ConfigurationImprovementCoordinateChange)

-----

### selectedTopologyDigest {#selectedtopologydigest}

#### Get Signature {#get-signature-26}

```ts
get selectedTopologyDigest(): string;
```

Baseline selected topology identity\.

<Heading level={5} id="returns&#45;26" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### unaffectedCount {#unaffectedcount}

#### Get Signature {#get-signature-27}

```ts
get unaffectedCount(): number;
```

Number of unaffected subjects in the complete impact partition\.

<Heading level={5} id="returns&#45;27" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-28}

```ts
get workspaceId(): string;
```

Principal workspace being reviewed\.

<Heading level={5} id="returns&#45;28" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
