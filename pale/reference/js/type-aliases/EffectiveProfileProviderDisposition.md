---
title: "Type Alias: EffectiveProfileProviderDisposition"
---

<a id="type&#45;alias&#45;effectiveprofileproviderdisposition"></a>

```ts
type EffectiveProfileProviderDisposition = 
  | {
  kind: "bound";
  provider: EffectiveProfileProviderKind;
}
  | {
  kind: "missing-binding";
}
  | {
  kind: "excluded-by-narrowing";
}
  | {
  kind: "effect-mismatch";
}
  | {
  kind: "recipe-contract-mismatch";
};
```

Private provider selection, independent of native readiness\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "bound";
  provider: EffectiveProfileProviderKind;
}
```

#### kind {#kind}

```ts
kind: "bound";
```

#### provider {#provider}

```ts
provider: EffectiveProfileProviderKind;
```

Exact selected provider family\.

-----

### Type Literal {#type-literal-1}

```ts
{
  kind: "missing-binding";
}
```

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "excluded-by-narrowing";
}
```

-----

### Type Literal {#type-literal-3}

```ts
{
  kind: "effect-mismatch";
}
```

-----

### Type Literal {#type-literal-4}

```ts
{
  kind: "recipe-contract-mismatch";
}
```
