---
title: "Type Alias: OrganizationSettlementAnswer"
---

<a id="type&#45;alias&#45;organizationsettlementanswer"></a>

```ts
type OrganizationSettlementAnswer = 
  | {
  attribution: OrganizationAttribution;
  kind: "supplied";
  value: OrganizationEvidenceRequirement;
}
  | {
  attribution: OrganizationAttribution;
  kind: "omitted";
  reason: string;
};
```

Pale obligation\-settlement answer, separate from native\-owner acceptance\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  attribution: OrganizationAttribution;
  kind: "supplied";
  value: OrganizationEvidenceRequirement;
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
value: OrganizationEvidenceRequirement;
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
