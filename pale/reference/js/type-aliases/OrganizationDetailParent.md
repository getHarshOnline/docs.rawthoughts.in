---
title: "Type Alias: OrganizationDetailParent"
---

<a id="type&#45;alias&#45;organizationdetailparent"></a>

```ts
type OrganizationDetailParent = 
  | {
  handle: OrganizationRecordHandle;
  kind: "record";
}
  | {
  handle: OrganizationCommunicationResolutionHandle;
  kind: "communication";
}
  | {
  handle: OrganizationServiceAssignmentHandle;
  kind: "assignment";
}
  | {
  handle: OrganizationResponsibilityProjectionHandle;
  kind: "projection";
}
  | {
  handle: OrganizationGenealogyHandle;
  kind: "genealogy";
};
```

Actual parent custody of a detail result, independently retained after return\.

These are issued opaque handles, not generic semantic cell values\. A nested
parent remains distinguishable even when its returned child list is empty\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  handle: OrganizationRecordHandle;
  kind: "record";
}
```

#### handle {#handle}

```ts
handle: OrganizationRecordHandle;
```

Exact owning variant payload\.

#### kind {#kind}

```ts
kind: "record";
```

-----

### Type Literal {#type-literal-1}

```ts
{
  handle: OrganizationCommunicationResolutionHandle;
  kind: "communication";
}
```

#### handle {#handle-1}

```ts
handle: OrganizationCommunicationResolutionHandle;
```

Exact owning variant payload\.

#### kind {#kind-1}

```ts
kind: "communication";
```

-----

### Type Literal {#type-literal-2}

```ts
{
  handle: OrganizationServiceAssignmentHandle;
  kind: "assignment";
}
```

#### handle {#handle-2}

```ts
handle: OrganizationServiceAssignmentHandle;
```

Exact owning variant payload\.

#### kind {#kind-2}

```ts
kind: "assignment";
```

-----

### Type Literal {#type-literal-3}

```ts
{
  handle: OrganizationResponsibilityProjectionHandle;
  kind: "projection";
}
```

#### handle {#handle-3}

```ts
handle: OrganizationResponsibilityProjectionHandle;
```

Exact owning variant payload\.

#### kind {#kind-3}

```ts
kind: "projection";
```

-----

### Type Literal {#type-literal-4}

```ts
{
  handle: OrganizationGenealogyHandle;
  kind: "genealogy";
}
```

#### handle {#handle-4}

```ts
handle: OrganizationGenealogyHandle;
```

Exact owning variant payload\.

#### kind {#kind-4}

```ts
kind: "genealogy";
```
