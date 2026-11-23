---
title: "Interface: AuthoringIngressLimits"
---

<a id="interface&#45;authoringingresslimits"></a>

Exact finite capture limits selected by \[`AuthoringIngressClass`\]\.

## Properties {#properties}

### maxDocumentBytes {#maxdocumentbytes}

```ts
maxDocumentBytes: bigint;
```

Maximum UTF\-8 bytes in one logical document\.

-----

### maxDocuments {#maxdocuments}

```ts
maxDocuments: number;
```

Maximum logical documents in the selected custody class\.

-----

### maxTotalBytes {#maxtotalbytes}

```ts
maxTotalBytes: bigint;
```

Maximum aggregate UTF\-8 bytes in the custody class\.
