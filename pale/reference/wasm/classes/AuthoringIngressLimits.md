---
title: "Class: AuthoringIngressLimits"
---

<a id="class&#45;authoringingresslimits"></a>

API\-owned finite source limits for one custody class\.

## Properties {#properties}

### maxDocumentBytes {#maxdocumentbytes}

```ts
readonly maxDocumentBytes: bigint;
```

Maximum bytes retained from one logical document\.

-----

### maxDocuments {#maxdocuments}

```ts
readonly maxDocuments: bigint;
```

Maximum logical documents as a non\-lossy JavaScript `bigint`\.

-----

### maxTotalBytes {#maxtotalbytes}

```ts
readonly maxTotalBytes: bigint;
```

Maximum aggregate bytes retained for the custody class\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-1}

`void`
