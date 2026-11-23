---
title: "Class: WorkspaceComparison"
---

<a id="class&#45;workspacecomparison"></a>

Opaque verified comparison of two admitted workspaces\.

## Accessors {#accessors}

### affectedCount {#affectedcount}

#### Get Signature {#get-signature}

```ts
get affectedCount(): number;
```

Exact affected\-subject count\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### changeRootCount {#changerootcount}

#### Get Signature {#get-signature-1}

```ts
get changeRootCount(): number;
```

Exact change\-root count\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### currentPrincipalUniverseDigest {#currentprincipaluniversedigest}

#### Get Signature {#get-signature-2}

```ts
get currentPrincipalUniverseDigest(): string;
```

Principal\-relative current universe digest\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### currentSemanticIrDigest {#currentsemanticirdigest}

#### Get Signature {#get-signature-3}

```ts
get currentSemanticIrDigest(): string;
```

Current semantic\-IR digest\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### priorPrincipalUniverseDigest {#priorprincipaluniversedigest}

#### Get Signature {#get-signature-4}

```ts
get priorPrincipalUniverseDigest(): string;
```

Principal\-relative predecessor universe digest\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### priorSemanticIrDigest {#priorsemanticirdigest}

#### Get Signature {#get-signature-5}

```ts
get priorSemanticIrDigest(): string;
```

Predecessor semantic\-IR digest\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### receiptDigest {#receiptdigest}

#### Get Signature {#get-signature-6}

```ts
get receiptDigest(): string;
```

Exact derivation\-receipt digest\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### unaffectedCount {#unaffectedcount}

#### Get Signature {#get-signature-7}

```ts
get unaffectedCount(): number;
```

Exact unaffected\-subject count\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

## Methods {#methods}

### changeRoots\(\) {#changeroots}

```ts
changeRoots(offset: number, limit: number): WorkspaceChangeRootPage;
```

Project one bounded page of exact change roots\.

#### Parameters {#parameters}

<Heading level={5} id="offset" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns-8}

[`WorkspaceChangeRootPage`](/pale/reference/js/classes/WorkspaceChangeRootPage)

-----

### compares\(\) {#compares}

```ts
compares(prior: PortableWorkspaceCompilation, current: PortableWorkspaceCompilation): boolean;
```

Test whether this comparison retains these exact ordered compilations\.

Equal public digests do not substitute for exact opaque source custody\.
This check grants no disclosure or runtime authority\.

#### Parameters {#parameters-1}

<Heading level={5} id="prior" className="scroll-mt-(--scroll-mt)">prior</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="current" className="scroll-mt-(--scroll-mt)">current</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-9}

`boolean`

-----

### compareSubject\(\) {#comparesubject}

```ts
compareSubject(subject: WorkspaceSubject): WorkspaceSubjectComparison;
```

Compare one subject's presence and typed output in this retained pair\.

A compiler\-produced subject from another comparison is also accepted;
absence from both sides is a successful result\. This synchronous query
copies at most two selected facts and their encoded projection, not a
fixed byte bound\. It does not recompile, traverse impact or observe native
state\. Inspect dependency impact separately with `impacts` or `explain`\.

#### Parameters {#parameters-2}

<Heading level={5} id="subject" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

#### Returns {#returns-10}

[`WorkspaceSubjectComparison`](/pale/reference/js/classes/WorkspaceSubjectComparison)

-----

### contributingRoots\(\) {#contributingroots}

```ts
contributingRoots(
   subject: WorkspaceSubject, 
   limit: number, 
   after?: 
  | WorkspaceContributingRootsCursor
  | null
): WorkspaceContributingRootsPage;
```

Page all verified change roots contributing to one current subject\.

The limit must be an integer from 0 through 65535\. The SDK applies its
64\-row default and 256\-row cap\. Resume with the exact ordered compilation
pair, receipt, full subject and raw limit, even when another limit would
normalize identically\. Fresh equal\-digest compilations are not substitutes\.
This reuses the verified contribution relation, not the preferred path
chosen by explanation\. Row limits do not bound bytes, time or aggregate
retained memory\. No recipient or native\-effect authority is admitted\.

# Errors {#errors}

Invalid numbers produce `InvalidArg`\. Continuation and internal failures
retain the SDK\-owned canonical diagnostic\.

#### Parameters {#parameters-3}

