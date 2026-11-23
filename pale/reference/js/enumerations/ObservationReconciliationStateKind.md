---
title: "Enumeration: ObservationReconciliationStateKind"
---

<a id="enumeration&#45;observationreconciliationstatekind"></a>

Reconciliation\-state kind independent of effect certainty\.

## Enumeration Members {#enumeration-members}

### InProgress {#inprogress}

```ts
InProgress: 2;
```

Case in progress\.

-----

### NotRequired {#notrequired}

```ts
NotRequired: 0;
```

No reconciliation obligation\.

-----

### Required {#required}

```ts
Required: 1;
```

Unresolved case retained\.

-----

### Settled {#settled}

```ts
Settled: 3;
```

Terminal result admitted\.

-----

### Unavailable {#unavailable}

```ts
Unavailable: 5;
```

Carrier absent\.

-----

### Unknown {#unknown}

```ts
Unknown: 4;
```

Frontier unobserved\.
