---
title: "Enumeration: PortableWorkspaceSourceState"
---

<a id="enumeration&#45;portableworkspacesourcestate"></a>

Direct named meaning at a source location, separate from proof membership\.

## Enumeration Members {#enumeration-members}

### NoDenotation {#nodenotation}

```ts
NoDenotation: 1;
```

The occurrence has no supported direct proof\-subject mapping\.

-----

### NoOccurrence {#nooccurrence}

```ts
NoOccurrence: 0;
```

No occurrence is indexed; the source or field may still exist\.

-----

### Selected {#selected}

```ts
Selected: 3;
```

The occurrence names a subject included in the selected proof\.

-----

### Unselected {#unselected}

```ts
Unselected: 2;
```

The occurrence names a subject excluded from the selected proof\.
