---
title: "Enumeration: ObservationProfileError"
---

<a id="enumeration&#45;observationprofileerror"></a>

Why profile rows could not be read; existing snapshot facts remain usable\.

## Enumeration Members {#enumeration-members}

### ContinuationMismatch {#continuationmismatch}

```ts
ContinuationMismatch: 4;
```

The token belongs to another query or limit pair\.

-----

### CoordinateMismatch {#coordinatemismatch}

```ts
CoordinateMismatch: 3;
```

The profile, private instance or composition changed\.

-----

### ExpiredSource {#expiredsource}

```ts
ExpiredSource: 1;
```

The original admitted source is no longer retained\.

-----

### InvalidLimit {#invalidlimit}

```ts
InvalidLimit: 5;
```

Both row limits must be between 1 and 256\.

-----

### NoProfileSource {#noprofilesource}

```ts
NoProfileSource: 0;
```

This snapshot was not produced from an effective profile\.

-----

### SourceMismatch {#sourcemismatch}

```ts
SourceMismatch: 2;
```

A supplied compilation has another admitted source\.
