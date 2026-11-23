---
title: "Interface: LocalConfigurationImprovementRequest"
---

<a id="interface&#45;localconfigurationimprovementrequest"></a>

Two absolute manifest locators and one common context for a fresh local review\.

Candidate Package files are not read\. Locators do not identify open editor
buffers, and capture does not promise an atomic snapshot across both roots\.

## Properties {#properties}

### baselineWorkspaceManifest {#baselineworkspacemanifest}

```ts
baselineWorkspaceManifest: string;
```

Baseline manifest; its Package source supplies the review\.

-----

### candidateWorkspaceManifest {#candidateworkspacemanifest}

```ts
candidateWorkspaceManifest: string;
```

Candidate manifest; only workspace and private inputs are captured\.

-----

### executionWorkspaceId {#executionworkspaceid}

```ts
executionWorkspaceId: string;
```

Common logical execution\-workspace selector\.

-----

### machineId {#machineid}

```ts
machineId: string;
```

Common private machine selector, not machine readiness\.

-----

### projectId {#projectid}

```ts
projectId: string;
```

Common logical project selector\.
