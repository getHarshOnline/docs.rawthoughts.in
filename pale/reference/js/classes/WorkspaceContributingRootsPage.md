---
title: "Class: WorkspaceContributingRootsPage"
---

<a id="class&#45;workspacecontributingrootspage"></a>

Owned roots contributing to one subject in a retained comparison\.

All results keep both compilations alive, including terminal and not\-present
results\. Child getters copy values, not graphs; garbage collection releases
this handle's ownership without changing semantic state\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy the SDK's already\-computed canonical answer without re\-encoding\.
These bytes cannot reconstruct the retained inputs or cursor\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-1}

```ts
get isComplete(): boolean;
```

Whether the contributing\-root set is exhausted\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### state {#state}

#### Get Signature {#get-signature-2}

```ts
get state(): WorkspaceContributingRootsState;
```

Current membership and impact, not a prior/current value comparison\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceContributingRootsState`](/pale/reference/js/enumerations/WorkspaceContributingRootsState)

## Methods {#methods}

### belongsTo\(\) {#belongsto}

```ts
belongsTo(comparison: WorkspaceComparison): boolean;
```

Check exact retained input\-pair and receipt custody, not equal digests\.
Recreating a comparison over the same retained ordered pair is compatible\.

#### Parameters {#parameters}

<Heading level={5} id="comparison" className="scroll-mt-(--scroll-mt)">comparison</Heading>

[`WorkspaceComparison`](/pale/reference/js/classes/WorkspaceComparison)

#### Returns {#returns-3}

`boolean`

-----

### comparison\(\) {#comparison-1}

```ts
comparison(): WorkspaceComparisonSummary;
```

Copy the parent receipt and independently typed prior/current coordinates\.

#### Returns {#returns-4}

[`WorkspaceComparisonSummary`](/pale/reference/js/classes/WorkspaceComparisonSummary)

-----

### continuation\(\) {#continuation}

```ts
continuation(): 
  | WorkspaceContributingRootsCursor
  | null;
```

Retain the next position, or return null after exhaustion\.

#### Returns {#returns-5}

\| [`WorkspaceContributingRootsCursor`](/pale/reference/js/classes/WorkspaceContributingRootsCursor)
\| `null`

-----

### roots\(\) {#roots}

```ts
roots(): WorkspaceChangeRoot[];
```

Copy the contributing roots in canonical root\-digest order\.

#### Returns {#returns-6}

[`WorkspaceChangeRoot`](/pale/reference/js/classes/WorkspaceChangeRoot)\[\]

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Copy the full subject whose current impact relation was queried\.

#### Returns {#returns-7}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
