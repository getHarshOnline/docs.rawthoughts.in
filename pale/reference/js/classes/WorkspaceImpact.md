---
title: "Class: WorkspaceImpact"
---

<a id="class&#45;workspaceimpact"></a>

One current subject in the complete reachability partition\.

## Accessors {#accessors}

### contributingRootCount {#contributingrootcount}

#### Get Signature {#get-signature}

```ts
get contributingRootCount(): number;
```

Exact number of contributing roots\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### state {#state}

#### Get Signature {#get-signature-1}

```ts
get state(): WorkspaceImpactState;
```

Root\-backed reachability classification\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceImpactState`](/pale/reference/js/enumerations/WorkspaceImpactState)

## Methods {#methods}

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Clone the typed causal subject\.

#### Returns {#returns-2}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
