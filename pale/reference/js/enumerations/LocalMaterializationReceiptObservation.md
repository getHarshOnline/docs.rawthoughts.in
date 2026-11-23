---
title: "Enumeration: LocalMaterializationReceiptObservation"
---

<a id="enumeration&#45;localmaterializationreceiptobservation"></a>

Observation of the immutable receipt slot after an unknown outcome\.

## Enumeration Members {#enumeration-members}

### Absent {#absent}

```ts
Absent: 2;
```

No receipt is visible at the admitted identity\.

-----

### Different {#different}

```ts
Different: 3;
```

Different bytes or mode occupy the admitted identity\.

-----

### Exact {#exact}

```ts
Exact: 1;
```

Exact admitted receipt bytes and mode are visible\.

-----

### NotConstructed {#notconstructed}

```ts
NotConstructed: 0;
```

Receipt bytes were not constructed before failure\.
