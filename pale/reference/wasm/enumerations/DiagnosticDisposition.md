---
title: "Enumeration: DiagnosticDisposition"
---

<a id="enumeration&#45;diagnosticdisposition"></a>

WebAssembly representation of API\-owned \[`DiagnosticDisposition`\]\.

## Enumeration Members {#enumeration-members}

### Blocked {#blocked}

```ts
Blocked: 2;
```

Current admitted state blocks the request\.

-----

### EffectOutcomeUnknown {#effectoutcomeunknown}

```ts
EffectOutcomeUnknown: 4;
```

An external effect may have occurred and requires reconciliation\.

-----

### InternalFailure {#internalfailure}

```ts
InternalFailure: 3;
```

Pale application invariant failure\.

-----

### InvalidInput {#invalidinput}

```ts
InvalidInput: 1;
```

Input or authored meaning requires correction\.

-----

### OperationalFailure {#operationalfailure}

```ts
OperationalFailure: 0;
```

Runtime prerequisite failure\.
