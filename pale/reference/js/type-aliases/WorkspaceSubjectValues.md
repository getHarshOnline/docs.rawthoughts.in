---
title: "Type Alias: WorkspaceSubjectValues"
---

<a id="type&#45;alias&#45;workspacesubjectvalues"></a>

```ts
type WorkspaceSubjectValues = 
  | {
  membership: "absent";
}
  | {
  membership: "prior-only";
  prior: WorkspaceFact;
}
  | {
  current: WorkspaceFact;
  membership: "current-only";
}
  | {
  comparison: WorkspaceValueComparison;
  current: WorkspaceFact;
  membership: "shared";
  prior: WorkspaceFact;
};
```

Subject membership and typed values in the retained comparison pair\.

Missing sides have no value\. Only a shared subject carries an equality
decision; an affected subject can still have equal outputs\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  membership: "absent";
}
```

-----

### Type Literal {#type-literal-1}

```ts
{
  membership: "prior-only";
  prior: WorkspaceFact;
}
```

#### membership {#membership}

```ts
membership: "prior-only";
```

#### prior {#prior}

```ts
prior: WorkspaceFact;
```

Predecessor's complete typed output\.

-----

### Type Literal {#type-literal-2}

```ts
{
  current: WorkspaceFact;
  membership: "current-only";
}
```

#### current {#current}

```ts
current: WorkspaceFact;
```

Current compilation's complete typed output\.

#### membership {#membership-1}

```ts
membership: "current-only";
```

-----

### Type Literal {#type-literal-3}

```ts
{
  comparison: WorkspaceValueComparison;
  current: WorkspaceFact;
  membership: "shared";
  prior: WorkspaceFact;
}
```

#### comparison {#comparison}

```ts
comparison: WorkspaceValueComparison;
```

Equality established by the application\.

#### current {#current-1}

```ts
current: WorkspaceFact;
```

Current compilation's complete typed output\.

#### membership {#membership-2}

```ts
membership: "shared";
```

#### prior {#prior-1}

```ts
prior: WorkspaceFact;
```

Predecessor's complete typed output\.
