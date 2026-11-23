---
title: "Class: AuthoringNavigation"
---

<a id="class&#45;authoringnavigation"></a>

Semantic navigation result for one exact admitted occurrence\.

## Properties {#properties}

### alternativesTruncated {#alternativestruncated}

```ts
readonly alternativesTruncated: boolean;
```

Report whether the API ceiling omitted completion alternatives\.

-----

### referencesTruncated {#referencestruncated}

```ts
readonly referencesTruncated: boolean;
```

Report whether the API ceiling omitted source references\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### alternatives\(\) {#alternatives}

```ts
alternatives(): AuthoringIdentity[];
```

Return all bounded same\-namespace completion alternatives\.

#### Returns {#returns-1}

[`AuthoringIdentity`](/pale/reference/wasm/classes/AuthoringIdentity)\[\]

-----

### definition\(\) {#definition}

```ts
definition(): AuthoringSourceLocation | undefined;
```

Return the canonical definition when the closure contains one\.

#### Returns {#returns-2}

[`AuthoringSourceLocation`](/pale/reference/wasm/classes/AuthoringSourceLocation) \| `undefined`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-3}

`void`

-----

### identity\(\) {#identity}

```ts
identity(): AuthoringIdentity | undefined;
```

Return the resolved identity, when the coordinate is semantic\.

#### Returns {#returns-4}

[`AuthoringIdentity`](/pale/reference/wasm/classes/AuthoringIdentity) \| `undefined`

-----

### occurrenceRole\(\) {#occurrencerole}

```ts
occurrenceRole(): 
  | AuthoringOccurrenceRole
  | undefined;
```

Return the semantic role of the queried occurrence\.

#### Returns {#returns-5}

\| [`AuthoringOccurrenceRole`](/pale/reference/wasm/enumerations/AuthoringOccurrenceRole)
\| `undefined`

-----

### references\(\) {#references}

```ts
references(): AuthoringSourceLocation[];
```

Return all retained references in deterministic order\.

#### Returns {#returns-6}

[`AuthoringSourceLocation`](/pale/reference/wasm/classes/AuthoringSourceLocation)\[\]
