---
title: "Class: ContractSchema"
---

<a id="class&#45;contractschema"></a>

One selected generated schema and its exact bytes\.

## Properties {#properties}

### registryId {#registryid}

```ts
readonly registryId: string;
```

Descriptor\-registry identity used for lookup\.

-----

### schemaSha256 {#schemasha256}

```ts
readonly schemaSha256: string;
```

SHA\-256 of the exact raw schema bytes\.

-----

### schemaUri {#schemauri}

```ts
readonly schemaUri: string;
```

Canonical schema URI\.

-----

### wireSchemaId {#wireschemaid}

```ts
readonly wireSchemaId: string | undefined;
```

Wire identity carried by standalone documents, when one exists\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### bytes\(\) {#bytes}

```ts
bytes(): Uint8Array;
```

Copy the exact raw schema into one owned `Uint8Array`\.

#### Returns {#returns-1}

`Uint8Array`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-2}

`void`
