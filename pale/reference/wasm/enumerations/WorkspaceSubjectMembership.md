---
title: "Enumeration: WorkspaceSubjectMembership"
---

<a id="enumeration&#45;workspacesubjectmembership"></a>

Subject membership in the comparison's predecessor and current compilations\.

## Enumeration Members {#enumeration-members}

### Absent {#absent}

```ts
Absent: 0;
```

Neither compilation contains the subject\.

-----

### CurrentOnly {#currentonly}

```ts
CurrentOnly: 2;
```

Only the current compilation contains the subject\.

-----

### PriorOnly {#prioronly}

```ts
PriorOnly: 1;
```

Only the predecessor contains the subject\.

-----

### Shared {#shared}

```ts
Shared: 3;
```

Both compilations contain the subject\.
