---
title: "Interface: LocalMaterializationReconciliation"
---

<a id="interface&#45;localmaterializationreconciliation"></a>

Bounded read\-back after settlement reported outcome\-unknown\.

## Properties {#properties}

### ownership {#ownership}

```ts
ownership: LocalMaterializationOwnershipObservation;
```

Current trusted ownership\-record relation\.

-----

### planDigest {#plandigest}

```ts
planDigest: string;
```

Exact admitted plan identity\.

-----

### receipt {#receipt}

```ts
receipt: LocalMaterializationReceiptObservation;
```

Current immutable receipt\-slot observation\.

-----

### repositoryId {#repositoryid}

```ts
repositoryId: string;
```

Repository whose unknown settlement is inspected\.
