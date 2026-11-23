---
title: "Class: AuthoringLiteralFact"
---

<a id="class&#45;authoringliteralfact"></a>

One allowed literal plus producer\-owned documentation\.

## Properties {#properties}

### description {#description}

```ts
readonly description: string | undefined;
```

Return variant\-specific producer documentation\.

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

### value\(\) {#value}

```ts
value(): AuthoringLiteral;
```

Return the exact literal admitted by the generated node\.

#### Returns {#returns-2}

[`AuthoringLiteral`](/pale/reference/wasm/classes/AuthoringLiteral)
