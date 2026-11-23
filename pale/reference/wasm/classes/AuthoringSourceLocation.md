---
title: "Class: AuthoringSourceLocation"
---

<a id="class&#45;authoringsourcelocation"></a>

Exact source label and path supplied by the compiler, including on rejection\.

## Properties {#properties}

### sourceLabel {#sourcelabel}

```ts
readonly sourceLabel: string;
```

Return the compiler logical source label\.

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

### path\(\) {#path}

```ts
path(): AuthoringInstancePathSegment[];
```

Return the complete exact instance path in stable order\.

#### Returns {#returns-2}

[`AuthoringInstancePathSegment`](/pale/reference/wasm/classes/AuthoringInstancePathSegment)\[\]
