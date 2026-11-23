---
title: "Class: ObservationProfileAssociation"
---

<a id="class&#45;observationprofileassociation"></a>

Association with one exact observation snapshot\.

## Accessors {#accessors}

### coordinates {#coordinates}

#### Get Signature {#get-signature}

```ts
get coordinates(): EffectiveProfileCoordinates;
```

Return all coordinates of the associated profile\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`EffectiveProfileCoordinates`](/pale/reference/js/interfaces/EffectiveProfileCoordinates)

-----

### cursor {#cursor}

#### Get Signature {#get-signature-1}

```ts
get cursor(): ObservationCursor;
```

Return the cursor of the exact retained snapshot\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor)

## Methods {#methods}

### belongsTo\(\) {#belongsto}

```ts
belongsTo(snapshot: ObservationSnapshot): boolean;
```

Test exact snapshot custody\. Equal cursors are insufficient\.

#### Parameters {#parameters}

<Heading level={5} id="snapshot" className="scroll-mt-(--scroll-mt)">snapshot</Heading>

[`ObservationSnapshot`](/pale/reference/js/classes/ObservationSnapshot)

#### Returns {#returns-2}

`boolean`
