---
title: "Class: WorkspaceChangeRootPage"
---

<a id="class&#45;workspacechangerootpage"></a>

One bounded page of exact change roots\.

## Properties {#properties}

### nextOffset {#nextoffset}

```ts
readonly nextOffset: number | undefined;
```

Next exact offset, or `undefined` at the end\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### canonicalBytes\(\) {#canonicalbytes}

```ts
canonicalBytes(): Uint8Array;
```

Copy the SDK's exact canonical page without reconstructing typed entries\.

#### Returns {#returns-1}

`Uint8Array`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-2}

`void`

-----

### intoEntries\(\) {#intoentries}

```ts
intoEntries(): WorkspaceChangeRoot[];
```

Consume the page and return its owned entries in canonical order\.

#### Returns {#returns-3}

[`WorkspaceChangeRoot`](/pale/reference/wasm/classes/WorkspaceChangeRoot)\[\]
