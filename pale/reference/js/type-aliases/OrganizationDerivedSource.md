---
title: "Type Alias: OrganizationDerivedSource"
---

<a id="type&#45;alias&#45;organizationderivedsource"></a>

```ts
type OrganizationDerivedSource = 
  | {
  interval: OrganizationInterval;
  kind: "occupant-binding";
  occupant: string;
  role: OrganizationRoleRef;
}
  | {
  interval: OrganizationInterval;
  kind: "provider-binding";
  provider: string;
  role: OrganizationRoleRef;
}
  | {
  kind: "leadership-participation";
  topic: string;
};
```

Complete source coordinate of an already\-derived edge\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  interval: OrganizationInterval;
  kind: "occupant-binding";
  occupant: string;
  role: OrganizationRoleRef;
}
```

#### interval {#interval}

```ts
interval: OrganizationInterval;
```

Source binding interval\.

#### kind {#kind}

```ts
kind: "occupant-binding";
```

#### occupant {#occupant}

```ts
occupant: string;
```

Occupant\.

#### role {#role}

```ts
role: OrganizationRoleRef;
```

Stable role\.

-----

### Type Literal {#type-literal-1}

```ts
{
  interval: OrganizationInterval;
  kind: "provider-binding";
  provider: string;
  role: OrganizationRoleRef;
}
```

#### interval {#interval-1}

```ts
interval: OrganizationInterval;
```

Source binding interval\.

#### kind {#kind-1}

```ts
kind: "provider-binding";
```

#### provider {#provider}

```ts
provider: string;
```

Provider\.

#### role {#role-1}

```ts
role: OrganizationRoleRef;
```

Stable role\.

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "leadership-participation";
  topic: string;
}
```

#### kind {#kind-2}

```ts
kind: "leadership-participation";
```

#### topic {#topic}

```ts
topic: string;
```

Exact owning variant payload\.
