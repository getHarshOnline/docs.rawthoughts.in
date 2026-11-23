---
title: "Type Alias: OrganizationResourceAnswer"
---

<a id="type&#45;alias&#45;organizationresourceanswer"></a>

```ts
type OrganizationResourceAnswer = 
  | {
  attribution: OrganizationAttribution;
  kind: "supplied";
  value: string;
}
  | {
  attribution: OrganizationAttribution;
  kind: "omitted";
  reason: string;
};
```

Actual attributed generic resource answer; no identity\-class cast\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  attribution: OrganizationAttribution;
  kind: "supplied";
  value: string;
}
```

#### attribution {#attribution}

```ts
attribution: OrganizationAttribution;
```

Original attribution\.

#### kind {#kind}

```ts
kind: "supplied";
```

#### value {#value}

```ts
value: string;
```

Typed value, not evidence that a declared requirement has occurred\.

-----

### Type Literal {#type-literal-1}

```ts
{
  attribution: OrganizationAttribution;
  kind: "omitted";
  reason: string;
}
```

#### attribution {#attribution-1}

```ts
attribution: OrganizationAttribution;
```

Original omission attribution\.

#### kind {#kind-1}

```ts
kind: "omitted";
```

#### reason {#reason}

```ts
reason: string;
```

Existing owner\-defined omission reason\.
