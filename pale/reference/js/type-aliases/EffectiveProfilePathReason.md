---
title: "Type Alias: EffectiveProfilePathReason"
---

<a id="type&#45;alias&#45;effectiveprofilepathreason"></a>

```ts
type EffectiveProfilePathReason = 
  | {
  contractId: string;
  kind: "origin-receipt";
}
  | {
  contractId: string;
  kind: "entry-contract";
}
  | {
  contractId: string;
  kind: "responsibility-contract";
}
  | {
  bindingId: string;
  kind: "provider-binding";
}
  | {
  edgeId: string;
  kind: "delegation-edge";
}
  | {
  contractId: string;
  kind: "termination-contract";
}
  | {
  contractId: string;
  kind: "settlement-contract";
}
  | {
  contractId: string;
  kind: "continuity-contract";
};
```

Copied selected\-path reason, distinct from an observation causal step\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  contractId: string;
  kind: "origin-receipt";
}
```

#### contractId {#contractid}

```ts
contractId: string;
```

Exact origin\-receipt contract\.

#### kind {#kind}

```ts
kind: "origin-receipt";
```

-----

### Type Literal {#type-literal-1}

```ts
{
  contractId: string;
  kind: "entry-contract";
}
```

#### contractId {#contractid-1}

```ts
contractId: string;
```

Exact entry contract\.

#### kind {#kind-1}

```ts
kind: "entry-contract";
```

-----

### Type Literal {#type-literal-2}

```ts
{
  contractId: string;
  kind: "responsibility-contract";
}
```

#### contractId {#contractid-2}

```ts
contractId: string;
```

Exact responsibility contract\.

#### kind {#kind-2}

```ts
kind: "responsibility-contract";
```

-----

### Type Literal {#type-literal-3}

```ts
{
  bindingId: string;
  kind: "provider-binding";
}
```

#### bindingId {#bindingid}

```ts
bindingId: string;
```

Exact provider\-binding identity\.

#### kind {#kind-3}

```ts
kind: "provider-binding";
```

-----

### Type Literal {#type-literal-4}

```ts
{
  edgeId: string;
  kind: "delegation-edge";
}
```

#### edgeId {#edgeid}

```ts
edgeId: string;
```

Exact delegation\-edge identity\.

#### kind {#kind-4}

```ts
kind: "delegation-edge";
```

-----

### Type Literal {#type-literal-5}

```ts
{
  contractId: string;
  kind: "termination-contract";
}
```

#### contractId {#contractid-3}

```ts
contractId: string;
```

Exact termination contract\.

#### kind {#kind-5}

```ts
kind: "termination-contract";
```

-----

### Type Literal {#type-literal-6}

```ts
{
  contractId: string;
  kind: "settlement-contract";
}
```

#### contractId {#contractid-4}

```ts
contractId: string;
```

Exact settlement contract\.

#### kind {#kind-6}

```ts
kind: "settlement-contract";
```

-----

### Type Literal {#type-literal-7}

```ts
{
  contractId: string;
  kind: "continuity-contract";
}
```

#### contractId {#contractid-5}

```ts
contractId: string;
```

Exact continuity contract\.

#### kind {#kind-7}

```ts
kind: "continuity-contract";
```
