---
title: "Interface: EffectiveAuthoringInspection"
---

<a id="interface&#45;effectiveauthoringinspection"></a>

Bounded join from one authoring identity to retained profile rows\.

## Properties {#properties}

### coordinates {#coordinates}

```ts
coordinates: EffectiveProfileCoordinates;
```

Exact admitted profile coordinate owning every associated row\.

-----

### entries {#entries}

```ts
entries: EffectiveProfileEntry[];
```

Complete copied rows in the SDK's deterministic association order\.

-----

### truncated {#truncated}

```ts
truncated: boolean;
```

Whether the fixed association ceiling omitted later rows\.
