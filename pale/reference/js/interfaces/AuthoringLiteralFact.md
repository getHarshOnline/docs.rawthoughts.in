---
title: "Interface: AuthoringLiteralFact"
---

<a id="interface&#45;authoringliteralfact"></a>

One allowed literal and its producer documentation\.

## Properties {#properties}

### booleanValue? {#booleanvalue}

```ts
booleanValue?: boolean;
```

Value for the `Boolean` member of \[`AuthoringLiteralKind`\]\.

-----

### description? {#description}

```ts
description?: string;
```

Variant\-specific producer documentation\.

-----

### integerValue? {#integervalue}

```ts
integerValue?: bigint;
```

Exact value for the `Integer` member of \[`AuthoringLiteralKind`\]\.

-----

### kind {#kind}

```ts
kind: AuthoringLiteralKind;
```

Non\-interchangeable literal family\.

-----

### stringValue? {#stringvalue}

```ts
stringValue?: string;
```

Value for the `String` member of \[`AuthoringLiteralKind`\]\.