<Heading level={5} id="subject&#45;1" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="limit&#45;1" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`WorkspaceContributingRootsCursor`](/pale/reference/js/classes/WorkspaceContributingRootsCursor)
\| `null`

#### Returns {#returns-11}

[`WorkspaceContributingRootsPage`](/pale/reference/js/classes/WorkspaceContributingRootsPage)

-----

### correspondOrganizationRecord\(\) {#correspondorganizationrecord}

```ts
correspondOrganizationRecord(
   selectedSide: OrganizationComparisonSide, 
   selected: OrganizationRecordHandle, 
   maximumInspected: number, 
   maximumCopiedBytes: number, 
   after?: 
  | OrganizationCorrespondenceCursor
  | null
): OrganizationCorrespondence;
```

Find the selected record's canonical key in the other retained compilation\.
Visits and copied UTF\-8 payload are separate SDK bounds, not time or total memory limits\.
A failure publishes no continuation; keep the original cursor for retry\.
This does not authorize recipient delivery or equate source identities across generations\.

# Errors {#errors-1}

Preserves SDK pair, record, side, limit and copy diagnostics\. Malformed numeric
transport limits reject as `InvalidArg` before the SDK query\.

#### Parameters {#parameters-4}

<Heading level={5} id="selectedside" className="scroll-mt-(--scroll-mt)">selectedSide</Heading>

[`OrganizationComparisonSide`](/pale/reference/js/enumerations/OrganizationComparisonSide)

<Heading level={5} id="selected" className="scroll-mt-(--scroll-mt)">selected</Heading>

[`OrganizationRecordHandle`](/pale/reference/js/classes/OrganizationRecordHandle)

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`OrganizationCorrespondenceCursor`](/pale/reference/js/classes/OrganizationCorrespondenceCursor)
\| `null`

#### Returns {#returns-12}

[`OrganizationCorrespondence`](/pale/reference/js/classes/OrganizationCorrespondence)

-----

### explain\(\) {#explain}

```ts
explain(subject: WorkspaceSubject): WorkspaceExplanation;
```

Explain one subject obtained from this comparison\.

# Errors {#errors-2}

Returns a native error with separate `diagnostic` bytes when the subject
did not originate in this comparison coordinate\.

#### Parameters {#parameters-5}

<Heading level={5} id="subject&#45;2" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

#### Returns {#returns-13}

[`WorkspaceExplanation`](/pale/reference/js/classes/WorkspaceExplanation)

-----

### impacts\(\) {#impacts}

```ts
impacts(offset: number, limit: number): WorkspaceImpactPage;
```

Project one bounded page of the complete impact partition\.

#### Parameters {#parameters-6}

<Heading level={5} id="offset&#45;1" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit&#45;2" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns-14}

[`WorkspaceImpactPage`](/pale/reference/js/classes/WorkspaceImpactPage)

-----

### subjects\(\) {#subjects}

```ts
subjects(limit: number, after?: 
  | WorkspaceComparisonSubjectCursor
  | null): WorkspaceComparisonSubjectPage;
```

Discover selected identities in either input, including prior\-only subjects\.

The limit must be an integer from 0 through 65535; the SDK owns the
64\-row default and 256\-row cap\. Resume with the exact ordered input pair,
receipt and raw limit\. A missing cursor starts a new enumeration\.
This reuses bounded fact\-map ranges, without a full union, graph walk,
receipt rebuild or eager value comparison\. The row limit and fixed copied
identity\-byte ceiling do not bound time or total retained memory\. No
recipient is admitted\.

# Errors {#errors-3}

Invalid numbers produce `InvalidArg`\. Mismatched continuations retain
the SDK\-owned canonical diagnostic and do not silently restart\.

#### Parameters {#parameters-7}

<Heading level={5} id="limit&#45;3" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

<Heading level={5} id="after&#45;2" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`WorkspaceComparisonSubjectCursor`](/pale/reference/js/classes/WorkspaceComparisonSubjectCursor)
\| `null`

#### Returns {#returns-15}

[`WorkspaceComparisonSubjectPage`](/pale/reference/js/classes/WorkspaceComparisonSubjectPage)

-----

### summary\(\) {#summary}

```ts
summary(): WorkspaceComparisonSummary;
```

Snapshot the API\-owned comparison coordinates and partition counts\.

#### Returns {#returns-16}

[`WorkspaceComparisonSummary`](/pale/reference/js/classes/WorkspaceComparisonSummary)
