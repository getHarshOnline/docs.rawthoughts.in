---
title: "Class: OrganizationCorrespondence"
---

<a id="class&#45;organizationcorrespondence"></a>

One bounded query result retaining its comparison pair and original selection\.

## Accessors {#accessors}

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature}

```ts
get copiedStringBytes(): number;
```

SDK returned UTF\-8 payload, excluding retained owners and repeated getter copies\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-1}

```ts
get inspected(): number;
```

Candidate keys examined, including nonmatches\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### selected {#selected}

#### Get Signature {#get-signature-2}

```ts
get selected(): OrganizationRecordHandle;
```

Independently retain the original record, without reconstructing its identity\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationRecordHandle`](/pale/reference/js/classes/OrganizationRecordHandle)

-----

### selectedSide {#selectedside}

#### Get Signature {#get-signature-3}

```ts
get selectedSide(): OrganizationComparisonSide;
```

Side supplying the original selection\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationComparisonSide`](/pale/reference/js/enumerations/OrganizationComparisonSide)

-----

### state {#state}

#### Get Signature {#get-signature-4}

```ts
get state(): OrganizationCorrespondenceState;
```

Copy the bounded result projection; handles retain their original owners\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationCorrespondenceState`](/pale/reference/js/type-aliases/OrganizationCorrespondenceState)

## Methods {#methods}

### belongsTo\(\) {#belongsto}

```ts
belongsTo(comparison: WorkspaceComparison): boolean;
```

Exact ordered comparison pair and receipt membership\.

#### Parameters {#parameters}

<Heading level={5} id="comparison" className="scroll-mt-(--scroll-mt)">comparison</Heading>

[`WorkspaceComparison`](/pale/reference/js/classes/WorkspaceComparison)

#### Returns {#returns-5}

`boolean`
