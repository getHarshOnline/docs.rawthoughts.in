---
title: "Class: AuthoringInstancePathSegment"
---

<a id="class&#45;authoringinstancepathsegment"></a>

One exact decoded\-key or array\-index step used for semantic navigation\.

## Methods {#methods}

### field\(\) {#field}

```ts
static field(name: string): AuthoringInstancePathSegment;
```

Construct one exact decoded\-key step\.

#### Parameters {#parameters}

<Heading level={5} id="name" className="scroll-mt-(--scroll-mt)">name</Heading>

`string`

#### Returns {#returns}

`AuthoringInstancePathSegment`

-----

### index\(\) {#index}

```ts
static index(index: number): AuthoringInstancePathSegment;
```

Construct one exact array\-member step\.

#### Parameters {#parameters-1}

<Heading level={5} id="index&#45;1" className="scroll-mt-(--scroll-mt)">index</Heading>

`number`

#### Returns {#returns-1}

`AuthoringInstancePathSegment`
