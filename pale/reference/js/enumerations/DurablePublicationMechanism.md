---
title: "Enumeration: DurablePublicationMechanism"
---

<a id="enumeration&#45;durablepublicationmechanism"></a>

Durable\-publication implementation compiled for this native target\.

## Enumeration Members {#enumeration-members}

### AppleFullFsync {#applefullfsync}

```ts
AppleFullFsync: 0;
```

Apple `F_FULLFSYNC`, then parent\-directory `fsync`\.

-----

### StandardSyncAll {#standardsyncall}

```ts
StandardSyncAll: 2;
```

Rust `sync_all` for the file and parent directory\.

-----

### UnixFsync {#unixfsync}

```ts
UnixFsync: 1;
```

POSIX file and parent\-directory `fsync`\.
