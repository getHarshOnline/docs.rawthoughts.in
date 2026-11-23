---
title: "Enumeration: ObservationStepCompletionKind"
---

<a id="enumeration&#45;observationstepcompletionkind"></a>

Completion state of one bounded observation step\.

## Enumeration Members {#enumeration-members}

### Complete {#complete}

```ts
Complete: 0;
```

The selected input for this snapshot and filter was exhausted\.

-----

### Incomplete {#incomplete}

```ts
Incomplete: 2;
```

The next indivisible result cannot fit, so these limits cannot continue\.

-----

### Stopped {#stopped}

```ts
Stopped: 1;
```

More input can remain; continue with the returned cursor\.
