---
title: "Interface: LocalMaterializationTargetResult"
---

<a id="interface&#45;localmaterializationtargetresult"></a>

Presentation\-neutral facts for one attempted repository settlement\.

## Properties {#properties}

### changedSurfaceCount {#changedsurfacecount}

```ts
changedSurfaceCount: number;
```

Number of repository surfaces changed on success\.

-----

### deferredEffectCount {#deferredeffectcount}

```ts
deferredEffectCount: number;
```

Number of effects kept outside the transaction\.

-----

### failureDiagnostic? {#failurediagnostic}

```ts
failureDiagnostic?: Buffer<ArrayBufferLike>;
```

Canonical diagnostic bytes for a no\-effect failure, when present\.

-----

### localGitExcludeChanged {#localgitexcludechanged}

```ts
localGitExcludeChanged: boolean;
```

Whether the managed Git\-exclude block changed\.

-----

### outcome {#outcome}

```ts
outcome: LocalMaterializationTargetOutcome;
```

Proven per\-repository outcome\.

-----

### repositoryId {#repositoryid}

```ts
repositoryId: string;
```

Logical repository attempted by this row\.
