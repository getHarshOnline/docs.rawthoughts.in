---
title: "Enumeration: DiagnosticRetry"
---

<a id="enumeration&#45;diagnosticretry"></a>

Node representation of API\-owned \[`DiagnosticRetry`\]\.

## Enumeration Members {#enumeration-members}

### AfterCorrection {#aftercorrection}

```ts
AfterCorrection: 1;
```

Retry after correction\.

-----

### AfterStateChange {#afterstatechange}

```ts
AfterStateChange: 2;
```

Retry after state changes\.

-----

### NotIndicated {#notindicated}

```ts
NotIndicated: 0;
```

No retry instruction is established\.

-----

### ReconcileFirst {#reconcilefirst}

```ts
ReconcileFirst: 3;
```

Reconcile before deciding whether to retry\.
