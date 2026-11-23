---
title: "Interface: SearchHit<R extends SearchRecord = SearchRecord>"
---

<a id="interface&#45;searchhit&#45;r&#45;extends&#45;searchrecord&#45;searchrecord"></a>

## Type Parameters {#type-parameters}

### R {#r}

`R` *extends* [`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord) \= [`SearchRecord`](/gazette/javascript/search/interfaces/SearchRecord)

## Properties {#properties}

### record {#record}

> `readonly` **record**: [`Captured`](/gazette/javascript/search/type-aliases/Captured)\<`R`\>

Owned immutable JSON snapshot; no rendered HTML or reconstructed metadata\.

-----

### score {#score}

> `readonly` **score**: `number`

Best matching provider relevance score; a full indexed\-title match precedes other hits\.
