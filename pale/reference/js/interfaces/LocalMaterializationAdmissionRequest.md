---
title: "Interface: LocalMaterializationAdmissionRequest"
---

<a id="interface&#45;localmaterializationadmissionrequest"></a>

Local directories and plan class admitted for one materialization run\.

## Properties {#properties}

### evidenceDirectory {#evidencedirectory}

```ts
evidenceDirectory: string;
```

Absolute directory selected for immutable evidence\.

-----

### kind {#kind}

```ts
kind: OneShotPlanKind;
```

Apply, explicit\-adoption, or removal law\.

-----

### savedPlanDirectory {#savedplandirectory}

```ts
savedPlanDirectory: string;
```

Absolute directory containing the exact saved plans\.
