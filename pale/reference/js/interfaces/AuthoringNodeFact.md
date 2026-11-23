---
title: "Interface: AuthoringNodeFact"
---

<a id="interface&#45;authoringnodefact"></a>

Complete generated structural facts for one inspected path\.

## Properties {#properties}

### allowedValues {#allowedvalues}

```ts
allowedValues: AuthoringLiteralFact[];
```

Closed literal vocabulary admitted at the path\.

-----

### description? {#description}

```ts
description?: string;
```

Producer documentation for the exact structural context\.

-----

### fields {#fields}

```ts
fields: AuthoringFieldFact[];
```

Deterministically ordered child fields\.

-----

### format? {#format}

```ts
format?: string;
```

Optional generated string format\.

-----

### maximum? {#maximum}

```ts
maximum?: bigint;
```

Inclusive integer upper bound\.

-----

### maxItems? {#maxitems}

```ts
maxItems?: bigint;
```

Inclusive collection\-size upper bound\.

-----

### maxLength? {#maxlength}

```ts
maxLength?: bigint;
```

Inclusive string\-length upper bound\.

-----

### minimum? {#minimum}

```ts
minimum?: bigint;
```

Inclusive integer lower bound\.

-----

### minItems? {#minitems}

```ts
minItems?: bigint;
```

Inclusive collection\-size lower bound\.

-----

### minLength? {#minlength}

```ts
minLength?: bigint;
```

Inclusive string\-length lower bound\.

-----

### pattern? {#pattern}

```ts
pattern?: string;
```

Optional generated string pattern\.

-----

### valueKinds {#valuekinds}

```ts
valueKinds: AuthoringValueKind[];
```

Structural categories admitted at the path\.
