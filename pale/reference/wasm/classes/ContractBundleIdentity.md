---
title: "Class: ContractBundleIdentity"
---

<a id="class&#45;contractbundleidentity"></a>

Exact embedded bundle coordinate, with only JavaScript\-safe integers\.

## Properties {#properties}

### memberCount {#membercount}

```ts
readonly memberCount: number;
```

Number of schemas in the embedded bundle\.

-----

### schemaManifestSha256 {#schemamanifestsha256}

```ts
readonly schemaManifestSha256: string;
```

RFC 8785 descriptor\-manifest digest\.

-----

### schemaSetSha256 {#schemasetsha256}

```ts
readonly schemaSetSha256: string;
```

Domain\-separated active schema\-set digest\.

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
