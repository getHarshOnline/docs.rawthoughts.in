---
title: "Enumeration: ConfigurationImprovementCoordinateChangeKind"
---

<a id="enumeration&#45;configurationimprovementcoordinatechangekind"></a>

Closed digest transition; payload fields follow this discriminant\.

## Enumeration Members {#enumeration-members}

### Changed {#changed}

```ts
Changed: 1;
```

Candidate and baseline have different digests\.

-----

### Unchanged {#unchanged}

```ts
Unchanged: 0;
```

Both compilations share the exact digest\.
