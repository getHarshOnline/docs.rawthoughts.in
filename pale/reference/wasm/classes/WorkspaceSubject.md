---
title: "Class: WorkspaceSubject"
---

<a id="class&#45;workspacesubject"></a>

Opaque typed subject coordinate emitted by verified comparison evidence\.

## Properties {#properties}

### componentId {#componentid}

```ts
readonly componentId: string | undefined;
```

Component identity, when this is a component subject\.

-----

### declarationId {#declarationid}

```ts
readonly declarationId: string | undefined;
```

Local declaration identity, when carried by this subject\.

-----

### declarationNamespaceId {#declarationnamespaceid}

```ts
readonly declarationNamespaceId: string | undefined;
```

Namespace of a declaration\-like subject\.

-----

### &#101;xportId {#exportid}

```ts
readonly exportId: string | undefined;
```

Selected export identity, when carried\.

-----

### extensionNamespaceId {#extensionnamespaceid}

```ts
readonly extensionNamespaceId: string | undefined;
```

Extension namespace identity, when carried\.

-----

### &#105;mporterModuleId {#importermoduleid}

```ts
readonly importerModuleId: string | undefined;
```

Importer module identity, when carried\.

-----

### localNamespaceId {#localnamespaceid}

```ts
readonly localNamespaceId: string | undefined;
```

Importer\-local namespace identity, when carried\.

-----

### moduleId {#moduleid}

```ts
readonly moduleId: string | undefined;
```

Module identity, when this is a module subject\.

-----

### ownerModuleId {#ownermoduleid}

```ts
readonly ownerModuleId: string | undefined;
```

Owning module for declaration\-like subjects\.

-----

### resourceId {#resourceid}

```ts
readonly resourceId: string | undefined;
```

Resource identity, when carried\.

-----

### sourceId {#sourceid}

```ts
readonly sourceId: string | undefined;
```

Receipt\-local source identity, when this is a source subject\.

-----

### sourceNamespaceId {#sourcenamespaceid}

```ts
readonly sourceNamespaceId: string | undefined;
```

Upstream namespace identity, when carried\.

-----

### upstreamModuleId {#upstreammoduleid}

```ts
readonly upstreamModuleId: string | undefined;
```

Upstream module identity, when carried\.

-----

### upstreamReleaseId {#upstreamreleaseid}

```ts
readonly upstreamReleaseId: string | undefined;
```

Upstream release identity, when carried\.

-----

### workspaceId {#workspaceid}

```ts
readonly workspaceId: string | undefined;
```

Workspace identity, when this is the complete workspace subject\.

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
kind(): WorkspaceSubjectKind;
```

Return the closed coordinate family\.

#### Returns {#returns-2}

[`WorkspaceSubjectKind`](/pale/reference/wasm/enumerations/WorkspaceSubjectKind)
