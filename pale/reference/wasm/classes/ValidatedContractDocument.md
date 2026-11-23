---
title: "Class: ValidatedContractDocument"
---

<a id="class&#45;validatedcontractdocument"></a>

Canonical result of structural document validation\.

## Properties {#properties}

### canonicalBytes {#canonicalbytes}

```ts
readonly canonicalBytes: Uint8Array;
```

Copy the RFC 8785 document bytes into one owned `Uint8Array`\.

-----

### schemaId {#schemaid}

```ts
readonly schemaId: string;
```

Admitted descriptor\-registry identity\.

-----

### schemaSha256 {#schemasha256}

```ts
readonly schemaSha256: string;
```

SHA\-256 of the schema that admitted the document\.

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
