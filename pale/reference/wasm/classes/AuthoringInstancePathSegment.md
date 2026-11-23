---
title: "Class: AuthoringInstancePathSegment"
---

<a id="class&#45;authoringinstancepathsegment"></a>

One exact path step used for semantic authoring navigation\.

## Properties {#properties}

### fieldValue {#fieldvalue}

```ts
readonly fieldValue: string | undefined;
```

Return the decoded key for a field segment\.

-----

### indexValue {#indexvalue}

```ts
readonly indexValue: bigint | undefined;
```

Return the exact array index as a non\-lossy JavaScript `bigint`\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-1}

`void`

-----

### kind\(\) {#kind}

```ts
kind(): AuthoringInstancePathSegmentKind;
```

Return the exact segment family\.

#### Returns {#returns-2}

[`AuthoringInstancePathSegmentKind`](/pale/reference/wasm/enumerations/AuthoringInstancePathSegmentKind)

-----

### field\(\) {#field}

```ts
static field(value: string): AuthoringInstancePathSegment;
```

Construct one exact field step\.

#### Parameters {#parameters}

<Heading level={5} id="value" className="scroll-mt-(--scroll-mt)">value</Heading>

`string`

#### Returns {#returns-3}

`AuthoringInstancePathSegment`

-----

### index\(\) {#index}

```ts
static index(value: number): AuthoringInstancePathSegment;
```

Construct one exact array\-member step\.

# Errors {#errors}

Returns a native `Error` when the value is not a JavaScript number
representing an integer from zero through `u32::MAX`\.

#### Parameters {#parameters-1}

<Heading level={5} id="value&#45;1" className="scroll-mt-(--scroll-mt)">value</Heading>

`number`

#### Returns {#returns-4}

`AuthoringInstancePathSegment`
