---
title: "Class: ObservationFreshness"
---

<a id="class&#45;observationfreshness"></a>

Temporal qualification of one fact\.

## Accessors {#accessors}

### kind {#kind}

#### Get Signature {#get-signature}

```ts
get kind(): ObservationFreshnessKind;
```

Return the closed freshness kind\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationFreshnessKind`](/pale/reference/js/enumerations/ObservationFreshnessKind)

-----

### revisionsBehind {#revisionsbehind}

#### Get Signature {#get-signature-1}

```ts
get revisionsBehind(): bigint | null;
```

Return the exact stale distance when applicable\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`bigint` \| `null`
