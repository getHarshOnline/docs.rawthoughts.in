---
title: "Interface: EffectiveProfileCompilationRequest"
---

<a id="interface&#45;effectiveprofilecompilationrequest"></a>

Complete captured input required after portable workspace admission\.

## Properties {#properties}

### executionWorkspaceId {#executionworkspaceid}

```ts
executionWorkspaceId: string;
```

Canonical execution\-workspace selector candidate\.

-----

### machineId {#machineid}

```ts
machineId: string;
```

Canonical private machine\-binding selector candidate\.

-----

### packageDocuments {#packagedocuments}

```ts
packageDocuments: CompilationDocument[];
```

Complete immutable Package document batch\.

-----

### privateInputs {#privateinputs}

```ts
privateInputs: OneShotPrivateInputs;
```

Fixed\-role private inputs captured by the caller\.

-----

### projectId {#projectid}

```ts
projectId: string;
```

Canonical project selector candidate\.
