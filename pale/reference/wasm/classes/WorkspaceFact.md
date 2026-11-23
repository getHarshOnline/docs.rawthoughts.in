---
title: "Class: WorkspaceFact"
---

<a id="class&#45;workspacefact"></a>

Lossless typed fact projection for a root or causal step\.

## Properties {#properties}

### byteLen {#bytelen}

```ts
readonly byteLen: number | undefined;
```

Source byte length\.

-----

### closureDigest {#closuredigest}

```ts
readonly closureDigest: string | undefined;
```

Closure digest\.

-----

### componentDigest {#componentdigest}

```ts
readonly componentDigest: string | undefined;
```

Component digest\.

-----

### moduleDigest {#moduledigest}

```ts
readonly moduleDigest: string | undefined;
```

Module digest\.

-----

### resolutionDigest {#resolutiondigest}

```ts
readonly resolutionDigest: string | undefined;
```

Resolution\-lock digest\.

-----

### sourceDigest {#sourcedigest}

```ts
readonly sourceDigest: string | undefined;
```

Source digest\.

-----

### sourcePath {#sourcepath}

```ts
readonly sourcePath: string | undefined;
```

Source path\.

-----

### surfaceDigest {#surfacedigest}

```ts
readonly surfaceDigest: string | undefined;
```

Import\-surface digest\.

-----

### universeDigest {#universedigest}

```ts
readonly universeDigest: string | undefined;
```

Universe\-lock digest\.

-----

### valueDigest {#valuedigest}

```ts
readonly valueDigest: string | undefined;
```

Value digest\.

-----

### workspaceSemanticIrDigest {#workspacesemanticirdigest}

```ts
readonly workspaceSemanticIrDigest: string | undefined;
```

Workspace semantic\-IR digest\.

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
kind(): WorkspaceFactKind;
```

Closed fact family\.

#### Returns {#returns-2}

[`WorkspaceFactKind`](/pale/reference/wasm/enumerations/WorkspaceFactKind)
