---
title: "Class: WorkspaceSubject"
---

<a id="class&#45;workspacesubject"></a>

Opaque typed subject returned by comparison or source inspection\.

## Accessors {#accessors}

### componentId {#componentid}

#### Get Signature {#get-signature}

```ts
get componentId(): string | null;
```

Component identity when this is a component subject\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### declarationId {#declarationid}

#### Get Signature {#get-signature-1}

```ts
get declarationId(): string | null;
```

Declaration identity, when carried\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### declarationNamespaceId {#declarationnamespaceid}

#### Get Signature {#get-signature-2}

```ts
get declarationNamespaceId(): string | null;
```

Declaration namespace identity, when carried\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### &#101;xportId {#exportid}

#### Get Signature {#get-signature-3}

```ts
get exportId(): string | null;
```

Export identity, when carried\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### extensionNamespaceId {#extensionnamespaceid}

#### Get Signature {#get-signature-4}

```ts
get extensionNamespaceId(): string | null;
```

Extension namespace identity, when carried\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### &#105;mporterModuleId {#importermoduleid}

#### Get Signature {#get-signature-5}

```ts
get importerModuleId(): string | null;
```

Importer module identity, when carried\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-6}

```ts
get kind(): WorkspaceSubjectKind;
```

Stable coordinate\-family name\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceSubjectKind`](/pale/reference/js/enumerations/WorkspaceSubjectKind)

-----

### localNamespaceId {#localnamespaceid}

#### Get Signature {#get-signature-7}

```ts
get localNamespaceId(): string | null;
```

Local namespace identity, when carried\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### moduleId {#moduleid}

#### Get Signature {#get-signature-8}

```ts
get moduleId(): string | null;
```

Module identity when this is a module subject\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### ownerModuleId {#ownermoduleid}

#### Get Signature {#get-signature-9}

```ts
get ownerModuleId(): string | null;
```

Owning module identity, when carried\.

<Heading level={5} id="returns&#45;9" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### resourceId {#resourceid}

#### Get Signature {#get-signature-10}

```ts
get resourceId(): string | null;
```

Resource identity, when carried\.

<Heading level={5} id="returns&#45;10" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### sourceId {#sourceid}

#### Get Signature {#get-signature-11}

```ts
get sourceId(): string | null;
```

Source identity when this is a source subject\.

<Heading level={5} id="returns&#45;11" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### sourceNamespaceId {#sourcenamespaceid}

#### Get Signature {#get-signature-12}

```ts
get sourceNamespaceId(): string | null;
```

Source namespace identity, when carried\.

<Heading level={5} id="returns&#45;12" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### upstreamModuleId {#upstreammoduleid}

#### Get Signature {#get-signature-13}

```ts
get upstreamModuleId(): string | null;
```

Upstream module identity, when carried\.

<Heading level={5} id="returns&#45;13" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### upstreamReleaseId {#upstreamreleaseid}

#### Get Signature {#get-signature-14}

```ts
get upstreamReleaseId(): string | null;
```

Upstream release identity, when carried\.

<Heading level={5} id="returns&#45;14" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-15}

```ts
get workspaceId(): string | null;
```

Workspace identity when this is a workspace subject\.

<Heading level={5} id="returns&#45;15" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`
