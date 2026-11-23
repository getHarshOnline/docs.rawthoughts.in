---
title: "Interface: IndexOptions"
---

<a id="interface&#45;indexoptions"></a>

## Extended by {#extended-by}

- [`LoadOptions`](/gazette/javascript/search/interfaces/LoadOptions)

## Properties {#properties}

### maxBytes {#maxbytes}

> `readonly` **maxBytes**: `number`

Complete captured JSON bytes, including result metadata and framing; at most MAX\_SEARCH\_BYTES\.

-----

### maxDocuments {#maxdocuments}

> `readonly` **maxDocuments**: `number`

-----

### maxQueryBytes {#maxquerybytes}

> `readonly` **maxQueryBytes**: `number`

-----

### maxResults {#maxresults}

> `readonly` **maxResults**: `number`

-----

### profile {#profile}

> `readonly` **profile**: `"lexical"` \| `"english"`

Explicit token processing, not an inferred declaration of document language\.
