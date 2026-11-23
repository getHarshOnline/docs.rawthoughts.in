---
title: "Interface: ConfigurationImprovementCandidateRequest"
---

<a id="interface&#45;configurationimprovementcandidaterequest"></a>

Fixed private inputs for a candidate that is already portably admitted\.

No workspace documents are accepted here; preparation reuses the supplied
opaque candidate instead of recompiling its source\.

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

Captured private source; no ambient filesystem access\.

-----

### projectId {#projectid}

```ts
projectId: string;
```

Selected logical project\.
