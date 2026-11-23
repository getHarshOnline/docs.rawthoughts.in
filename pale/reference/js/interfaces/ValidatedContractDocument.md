---
title: "Interface: ValidatedContractDocument"
---

<a id="interface&#45;validatedcontractdocument"></a>

Canonical result of structural document validation\.

## Properties {#properties}

### canonicalBytes {#canonicalbytes}

```ts
canonicalBytes: Buffer;
```

RFC 8785 document bytes\.

-----

### schemaId {#schemaid}

```ts
schemaId: string;
```

Admitted registry identity\.

-----

### schemaSha256 {#schemasha256}

```ts
schemaSha256: string;
```

SHA\-256 of the admitting schema\.
