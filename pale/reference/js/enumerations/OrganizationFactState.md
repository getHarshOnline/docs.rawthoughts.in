---
title: "Enumeration: OrganizationFactState"
---

<a id="enumeration&#45;organizationfactstate"></a>

Typed observation of the owning effective\-state enum, with no state algebra\.

## Enumeration Members {#enumeration-members}

### Absent {#absent}

```ts
Absent: 1;
```

Explicitly absent\.

-----

### Denied {#denied}

```ts
Denied: 2;
```

Explicitly denied\.

-----

### Present {#present}

```ts
Present: 0;
```

Selected and effective\.

-----

### Revoked {#revoked}

```ts
Revoked: 6;
```

Explicitly revoked\.

-----

### Stale {#stale}

```ts
Stale: 4;
```

Outside the owner's freshness boundary\.

-----

### Superseded {#superseded}

```ts
Superseded: 5;
```

Replaced by another owner fact\.

-----

### Unknown {#unknown}

```ts
Unknown: 3;
```

Current fact cannot be established\.
