---
title: "Class: AuthoringPathSegment"
---

<a id="class&#45;authoringpathsegment"></a>

One structural grammar step used for hover and completion inspection\.

## Methods {#methods}

### arrayItem\(\) {#arrayitem}

```ts
static arrayItem(): AuthoringPathSegment;
```

Construct one structural array\-item step\.

#### Returns {#returns}

`AuthoringPathSegment`

-----

### field\(\) {#field}

```ts
static field(name: string): AuthoringPathSegment;
```

Construct one exact field step\.

#### Parameters {#parameters}

<Heading level={5} id="name" className="scroll-mt-(--scroll-mt)">name</Heading>

`string`

#### Returns {#returns-1}

`AuthoringPathSegment`
