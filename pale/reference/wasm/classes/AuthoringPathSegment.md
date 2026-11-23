---
title: "Class: AuthoringPathSegment"
---

<a id="class&#45;authoringpathsegment"></a>

One structural path step supplied by a tolerant host parser\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-1}

`void`

-----

### arrayItem\(\) {#arrayitem}

```ts
static arrayItem(): AuthoringPathSegment;
```

Construct one structural array\-item step\.

#### Returns {#returns-2}

`AuthoringPathSegment`

-----

### field\(\) {#field}

```ts
static field(value: string): AuthoringPathSegment;
```

Construct one exact field step\.

#### Parameters {#parameters}

<Heading level={5} id="value" className="scroll-mt-(--scroll-mt)">value</Heading>

`string`

#### Returns {#returns-3}

`AuthoringPathSegment`
