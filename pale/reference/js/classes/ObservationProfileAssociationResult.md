---
title: "Class: ObservationProfileAssociationResult"
---

<a id="class&#45;observationprofileassociationresult"></a>

A profile association or a typed refusal\.

## Accessors {#accessors}

### association {#association}

#### Get Signature {#get-signature}

```ts
get association(): 
  | ObservationProfileAssociation
  | null;
```

Return the association only when the check qualified\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationProfileAssociation`](/pale/reference/js/classes/ObservationProfileAssociation)
\| `null`

-----

### error {#error}

#### Get Signature {#get-signature-1}

```ts
get error(): 
  | ObservationProfileError
  | null;
```

Return the refusal without converting it to text or an exception\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationProfileError`](/pale/reference/js/enumerations/ObservationProfileError)
\| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-2}

```ts
get kind(): ObservationProfileAssociationResultKind;
```

Select the associated or refused branch\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationProfileAssociationResultKind`](/pale/reference/js/enumerations/ObservationProfileAssociationResultKind)
