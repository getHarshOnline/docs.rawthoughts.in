---
title: "Class: ObservationReconciliationState"
---

<a id="class&#45;observationreconciliationstate"></a>

Reconciliation state and exact case/result coordinate\.

## Accessors {#accessors}

### caseDigest {#casedigest}

#### Get Signature {#get-signature}

```ts
get caseDigest(): string | null;
```

Return the active reconciliation case digest, when any\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-1}

```ts
get kind(): ObservationReconciliationStateKind;
```

Return the closed reconciliation kind\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationReconciliationStateKind`](/pale/reference/js/enumerations/ObservationReconciliationStateKind)

-----

### resultDigest {#resultdigest}

#### Get Signature {#get-signature-2}

```ts
get resultDigest(): string | null;
```

Return the terminal result digest when settled\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`
