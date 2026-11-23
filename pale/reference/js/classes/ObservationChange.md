---
title: "Class: ObservationChange"
---

<a id="class&#45;observationchange"></a>

One deterministic fact change\.

## Accessors {#accessors}

### category {#category}

#### Get Signature {#get-signature}

```ts
get category(): ObservationCategory | null;
```

Return the removed category for a removal\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCategory`](/pale/reference/js/enumerations/ObservationCategory) \| `null`

-----

### fact {#fact}

#### Get Signature {#get-signature-1}

```ts
get fact(): ObservationFact | null;
```

Return the complete successor fact for an upsert\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationFact`](/pale/reference/js/classes/ObservationFact) \| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-2}

```ts
get kind(): ObservationChangeKind;
```

Return the closed change kind\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationChangeKind`](/pale/reference/js/enumerations/ObservationChangeKind)

-----

### subject {#subject}

#### Get Signature {#get-signature-3}

```ts
get subject(): ObservationSubject | null;
```

Return the removed subject for a removal\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationSubject`](/pale/reference/js/classes/ObservationSubject) \| `null`
