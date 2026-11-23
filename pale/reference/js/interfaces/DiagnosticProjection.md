---
title: "Interface: DiagnosticProjection"
---

<a id="interface&#45;diagnosticprojection"></a>

Typed unadmitted candidate forwarded to \[`DiagnosticProjection`\]\.

## Properties {#properties}

### causes {#causes}

```ts
causes: string[];
```

Ordered cause messages\.

-----

### code {#code}

```ts
code: string;
```

Stable diagnostic code candidate\.

-----

### disposition {#disposition}

```ts
disposition: DiagnosticDisposition;
```

Recovery\-relevant failure class\.

-----

### effect {#effect}

```ts
effect: DiagnosticEffectCertainty;
```

Relationship to any external effect\.

-----

### help {#help}

```ts
help: string[];
```

Ordered recovery suggestions\.

-----

### omittedCauses {#omittedcauses}

```ts
omittedCauses: number;
```

Causes already omitted by the source\-chain owner\.

-----

### retry {#retry}

```ts
retry: DiagnosticRetry;
```

Retry posture\.

-----

### stage {#stage}

```ts
stage: DiagnosticStage;
```

Processing stage that established the failure\.

-----

### summary {#summary}

```ts
summary: string;
```

Concise diagnostic summary candidate\.
