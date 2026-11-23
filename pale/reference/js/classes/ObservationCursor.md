---
title: "Class: ObservationCursor"
---

<a id="class&#45;observationcursor"></a>

Opaque generation/revision cursor issued by the API\.

## Accessors {#accessors}

### generation {#generation}

#### Get Signature {#get-signature}

```ts
get generation(): ObservationGeneration;
```

Return the admitted generation coordinate\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationGeneration`](/pale/reference/js/classes/ObservationGeneration)

-----

### revision {#revision}

#### Get Signature {#get-signature-1}

```ts
get revision(): ObservationRevision;
```

Return the revision within this cursor's `generation`\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationRevision`](/pale/reference/js/classes/ObservationRevision)
