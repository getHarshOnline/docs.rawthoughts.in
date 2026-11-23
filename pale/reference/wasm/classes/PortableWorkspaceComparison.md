---
title: "Class: PortableWorkspaceComparison"
---

<a id="class&#45;portableworkspacecomparison"></a>

Opaque comparison and retained proof owner for two workspace handles\.

## Properties {#properties}

### affectedCount {#affectedcount}

```ts
readonly affectedCount: number;
```

Number of current subjects reachable from a root\.

-----

### changeRootCount {#changerootcount}

```ts
readonly changeRootCount: number;
```

Number of exact source\-change roots\.

-----

### currentPrincipalUniverseDigest {#currentprincipaluniversedigest}

```ts
readonly currentPrincipalUniverseDigest: string;
```

Principal\-relative current universe digest\.

-----

### currentSemanticIrDigest {#currentsemanticirdigest}

```ts
readonly currentSemanticIrDigest: string;
```

Current semantic\-IR digest\.

-----

### priorPrincipalUniverseDigest {#priorprincipaluniversedigest}

```ts
readonly priorPrincipalUniverseDigest: string;
```

Principal\-relative predecessor universe digest\.

-----

### priorSemanticIrDigest {#priorsemanticirdigest}

```ts
readonly priorSemanticIrDigest: string;
```

Predecessor semantic\-IR digest\.

-----

### receiptDigest {#receiptdigest}

```ts
readonly receiptDigest: string;
```

Domain\-separated identity of the verified derivation receipt\.

-----

### unaffectedCount {#unaffectedcount}

```ts
readonly unaffectedCount: number;
```

Number of current subjects outside every root closure\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### changeRoots\(\) {#changeroots}

```ts
changeRoots(offset: number, limit: number): WorkspaceChangeRootPage;
```

Project one bounded page of exact change roots\.

Offset and limit must be JavaScript numbers representing exact integers\.
The offset range is `0..=u32::MAX`; the limit range is `0..=u16::MAX`\.
Invalid values return a host error instead of being coerced\.

# Errors {#errors}

Returns a native `Error` when either page coordinate is not an exact
integer in its declared range\.

#### Parameters {#parameters}

<Heading level={5} id="offset" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns-1}

[`WorkspaceChangeRootPage`](/pale/reference/wasm/classes/WorkspaceChangeRootPage)

-----

### compareSubject\(\) {#comparesubject}

```ts
compareSubject(subject: WorkspaceSubject): WorkspaceSubjectComparison;
```

Compare the typed outputs for one full subject identity\.

Membership is separate from equality and dependency impact\. A valid
subject from another compilation can be absent from both sides\.
This synchronous call copies up to two facts and encodes the answer;
it does not provide a fixed byte or elapsed\-time bound\.

A valid supplied subject handle is consumed\. Use the result's `subject()`
method to obtain a new copy for another query\.

# Errors {#errors-1}

Returns a host error for a missing, freed, or wrong\-class subject without
retaining a borrow of this comparison\.

#### Parameters {#parameters-1}

<Heading level={5} id="subject" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/wasm/classes/WorkspaceSubject)

#### Returns {#returns-2}

[`WorkspaceSubjectComparison`](/pale/reference/wasm/classes/WorkspaceSubjectComparison)

-----

### explain\(\) {#explain}

```ts
explain(subject: WorkspaceSubject): WorkspaceExplanation;
```

Explain a full subject identity against this retained comparison\.

A valid subject from another compilation is accepted\. If this pair does
not contain it, the answer is `NotPresent`, not an identity error\.

# Errors {#errors-2}

Returns a native `Error` with separate structured `diagnostic` data if
admitted proof contradicts its comparison identities or causal invariants\.

#### Parameters {#parameters-2}

<Heading level={5} id="subject&#45;1" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/wasm/classes/WorkspaceSubject)

#### Returns {#returns-3}

[`WorkspaceExplanation`](/pale/reference/wasm/classes/WorkspaceExplanation)

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-4}

`void`

-----

### impacts\(\) {#impacts}

```ts
impacts(offset: number, limit: number): WorkspaceImpactPage;
```

Project one bounded page of the complete impact partition\.

Offset and limit must be JavaScript numbers representing exact integers\.
The offset range is `0..=u32::MAX`; the limit range is `0..=u16::MAX`\.
Invalid values return a host error instead of being coerced\.

# Errors {#errors-3}

Returns a native `Error` when either page coordinate is not an exact
integer in its declared range\.

#### Parameters {#parameters-3}

<Heading level={5} id="offset&#45;1" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit&#45;1" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns-5}

[`WorkspaceImpactPage`](/pale/reference/wasm/classes/WorkspaceImpactPage)
