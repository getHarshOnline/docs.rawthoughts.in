---
title: "Enumeration: DiagnosticRetry"
---

<a id="enumeration&#45;diagnosticretry"></a>

WebAssembly representation of API\-owned \[`DiagnosticRetry`\]\.

## Enumeration Members {#enumeration-members}

### AfterCorrection {#aftercorrection}

```ts
AfterCorrection: 1;
```

Retry after correcting input or authored meaning\.

-----

### AfterStateChange {#afterstatechange}

```ts
AfterStateChange: 2;
```

Retry after admitted state changes\.

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

Reconcile evidence before deciding whether to retry\.
