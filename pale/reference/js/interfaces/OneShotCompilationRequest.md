---
title: "Interface: OneShotCompilationRequest"
---

<a id="interface&#45;oneshotcompilationrequest"></a>

Complete captured source family for one effect\-free one\-shot compilation\.

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

Canonical machine selector candidate\.

-----

### packageDocuments {#packagedocuments}

```ts
packageDocuments: CompilationDocument[];
```

Complete captured Package document batch\.

-----

### privateInputs {#privateinputs}

```ts
privateInputs: OneShotPrivateInputs;
```

Fixed\-role private source batch\.

-----

### projectId {#projectid}

```ts
projectId: string;
```

Canonical project selector candidate\.

-----

### workspace {#workspace}

```ts
workspace: PortableWorkspaceRequest;
```

Complete captured workspace source batch\.
