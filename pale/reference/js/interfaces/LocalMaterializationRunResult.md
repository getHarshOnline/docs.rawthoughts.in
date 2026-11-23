---
title: "Interface: LocalMaterializationRunResult"
---

<a id="interface&#45;localmaterializationrunresult"></a>

Binding\-safe result of one settled repository\-scoped run\.

## Properties {#properties}

### canonicalBytes {#canonicalbytes}

```ts
canonicalBytes: Buffer;
```

Canonical application\-admitted `run-result.v1` bytes\.

-----

### kind {#kind}

```ts
kind: OneShotPlanKind;
```

Requested plan operation\.

-----

### outcome {#outcome}

```ts
outcome: LocalMaterializationRunOutcome;
```

Aggregate repository\-scoped outcome\.

-----

### succeededTargetCount {#succeededtargetcount}

```ts
succeededTargetCount: number;
```

Number of repositories fully settled\.

-----

### targetCount {#targetcount}

```ts
targetCount: number;
```

Number of repository results included\.

-----

### targets {#targets}

```ts
targets: LocalMaterializationTargetResult[];
```

Ordered result rows for attempted repositories\.
