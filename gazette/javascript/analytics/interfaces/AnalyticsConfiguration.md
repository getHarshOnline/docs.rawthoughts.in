---
title: "Interface: AnalyticsConfiguration"
---

<a id="interface&#45;analyticsconfiguration"></a>

## Properties {#properties}

### loadTimeoutMs? {#loadtimeoutms}

> `optional` **loadTimeoutMs?**: `number`

Positive tag\-load timeout, at most 30000 milliseconds; default 10000\.

-----

### maxEvents? {#maxevents}

> `optional` **maxEvents?**: `number`

Positive module\-submitted event ceiling, at most 1000; default 1000\.

-----

### measurementId {#measurementid}

> **measurementId**: `string`

Exact explicit GA4 G\- ID, at most 64 ASCII characters; not account/property certification\.

-----

### publicPageUrl {#publicpageurl}

> **publicPageUrl**: `string`

Exact resolved canonical public HTTP\(S\) URL, without credentials/query/fragment\.
