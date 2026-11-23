---
title: "Interface: ConfigurationImprovementProposalRequest"
---

<a id="interface&#45;configurationimprovementproposalrequest"></a>

Candidate source for the explicit propose/evaluate route\.

Package source is absent: the API retains the baseline's admitted Package
owner\. This request captures source but does not itself admit the candidate\.

## Properties {#properties}

### executionWorkspaceId {#executionworkspaceid}

```ts
executionWorkspaceId: string;
```

Selected logical execution workspace\.

-----

### machineId {#machineid}

```ts
machineId: string;
```

Selected machine binding, not realization evidence\.

-----

### privateInputs {#privateinputs}

```ts
privateInputs: OneShotPrivateInputs;
```

Captured private profile inputs\.

-----

### projectId {#projectid}

```ts
projectId: string;
```

Selected logical project\.

-----

### workspace {#workspace}

```ts
workspace: PortableWorkspaceRequest;
```

Complete captured portable workspace candidate\.
