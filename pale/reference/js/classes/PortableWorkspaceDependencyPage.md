---
title: "Class: PortableWorkspaceDependencyPage"
---

<a id="class&#45;portableworkspacedependencypage"></a>

Copied selected fact and one page of its direct proof inputs\.

A pending continuation retains the compilation\. Terminal results contain
owned copies without retaining its graph\. Both remain readable independently
of the caller's compilation variable; neither confers authority\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy the SDK's canonical projection without re\-encoding or cursor bytes\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature-1}

```ts
get copiedStringBytes(): number;
```

UTF\-8 bytes copied into the dependency\-step string fields\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-2}

```ts
get isComplete(): boolean;
```

Whether this input list is exhausted or the subject is unselected\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### principalUniverseDigest {#principaluniversedigest}

#### Get Signature {#get-signature-3}

```ts
get principalUniverseDigest(): string;
```

Principal\-universe identity of the queried compilation\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### semanticIrDigest {#semanticirdigest}

#### Get Signature {#get-signature-4}

```ts
get semanticIrDigest(): string;
```

Semantic\-IR identity, not a substitute for continuation custody\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### continuation\(\) {#continuation}

```ts
continuation(): 
  | PortableWorkspaceDependencyCursor
  | null;
```

Retain the next exact input position, or return null after exhaustion\.

#### Returns {#returns-5}

\| [`PortableWorkspaceDependencyCursor`](/pale/reference/js/classes/PortableWorkspaceDependencyCursor)
\| `null`

-----

### dependencies\(\) {#dependencies}

```ts
dependencies(): WorkspaceCausalStep[];
```

Copy direct input facts in compiler proof\-digest order\.
Each input contributes to this root under the root's derivation rule;
this is not a transitive closure or a provider\-readiness decision\.

#### Returns {#returns-6}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep)\[\]

-----

### root\(\) {#root}

```ts
root(): WorkspaceCausalStep | null;
```

Copy the selected fact, or return null if the subject is unselected\.

#### Returns {#returns-7}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep) \| `null`

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Copy the complete selected subject\.

#### Returns {#returns-8}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
