---
title: "Interface: LoadOptions"
---

<a id="interface&#45;loadoptions"></a>

## Extends {#extends}

- [`IndexOptions`](/gazette/javascript/search/interfaces/IndexOptions)

## Properties {#properties}

### allowNetwork {#allownetwork}

> `readonly` **allowNetwork**: `true`

-----

### maxBytes {#maxbytes}

> `readonly` **maxBytes**: `number`

Complete captured JSON bytes, including result metadata and framing; at most MAX\_SEARCH\_BYTES\.

#### Inherited from {#inherited-from}

[`IndexOptions`](/gazette/javascript/search/interfaces/IndexOptions)\.[`maxBytes`](/gazette/javascript/search/interfaces/IndexOptions#maxbytes)

-----

### maxDocuments {#maxdocuments}

> `readonly` **maxDocuments**: `number`

#### Inherited from {#inherited-from-1}

[`IndexOptions`](/gazette/javascript/search/interfaces/IndexOptions)\.[`maxDocuments`](/gazette/javascript/search/interfaces/IndexOptions#maxdocuments)

-----

### maxQueryBytes {#maxquerybytes}

> `readonly` **maxQueryBytes**: `number`

#### Inherited from {#inherited-from-2}

[`IndexOptions`](/gazette/javascript/search/interfaces/IndexOptions)\.[`maxQueryBytes`](/gazette/javascript/search/interfaces/IndexOptions#maxquerybytes)

-----

### maxResponseBytes {#maxresponsebytes}

> `readonly` **maxResponseBytes**: `number`

Complete HTTP response bytes, independently bounded by MAX\_SEARCH\_BYTES\.

-----

### maxResults {#maxresults}

> `readonly` **maxResults**: `number`

#### Inherited from {#inherited-from-3}

[`IndexOptions`](/gazette/javascript/search/interfaces/IndexOptions)\.[`maxResults`](/gazette/javascript/search/interfaces/IndexOptions#maxresults)

-----

### profile {#profile}

> `readonly` **profile**: `"lexical"` \| `"english"`

Explicit token processing, not an inferred declaration of document language\.

#### Inherited from {#inherited-from-4}

[`IndexOptions`](/gazette/javascript/search/interfaces/IndexOptions)\.[`profile`](/gazette/javascript/search/interfaces/IndexOptions#profile)

-----

### timeoutMs {#timeoutms}

> `readonly` **timeoutMs**: `number`
