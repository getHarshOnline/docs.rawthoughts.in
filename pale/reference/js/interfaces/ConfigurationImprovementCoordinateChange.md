---
title: "Interface: ConfigurationImprovementCoordinateChange"
---

<a id="interface&#45;configurationimprovementcoordinatechange"></a>

Lossless digest transition; unselected variant fields are absent\.

## Properties {#properties}

### candidateDigest? {#candidatedigest}

```ts
candidateDigest?: string;
```

Candidate digest, present only for changed\.

-----

### digest? {#digest}

```ts
digest?: string;
```

Shared digest, present only for unchanged\.

-----

### kind {#kind}

```ts
kind: ConfigurationImprovementCoordinateChangeKind;
```

Exact API\-owned variant\.

-----

### priorDigest? {#priordigest}

```ts
priorDigest?: string;
```

Prior digest, present only for changed\.
