---
title: "Enumeration: AuthoringInspectionState"
---

<a id="enumeration&#45;authoringinspectionstate"></a>

Availability of structural authoring help at one coordinate\.

## Enumeration Members {#enumeration-members}

### Available {#available}

```ts
Available: 0;
```

The generated grammar contains the selected path\.

-----

### TextDocument {#textdocument}

```ts
TextDocument: 1;
```

The source is substantive text rather than TOML grammar\.

-----

### UnknownDocument {#unknowndocument}

```ts
UnknownDocument: 2;
```

The compilation does not own the requested label\.

-----

### UnknownPath {#unknownpath}

```ts
UnknownPath: 3;
```

The structural path is outside the selected grammar\.
