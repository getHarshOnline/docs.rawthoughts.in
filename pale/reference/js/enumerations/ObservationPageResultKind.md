---
title: "Enumeration: ObservationPageResultKind"
---

<a id="enumeration&#45;observationpageresultkind"></a>

Page query disposition\.

## Enumeration Members {#enumeration-members}

### Cancelled {#cancelled}

```ts
Cancelled: 1;
```

Cancellation was observed before the step began\.

-----

### Ready {#ready}

```ts
Ready: 0;
```

A valid page returned; inspect its completion before assuming exhaustion\.

-----

### Resynchronize {#resynchronize}

```ts
Resynchronize: 2;
```

The supplied cursor cannot continue; obtain a fresh snapshot\.
