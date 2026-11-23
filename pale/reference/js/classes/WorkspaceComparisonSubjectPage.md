---
title: "Class: WorkspaceComparisonSubjectPage"
---

<a id="class&#45;workspacecomparisonsubjectpage"></a>

Identities selected on either side of one exact comparison, without values\.

Shared identities appear once\. Both terminal and pending pages retain the
exact input pair\. Use the existing point comparison for membership and values;
identity discovery does not classify impact or source occurrences\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy the SDK's canonical projection without re\-encoding opaque custody\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-1}

```ts
get inspected(): number;
```

Map entries fetched, including at most one look\-ahead entry per side\.
Look\-ahead is charged again on resume; this excludes range\-seek comparisons\.

# Errors {#errors}

Returns a projection error if the count cannot fit the Node ABI\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-2}

```ts
get isComplete(): boolean;
```

Whether both retained subject ranges are exhausted\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### keyComparisons {#keycomparisons}

#### Get Signature {#get-signature-3}

```ts
get keyComparisons(): number;
```

Merge\-head comparisons, excluding comparisons inside the two range seeks\.
This is mechanical work accounting, not semantic or causal identity\.

# Errors {#errors-1}

Returns a projection error if the count cannot fit the Node ABI\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### subjectIdentityBytes {#subjectidentitybytes}

#### Get Signature {#get-signature-4}

```ts
get subjectIdentityBytes(): number;
```

UTF\-8 bytes copied from the variable\-length subject identities\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

## Methods {#methods}

### belongsTo\(\) {#belongsto}

```ts
belongsTo(comparison: WorkspaceComparison): boolean;
```

Check the exact retained ordered input pair and receipt, not equal digests\.
Recreating a comparison over that same retained pair remains compatible\.

#### Parameters {#parameters}

<Heading level={5} id="comparison" className="scroll-mt-(--scroll-mt)">comparison</Heading>

[`WorkspaceComparison`](/pale/reference/js/classes/WorkspaceComparison)

#### Returns {#returns-5}

`boolean`

-----

### comparison\(\) {#comparison-1}

```ts
comparison(): WorkspaceComparisonSummary;
```

Copy the existing comparison summary and its exact prior/current coordinates\.
Its current\-impact counts are not a count of this union's subjects\.

#### Returns {#returns-6}

[`WorkspaceComparisonSummary`](/pale/reference/js/classes/WorkspaceComparisonSummary)

-----

### continuation\(\) {#continuation}

```ts
continuation(): 
  | WorkspaceComparisonSubjectCursor
  | null;
```

Retain the next full subject position, or return null after exhaustion\.

#### Returns {#returns-7}

\| [`WorkspaceComparisonSubjectCursor`](/pale/reference/js/classes/WorkspaceComparisonSubjectCursor)
\| `null`

-----

### subjects\(\) {#subjects}

```ts
subjects(): WorkspaceSubject[];
```

Copy complete identities, once each in canonical subject order\.

#### Returns {#returns-8}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)\[\]
