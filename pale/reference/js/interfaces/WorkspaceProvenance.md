---
title: "Interface: WorkspaceProvenance"
---

<a id="interface&#45;workspaceprovenance"></a>

Lossless provenance snapshot; fields not belonging to the selected closed kind are absent\.

## Properties {#properties}

### &#101;xportId? {#exportid}

```ts
exportId?: string;
```

Selected export identity\.

-----

### extensionNamespaceId? {#extensionnamespaceid}

```ts
extensionNamespaceId?: string;
```

Extension\-owning namespace identity\.

-----

### &#105;mporterModuleId? {#importermoduleid}

```ts
importerModuleId?: string;
```

Importing module identity\.

-----

### kind {#kind}

```ts
kind: WorkspaceProvenanceKind;
```

Closed provenance family\.

-----

### localNamespaceId? {#localnamespaceid}

```ts
localNamespaceId?: string;
```

Importer\-local namespace identity\.

-----

### moduleDigest? {#moduledigest}

```ts
moduleDigest?: string;
```

Selected module digest\.

-----

### moduleId? {#moduleid}

```ts
moduleId?: string;
```

Module or extension owner identity\.

-----

### releaseId? {#releaseid}

```ts
releaseId?: string;
```

Selected release identity\.

-----

### sourceId? {#sourceid}

```ts
sourceId?: string;
```

Direct source identity\.

-----

### sourceNamespaceId? {#sourcenamespaceid}

```ts
sourceNamespaceId?: string;
```

Upstream namespace identity\.

-----

### targetDeclarationId? {#targetdeclarationid}

```ts
targetDeclarationId?: string;
```

Extension target declaration identity\.

-----

### targetNamespaceId? {#targetnamespaceid}

```ts
targetNamespaceId?: string;
```

Extension target namespace identity\.

-----

### upstreamModuleId? {#upstreammoduleid}

```ts
upstreamModuleId?: string;
```

Upstream module identity\.

-----

### upstreamReleaseId? {#upstreamreleaseid}

```ts
upstreamReleaseId?: string;
```

Upstream release identity\.
