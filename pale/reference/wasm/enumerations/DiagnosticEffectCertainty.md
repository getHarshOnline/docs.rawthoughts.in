---
title: "Enumeration: DiagnosticEffectCertainty"
---

<a id="enumeration&#45;diagnosticeffectcertainty"></a>

WebAssembly representation of API\-owned \[`DiagnosticEffectCertainty`\]\.

## Enumeration Members {#enumeration-members}

### Confirmed {#confirmed}

```ts
Confirmed: 2;
```

Owner evidence confirms the effect and result\.

-----

### NotApplicable {#notapplicable}

```ts
NotApplicable: 0;
```

No external\-effect boundary exists\.

-----

### NotStarted {#notstarted}

```ts
NotStarted: 1;
```

The effect boundary is proven not to have started\.

-----

### OutcomeUnknown {#outcomeunknown}

```ts
OutcomeUnknown: 3;
```

Available evidence cannot establish whether the external effect occurred\.
