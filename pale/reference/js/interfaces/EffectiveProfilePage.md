---
title: "Interface: EffectiveProfilePage"
---

<a id="interface&#45;effectiveprofilepage"></a>

One exact API\-owned bounded page\.

## Properties {#properties}

### canonicalBytes {#canonicalbytes}

```ts
canonicalBytes: Buffer;
```

Exact RFC 8785 bytes produced once by `pale-sdk`\.

-----

### entries {#entries}

```ts
entries: EffectiveProfileEntry[];
```

Complete copied rows in the exact order of the canonical page\.

-----

### entryCount {#entrycount}

```ts
entryCount: number;
```

Number of complete entries in the page\.

-----

### nextOffset? {#nextoffset}

```ts
nextOffset?: number;
```

Next zero\-based offset, or `None` for the terminal page\.

-----

### offset {#offset}

```ts
offset: number;
```

Exact zero\-based offset represented by the page\.

-----

### section {#section}

```ts
section: EffectiveProfileSection;
```

Section represented by the page\.
