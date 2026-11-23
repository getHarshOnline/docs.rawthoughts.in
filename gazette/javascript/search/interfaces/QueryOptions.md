---
title: "Interface: QueryOptions"
---

<a id="interface&#45;queryoptions"></a>

## Extended by {#extended-by}

- [`BrowseOptions`](/gazette/javascript/search/interfaces/BrowseOptions)

## Properties {#properties}

### bool? {#bool}

> `readonly` `optional` **bool?**: `"AND"` \| `"OR"`

AND requires every processed query term across the selected fields\.

-----

### expand? {#expand}

> `readonly` `optional` **expand?**: `boolean`

Prefix matching; English includes literal token prefixes alongside stems\.

-----

### fields? {#fields}

> `readonly` `optional` **fields?**: `Readonly`\<`Partial`\<`Record`\<[`SearchField`](/gazette/javascript/search/type-aliases/SearchField), `number`\>\>\>

-----

### limit {#limit}

> `readonly` **limit**: `number`
