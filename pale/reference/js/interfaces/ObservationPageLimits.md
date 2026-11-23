---
title: "Interface: ObservationPageLimits"
---

<a id="interface&#45;observationpagelimits"></a>

Work and output limits for one observation\-page step\.

Zero selects the application's default\. The application caps larger values
at its owned ceilings\.
A returned cursor binds these values to the exact snapshot and filter\.
Reaching a limit does not prove that later facts are absent\.

## Properties {#properties}

### maximumCopiedStringBytes {#maximumcopiedstringbytes}

```ts
maximumCopiedStringBytes: number;
```

Maximum UTF\-8 string bytes this step can copy\.

-----

### maximumInspected {#maximuminspected}

```ts
maximumInspected: number;
```

Maximum retained facts this step can inspect\.

-----

### maximumReturned {#maximumreturned}

```ts
maximumReturned: number;
```

Maximum matching facts this step can copy\.
