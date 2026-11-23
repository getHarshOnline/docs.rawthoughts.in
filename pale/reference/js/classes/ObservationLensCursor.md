---
title: "Class: ObservationLensCursor"
---

<a id="class&#45;observationlenscursor"></a>

Opaque continuation for one exact bounded lens query\.

It binds the snapshot, filter, causal\-path choice, raw limits, and next
subject\. Pass it only to the same query\. Its position does not prove that
later subjects are absent\.

## Accessors {#accessors}

### inspectedPosition {#inspectedposition}

#### Get Signature {#get-signature}

```ts
get inspectedPosition(): number;
```

Return how many retained subjects precede the next step\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### snapshot {#snapshot}

#### Get Signature {#get-signature-1}

```ts
get snapshot(): ObservationCursor;
```

Return the exact snapshot cursor\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor)
