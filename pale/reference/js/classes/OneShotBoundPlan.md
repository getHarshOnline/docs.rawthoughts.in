---
title: "Class: OneShotBoundPlan"
---

<a id="class&#45;oneshotboundplan"></a>

Complete deterministic plan after machine\-local observations are bound\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy canonical complete materialization\-plan bytes\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### kind {#kind}

#### Get Signature {#get-signature-1}

```ts
get kind(): OneShotPlanKind;
```

Requested plan operation\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OneShotPlanKind`](/pale/reference/js/enumerations/OneShotPlanKind)

-----

### repositoryId {#repositoryid}

#### Get Signature {#get-signature-2}

```ts
get repositoryId(): string;
```

Selected logical repository\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
