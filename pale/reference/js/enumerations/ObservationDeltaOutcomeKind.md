---
title: "Enumeration: ObservationDeltaOutcomeKind"
---

<a id="enumeration&#45;observationdeltaoutcomekind"></a>

Delta outcome kind\.

## Enumeration Members {#enumeration-members}

### Backpressured {#backpressured}

```ts
Backpressured: 4;
```

Complete delta exceeded the declared bound\.

-----

### Cancelled {#cancelled}

```ts
Cancelled: 3;
```

Cancelled before projection\.

-----

### CaughtUp {#caughtup}

```ts
CaughtUp: 0;
```

Caller is current\.

-----

### Delta {#delta}

```ts
Delta: 1;
```

Complete adjacent delta returned\.

-----

### Resynchronize {#resynchronize}

```ts
Resynchronize: 2;
```

Full snapshot required\.
