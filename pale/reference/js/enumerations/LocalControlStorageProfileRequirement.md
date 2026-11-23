---
title: "Enumeration: LocalControlStorageProfileRequirement"
---

<a id="enumeration&#45;localcontrolstorageprofilerequirement"></a>

Source\-owned unresolved admission coordinate, returned in canonical order\.

## Enumeration Members {#enumeration-members}

### AuthorityCheckpointCadence {#authoritycheckpointcadence}

```ts
AuthorityCheckpointCadence: 14;
```

Recovery\-checkpoint cadence\.

-----

### AuthorityCompactionPolicy {#authoritycompactionpolicy}

```ts
AuthorityCompactionPolicy: 16;
```

Prefix\-compaction policy\.

-----

### AuthorityCorruptionChecksum {#authoritycorruptionchecksum}

```ts
AuthorityCorruptionChecksum: 8;
```

Corruption\-checksum algorithm\.

-----

### AuthorityCorruptionChecksumBytes {#authoritycorruptionchecksumbytes}

```ts
AuthorityCorruptionChecksumBytes: 9;
```

Corruption\-checksum width\.

-----

### AuthorityFrameEncoding {#authorityframeencoding}

```ts
AuthorityFrameEncoding: 7;
```

Authority\-frame encoding\.

-----

### AuthorityMaximumCheckpointBytes {#authoritymaximumcheckpointbytes}

```ts
AuthorityMaximumCheckpointBytes: 11;
```

Recovery\-checkpoint byte ceiling\.

-----

### AuthorityMaximumCheckpointCandidates {#authoritymaximumcheckpointcandidates}

```ts
AuthorityMaximumCheckpointCandidates: 12;
```

Recovery checkpoint candidate bound\.

-----

### AuthorityMaximumEntryBytes {#authoritymaximumentrybytes}

```ts
AuthorityMaximumEntryBytes: 10;
```

Journal\-entry byte ceiling\.

-----

### AuthorityMaximumTailEntries {#authoritymaximumtailentries}

```ts
AuthorityMaximumTailEntries: 13;
```

Contiguous recovery\-tail entry bound\.

-----

### AuthorityRetentionPolicy {#authorityretentionpolicy}

```ts
AuthorityRetentionPolicy: 15;
```

Journal and checkpoint retention policy\.

-----

### BackupRestorePolicy {#backuprestorepolicy}

```ts
BackupRestorePolicy: 17;
```

Verified backup and inactive\-restore policy\.

-----

### SqliteCheckpointFullFsync {#sqlitecheckpointfullfsync}

```ts
SqliteCheckpointFullFsync: 3;
```

Checkpoint full\-filesystem synchronization policy\.

-----

### SqliteCheckpointMode {#sqlitecheckpointmode}

```ts
SqliteCheckpointMode: 4;
```

Measured WAL checkpoint mode\.

-----

### SqliteCompileOptions {#sqlitecompileoptions}

```ts
SqliteCompileOptions: 0;
```

Exact `SQLite` compile\-option fingerprint\.

-----

### SqliteDurabilityGrouping {#sqlitedurabilitygrouping}

```ts
SqliteDurabilityGrouping: 6;
```

Durability grouping and release delay\.

-----

### SqliteFullFsync {#sqlitefullfsync}

```ts
SqliteFullFsync: 2;
```

Full\-filesystem synchronization policy\.

-----

### SqliteSynchronous {#sqlitesynchronous}

```ts
SqliteSynchronous: 1;
```

Transaction synchronization and barrier policy\.

-----

### SqliteWalAutocheckpointFrames {#sqlitewalautocheckpointframes}

```ts
SqliteWalAutocheckpointFrames: 5;
```

Automatic WAL checkpoint threshold\.
