---
title: "Class: ObservationCausalPath"
---

<a id="class&#45;observationcausalpath"></a>

One bounded exact causal proof\.

## Accessors {#accessors}

### generation {#generation}

#### Get Signature {#get-signature}

```ts
get generation(): ObservationGeneration;
```

Return the generation in which the proof is meaningful\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationGeneration`](/pale/reference/js/classes/ObservationGeneration)

-----

### steps {#steps}

#### Get Signature {#get-signature-1}

```ts
get steps(): ObservationCausalStep[];
```

Return the ordered compiler\-owned proof steps\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCausalStep`](/pale/reference/js/classes/ObservationCausalStep)\[\]

-----

### subject {#subject}

#### Get Signature {#get-signature-2}

```ts
get subject(): ObservationSubject;
```

Return the exact selected subject\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationSubject`](/pale/reference/js/classes/ObservationSubject)
