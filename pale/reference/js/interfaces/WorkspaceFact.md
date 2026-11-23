---
title: "Interface: WorkspaceFact"
---

<a id="interface&#45;workspacefact"></a>

Lossless fact snapshot; fields not belonging to the selected closed kind are absent\.

## Properties {#properties}

### byteLen? {#bytelen}

```ts
byteLen?: number;
```

Exact source byte length\.

-----

### closureDigest? {#closuredigest}

```ts
closureDigest?: string;
```

Closure digest\.

-----

### componentDigest? {#componentdigest}

```ts
componentDigest?: string;
```

Component digest\.

-----

### kind {#kind}

```ts
kind: WorkspaceFactKind;
```

Closed fact family\.

-----

### moduleDigest? {#moduledigest}

```ts
moduleDigest?: string;
```

Module digest\.

-----

### resolutionDigest? {#resolutiondigest}

```ts
resolutionDigest?: string;
```

Resolution\-lock digest\.

-----

### sourceDigest? {#sourcedigest}

```ts
sourceDigest?: string;
```

Source\-content digest\.

-----

### sourcePath? {#sourcepath}

```ts
sourcePath?: string;
```

Logical source path\.

-----

### surfaceDigest? {#surfacedigest}

```ts
surfaceDigest?: string;
```

Import\-surface digest\.

-----

### universeDigest? {#universedigest}

```ts
universeDigest?: string;
```

Universe\-lock digest\.

-----

### valueDigest? {#valuedigest}

```ts
valueDigest?: string;
```

Domain\-separated value digest\.

-----

### workspaceSemanticIrDigest? {#workspacesemanticirdigest}

```ts
workspaceSemanticIrDigest?: string;
```

Workspace semantic\-IR digest\.
