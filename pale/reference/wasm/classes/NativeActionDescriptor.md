---
title: "Class: NativeActionDescriptor"
---

<a id="class&#45;nativeactiondescriptor"></a>

One effect\-free native\-action descriptor owned by the API registry\.

## Properties {#properties}

### actionId {#actionid}

```ts
readonly actionId: string;
```

Exact compiled action identity\.

-----

### description {#description}

```ts
readonly description: string;
```

Registry\-owned concise action description\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### contractBytes\(\) {#contractbytes}

```ts
contractBytes(): Uint8Array;
```

Copy the exact canonical action contract into one `Uint8Array`\.

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

### payloadSchemaBytes\(\) {#payloadschemabytes}

```ts
payloadSchemaBytes(): Uint8Array;
```

Copy the self\-contained payload schema into one `Uint8Array`\.

#### Returns {#returns-3}

`Uint8Array`
