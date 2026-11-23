---
title: "Type Alias: RecipientQualifiedOrganizationCorrespondenceState"
---

<a id="type&#45;alias&#45;recipientqualifiedorganizationcorrespondencestate"></a>

```ts
type RecipientQualifiedOrganizationCorrespondenceState = 
  | {
  cursor: RecipientQualifiedOrganizationCorrespondenceCursor;
  kind: "searching";
}
  | {
  kind: "unmatched";
}
  | {
  kind: "matched";
  other: RecipientQualifiedOrganizationEntry;
  values: WorkspaceValueComparison;
};
```

Incomplete search, complete absence, or an admitted same\-key comparison\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  cursor: RecipientQualifiedOrganizationCorrespondenceCursor;
  kind: "searching";
}
```

#### cursor {#cursor}

```ts
cursor: RecipientQualifiedOrganizationCorrespondenceCursor;
```

Authority\-bound continuation\.

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
  other: RecipientQualifiedOrganizationEntry;
  values: WorkspaceValueComparison;
}
```

#### kind {#kind-1}

```ts
kind: "matched";
```

#### other {#other}

```ts
other: RecipientQualifiedOrganizationEntry;
```

Admitted row from the other side\.

#### values {#values}

```ts
values: WorkspaceValueComparison;
```

Complete typed value comparison\.
