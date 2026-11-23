---
title: "Interface: SearchIndex<R extends SearchRecord = SearchRecord>"
---

<a id="interface&#45;searchindex&#45;r&#45;extends&#45;searchrecord&#45;searchrecord"></a>

## Type Parameters {#type-parameters}

### R {#r}

`R` *extends* [`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord) \= [`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord)

## Properties {#properties}

### profile {#profile}

> `readonly` **profile**: `"lexical"` \| `"english"`

-----

### size {#size}

> `readonly` **size**: `number`

## Methods {#methods}

### browse\(\) {#browse}

> **browse**\(`query`: `string`, `options`: [`BrowseOptions`](/gazette/javascript/search/interfaces/BrowseOptions)\): [`BrowseResults`](/gazette/javascript/search/interfaces/BrowseResults)\<`R`\>

Complete eligible\-corpus filtering/counting/sorting precedes the bounded slice\.

#### Parameters {#parameters}

<Heading level={5} id="query" className="scroll-mt-(--scroll-mt)">query</Heading>

`string`

<Heading level={5} id="options" className="scroll-mt-(--scroll-mt)">options</Heading>

[`BrowseOptions`](/gazette/javascript/search/interfaces/BrowseOptions)

#### Returns {#returns}

[`BrowseResults`](/gazette/javascript/search/interfaces/BrowseResults)\<`R`\>

-----

### search\(\) {#search}

> **search**\(`query`: `string`, `options`: [`QueryOptions`](/gazette/javascript/search/interfaces/QueryOptions)\): readonly [`SearchHit`](/gazette/javascript/search/interfaces/SearchHit)\<`R`\>\[\]

#### Parameters {#parameters-1}

<Heading level={5} id="query&#45;1" className="scroll-mt-(--scroll-mt)">query</Heading>

`string`

<Heading level={5} id="options&#45;1" className="scroll-mt-(--scroll-mt)">options</Heading>

[`QueryOptions`](/gazette/javascript/search/interfaces/QueryOptions)

#### Returns {#returns-1}

readonly [`SearchHit`](/gazette/javascript/search/interfaces/SearchHit)\<`R`\>\[\]
