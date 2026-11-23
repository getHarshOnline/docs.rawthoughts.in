---
title: "Class: ObservationLensDisposition"
---

<a id="class&#45;observationlensdisposition"></a>

Typed visual\-lens result\.

## Accessors {#accessors}

### cancelledContinuation {#cancelledcontinuation}

#### Get Signature {#get-signature}

```ts
get cancelledContinuation(): ObservationLensCursor | null;
```

Return the unchanged continuation after cancellation, if any\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationLensCursor`](/pale/reference/js/classes/ObservationLensCursor) \| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-1}

```ts
get kind(): ObservationLensDispositionKind;
```

Return the closed disposition kind\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationLensDispositionKind`](/pale/reference/js/enumerations/ObservationLensDispositionKind)

-----

### lens {#lens}

#### Get Signature {#get-signature-2}

```ts
get lens(): ObservationLens | null;
```

Return the bounded lens step when ready\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationLens`](/pale/reference/js/classes/ObservationLens) \| `null`

-----

### resynchronization {#resynchronization}

#### Get Signature {#get-signature-3}

```ts
get resynchronization(): 
  | ObservationResynchronization
  | null;
```

Return the recovery instruction for a mismatched continuation\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationResynchronization`](/pale/reference/js/classes/ObservationResynchronization)
\| `null`
