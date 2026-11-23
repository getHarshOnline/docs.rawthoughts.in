---
title: "Enumeration: LocalControlStorageStateKind"
---

<a id="enumeration&#45;localcontrolstoragestatekind"></a>

Mutually exclusive physical inspection states\.

## Enumeration Members {#enumeration-members}

### Empty {#empty}

```ts
Empty: 1;
```

The canonical database is a private, zero\-length regular file\.

-----

### Missing {#missing}

```ts
Missing: 0;
```

Canonical descendants or the database leaf are absent\.

-----

### ProfileUnselected {#profileunselected}

```ts
ProfileUnselected: 2;
```

Structural bytes match but admission requirements remain unresolved\.

-----

### Ready {#ready}

```ts
Ready: 3;
```

Physical source and profile checks match; no runtime authority follows\.

-----

### Rejected {#rejected}

```ts
Rejected: 4;
```

Persistent bytes or entry shape contradict the expected identity\.
