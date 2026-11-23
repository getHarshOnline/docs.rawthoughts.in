---
title: "Class: ObservationProfileResult"
---

<a id="class&#45;observationprofileresult"></a>

A completed query or contextual refusal, not an operation\-failure diagnostic\.

## Accessors {#accessors}

### error {#error}

#### Get Signature {#get-signature}

```ts
get error(): 
  | ObservationProfileError
  | null;
```

Return the refusal without converting it to a message or exception\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationProfileError`](/pale/reference/js/enumerations/ObservationProfileError)
\| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-1}

```ts
get kind(): ObservationProfileResultKind;
```

Select the page or refusal branch\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationProfileResultKind`](/pale/reference/js/enumerations/ObservationProfileResultKind)

-----

### page {#page}

#### Get Signature {#get-signature-2}

```ts
get page(): ObservationProfilePage | null;
```

Return the page only when this query qualified\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationProfilePage`](/pale/reference/js/classes/ObservationProfilePage) \| `null`
