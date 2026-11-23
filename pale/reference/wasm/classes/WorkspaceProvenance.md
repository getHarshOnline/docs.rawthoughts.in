---
title: "Class: WorkspaceProvenance"
---

<a id="class&#45;workspaceprovenance"></a>

Lossless provenance projection for one causal step\.

## Properties {#properties}

### &#101;xportId {#exportid}

```ts
readonly exportId: string | undefined;
```

Selected export identity\.

-----

### extensionNamespaceId {#extensionnamespaceid}

```ts
readonly extensionNamespaceId: string | undefined;
```

Extension namespace identity\.

-----

### &#105;mporterModuleId {#importermoduleid}

```ts
readonly importerModuleId: string | undefined;
```

Importer module identity\.

-----

### localNamespaceId {#localnamespaceid}

```ts
readonly localNamespaceId: string | undefined;
```

Local namespace identity\.

-----

### moduleDigest {#moduledigest}

```ts
readonly moduleDigest: string | undefined;
```

Selected module digest\.

-----

### moduleId {#moduleid}

```ts
readonly moduleId: string | undefined;
```

Module or extension owner identity\.

-----

### releaseId {#releaseid}

```ts
readonly releaseId: string | undefined;
```

Selected release identity\.

-----

### sourceId {#sourceid}

```ts
readonly sourceId: string | undefined;
```

Direct source identity\.

-----

### sourceNamespaceId {#sourcenamespaceid}

```ts
readonly sourceNamespaceId: string | undefined;
```

Upstream namespace identity\.

-----

### targetDeclarationId {#targetdeclarationid}

```ts
readonly targetDeclarationId: string | undefined;
```

Extension target declaration identity\.

-----

### targetNamespaceId {#targetnamespaceid}

```ts
readonly targetNamespaceId: string | undefined;
```

Extension target namespace identity\.

-----

### upstreamModuleId {#upstreammoduleid}

```ts
readonly upstreamModuleId: string | undefined;
```

Upstream module identity\.

-----

### upstreamReleaseId {#upstreamreleaseid}

```ts
readonly upstreamReleaseId: string | undefined;
```

Upstream release identity\.

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
kind(): WorkspaceProvenanceKind;
```

Closed provenance family\.

#### Returns {#returns-2}

[`WorkspaceProvenanceKind`](/pale/reference/wasm/enumerations/WorkspaceProvenanceKind)
