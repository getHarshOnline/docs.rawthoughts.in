---
title: "Enumeration: ObservationReadinessState"
---

<a id="enumeration&#45;observationreadinessstate"></a>

Readiness state independent of health and native evidence\.

## Enumeration Members {#enumeration-members}

### Blocked {#blocked}

```ts
Blocked: 1;
```

Policy forbids the subject\.

-----

### Narrowed {#narrowed}

```ts
Narrowed: 2;
```

Positive policy omitted the subject\.

-----

### Ready {#ready}

```ts
Ready: 0;
```

Applicable readiness predicate passed\.

-----

### Unavailable {#unavailable}

```ts
Unavailable: 4;
```

Required binding or carrier is absent\.

-----

### Unproven {#unproven}

```ts
Unproven: 3;
```

Native evidence is absent\.
