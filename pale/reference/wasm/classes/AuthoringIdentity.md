---
title: "Class: AuthoringIdentity"
---

<a id="class&#45;authoringidentity"></a>

Resolved binding\-safe semantic identity\.

## Properties {#properties}

### authoredValue {#authoredvalue}

```ts
readonly authoredValue: string;
```

Return the exact scalar spelling valid in the reference scope\.

-----

### value {#value}

```ts
readonly value: string;
```

Return the canonical compiler\-owned display form\.

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
kind(): AuthoringIdentityKind;
```

Return the non\-interchangeable identity namespace\.

#### Returns {#returns-2}

[`AuthoringIdentityKind`](/pale/reference/wasm/enumerations/AuthoringIdentityKind)
