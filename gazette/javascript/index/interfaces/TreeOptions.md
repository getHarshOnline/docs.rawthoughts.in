---
title: "Interface: TreeOptions"
---

<a id="interface&#45;treeoptions"></a>

Explicit complete\-tree reads; semantic selection and capture limits use the Rust Tree JSON\.

## Properties {#properties}

### allowRead {#allowread}

> **allowRead**: `boolean`

Explicit permission for complete native capture\. A valid pin does not imply permission\.

-----

### queryBytes? {#querybytes}

> `optional` **queryBytes?**: `number`

Maximum exact native Tree JSON bytes before decoding; default 16 KiB\.
