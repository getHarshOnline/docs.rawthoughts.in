---
title: "Class: ObservationFilter"
---

<a id="class&#45;observationfilter"></a>

Opaque API\-owned filter; setters only compose the canonical filter algebra\.

## Constructors {#constructors}

### Constructor {#constructor}

```ts
new ObservationFilter(): ObservationFilter;
```

Construct an unrestricted filter\.

#### Returns {#returns}

`ObservationFilter`

## Methods {#methods}

### selectCategory\(\) {#selectcategory}

```ts
selectCategory(category: ObservationCategory): void;
```

Restrict this filter to one independent category\.

#### Parameters {#parameters}

<Heading level={5} id="category" className="scroll-mt-(--scroll-mt)">category</Heading>

[`ObservationCategory`](/pale/reference/js/enumerations/ObservationCategory)

#### Returns {#returns-1}

`void`

-----

### selectFreshness\(\) {#selectfreshness}

```ts
selectFreshness(freshness: ObservationFreshnessClass): void;
```

Restrict this filter to one freshness class\.

#### Parameters {#parameters-1}

<Heading level={5} id="freshness" className="scroll-mt-(--scroll-mt)">freshness</Heading>

[`ObservationFreshnessClass`](/pale/reference/js/enumerations/ObservationFreshnessClass)

#### Returns {#returns-2}

`void`

-----

### selectSubject\(\) {#selectsubject}

```ts
selectSubject(subject: ObservationSubject): void;
```

Restrict this filter to one API\-issued subject\.

#### Parameters {#parameters-2}

<Heading level={5} id="subject" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`ObservationSubject`](/pale/reference/js/classes/ObservationSubject)

#### Returns {#returns-3}

`void`
