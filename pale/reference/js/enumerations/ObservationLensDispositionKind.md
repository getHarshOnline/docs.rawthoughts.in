---
title: "Enumeration: ObservationLensDispositionKind"
---

<a id="enumeration&#45;observationlensdispositionkind"></a>

Cooperative visual\-lens disposition\.

## Enumeration Members {#enumeration-members}

### Cancelled {#cancelled}

```ts
Cancelled: 2;
```

Cancelled before this step began; the supplied cursor is unchanged\.

-----

### Ready {#ready}

```ts
Ready: 0;
```

A valid lens step returned; inspect its completion before assuming exhaustion\.

-----

### Resynchronize {#resynchronize}

```ts
Resynchronize: 1;
```

The supplied cursor cannot continue; obtain a fresh snapshot\.
