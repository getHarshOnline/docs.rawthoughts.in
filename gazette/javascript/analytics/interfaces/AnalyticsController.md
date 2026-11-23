---
title: "Interface: AnalyticsController"
---

<a id="interface&#45;analyticscontroller"></a>

## Methods {#methods}

### event\(\) {#event}

> **event**\(`name`: [`AnalyticsEvent`](/gazette/javascript/analytics/type-aliases/AnalyticsEvent), `coordinates`: [`AnalyticsCoordinates`](/gazette/javascript/analytics/interfaces/AnalyticsCoordinates)\): [`AnalyticsSubmission`](/gazette/javascript/analytics/type-aliases/AnalyticsSubmission)

#### Parameters {#parameters}

<Heading level={5} id="name" className="scroll-mt-(--scroll-mt)">name</Heading>

[`AnalyticsEvent`](/gazette/javascript/analytics/type-aliases/AnalyticsEvent)

<Heading level={5} id="coordinates" className="scroll-mt-(--scroll-mt)">coordinates</Heading>

[`AnalyticsCoordinates`](/gazette/javascript/analytics/interfaces/AnalyticsCoordinates)

#### Returns {#returns}

[`AnalyticsSubmission`](/gazette/javascript/analytics/type-aliases/AnalyticsSubmission)

-----

### grant\(\) {#grant}

> **grant**\(\): `Promise`\<[`AnalyticsStatus`](/gazette/javascript/analytics/interfaces/AnalyticsStatus)\>

Explicit invocation by the Theme after consent; no UI/persistence policy inferred\.

#### Returns {#returns-1}

`Promise`\<[`AnalyticsStatus`](/gazette/javascript/analytics/interfaces/AnalyticsStatus)\>

-----

### status\(\) {#status}

> **status**\(\): [`AnalyticsStatus`](/gazette/javascript/analytics/interfaces/AnalyticsStatus)

#### Returns {#returns-2}

[`AnalyticsStatus`](/gazette/javascript/analytics/interfaces/AnalyticsStatus)

-----

### withdraw\(\) {#withdraw}

> **withdraw**\(\): [`AnalyticsStatus`](/gazette/javascript/analytics/interfaces/AnalyticsStatus)

Terminal for this document; a later grant refuses with analytics\_new\_document\_required\.

#### Returns {#returns-3}

[`AnalyticsStatus`](/gazette/javascript/analytics/interfaces/AnalyticsStatus)
