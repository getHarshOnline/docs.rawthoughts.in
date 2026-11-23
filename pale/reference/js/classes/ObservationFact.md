---
title: "Class: ObservationFact"
---

<a id="class&#45;observationfact"></a>

One independently typed observation fact\.

## Accessors {#accessors}

### category {#category}

#### Get Signature {#get-signature}

```ts
get category(): ObservationCategory;
```

Return the independent fact axis\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCategory`](/pale/reference/js/enumerations/ObservationCategory)

-----

### effectCertainty {#effectcertainty}

#### Get Signature {#get-signature-1}

```ts
get effectCertainty(): 
  | DiagnosticEffectCertainty
  | null;
```

Return effect certainty only on the effect axis\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`DiagnosticEffectCertainty`](/pale/reference/js/enumerations/DiagnosticEffectCertainty)
\| `null`

-----

### freshness {#freshness}

#### Get Signature {#get-signature-2}

```ts
get freshness(): ObservationFreshness;
```

Return the fact's temporal qualification\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationFreshness`](/pale/reference/js/classes/ObservationFreshness)

-----

### healthState {#healthstate}

#### Get Signature {#get-signature-3}

```ts
get healthState(): 
  | ObservationHealthState
  | null;
```

Return health state only on the health axis\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationHealthState`](/pale/reference/js/enumerations/ObservationHealthState)
\| `null`

-----

### nativeState {#nativestate}

#### Get Signature {#get-signature-4}

```ts
get nativeState(): ObservationNativeState | null;
```

Return native evidence only on the native\-owner axis\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationNativeState`](/pale/reference/js/classes/ObservationNativeState) \| `null`

-----

### operationExposure {#operationexposure}

#### Get Signature {#get-signature-5}

```ts
get operationExposure(): OperationExposure | null;
```

Return operation exposure only on that axis\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OperationExposure`](/pale/reference/js/enumerations/OperationExposure) \| `null`

-----

### processIntent {#processintent}

#### Get Signature {#get-signature-6}

```ts
get processIntent(): 
  | ObservationProcessIntent
  | null;
```

Return process intent only on that axis\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationProcessIntent`](/pale/reference/js/enumerations/ObservationProcessIntent)
\| `null`

-----

### readinessState {#readinessstate}

#### Get Signature {#get-signature-7}

```ts
get readinessState(): 
  | ObservationReadinessState
  | null;
```

Return readiness only on the readiness axis\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationReadinessState`](/pale/reference/js/enumerations/ObservationReadinessState)
\| `null`

-----

### reconciliationState {#reconciliationstate}

#### Get Signature {#get-signature-8}

```ts
get reconciliationState(): 
  | ObservationReconciliationState
  | null;
```

Return reconciliation state only on that axis\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationReconciliationState`](/pale/reference/js/classes/ObservationReconciliationState)
\| `null`

-----

### requirementDisposition {#requirementdisposition}

#### Get Signature {#get-signature-9}

```ts
get requirementDisposition(): 
  | RequirementDisposition
  | null;
```

Return capability disposition only on that independent axis\.

<Heading level={5} id="returns&#45;9" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`RequirementDisposition`](/pale/reference/js/type-aliases/RequirementDisposition)
\| `null`

-----

### subject {#subject}

#### Get Signature {#get-signature-10}

```ts
get subject(): ObservationSubject | null;
```

Return the exact subject when this axis is subject\-scoped\.

<Heading level={5} id="returns&#45;10" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationSubject`](/pale/reference/js/classes/ObservationSubject) \| `null`
