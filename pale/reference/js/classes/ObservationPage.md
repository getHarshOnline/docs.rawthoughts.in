---
title: "Class: ObservationPage"
---

<a id="class&#45;observationpage"></a>

One valid bounded observation\-page step\.

## Accessors {#accessors}

### completion {#completion}

#### Get Signature {#get-signature}

```ts
get completion(): ObservationStepCompletionKind;
```

Return whether this step exhausted its selected input\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationStepCompletionKind`](/pale/reference/js/enumerations/ObservationStepCompletionKind)

-----

### continuation {#continuation}

#### Get Signature {#get-signature-1}

```ts
get continuation(): ObservationPageCursor | null;
```

Return the continuation when matching facts remain\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationPageCursor`](/pale/reference/js/classes/ObservationPageCursor) \| `null`

-----

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature-2}

```ts
get copiedStringBytes(): number;
```

Return variable\-length UTF\-8 bytes copied by this step\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### cursor {#cursor}

#### Get Signature {#get-signature-3}

```ts
get cursor(): ObservationCursor;
```

Return the exact snapshot cursor\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor)

-----

### facts {#facts}

#### Get Signature {#get-signature-4}

```ts
get facts(): ObservationFact[];
```

Return deterministically ordered typed facts\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationFact`](/pale/reference/js/classes/ObservationFact)\[\]

-----

### inspected {#inspected}

#### Get Signature {#get-signature-5}

```ts
get inspected(): number;
```

Return retained facts examined by this step\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### minimumRequired {#minimumrequired}

#### Get Signature {#get-signature-6}

```ts
get minimumRequired(): number | null;
```

Return the minimum bound needed by an indivisible result, if applicable\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `null`

-----

### snapshotOmittedCount {#snapshotomittedcount}

#### Get Signature {#get-signature-7}

```ts
get snapshotOmittedCount(): number;
```

Return facts omitted when the bounded snapshot was constructed\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### stoppedBy {#stoppedby}

#### Get Signature {#get-signature-8}

```ts
get stoppedBy(): 
  | ObservationStepLimitKind
  | null;
```

Return the resource that stopped this step, if any\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationStepLimitKind`](/pale/reference/js/enumerations/ObservationStepLimitKind)
\| `null`
