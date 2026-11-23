---
title: "Enumeration: LocalMaterializationRunOutcome"
---

<a id="enumeration&#45;localmaterializationrunoutcome"></a>

Aggregate result of one application\-admitted settlement\.

## Enumeration Members {#enumeration-members}

### FailedNoEffect {#failednoeffect}

```ts
FailedNoEffect: 2;
```

The first repository retained no materialization effect\.

-----

### Partial {#partial}

```ts
Partial: 1;
```

A successful prefix settled before a later no\-effect failure\.

-----

### Succeeded {#succeeded}

```ts
Succeeded: 0;
```

Every selected repository settled with an immutable receipt\.
