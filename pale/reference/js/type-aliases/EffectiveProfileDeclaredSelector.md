---
title: "Type Alias: EffectiveProfileDeclaredSelector"
---

<a id="type&#45;alias&#45;effectiveprofiledeclaredselector"></a>

```ts
type EffectiveProfileDeclaredSelector = 
  | {
  kind: "exact";
  resourceId: string;
}
  | {
  kind: "all-from-package";
  packageId: string;
};
```

Copied declared selector before compiler closure expansion\.
Each literal kind exposes only its required coordinate\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "exact";
  resourceId: string;
}
```

#### kind {#kind}

```ts
kind: "exact";
```

#### resourceId {#resourceid}

```ts
resourceId: string;
```

Exact declared resource\.

-----

### Type Literal {#type-literal-1}

```ts
{
  kind: "all-from-package";
  packageId: string;
}
```

#### kind {#kind-1}

```ts
kind: "all-from-package";
```

#### packageId {#packageid}

```ts
packageId: string;
```

Package scope of the declaration\.
