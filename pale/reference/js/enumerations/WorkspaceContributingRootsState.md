---
title: "Enumeration: WorkspaceContributingRootsState"
---

<a id="enumeration&#45;workspacecontributingrootsstate"></a>

Current\-partition membership and impact, independently of value equality\.

## Enumeration Members {#enumeration-members}

### Affected {#affected}

```ts
Affected: 2;
```

Current subject has contributing roots; a terminal page can be empty\.

-----

### NotPresent {#notpresent}

```ts
NotPresent: 0;
```

Not present in the current partition, even if present in the prior input\.

-----

### Unaffected {#unaffected}

```ts
Unaffected: 1;
```

Current subject is outside every verified change\-root closure\.
