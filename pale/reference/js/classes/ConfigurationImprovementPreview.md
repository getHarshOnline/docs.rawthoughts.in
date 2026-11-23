---
title: "Class: ConfigurationImprovementPreview"
---

<a id="class&#45;configurationimprovementpreview"></a>

A reviewable candidate; terminal disposition consumes it without effects\.

## Accessors {#accessors}

### phase {#phase}

#### Get Signature {#get-signature}

```ts
get phase(): ConfigurationImprovementPhase;
```

Current API\-owned phase\.

# Errors {#errors}

Returns a host\-argument error after this stage has been consumed\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementPhase`](/pale/reference/js/enumerations/ConfigurationImprovementPhase)

## Methods {#methods}

### accept\(\) {#accept}

```ts
accept(): ConfigurationImprovementTerminal;
```

Accept for presentation to a separate authority/effect gate\.

# Errors {#errors-1}

Returns a host error if already consumed\. This transition causes no effect\.

#### Returns {#returns-1}

[`ConfigurationImprovementTerminal`](/pale/reference/js/classes/ConfigurationImprovementTerminal)

-----

### baselineProfile\(\) {#baselineprofile}

```ts
baselineProfile(): EffectiveProfileCompilation;
```

Retain the immutable baseline profile for its existing query interface\.

# Errors {#errors-2}

Returns a host error after terminal consumption\.

#### Returns {#returns-2}

[`EffectiveProfileCompilation`](/pale/reference/js/classes/EffectiveProfileCompilation)

-----

### cancel\(\) {#cancel}

```ts
cancel(): ConfigurationImprovementTerminal;
```

Cancel review without asserting a native cancellation\.

# Errors {#errors-3}

Returns a host error if already consumed\. This transition causes no effect\.

#### Returns {#returns-3}

[`ConfigurationImprovementTerminal`](/pale/reference/js/classes/ConfigurationImprovementTerminal)

-----

### candidateProfile\(\) {#candidateprofile}

```ts
candidateProfile(): EffectiveProfileCompilation;
```

Retain the immutable candidate profile without recompiling its source\.

# Errors {#errors-4}

Returns a host error after terminal consumption\.

#### Returns {#returns-4}

[`EffectiveProfileCompilation`](/pale/reference/js/classes/EffectiveProfileCompilation)

-----

### changeRoots\(\) {#changeroots}

```ts
changeRoots(offset: number, limit: number): WorkspaceChangeRootPage;
```

Page the existing change\-root owner without deriving another graph\.

# Errors {#errors-5}

Returns a host error after terminal consumption\.

#### Parameters {#parameters}

<Heading level={5} id="offset" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns-5}

[`WorkspaceChangeRootPage`](/pale/reference/js/classes/WorkspaceChangeRootPage)

-----

### comparisonSummary\(\) {#comparisonsummary}

```ts
comparisonSummary(): WorkspaceComparisonSummary;
```

Project the retained comparison identity and cardinalities\.

# Errors {#errors-6}

Returns a host error after terminal consumption\.

#### Returns {#returns-6}

[`WorkspaceComparisonSummary`](/pale/reference/js/classes/WorkspaceComparisonSummary)

-----

### explain\(\) {#explain}

```ts
explain(subject: WorkspaceSubject): WorkspaceExplanation;
```

Explain a subject through the same retained comparison owner\.

# Errors {#errors-7}

Returns consumed\-handle misuse or the exact API subject diagnostic\.

#### Parameters {#parameters-1}

<Heading level={5} id="subject" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

#### Returns {#returns-7}

[`WorkspaceExplanation`](/pale/reference/js/classes/WorkspaceExplanation)

-----

### impacts\(\) {#impacts}

```ts
impacts(offset: number, limit: number): WorkspaceImpactPage;
```

Page the canonical complete impact partition\.

# Errors {#errors-8}

Returns a host error after terminal consumption\.

#### Parameters {#parameters-2}

<Heading level={5} id="offset&#45;1" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit&#45;1" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns-8}

[`WorkspaceImpactPage`](/pale/reference/js/classes/WorkspaceImpactPage)

-----

### inspectCandidateSubject\(\) {#inspectcandidatesubject}

```ts
inspectCandidateSubject(
   subject: WorkspaceSubject, 
   inputLimit: number, 
   maximumInspected: number, 
   maximumReturned: number, 
   after?: 
  | PortableWorkspaceSubjectInspectionCursor
  | null
): PortableWorkspaceSubjectInspection;
```

Inspect exact candidate source and proof evidence without recompiling\.

The preview retains the candidate compilation that owns this query\. Resume
with the same preview, subject, raw limits, and opaque continuation\. The
returned rows grant no source\-disclosure or configuration\-write authority\.

# Errors {#errors-9}

Invalid limits produce a host\-argument error\. A consumed preview, a cursor
from another owner, or inconsistent retained proof returns its existing error\.

#### Parameters {#parameters-3}

<Heading level={5} id="subject&#45;1" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="inputlimit" className="scroll-mt-(--scroll-mt)">inputLimit</Heading>

`number`

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`PortableWorkspaceSubjectInspectionCursor`](/pale/reference/js/classes/PortableWorkspaceSubjectInspectionCursor)
\| `null`

#### Returns {#returns-9}

[`PortableWorkspaceSubjectInspection`](/pale/reference/js/classes/PortableWorkspaceSubjectInspection)

-----

### markStale\(\) {#markstale}

```ts
markStale(): ConfigurationImprovementTerminal;
```

Mark stale after the caller proves its separately owned coordinate changed\.

# Errors {#errors-10}

Returns a host error if already consumed\. This transition causes no effect\.

#### Returns {#returns-10}

[`ConfigurationImprovementTerminal`](/pale/reference/js/classes/ConfigurationImprovementTerminal)

-----

### reject\(\) {#reject}

```ts
reject(): ConfigurationImprovementTerminal;
```

Reject the candidate without changing any source\.

# Errors {#errors-11}

Returns a host error if already consumed\. This transition causes no effect\.

#### Returns {#returns-11}

[`ConfigurationImprovementTerminal`](/pale/reference/js/classes/ConfigurationImprovementTerminal)

-----

### summary\(\) {#summary}

```ts
summary(): ConfigurationImprovementPreviewSummary;
```

Snapshot exact review coordinates without source or native values\.

# Errors {#errors-12}

Returns a host error after terminal consumption\.

#### Returns {#returns-12}

[`ConfigurationImprovementPreviewSummary`](/pale/reference/js/classes/ConfigurationImprovementPreviewSummary)
