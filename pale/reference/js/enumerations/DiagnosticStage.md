---
title: "Enumeration: DiagnosticStage"
---

<a id="enumeration&#45;diagnosticstage"></a>

Node representation of API\-owned \[`DiagnosticStage`\]\.

## Enumeration Members {#enumeration-members}

### Compilation {#compilation}

```ts
Compilation: 5;
```

Compiler resolution or sealing\.

-----

### ContractValidation {#contractvalidation}

```ts
ContractValidation: 1;
```

Generated contract validation\.

-----

### HostObservation {#hostobservation}

```ts
HostObservation: 13;
```

External prerequisite observation\.

-----

### InputAdmission {#inputadmission}

```ts
InputAdmission: 0;
```

External input admission\.

-----

### Internal {#internal}

```ts
Internal: 14;
```

Other Pale application invariant\.

-----

### Materialization {#materialization}

```ts
Materialization: 11;
```

Materialization or reconciliation\.

-----

### NativeAction {#nativeaction}

```ts
NativeAction: 12;
```

Pure native\-action computation\.

-----

### OperationAdmission {#operationadmission}

```ts
OperationAdmission: 7;
```

Operation admission\.

-----

### PackageLoading {#packageloading}

```ts
PackageLoading: 3;
```

Package source loading\.

-----

### Planning {#planning}

```ts
Planning: 10;
```

Effect\-free planning\.

-----

### Rendering {#rendering}

```ts
Rendering: 6;
```

Generated\-surface rendering\.

-----

### ResidentAdmission {#residentadmission}

```ts
ResidentAdmission: 8;
```

Resident generation or durable transition admission\.

-----

### ResidentRecovery {#residentrecovery}

```ts
ResidentRecovery: 9;
```

Resident recovery and safe\-continuation proof\.

-----

### SemanticAdmission {#semanticadmission}

```ts
SemanticAdmission: 2;
```

Owner\-specific semantic admission\.

-----

### WorkspaceLoading {#workspaceloading}

```ts
WorkspaceLoading: 4;
```

Workspace source loading\.
