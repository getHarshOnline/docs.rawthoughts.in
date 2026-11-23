---
title: "Class: AuthoringLiteral"
---

<a id="class&#45;authoringliteral"></a>

Lossless projection of one generated TOML literal\.

## Properties {#properties}

### booleanValue {#booleanvalue}

```ts
readonly booleanValue: boolean | undefined;
```

Return the Boolean member when this is a Boolean literal\.

-----

### integerValue {#integervalue}

```ts
readonly integerValue: bigint | undefined;
```

Return the signed integer member as a non\-lossy JavaScript `bigint`\.

-----

### stringValue {#stringvalue}

```ts
readonly stringValue: string | undefined;
```

Return the string member when this is a string literal\.

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
kind(): AuthoringLiteralKind;
```

Return the literal family\.

#### Returns {#returns-2}

[`AuthoringLiteralKind`](/pale/reference/wasm/enumerations/AuthoringLiteralKind)
