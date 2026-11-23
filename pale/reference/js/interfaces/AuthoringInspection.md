---
title: "Interface: AuthoringInspection"
---

<a id="interface&#45;authoringinspection"></a>

Complete API\-owned structural inspection response\.

## Properties {#properties}

### definition? {#definition}

```ts
definition?: string;
```

Selected named definition for a shared\-definition grammar\.

-----

### node? {#node}

```ts
node?: AuthoringNodeFact;
```

Generated structural facts when `state` is `Available`\.

-----

### schemaId? {#schemaid}

```ts
schemaId?: string;
```

Descriptor identity of the selected grammar, when available\.

-----

### state {#state}

```ts
state: AuthoringInspectionState;
```

Availability classification for the exact request\.
