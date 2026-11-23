---
title: "Interface: LocalMaterializationDrift"
---

<a id="interface&#45;localmaterializationdrift"></a>

One exact API\-derived reason a repository differs from its projection\.

## Properties {#properties}

### action? {#action}

```ts
action?: LocalMaterializationAction;
```

Required file transition for surface or machine\-local drift\.

-----

### kind {#kind}

```ts
kind: LocalMaterializationDriftKind;
```

Closed variant retaining the drift's semantic class\.

-----

### machineEffectKind? {#machineeffectkind}

```ts
machineEffectKind?: GitExcludeProtection;
```

Closed machine\-local effect kind for machine\-local drift\.

-----

### ownershipChange? {#ownershipchange}

```ts
ownershipChange?: LocalMaterializationOwnershipChange;
```

Required ownership transition for ownership drift\.

-----

### relativePath? {#relativepath}

```ts
relativePath?: string;
```

Confined relative path when the variant identifies one file\.

-----

### statusLabel {#statuslabel}

```ts
statusLabel: string;
```

Canonical presentation label owned by the API\.
