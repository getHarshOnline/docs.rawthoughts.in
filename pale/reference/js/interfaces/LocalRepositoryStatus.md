---
title: "Interface: LocalRepositoryStatus"
---

<a id="interface&#45;localrepositorystatus"></a>

Complete read\-only comparison for one local repository\.

## Properties {#properties}

### drift {#drift}

```ts
drift: LocalMaterializationDrift[];
```

Deterministically ordered drift partition\.

-----

### isClean {#isclean}

```ts
isClean: boolean;
```

Whether every observed surface and ownership fact matches\.

-----

### repositoryId {#repositoryid}

```ts
repositoryId: string;
```

Logical repository selected from the admitted compilation\.
