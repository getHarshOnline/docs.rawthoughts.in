---
title: "Class: OrganizationDetailPage"
---

<a id="class&#45;organizationdetailpage"></a>

One typed detail section with its parent, visit count and continuation\.

## Accessors {#accessors}

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature}

```ts
get copiedStringBytes(): number;
```

SDK copied string payload, not all native/JavaScript allocation\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-1}

```ts
get inspected(): number;
```

Actual direct member visits, excluding separately queried nested collections\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-2}

```ts
get isComplete(): boolean;
```

This section exhausted, not the complete record or World\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### parent {#parent}

#### Get Signature {#get-signature-3}

```ts
get parent(): OrganizationDetailParent;
```

Actual typed parent, not a value\-based reconstruction of its member\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationDetailParent`](/pale/reference/js/type-aliases/OrganizationDetailParent)

-----

### record {#record}

#### Get Signature {#get-signature-4}

```ts
get record(): OrganizationRecordHandle;
```

Source lookup remains under the root record's existing source owner\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationRecordHandle`](/pale/reference/js/classes/OrganizationRecordHandle)

-----

### rows {#rows}

#### Get Signature {#get-signature-5}

```ts
get rows(): OrganizationDetailRows;
```

One closed section payload; arrays copy only the current bounded page\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationDetailRows`](/pale/reference/js/type-aliases/OrganizationDetailRows)

## Methods {#methods}

### continuation\(\) {#continuation}

```ts
continuation(): OrganizationDetailCursor | null;
```

Actual section/nested\-parent continuation, or null after exhaustion\.

#### Returns {#returns-6}

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`
