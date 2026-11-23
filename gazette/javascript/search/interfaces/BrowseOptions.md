---
title: "Interface: BrowseOptions"
---

<a id="interface&#45;browseoptions"></a>

## Extends {#extends}

- [`QueryOptions`](/gazette/javascript/search/interfaces/QueryOptions)

## Properties {#properties}

### bool? {#bool}

> `readonly` `optional` **bool?**: `"AND"` \| `"OR"`

AND requires every processed query term across the selected fields\.

#### Inherited from {#inherited-from}

[`QueryOptions`](/gazette/javascript/search/interfaces/QueryOptions)\.[`bool`](/gazette/javascript/search/interfaces/QueryOptions#bool)

-----

### expand? {#expand}

> `readonly` `optional` **expand?**: `boolean`

Prefix matching; English includes literal token prefixes alongside stems\.

#### Inherited from {#inherited-from-1}

[`QueryOptions`](/gazette/javascript/search/interfaces/QueryOptions)\.[`expand`](/gazette/javascript/search/interfaces/QueryOptions#expand)

-----

### fields? {#fields}

> `readonly` `optional` **fields?**: `Readonly`\<`Partial`\<`Record`\<[`SearchField`](/gazette/javascript/search/type-aliases/SearchField), `number`\>\>\>

#### Inherited from {#inherited-from-2}

[`QueryOptions`](/gazette/javascript/search/interfaces/QueryOptions)\.[`fields`](/gazette/javascript/search/interfaces/QueryOptions#fields)

-----

### filters? {#filters}

> `readonly` `optional` **filters?**: [`SearchFilters`](/gazette/javascript/search/interfaces/SearchFilters)

-----

### limit {#limit}

> `readonly` **limit**: `number`

#### Inherited from {#inherited-from-3}

[`QueryOptions`](/gazette/javascript/search/interfaces/QueryOptions)\.[`limit`](/gazette/javascript/search/interfaces/QueryOptions#limit)

-----

### offset? {#offset}

> `readonly` `optional` **offset?**: `number`

-----

### sort? {#sort}

> `readonly` `optional` **sort?**: `"relevance"` \| `"latest"` \| `"oldest"`

Publication\-day order; timestamps use UTC days, unknown times follow known times within a day\.
