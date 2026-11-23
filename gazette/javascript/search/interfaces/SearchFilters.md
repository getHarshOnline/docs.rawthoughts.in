---
title: "Interface: SearchFilters"
---

<a id="interface&#45;searchfilters"></a>

Exact native identities; values within one dimension are OR, dimensions are AND\.

## Properties {#properties}

### author? {#author}

> `readonly` `optional` **author?**: readonly `string`\[\]

-----

### classification? {#classification}

> `readonly` `optional` **classification?**: readonly \{ `readonly` `taxonomy`: `string`; `readonly` `term`: `string`; \}\[\]

-----

### keyword? {#keyword}

> `readonly` `optional` **keyword?**: readonly `string`\[\]

Exact authored phrases, without tokenization, case folding or taxonomy inference\.

-----

### kind? {#kind}

> `readonly` `optional` **kind?**: readonly `string`\[\]

-----

### project? {#project}

> `readonly` `optional` **project?**: readonly `string`\[\]

-----

### site? {#site}

> `readonly` `optional` **site?**: readonly `string`\[\]
