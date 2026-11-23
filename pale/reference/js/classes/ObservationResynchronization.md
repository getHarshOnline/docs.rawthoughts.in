---
title: "Class: ObservationResynchronization"
---

<a id="class&#45;observationresynchronization"></a>

Typed instruction to request a new complete snapshot\.

## Accessors {#accessors}

### current {#current}

#### Get Signature {#get-signature}

```ts
get current(): ObservationCursor;
```

Return the current cursor from which to restart\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor)

-----

### currentGeneration {#currentgeneration}

#### Get Signature {#get-signature-1}

```ts
get currentGeneration(): ObservationGeneration | null;
```

Return the current generation when a generation mismatch occurred\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationGeneration`](/pale/reference/js/classes/ObservationGeneration) \| `null`

-----

### currentRevision {#currentrevision}

#### Get Signature {#get-signature-2}

```ts
get currentRevision(): ObservationRevision | null;
```

Return the current revision when a revision gap occurred\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationRevision`](/pale/reference/js/classes/ObservationRevision) \| `null`

-----

### reason {#reason}

#### Get Signature {#get-signature-3}

```ts
get reason(): ObservationResynchronizationReason;
```

Return the exact recovery reason\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationResynchronizationReason`](/pale/reference/js/enumerations/ObservationResynchronizationReason)

-----

### requestedGeneration {#requestedgeneration}

#### Get Signature {#get-signature-4}

```ts
get requestedGeneration(): ObservationGeneration | null;
```

Return the caller\-held generation when a generation mismatch occurred\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationGeneration`](/pale/reference/js/classes/ObservationGeneration) \| `null`

-----

### requestedRevision {#requestedrevision}

#### Get Signature {#get-signature-5}

```ts
get requestedRevision(): ObservationRevision | null;
```

Return the caller\-held revision when a revision gap occurred\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationRevision`](/pale/reference/js/classes/ObservationRevision) \| `null`
