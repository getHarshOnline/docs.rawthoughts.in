---
title: "Type Alias: OrganizationPlacementAnswer"
---

<a id="type&#45;alias&#45;organizationplacementanswer"></a>

```ts
type OrganizationPlacementAnswer = 
  | {
  attribution: OrganizationAttribution;
  kind: "supplied";
  value: OrganizationResponsibilityPlacement;
}
  | {
  attribution: OrganizationAttribution;
  kind: "omitted";
  reason: string;
};
```

Actual attributed responsibility placement\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  attribution: OrganizationAttribution;
  kind: "supplied";
  value: OrganizationResponsibilityPlacement;
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
value: OrganizationResponsibilityPlacement;
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
