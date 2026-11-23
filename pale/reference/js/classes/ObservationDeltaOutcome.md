---
title: "Class: ObservationDeltaOutcome"
---

<a id="class&#45;observationdeltaoutcome"></a>

Typed delta outcome retaining all recovery coordinates\.

## Accessors {#accessors}

### cancelledAt {#cancelledat}

#### Get Signature {#get-signature}

```ts
get cancelledAt(): ObservationCursor | null;
```

Return the completely applied cursor retained after cancellation\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor) \| `null`

-----

### changes {#changes}

#### Get Signature {#get-signature-1}

```ts
get changes(): ObservationChange[];
```

Return the complete ordered change batch for a delta\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationChange`](/pale/reference/js/classes/ObservationChange)\[\]

-----

### cursor {#cursor}

#### Get Signature {#get-signature-2}

```ts
get cursor(): ObservationCursor | null;
```

Return the current cursor for caught\-up or backpressured outcomes\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor) \| `null`

-----

### from {#from}

#### Get Signature {#get-signature-3}

```ts
get from(): ObservationCursor | null;
```

Return the predecessor cursor for a complete delta\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor) \| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-4}

```ts
get kind(): ObservationDeltaOutcomeKind;
```

Return the closed outcome kind\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationDeltaOutcomeKind`](/pale/reference/js/enumerations/ObservationDeltaOutcomeKind)

-----

### maximumChanges {#maximumchanges}

#### Get Signature {#get-signature-5}

```ts
get maximumChanges(): number | null;
```

Return the caller\-declared change ceiling after backpressure\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `null`

-----

### pendingChanges {#pendingchanges}

#### Get Signature {#get-signature-6}

```ts
get pendingChanges(): number | null;
```

Return the required atomic change count after backpressure\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `null`

-----

### recovery {#recovery}

#### Get Signature {#get-signature-7}

```ts
get recovery(): 
  | RequestSnapshot
  | null;
```

Return the safe recovery action after backpressure\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`RequestSnapshot`](/pale/reference/js/enumerations/ObservationBackpressureRecovery#requestsnapshot)
\| `null`

-----

### resynchronization {#resynchronization}

#### Get Signature {#get-signature-8}

```ts
get resynchronization(): 
  | ObservationResynchronization
  | null;
```

Return the recovery instruction when resynchronization is required\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationResynchronization`](/pale/reference/js/classes/ObservationResynchronization)
\| `null`

-----

### successorOmittedFactCount {#successoromittedfactcount}

#### Get Signature {#get-signature-9}

```ts
get successorOmittedFactCount(): number | null;
```

Return the omitted\-fact count installed with a complete delta\.

<Heading level={5} id="returns&#45;9" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `null`

-----

### to {#to}

#### Get Signature {#get-signature-10}

```ts
get to(): ObservationCursor | null;
```

Return the successor cursor for a complete delta\.

<Heading level={5} id="returns&#45;10" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor) \| `null`
