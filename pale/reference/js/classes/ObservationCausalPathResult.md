---
title: "Class: ObservationCausalPathResult"
---

<a id="class&#45;observationcausalpathresult"></a>

Typed causal query result\.

## Accessors {#accessors}

### kind {#kind}

#### Get Signature {#get-signature}

```ts
get kind(): ObservationCausalResultKind;
```

Return the closed query disposition\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCausalResultKind`](/pale/reference/js/enumerations/ObservationCausalResultKind)

-----

### path {#path}

#### Get Signature {#get-signature-1}

```ts
get path(): ObservationCausalPath | null;
```

Return the exact proof when found\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCausalPath`](/pale/reference/js/classes/ObservationCausalPath) \| `null`

-----

### resynchronization {#resynchronization}

#### Get Signature {#get-signature-2}

```ts
get resynchronization(): 
  | ObservationResynchronization
  | null;
```

Return the recovery instruction for a stale selector generation\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationResynchronization`](/pale/reference/js/classes/ObservationResynchronization)
\| `null`
