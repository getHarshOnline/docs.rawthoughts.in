---
title: "Type Alias: RequirementDisposition"
---

<a id="type&#45;alias&#45;requirementdisposition"></a>

```ts
type RequirementDisposition = 
  | {
  kind: "satisfied";
}
  | {
  kind: "provider-binding-absent";
}
  | {
  kind: "narrowed";
  reason: NarrowingReason;
}
  | {
  kind: "blocked";
  reason: PolicyBlock;
};
```

Portable requirement outcome with the reason required by its literal kind\.
Configuration does not establish native readiness or authorize effects\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "satisfied";
}
```

-----

### Type Literal {#type-literal-1}

```ts
{
  kind: "provider-binding-absent";
}
```

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "narrowed";
  reason: NarrowingReason;
}
```

#### kind {#kind}

```ts
kind: "narrowed";
```

#### reason {#reason}

```ts
reason: NarrowingReason;
```

Exact omitted policy dimension\.

-----

### Type Literal {#type-literal-3}

```ts
{
  kind: "blocked";
  reason: PolicyBlock;
}
```

#### kind {#kind-1}

```ts
kind: "blocked";
```

#### reason {#reason-1}

```ts
reason: PolicyBlock;
```

Exact blocking dimension\.
