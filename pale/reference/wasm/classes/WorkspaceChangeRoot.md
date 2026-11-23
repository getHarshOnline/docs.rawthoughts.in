---
title: "Class: WorkspaceChangeRoot"
---

<a id="class&#45;workspacechangeroot"></a>

One exact source\-change root from a verified comparison receipt\.

## Properties {#properties}

### rootDigest {#rootdigest}

```ts
readonly rootDigest: string;
```

Content address of the exact root\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### currentFact\(\) {#currentfact}

```ts
currentFact(): WorkspaceFact | undefined;
```

Exact current fact, absent only for a removed root\.

#### Returns {#returns-1}

[`WorkspaceFact`](/pale/reference/wasm/classes/WorkspaceFact) \| `undefined`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-2}

`void`

-----

### kind\(\) {#kind}

```ts
kind(): WorkspaceChangeKind;
```

Closed transition\.

#### Returns {#returns-3}

[`WorkspaceChangeKind`](/pale/reference/wasm/enumerations/WorkspaceChangeKind)

-----

### priorFact\(\) {#priorfact}

```ts
priorFact(): WorkspaceFact | undefined;
```

Exact predecessor fact, absent only for an added root\.

#### Returns {#returns-4}

[`WorkspaceFact`](/pale/reference/wasm/classes/WorkspaceFact) \| `undefined`

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Clone the typed subject for inspection or explanation\.

#### Returns {#returns-5}

[`WorkspaceSubject`](/pale/reference/wasm/classes/WorkspaceSubject)
