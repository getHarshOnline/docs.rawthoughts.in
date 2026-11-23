---
title: "Class: WorkspaceImpact"
---

<a id="class&#45;workspaceimpact"></a>

One current subject in the complete reachability partition\.

## Properties {#properties}

### contributingRootCount {#contributingrootcount}

```ts
readonly contributingRootCount: number;
```

Exact count of roots whose closure reaches this subject\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-1}

`void`

-----

### state\(\) {#state}

```ts
state(): WorkspaceImpactState;
```

Root\-backed reachability classification\.

#### Returns {#returns-2}

[`WorkspaceImpactState`](/pale/reference/wasm/enumerations/WorkspaceImpactState)

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Clone the typed subject for inspection or explanation\.

#### Returns {#returns-3}

[`WorkspaceSubject`](/pale/reference/wasm/classes/WorkspaceSubject)
