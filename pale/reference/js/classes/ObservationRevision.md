---
title: "Class: ObservationRevision"
---

<a id="class&#45;observationrevision"></a>

Owned revision coordinate\.

## Accessors {#accessors}

### kind {#kind}

#### Get Signature {#get-signature}

```ts
get kind(): ObservationRevisionKind;
```

Return the closed revision kind\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationRevisionKind`](/pale/reference/js/enumerations/ObservationRevisionKind)

-----

### sequence {#sequence}

#### Get Signature {#get-signature-1}

```ts
get sequence(): bigint | null;
```

Return the durable resident sequence when it exists\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`bigint` \| `null`
