---
title: "Interface: AnalyticsStatus"
---

<a id="interface&#45;analyticsstatus"></a>

## Properties {#properties}

### consent {#consent}

> `readonly` **consent**: `"granted"` \| `"withheld"` \| `"withdrawn"`

-----

### eventsSubmitted {#eventssubmitted}

> `readonly` **eventsSubmitted**: `number`

-----

### mayHaveEffects {#mayhaveeffects}

> `readonly` **mayHaveEffects**: `boolean`

A tag was requested; no recall or remote\-delivery claim\.

-----

### tag {#tag}

> `readonly` **tag**: `"loaded"` \| `"failed"` \| `"loading"` \| `"not-requested"`
