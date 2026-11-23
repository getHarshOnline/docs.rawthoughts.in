---
title: "Enumeration: LocalControlStorageRejectionKind"
---

<a id="enumeration&#45;localcontrolstoragerejectionkind"></a>

Distinct persistent rejection reasons, projected without reclassification\.

## Enumeration Members {#enumeration-members}

### CorruptOrPartial {#corruptorpartial}

```ts
CorruptOrPartial: 1;
```

Required initial\-v1 structures cannot be decoded\.

-----

### NewerVersion {#newerversion}

```ts
NewerVersion: 8;
```

Persisted schema version is newer than the process understands\.

-----

### SourceIdentityMismatch {#sourceidentitymismatch}

```ts
SourceIdentityMismatch: 7;
```

Source or resultant\-schema identity differs from embedded source\.

-----

### SqliteBuildMismatch {#sqlitebuildmismatch}

```ts
SqliteBuildMismatch: 9;
```

Runtime `SQLite` build differs from the initialization observation\.

-----

### StructuralProfileMismatch {#structuralprofilemismatch}

```ts
StructuralProfileMismatch: 10;
```

A fixed structural connection setting differs from the manifest\.

-----

### UnsafeEntryKind {#unsafeentrykind}

```ts
UnsafeEntryKind: 0;
```

The leaf is not a private, non\-symlink regular file\.

-----

### WrongControlIncarnation {#wrongcontrolincarnation}

```ts
WrongControlIncarnation: 4;
```

Persisted control incarnation does not match\.

-----

### WrongDeploymentScope {#wrongdeploymentscope}

```ts
WrongDeploymentScope: 6;
```

Persisted immutable deployment scope does not match\.

-----

### WrongLogicalStoreId {#wronglogicalstoreid}

```ts
WrongLogicalStoreId: 3;
```

Persisted logical identity does not match\.

-----

### WrongPrincipalScope {#wrongprincipalscope}

```ts
WrongPrincipalScope: 5;
```

Persisted principal scope does not match\.

-----

### WrongStoreKind {#wrongstorekind}

```ts
WrongStoreKind: 2;
```

Persisted store kind names the other physical class\.
