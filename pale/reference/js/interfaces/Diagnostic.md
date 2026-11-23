---
title: "Interface: Diagnostic"
---

<a id="interface&#45;diagnostic"></a>

Immutable Node\.js view of one API\-admitted diagnostic\.

The projection copies only presentation\-safe fields from the API\-admitted
diagnostic\. `canonicalBytes` retains the exact admitted record; JavaScript
never parses the error message or recreates diagnostic policy\.

## Properties {#properties}

### canonicalBytes {#canonicalbytes}

```ts
canonicalBytes: Buffer;
```

Exact RFC 8785 `diagnostic.v1` bytes\.

-----

### causes {#causes}

```ts
causes: string[];
```

Ordered source\-chain messages\.

-----

### code {#code}

```ts
code: string;
```

Stable machine\-readable failure code\.

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

Typed external\-effect certainty\.

-----

### facts {#facts}

```ts
facts: DiagnosticFact[];
```

Ordered presentation facts\.

-----

### help {#help}

```ts
help: string[];
```

Ordered recovery suggestions\.

-----

### identity {#identity}

```ts
identity: string;
```

Opaque identity of the exact admitted bytes\.

-----

### notes {#notes}

```ts
notes: string[];
```

Ordered contextual explanations\.

-----

### retry {#retry}

```ts
retry: DiagnosticRetry;
```

Typed retry posture\.

-----

### severity {#severity}

```ts
severity: string;
```

Stable severity string\.

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

Concise redaction\-safe explanation\.
