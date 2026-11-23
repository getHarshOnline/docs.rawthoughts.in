---
title: "Interface: PackageDistributionInspection"
---

<a id="interface&#45;packagedistributioninspection"></a>

Canonically ordered lock inputs derived by the API owner\.

## Properties {#properties}

### canonicalBytes {#canonicalbytes}

```ts
canonicalBytes: Buffer;
```

Canonical API\-owned bytes for durable transport\.

-----

### compiler {#compiler}

```ts
compiler: string;
```

Compiler contract required by the inspected releases\.

-----

### packages {#packages}

```ts
packages: PackageReleaseIdentity[];
```

Canonically ordered exact Package release identities\.

-----

### schemaManifestSha256 {#schemamanifestsha256}

```ts
schemaManifestSha256: string;
```

Digest of the generated schema manifest used for admission\.

-----

### schemaSetSha256 {#schemasetsha256}

```ts
schemaSetSha256: string;
```

Digest of the complete generated schema byte set used for admission\.
