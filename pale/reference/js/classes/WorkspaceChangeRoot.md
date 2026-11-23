---
title: "Class: WorkspaceChangeRoot"
---

<a id="class&#45;workspacechangeroot"></a>

One exact source\-change root\.

## Accessors {#accessors}

### kind {#kind}

#### Get Signature {#get-signature}

```ts
get kind(): WorkspaceChangeKind;
```

Closed transition name\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceChangeKind`](/pale/reference/js/enumerations/WorkspaceChangeKind)

-----

### rootDigest {#rootdigest}

#### Get Signature {#get-signature-1}

```ts
get rootDigest(): string;
```

Exact root content address\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### currentFact\(\) {#currentfact}

```ts
currentFact(): WorkspaceFact | null;
```

Exact current fact, absent only for a removed root\.

#### Returns {#returns-2}

[`WorkspaceFact`](/pale/reference/js/interfaces/WorkspaceFact) \| `null`

-----

### priorFact\(\) {#priorfact}

```ts
priorFact(): WorkspaceFact | null;
```

Exact predecessor fact, absent only for an added root\.

#### Returns {#returns-3}

[`WorkspaceFact`](/pale/reference/js/interfaces/WorkspaceFact) \| `null`

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Clone the typed causal subject\.

#### Returns {#returns-4}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
