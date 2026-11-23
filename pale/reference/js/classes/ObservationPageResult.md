---
title: "Class: ObservationPageResult"
---

<a id="class&#45;observationpageresult"></a>

Typed page query result; resynchronization is data, not an exception\.

## Accessors {#accessors}

### cancelledContinuation {#cancelledcontinuation}

#### Get Signature {#get-signature}

```ts
get cancelledContinuation(): ObservationPageCursor | null;
```

Return the unchanged continuation after cancellation, if any\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationPageCursor`](/pale/reference/js/classes/ObservationPageCursor) \| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-1}

```ts
get kind(): ObservationPageResultKind;
```

Return the closed result kind\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationPageResultKind`](/pale/reference/js/enumerations/ObservationPageResultKind)

-----

### page {#page}

#### Get Signature {#get-signature-2}

```ts
get page(): ObservationPage | null;
```

Return the bounded page when ready\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationPage`](/pale/reference/js/classes/ObservationPage) \| `null`

-----

### resynchronization {#resynchronization}

#### Get Signature {#get-signature-3}

```ts
get resynchronization(): 
  | ObservationResynchronization
  | null;
```

Return the full\-snapshot instruction when resynchronization is required\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationResynchronization`](/pale/reference/js/classes/ObservationResynchronization)
\| `null`
