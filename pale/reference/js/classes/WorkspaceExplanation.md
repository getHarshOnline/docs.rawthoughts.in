---
title: "Class: WorkspaceExplanation"
---

<a id="class&#45;workspaceexplanation"></a>

Deterministic causal explanation result\.

## Accessors {#accessors}

### frontier {#frontier}

#### Get Signature {#get-signature}

```ts
get frontier(): 
  | WorkspaceExplanationFrontier
  | null;
```

Proof frontier, when affected\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`WorkspaceExplanationFrontier`](/pale/reference/js/enumerations/WorkspaceExplanationFrontier)
\| `null`

-----

### state {#state}

#### Get Signature {#get-signature-1}

```ts
get state(): WorkspaceExplanationState;
```

Exact query outcome\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceExplanationState`](/pale/reference/js/enumerations/WorkspaceExplanationState)

## Methods {#methods}

### root\(\) {#root}

```ts
root(): WorkspaceChangeRoot | null;
```

Deterministically selected root, when affected\.

#### Returns {#returns-2}

[`WorkspaceChangeRoot`](/pale/reference/js/classes/WorkspaceChangeRoot) \| `null`

-----

### steps\(\) {#steps}

```ts
steps(): WorkspaceCausalStep[];
```

Complete shortest typed proof sequence\.

#### Returns {#returns-3}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep)\[\]

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Exact query subject\.

#### Returns {#returns-4}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
