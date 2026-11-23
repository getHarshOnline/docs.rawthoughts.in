---
title: "Interface: HistoryOptions"
---

<a id="interface&#45;historyoptions"></a>

Native history observation only; coordination\-file permission is separately explicit in request\.read\.

## Properties {#properties}

### allowRead {#allowread}

> **allowRead**: `boolean`

-----

### inputBytes? {#inputbytes}

> `optional` **inputBytes?**: `number`

Exact request JSON ceiling; default 16 KiB\.

-----

### resultBytes? {#resultbytes}

> `optional` **resultBytes?**: `number`

Complete report or reserved failure envelope ceiling; default 1 MiB\.
