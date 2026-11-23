---
title: "Class: EffectiveAuthoringPage"
---

<a id="class&#45;effectiveauthoringpage"></a>

Copied profile rows and a continuation over their original retained owner\.

## Accessors {#accessors}

### coordinates {#coordinates}

#### Get Signature {#get-signature}

```ts
get coordinates(): EffectiveProfileCoordinates;
```

Full profile coordinate, including its private instance identity\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`EffectiveProfileCoordinates`](/pale/reference/js/interfaces/EffectiveProfileCoordinates)

-----

### entries {#entries}

#### Get Signature {#get-signature-1}

```ts
get entries(): EffectiveProfileEntry[];
```

Copy associated rows using the existing typed profile projection\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`EffectiveProfileEntry`](/pale/reference/js/classes/EffectiveProfileEntry)\[\]

## Methods {#methods}

### continuation\(\) {#continuation}

```ts
continuation(): 
  | EffectiveAuthoringContinuation
  | null;
```

Share the continuation, or return `null` when no rows remain\.

#### Returns {#returns-2}

\| [`EffectiveAuthoringContinuation`](/pale/reference/js/classes/EffectiveAuthoringContinuation)
\| `null`
