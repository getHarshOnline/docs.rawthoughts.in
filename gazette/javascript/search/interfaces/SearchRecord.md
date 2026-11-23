---
title: "Interface: SearchRecord"
---

<a id="interface&#45;searchrecord"></a>

## Indexable {#indexable}

> `readonly` \[`key`: `string`\]: [`Json`](/gazette/javascript/search/type-aliases/Json) \| `undefined`

## Properties {#properties}

### body {#body}

> `readonly` **body**: `string`

-----

### content {#gazette-anchor-content}

> `readonly` **content**: \{`readonly` \[`key`: `string`\]: [`Json`](/gazette/javascript/search/type-aliases/Json) \| `undefined`; `readonly` `documentation?`: `boolean`; `readonly` `id`: `string`; `readonly` `keywords?`: readonly `string`\[\]; `readonly` `title`: `string`; \}

#### Index Signature {#index-signature}

`readonly` \[`key`: `string`\]: [`Json`](/gazette/javascript/search/type-aliases/Json) \| `undefined`

#### documentation? {#documentation}

> `readonly` `optional` **documentation?**: `boolean`

Resolved documentation category; includes collections, journeys and contained examples\.

#### id {#id}

> `readonly` **id**: `string`

Authored content key or exact canonical provider\-documentation address\.

#### keywords? {#keywords}

> `readonly` `optional` **keywords?**: readonly `string`\[\]

#### title {#title}

> `readonly` **title**: `string`

Display label; provider records retain their optional native title separately\.

-----

### indexed? {#indexed}

> `readonly` `optional` **indexed?**: `Readonly`\<`Partial`\<`Record`\<`"body"` \| `"summary"` \| `"title"` \| `"description"` \| `"route"` \| `"notes"`, `string`\>\> \& `Partial`\<`Record`\<`"keywords"` \| `"projects"`, readonly `string`\[\]\>\>\>

Explicit emitted ranking selection; omitted only for the direct complete\-corpus SDK operation\.

-----

### projects {#projects}

> `readonly` **projects**: readonly \{`readonly` \[`key`: `string`\]: [`Json`](/gazette/javascript/search/type-aliases/Json) \| `undefined`; `readonly` `project`: \{`readonly` \[`key`: `string`\]: [`Json`](/gazette/javascript/search/type-aliases/Json) \| `undefined`; `readonly` `id`: `string`; `readonly` `name?`: `string`; \}; \}\[\]

-----

### route {#route}

> `readonly` **route**: \{`readonly` \[`key`: `string`\]: [`Json`](/gazette/javascript/search/type-aliases/Json); `readonly` `canonical_url`: `string`; `readonly` `url`: `string`; \}

#### Index Signature {#index-signature-1}

`readonly` \[`key`: `string`\]: [`Json`](/gazette/javascript/search/type-aliases/Json)

#### canonical\_url {#canonical-url}

> `readonly` **canonical\_url**: `string`

Canonical original, which may belong to another publication site\.

#### url {#url}

> `readonly` **url**: `string`

Serving destination and search identity; never inferred from canonical metadata\.

-----

### summary? {#summary}

> `readonly` `optional` **summary?**: `string`
