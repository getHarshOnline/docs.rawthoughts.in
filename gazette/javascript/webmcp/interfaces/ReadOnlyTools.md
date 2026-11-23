---
title: "Interface: ReadOnlyTools"
---

<a id="interface&#45;readonlytools"></a>

## Properties {#properties}

### currentPage? {#currentpage}

> `readonly` `optional` **currentPage?**: \(`options`: \{ `signal`: `AbortSignal`; \}\) \=\> [`Json`](/gazette/javascript/search/type-aliases/Json) \| `Promise`\<[`Json`](/gazette/javascript/search/type-aliases/Json)\>

Already admitted public projection, not private inspection data or scraped DOM\.

#### Parameters {#parameters}

<Heading level={5} id="options" className="scroll-mt-(--scroll-mt)">options</Heading>

<Heading level={6} id="signal" className="scroll-mt-(--scroll-mt)">signal</Heading>

`AbortSignal`

#### Returns {#returns}

[`Json`](/gazette/javascript/search/type-aliases/Json) \| `Promise`\<[`Json`](/gazette/javascript/search/type-aliases/Json)\>

-----

### limits {#limits}

> `readonly` **limits**: [`WebMcpLimits`](/gazette/javascript/webmcp/interfaces/WebMcpLimits)

-----

### search? {#search}

> `readonly` `optional` **search?**: \(`query`: `string`, `options`: \{ `limit`: `number`; `signal`: `AbortSignal`; \}\) \=\> readonly \([`Json`](/gazette/javascript/search/type-aliases/Json) \| [`SearchHit`](/gazette/javascript/search/interfaces/SearchHit)\<[`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord)\>\)\[\] \| `Promise`\<readonly \([`Json`](/gazette/javascript/search/type-aliases/Json) \| [`SearchHit`](/gazette/javascript/search/interfaces/SearchHit)\<[`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord)\>\)\[\]\>

Reuse existing search; return the complete requested hits without another resolver\.

#### Parameters {#parameters-1}

<Heading level={5} id="query" className="scroll-mt-(--scroll-mt)">query</Heading>

`string`

<Heading level={5} id="options&#45;1" className="scroll-mt-(--scroll-mt)">options</Heading>

<Heading level={6} id="limit" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

<Heading level={6} id="signal&#45;1" className="scroll-mt-(--scroll-mt)">signal</Heading>

`AbortSignal`

#### Returns {#returns-1}

readonly \([`Json`](/gazette/javascript/search/type-aliases/Json) \| [`SearchHit`](/gazette/javascript/search/interfaces/SearchHit)\<[`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord)\>\)\[\] \| `Promise`\<readonly \([`Json`](/gazette/javascript/search/type-aliases/Json) \| [`SearchHit`](/gazette/javascript/search/interfaces/SearchHit)\<[`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord)\>\)\[\]\>

-----

### tools {#tools}

> `readonly` **tools**: readonly [`ReadOnlyTool`](/gazette/javascript/webmcp/type-aliases/ReadOnlyTool)\[\]
