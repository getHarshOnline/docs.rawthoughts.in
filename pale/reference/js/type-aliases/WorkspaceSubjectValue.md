---
title: "Type Alias: WorkspaceSubjectValue"
---

<a id="type&#45;alias&#45;workspacesubjectvalue"></a>

```ts
type WorkspaceSubjectValue = 
  | {
  kind: "source";
  sourceId: string;
}
  | {
  componentId: string;
  kind: "component";
}
  | {
  kind: "module";
  moduleId: string;
}
  | {
  declarationId: string;
  kind: "declaration";
  namespaceId: string;
  ownerModuleId: string;
}
  | {
  exportId: string;
  importerModuleId: string;
  kind: "import";
  localNamespaceId: string;
  sourceNamespaceId: string;
  upstreamModuleId: string;
  upstreamReleaseId: string;
}
  | {
  extensionNamespaceId: string;
  kind: "extension";
  ownerModuleId: string;
  targetDeclarationId: string;
  targetNamespaceId: string;
}
  | {
  declarationId: string;
  kind: "policy";
  namespaceId: string;
  ownerModuleId: string;
}
  | {
  kind: "responsibility-closure";
}
  | {
  kind: "organizational-translation-closure";
}
  | {
  kind: "experience-composition";
}
  | {
  kind: "resource";
  ownerModuleId: string;
  resourceId: string;
}
  | {
  kind: "resolution-lock";
}
  | {
  kind: "universe-lock";
}
  | {
  kind: "workspace";
  workspaceId: string;
};
```

Complete copied selector, narrowed by its `kind` in JavaScript\.

Each variant contains only its required coordinates\. Reading or changing
this output value performs no admission\. It is not a `WorkspaceSubject`
accepted by comparison queries\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "source";
  sourceId: string;
}
```

#### kind {#kind}

```ts
kind: "source";
```

#### sourceId {#sourceid}

```ts
sourceId: string;
```

Receipt\-local source identity\.

-----

### Type Literal {#type-literal-1}

```ts
{
  componentId: string;
  kind: "component";
}
```

#### componentId {#componentid}

```ts
componentId: string;
```

Component identity\.

#### kind {#kind-1}

```ts
kind: "component";
```

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "module";
  moduleId: string;
}
```

#### kind {#kind-2}

```ts
kind: "module";
```

#### moduleId {#moduleid}

```ts
moduleId: string;
```

Module identity\.

-----

### Type Literal {#type-literal-3}

```ts
{
  declarationId: string;
  kind: "declaration";
  namespaceId: string;
  ownerModuleId: string;
}
```

#### declarationId {#declarationid}

```ts
declarationId: string;
```

Identity local to the namespace\.

#### kind {#kind-3}

```ts
kind: "declaration";
```

#### namespaceId {#namespaceid}

```ts
namespaceId: string;
```

Declaration namespace\.

#### ownerModuleId {#ownermoduleid}

```ts
ownerModuleId: string;
```

Canonical owner module\.

-----

### Type Literal {#type-literal-4}

```ts
{
  exportId: string;
  importerModuleId: string;
  kind: "import";
  localNamespaceId: string;
  sourceNamespaceId: string;
  upstreamModuleId: string;
  upstreamReleaseId: string;
}
```

#### &#101;xportId {#exportid}

```ts
exportId: string;
```

Named upstream export\.

#### &#105;mporterModuleId {#importermoduleid}

```ts
importerModuleId: string;
```

Importing module\.

#### kind {#kind-4}

```ts
kind: "import";
```

#### localNamespaceId {#localnamespaceid}

```ts
localNamespaceId: string;
```

Namespace bound by the importer\.

#### sourceNamespaceId {#sourcenamespaceid}

```ts
sourceNamespaceId: string;
```

Namespace selected from the upstream export\.

#### upstreamModuleId {#upstreammoduleid}

```ts
upstreamModuleId: string;
```

Selected upstream module\.

#### upstreamReleaseId {#upstreamreleaseid}

```ts
upstreamReleaseId: string;
```

Selected upstream release\.

-----

### Type Literal {#type-literal-5}

```ts
{
  extensionNamespaceId: string;
  kind: "extension";
  ownerModuleId: string;
  targetDeclarationId: string;
  targetNamespaceId: string;
}
```

#### extensionNamespaceId {#extensionnamespaceid}

```ts
extensionNamespaceId: string;
```

Namespace owning the extension rule\.

#### kind {#kind-5}

```ts
kind: "extension";
```

#### ownerModuleId {#ownermoduleid-1}

```ts
ownerModuleId: string;
```

Extension owner module\.

#### targetDeclarationId {#targetdeclarationid}

```ts
targetDeclarationId: string;
```

Identity of the extended declaration\.

#### targetNamespaceId {#targetnamespaceid}

```ts
targetNamespaceId: string;
```

Namespace of the extended declaration\.

-----

### Type Literal {#type-literal-6}

```ts
{
  declarationId: string;
  kind: "policy";
  namespaceId: string;
  ownerModuleId: string;
}
```

#### declarationId {#declarationid-1}

```ts
declarationId: string;
```

Identity local to the namespace\.

#### kind {#kind-6}

```ts
kind: "policy";
```

#### namespaceId {#namespaceid-1}

```ts
namespaceId: string;
```

Declaration namespace\.

#### ownerModuleId {#ownermoduleid-2}

```ts
ownerModuleId: string;
```

Canonical owner module\.

-----

### Type Literal {#type-literal-7}

```ts
{
  kind: "responsibility-closure";
}
```

-----

### Type Literal {#type-literal-8}

```ts
{
  kind: "organizational-translation-closure";
}
```

-----

### Type Literal {#type-literal-9}

```ts
{
  kind: "experience-composition";
}
```

-----

### Type Literal {#type-literal-10}

```ts
{
  kind: "resource";
  ownerModuleId: string;
  resourceId: string;
}
```

#### kind {#kind-7}

```ts
kind: "resource";
```

#### ownerModuleId {#ownermoduleid-3}

```ts
ownerModuleId: string;
```

Selecting module\.

#### resourceId {#resourceid}

```ts
resourceId: string;
```

Workspace\-local resource identity\.

-----

### Type Literal {#type-literal-11}

```ts
{
  kind: "resolution-lock";
}
```

-----

### Type Literal {#type-literal-12}

```ts
{
  kind: "universe-lock";
}
```

-----

### Type Literal {#type-literal-13}

```ts
{
  kind: "workspace";
  workspaceId: string;
}
```

#### kind {#kind-8}

```ts
kind: "workspace";
```

#### workspaceId {#workspaceid}

```ts
workspaceId: string;
```

Principal\-relative workspace identity\.
