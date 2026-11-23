---
title: "Interface: ContractSchema"
---

<a id="interface&#45;contractschema"></a>

One selected generated schema and its exact bytes\.

## Properties {#properties}

### bytes {#bytes}

```ts
bytes: Buffer;
```

Exact raw schema bytes\.

-----

### registryId {#registryid}

```ts
registryId: string;
```

Descriptor\-registry identity\.

-----

### schemaSha256 {#schemasha256}

```ts
schemaSha256: string;
```

SHA\-256 of the exact schema bytes\.

-----

### schemaUri {#schemauri}

```ts
schemaUri: string;
```

Canonical schema URI\.

-----

### wireSchemaId? {#wireschemaid}

```ts
wireSchemaId?: string;
```

Standalone wire identity, when present\.
