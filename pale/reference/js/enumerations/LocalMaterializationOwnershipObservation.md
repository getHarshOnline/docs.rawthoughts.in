---
title: "Enumeration: LocalMaterializationOwnershipObservation"
---

<a id="enumeration&#45;localmaterializationownershipobservation"></a>

Trusted ownership\-record relation to an admitted transition\.

## Enumeration Members {#enumeration-members}

### MatchesPost {#matchespost}

```ts
MatchesPost: 2;
```

The trusted record matches the admitted post\-state\.

-----

### MatchesPrior {#matchesprior}

```ts
MatchesPrior: 1;
```

The trusted record matches the admitted pre\-state\.

-----

### Other {#other}

```ts
Other: 3;
```

A trusted record matches neither admitted endpoint\.

-----

### Unowned {#unowned}

```ts
Unowned: 0;
```

No trusted ownership record is present\.
