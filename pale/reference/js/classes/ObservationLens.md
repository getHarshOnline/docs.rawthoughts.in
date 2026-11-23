---
title: "Class: ObservationLens"
---

<a id="class&#45;observationlens"></a>

Bounded generation\-bound visualization substrate\.

## Accessors {#accessors}

### causalPathLookups {#causalpathlookups}

#### Get Signature {#get-signature}

```ts
get causalPathLookups(): number;
```

Return causal\-path lookups performed by this step\.

A stopped step can count a lookup for an unreturned subject\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### causalPaths {#causalpaths}

#### Get Signature {#get-signature-1}

```ts
get causalPaths(): ObservationCausalPath[];
```

Return retained causal paths when requested\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCausalPath`](/pale/reference/js/classes/ObservationCausalPath)\[\]

-----

### causalSteps {#causalsteps}

#### Get Signature {#get-signature-2}

```ts
get causalSteps(): number;
```

Return causal steps copied by this step\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### completion {#completion}

#### Get Signature {#get-signature-3}

```ts
get completion(): ObservationStepCompletionKind;
```

Return whether this step exhausted its selected input\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationStepCompletionKind`](/pale/reference/js/enumerations/ObservationStepCompletionKind)

-----

### continuation {#continuation}

#### Get Signature {#get-signature-4}

```ts
get continuation(): ObservationLensCursor | null;
```

Return the continuation when selected subjects may remain\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationLensCursor`](/pale/reference/js/classes/ObservationLensCursor) \| `null`

-----

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature-5}

```ts
get copiedStringBytes(): number;
```

Return variable\-length UTF\-8 bytes copied by this step\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### cursor {#cursor}

#### Get Signature {#get-signature-6}

```ts
get cursor(): ObservationCursor;
```

Return the exact source snapshot coordinate\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor)

-----

### inspectedSubjects {#inspectedsubjects}

#### Get Signature {#get-signature-7}

```ts
get inspectedSubjects(): number;
```

Return retained subjects examined by this step\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### minimumRequired {#minimumrequired}

#### Get Signature {#get-signature-8}

```ts
get minimumRequired(): number | null;
```

Return the minimum bound needed by an indivisible result, if applicable\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `null`

-----

### nodes {#nodes}

#### Get Signature {#get-signature-9}

```ts
get nodes(): ObservationLensNode[];
```

Return deterministically ordered subject nodes\.

<Heading level={5} id="returns&#45;9" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationLensNode`](/pale/reference/js/classes/ObservationLensNode)\[\]

-----

### snapshotOmittedCount {#snapshotomittedcount}

#### Get Signature {#get-signature-10}

```ts
get snapshotOmittedCount(): number;
```

Return owner facts omitted when the bounded snapshot was constructed\.

<Heading level={5} id="returns&#45;10" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### stoppedBy {#stoppedby}

#### Get Signature {#get-signature-11}

```ts
get stoppedBy(): 
  | ObservationStepLimitKind
  | null;
```

Return the resource that stopped this step, if any\.

<Heading level={5} id="returns&#45;11" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationStepLimitKind`](/pale/reference/js/enumerations/ObservationStepLimitKind)
\| `null`
