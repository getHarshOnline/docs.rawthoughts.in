---
title: "Interface: BrowseResults<R extends SearchRecord = SearchRecord>"
---

<a id="interface&#45;browseresults&#45;r&#45;extends&#45;searchrecord&#45;searchrecord"></a>

## Type Parameters {#type-parameters}

### R {#r}

`R` *extends* [`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord) \= [`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord)

## Properties {#properties}

### facets {#facets}

> `readonly` **facets**: \{ `readonly` `author`: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]; `readonly` `classification`: readonly [`ClassificationFacet`](/gazette/javascript/search/interfaces/ClassificationFacet)\[\]; `readonly` `keyword`: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]; `readonly` `kind`: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]; `readonly` `project`: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]; `readonly` `site`: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]; \}

Counts over that same complete population; absent metadata contributes no value\.

#### author {#author}

> `readonly` **author**: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]

#### classification {#classification}

> `readonly` **classification**: readonly [`ClassificationFacet`](/gazette/javascript/search/interfaces/ClassificationFacet)\[\]

#### keyword {#keyword}

> `readonly` **keyword**: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]

#### kind {#kind}

> `readonly` **kind**: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]

#### project {#project}

> `readonly` **project**: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]

#### site {#site}

> `readonly` **site**: readonly [`SearchFacet`](/gazette/javascript/search/interfaces/SearchFacet)\[\]

-----

### hits {#hits}

> `readonly` **hits**: readonly [`SearchHit`](/gazette/javascript/search/interfaces/SearchHit)\<`R`\>\[\]

-----

### limit {#limit}

> `readonly` **limit**: `number`

-----

### offset {#offset}

> `readonly` **offset**: `number`

-----

### total {#total}

> `readonly` **total**: `number`

Complete matching population after filters, before pagination\.
