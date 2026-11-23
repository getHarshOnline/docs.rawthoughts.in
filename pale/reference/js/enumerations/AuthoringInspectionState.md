---
title: "Enumeration: AuthoringInspectionState"
---

<a id="enumeration&#45;authoringinspectionstate"></a>

Availability of generated grammar facts at one admitted source coordinate\.

## Enumeration Members {#enumeration-members}

### Available {#available}

```ts
Available: 0;
```

The selected structural path exists\.

-----

### TextDocument {#textdocument}

```ts
TextDocument: 1;
```

The selected document is substantive text rather than TOML\.

-----

### UnknownDocument {#unknowndocument}

```ts
UnknownDocument: 2;
```

The compilation does not own the logical label\.

-----

### UnknownPath {#unknownpath}

```ts
UnknownPath: 3;
```

The document is known but the structural path is outside its grammar\.
