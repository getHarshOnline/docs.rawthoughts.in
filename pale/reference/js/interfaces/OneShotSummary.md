---
title: "Interface: OneShotSummary"
---

<a id="interface&#45;oneshotsummary"></a>

Flat binding\-safe summary of one admitted one\-shot compilation\.

## Properties {#properties}

### canonicalBytes {#canonicalbytes}

```ts
canonicalBytes: Buffer;
```

Complete API\-owned canonical summary bytes\.

-----

### executionWorkspaceId {#executionworkspaceid}

```ts
executionWorkspaceId: string;
```

Canonical execution\-workspace identity\.

-----

### instanceDigest {#instancedigest}

```ts
instanceDigest: string;
```

Complete private\-instance digest\.

-----

### oneShotCompilationDigest {#oneshotcompilationdigest}

```ts
oneShotCompilationDigest: string;
```

Post\-render one\-shot output digest\.

-----

### profileDigest {#profiledigest}

```ts
profileDigest: string;
```

Effective profile digest\.

-----

### projectId {#projectid}

```ts
projectId: string;
```

Canonical project identity\.

-----

### repositoryCount {#repositorycount}

```ts
repositoryCount: number;
```

Number of selected repositories\.

-----

### repositoryIds {#repositoryids}

```ts
repositoryIds: string[];
```

Stable repository identities\.

-----

### schemaManifestSha256 {#schemamanifestsha256}

```ts
schemaManifestSha256: string;
```

Descriptor\-manifest digest\.

-----

### schemaSetSha256 {#schemasetsha256}

```ts
schemaSetSha256: string;
```

Raw\-schema\-set digest\.
