---
title: "Class: ObservationPageCursor"
---

<a id="class&#45;observationpagecursor"></a>

Opaque continuation for one exact filtered snapshot page\.

It binds the snapshot, filter, raw limits, and next fact\. Pass it only to
the same query\. Its position does not prove that later facts are absent\.

## Accessors {#accessors}

### inspectedPosition {#inspectedposition}

#### Get Signature {#get-signature}

```ts
get inspectedPosition(): number;
```

Return how many retained facts precede the next step\.

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
