---
title: "Interface: AuthoringFieldFact"
---

<a id="interface&#45;authoringfieldfact"></a>

One generated child\-field fact\.

## Properties {#properties}

### allowedValues {#allowedvalues}

```ts
allowedValues: AuthoringLiteralFact[];
```

Closed literal vocabulary for the field\.

-----

### description? {#description}

```ts
description?: string;
```

Producer documentation for the field\.

-----

### name {#name}

```ts
name: string;
```

Exact authored key spelling\.

-----

### presence {#presence}

```ts
presence: AuthoringFieldPresence;
```

Requiredness across applicable structural variants\.

-----

### valueKinds {#valuekinds}

```ts
valueKinds: AuthoringValueKind[];
```

Structural value categories admitted for the field\.
