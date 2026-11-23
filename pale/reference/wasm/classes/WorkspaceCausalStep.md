---
title: "Class: WorkspaceCausalStep"
---

<a id="class&#45;workspacecausalstep"></a>

One complete typed fact on a shortest causal path\.

## Properties {#properties}

### nodeDigest {#nodedigest}

```ts
readonly nodeDigest: string;
```

Exact proof\-node digest\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### fact\(\) {#fact}

```ts
fact(): WorkspaceFact;
```

Exact produced fact\.

#### Returns {#returns-1}

[`WorkspaceFact`](/pale/reference/wasm/classes/WorkspaceFact)

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-2}

`void`

-----

### provenance\(\) {#provenance}

```ts
provenance(): WorkspaceProvenance;
```

Exact provenance\.

#### Returns {#returns-3}

[`WorkspaceProvenance`](/pale/reference/wasm/classes/WorkspaceProvenance)

-----

### rule\(\) {#rule}

```ts
rule(): WorkspaceDerivationRule;
```

Deterministic rule\.

#### Returns {#returns-4}

[`WorkspaceDerivationRule`](/pale/reference/wasm/enumerations/WorkspaceDerivationRule)

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Semantic subject\.

#### Returns {#returns-5}

[`WorkspaceSubject`](/pale/reference/wasm/classes/WorkspaceSubject)
