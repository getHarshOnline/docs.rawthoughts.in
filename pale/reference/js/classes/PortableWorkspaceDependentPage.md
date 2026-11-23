---
title: "Class: PortableWorkspaceDependentPage"
---

<a id="class&#45;portableworkspacedependentpage"></a>

Selected fact and direct consumers found within one candidate scan budget\.

Terminal and unselected results keep their compilation alive too\. Child
getters copy existing values while the graph remains shared\. Garbage
collection releases this handle's ownership without changing semantic state\.

## Accessors {#accessors}

### admissionEvidenceDigest {#admissionevidencedigest}

#### Get Signature {#get-signature}

```ts
get admissionEvidenceDigest(): string;
```

Owner\-admission evidence used by that compilation\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature-1}

```ts
get canonicalBytes(): Buffer;
```

Copy the SDK's already\-computed canonical projection without re\-encoding\.
The bytes do not reconstruct the owner or continuation\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### inputDigestComparisons {#inputdigestcomparisons}

#### Get Signature {#get-signature-2}

```ts
get inputDigestComparisons(): number;
```

Actual candidate input\-search comparisons, excluding root lookup\.
The count can vary with the standard library; it is not semantic identity,
generation membership, a time bound or causal evidence\.

# Errors {#errors}

Returns a projection error if the count cannot fit the Node ABI\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-3}

```ts
get inspected(): number;
```

Candidate nodes examined, including leaves and nonmatches\.

# Errors {#errors-1}

Returns a projection error if the count cannot fit the Node ABI\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-4}

```ts
get isComplete(): boolean;
```

Whether the candidate scan is exhausted or the root is unselected\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### principalUniverseDigest {#principaluniversedigest}

#### Get Signature {#get-signature-5}

```ts
get principalUniverseDigest(): string;
```

Principal\-universe identity from the same owner\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### semanticIrDigest {#semanticirdigest}

#### Get Signature {#get-signature-6}

```ts
get semanticIrDigest(): string;
```

Semantic\-IR digest, not a replacement for compilation custody\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-7}

```ts
get workspaceId(): string;
```

Workspace identity from the exact producing compilation\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### belongsTo\(\) {#belongsto}

```ts
belongsTo(workspace: PortableWorkspaceCompilation): boolean;
```

Check whether this result came from this same compilation, not equal digests\.

#### Parameters {#parameters}

<Heading level={5} id="workspace" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-8}

`boolean`

-----

### continuation\(\) {#continuation}

```ts
continuation(): 
  | PortableWorkspaceDependentCursor
  | null;
```

Retain the next candidate position, or return null after exhaustion\.

#### Returns {#returns-9}

\| [`PortableWorkspaceDependentCursor`](/pale/reference/js/classes/PortableWorkspaceDependentCursor)
\| `null`

-----

### dependents\(\) {#dependents}

```ts
dependents(): WorkspaceCausalStep[];
```

Copy consumers in compiler node\-digest order\.
Each uses the root as a direct input under its own derivation rule;
this does not claim transitive impact or runtime causation\.

#### Returns {#returns-10}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep)\[\]

-----

### root\(\) {#root}

```ts
root(): WorkspaceCausalStep | null;
```

Copy the selected root, or return null for an unselected subject\.

#### Returns {#returns-11}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep) \| `null`

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Copy the full subject whose direct consumers were requested\.

#### Returns {#returns-12}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
