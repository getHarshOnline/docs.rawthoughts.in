---
title: "Class: WorkspaceExplanation"
---

<a id="class&#45;workspaceexplanation"></a>

Deterministic causal explanation for one comparison subject\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### canonicalBytes\(\) {#canonicalbytes}

```ts
canonicalBytes(): Uint8Array;
```

Copy the SDK's exact canonical explanation, including its causal witness\.

#### Returns {#returns-1}

`Uint8Array`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-2}

`void`

-----

### frontier\(\) {#frontier}

```ts
frontier(): 
  | WorkspaceExplanationFrontier
  | undefined;
```

Proof DAG frontier, when affected\.

#### Returns {#returns-3}

\| [`WorkspaceExplanationFrontier`](/pale/reference/wasm/enumerations/WorkspaceExplanationFrontier)
\| `undefined`

-----

### root\(\) {#root}

```ts
root(): WorkspaceChangeRoot | undefined;
```

Deterministically selected root, when affected\.

#### Returns {#returns-4}

[`WorkspaceChangeRoot`](/pale/reference/wasm/classes/WorkspaceChangeRoot) \| `undefined`

-----

### state\(\) {#state}

```ts
state(): WorkspaceExplanationState;
```

Exact query outcome\.

#### Returns {#returns-5}

[`WorkspaceExplanationState`](/pale/reference/wasm/enumerations/WorkspaceExplanationState)

-----

### steps\(\) {#steps}

```ts
steps(): WorkspaceCausalStep[];
```

Complete shortest typed proof sequence\.

#### Returns {#returns-6}

[`WorkspaceCausalStep`](/pale/reference/wasm/classes/WorkspaceCausalStep)\[\]

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Clone the typed query subject\.

#### Returns {#returns-7}

[`WorkspaceSubject`](/pale/reference/wasm/classes/WorkspaceSubject)
