---
title: "Type Alias: OrganizationResponsibilityPlacement"
---

<a id="type&#45;alias&#45;organizationresponsibilityplacement"></a>

```ts
type OrganizationResponsibilityPlacement = 
  | {
  kind: "vertical-local";
  resource: string;
}
  | {
  contract: OrganizationServiceRef;
  kind: "directional-service";
};
```

Actual responsibility placement without guessing a scope from a resource\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "vertical-local";
  resource: string;
}
```

#### kind {#kind}

```ts
kind: "vertical-local";
```

#### resource {#resource}

```ts
resource: string;
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-1}

```ts
{
  contract: OrganizationServiceRef;
  kind: "directional-service";
}
```

#### contract {#contract}

```ts
contract: OrganizationServiceRef;
```

Exact owning variant payload\.

#### kind {#kind-1}

```ts
kind: "directional-service";
```
