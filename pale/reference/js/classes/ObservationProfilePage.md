---
title: "Class: ObservationProfilePage"
---

<a id="class&#45;observationprofilepage"></a>

Original profile rows and the progress of this bounded query\.

## Accessors {#accessors}

### continuation {#continuation}

#### Get Signature {#get-signature}

```ts
get continuation(): 
  | ObservationProfileContinuation
  | null;
```

Continue if rows remain\. An empty page can still have a continuation\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`ObservationProfileContinuation`](/pale/reference/js/classes/ObservationProfileContinuation)
\| `null`

-----

### coordinates {#coordinates}

#### Get Signature {#get-signature-1}

```ts
get coordinates(): EffectiveProfileCoordinates;
```

Identify the producing profile; this does not establish native readiness\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`EffectiveProfileCoordinates`](/pale/reference/js/interfaces/EffectiveProfileCoordinates)

-----

### entries {#entries}

#### Get Signature {#get-signature-2}

```ts
get entries(): EffectiveProfileEntry[];
```

Return original row payloads with their existing explanation handles\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`EffectiveProfileEntry`](/pale/reference/js/classes/EffectiveProfileEntry)\[\]

-----

### inspected {#inspected}

#### Get Signature {#get-signature-3}

```ts
get inspected(): number;
```

Count all examined rows, including rows that did not match\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### mapping {#mapping}

#### Get Signature {#get-signature-4}

```ts
get mapping(): ObservationProfileMapping;
```

Distinguish unsupported categories from an empty intermediate page\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationProfileMapping`](/pale/reference/js/enumerations/ObservationProfileMapping)
