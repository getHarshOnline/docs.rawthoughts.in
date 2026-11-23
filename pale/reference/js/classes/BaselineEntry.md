---
title: "Class: BaselineEntry"
---

<a id="class&#45;baselineentry"></a>

One caller\-captured pre\-mutation baseline observation\.

## Methods {#methods}

### absent\(\) {#absent}

```ts
static absent(relativePath: string): BaselineEntry;
```

Construct an explicit absent\-file observation\.

#### Parameters {#parameters}

<Heading level={5} id="relativepath" className="scroll-mt-(--scroll-mt)">relativePath</Heading>

`string`

#### Returns {#returns}

`BaselineEntry`

-----

### present\(\) {#present}

```ts
static present(
   relativePath: string, 
   sha256: string, 
   unixMode: number
): BaselineEntry;
```

Construct an explicit present\-file observation\.

#### Parameters {#parameters-1}

<Heading level={5} id="relativepath&#45;1" className="scroll-mt-(--scroll-mt)">relativePath</Heading>

`string`

<Heading level={5} id="sha256" className="scroll-mt-(--scroll-mt)">sha256</Heading>

`string`

<Heading level={5} id="unixmode" className="scroll-mt-(--scroll-mt)">unixMode</Heading>

`number`

#### Returns {#returns-1}

`BaselineEntry`
