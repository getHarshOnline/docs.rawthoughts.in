---
title: "Class: AuthoringNodeFact"
---

<a id="class&#45;authoringnodefact"></a>

Bounded structural facts for one authoring position\.

## Properties {#properties}

### description {#description}

```ts
readonly description: string | undefined;
```

Return producer documentation for this structural context\.

-----

### format {#format}

```ts
readonly format: string | undefined;
```

Return the optional generated string format\.

-----

### maximum {#maximum}

```ts
readonly maximum: bigint | undefined;
```

Return the inclusive integer upper bound as a non\-lossy `bigint`\.

-----

### maxItems {#maxitems}

```ts
readonly maxItems: bigint | undefined;
```

Return the inclusive collection\-size upper bound as a non\-lossy `bigint`\.

-----

### maxLength {#maxlength}

```ts
readonly maxLength: bigint | undefined;
```

Return the inclusive string\-length upper bound as a non\-lossy `bigint`\.

-----

### minimum {#minimum}

```ts
readonly minimum: bigint | undefined;
```

Return the inclusive integer lower bound as a non\-lossy `bigint`\.

-----

### minItems {#minitems}

```ts
readonly minItems: bigint | undefined;
```

Return the inclusive collection\-size lower bound as a non\-lossy `bigint`\.

-----

### minLength {#minlength}

```ts
readonly minLength: bigint | undefined;
```

Return the inclusive string\-length lower bound as a non\-lossy `bigint`\.

-----

### pattern {#pattern}

```ts
readonly pattern: string | undefined;
```

Return the optional generated string pattern\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### allowedValues\(\) {#allowedvalues}

```ts
allowedValues(): AuthoringLiteralFact[];
```

Return the complete bounded literal vocabulary\.

#### Returns {#returns-1}

[`AuthoringLiteralFact`](/pale/reference/wasm/classes/AuthoringLiteralFact)\[\]

-----

### fields\(\) {#fields}

```ts
fields(): AuthoringFieldFact[];
```

Return every deterministic child\-field fact in stable order\.

#### Returns {#returns-2}

[`AuthoringFieldFact`](/pale/reference/wasm/classes/AuthoringFieldFact)\[\]

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-3}

`void`

-----

### valueKinds\(\) {#valuekinds}

```ts
valueKinds(): AuthoringValueKind[];
```

Return every admitted structural value category in stable order\.

#### Returns {#returns-4}

[`AuthoringValueKind`](/pale/reference/wasm/enumerations/AuthoringValueKind)\[\]
