---
title: "Type Alias: OrganizationNode"
---

<a id="type&#45;alias&#45;organizationnode"></a>

```ts
type OrganizationNode = 
  | {
  kind: "scope";
  scope: OrganizationScopeRef;
}
  | {
  kind: "organization";
  organization: OrganizationRef;
}
  | {
  group: OrganizationGroupRef;
  kind: "group";
}
  | {
  kind: "discipline-tree";
  tree: OrganizationTreeRef;
}
  | {
  kind: "role";
  role: OrganizationRoleRef;
}
  | {
  kind: "occupant";
  occupant: string;
}
  | {
  kind: "provider";
  provider: string;
}
  | {
  kind: "native-resource";
  nativeResource: string;
}
  | {
  kind: "object";
  object: string;
};
```

Existing endpoint kind; no identity is inferred from a display label\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "scope";
  scope: OrganizationScopeRef;
}
```

#### kind {#kind}

```ts
kind: "scope";
```

#### scope {#scope}

```ts
scope: OrganizationScopeRef;
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-1}

```ts
{
  kind: "organization";
  organization: OrganizationRef;
}
```

#### kind {#kind-1}

```ts
kind: "organization";
```

#### organization {#organization}

```ts
organization: OrganizationRef;
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-2}

```ts
{
  group: OrganizationGroupRef;
  kind: "group";
}
```

#### group {#group}

```ts
group: OrganizationGroupRef;
```

Exact owning variant payload\.

#### kind {#kind-2}

```ts
kind: "group";
```

-----

### Type Literal {#type-literal-3}

```ts
{
  kind: "discipline-tree";
  tree: OrganizationTreeRef;
}
```

#### kind {#kind-3}

```ts
kind: "discipline-tree";
```

#### tree {#tree}

```ts
tree: OrganizationTreeRef;
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-4}

```ts
{
  kind: "role";
  role: OrganizationRoleRef;
}
```

#### kind {#kind-4}

```ts
kind: "role";
```

#### role {#role}

```ts
role: OrganizationRoleRef;
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-5}

```ts
{
  kind: "occupant";
  occupant: string;
}
```

#### kind {#kind-5}

```ts
kind: "occupant";
```

#### occupant {#occupant}

```ts
occupant: string;
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-6}

```ts
{
  kind: "provider";
  provider: string;
}
```

#### kind {#kind-6}

```ts
kind: "provider";
```

#### provider {#provider}

```ts
provider: string;
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-7}

```ts
{
  kind: "native-resource";
  nativeResource: string;
}
```

#### kind {#kind-7}

```ts
kind: "native-resource";
```

#### nativeResource {#nativeresource}

```ts
nativeResource: string;
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-8}

```ts
{
  kind: "object";
  object: string;
}
```

#### kind {#kind-8}

```ts
kind: "object";
```

#### object {#object}

```ts
object: string;
```

Exact owning variant payload\.
