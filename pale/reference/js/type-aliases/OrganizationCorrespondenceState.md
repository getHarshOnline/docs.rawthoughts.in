---
title: "Type Alias: OrganizationCorrespondenceState"
---

<a id="type&#45;alias&#45;organizationcorrespondencestate"></a>

```ts
type OrganizationCorrespondenceState = 
  | {
  cursor: OrganizationCorrespondenceCursor;
  kind: "searching";
}
  | {
  kind: "unmatched";
}
  | {
  kind: "matched";
  other: OrganizationEntry;
  values: WorkspaceValueComparison;
};
```

Incomplete search, complete absence, or a same\-key canonical value comparison\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  cursor: OrganizationCorrespondenceCursor;
  kind: "searching";
}
```

#### cursor {#cursor}

```ts
cursor: OrganizationCorrespondenceCursor;
```

Continuation with unchanged pair, selection and raw limits\.

#### kind {#kind}

```ts
kind: "searching";
```

-----

### Type Literal {#type-literal-1}

```ts
{
  kind: "unmatched";
}
```

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "matched";
  other: OrganizationEntry;
  values: WorkspaceValueComparison;
}
```

#### kind {#kind-1}

```ts
kind: "matched";
```

#### other {#other}

```ts
other: OrganizationEntry;
```

Shallow row and retained source/detail handle from the opposite side\.

#### values {#values}

```ts
values: WorkspaceValueComparison;
```

Complete canonical value comparison, not shallow row equality\.
