---
title: "Class: PortableWorkspaceSubjectInspection"
---

<a id="class&#45;portableworkspacesubjectinspection"></a>

Owned fact and source evidence from one retained supplied\-input compilation\.

Terminal and unselected results keep that compilation alive too\. Child getters
copy values; the graph remains shared\. Garbage collection releases this handle's
ownership, without changing semantic state or authorizing source disclosure\.

## Accessors {#accessors}

### admissionEvidenceDigest {#admissionevidencedigest}

#### Get Signature {#get-signature}

```ts
get admissionEvidenceDigest(): string;
```

Owner\-admission evidence identity used by the compilation\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature-1}

```ts
get canonicalBytes(): Buffer;
```

Copy the SDK's already\-computed canonical projection without re\-encoding\.
The bytes do not encode or reconstruct the owner or continuation\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### dependencyCopiedStringBytes {#dependencycopiedstringbytes}

#### Get Signature {#get-signature-2}

```ts
get dependencyCopiedStringBytes(): number;
```

UTF\-8 bytes copied into direct dependency strings on this page\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### inputsComplete {#inputscomplete}

#### Get Signature {#get-signature-3}

```ts
get inputsComplete(): boolean;
```

Whether direct input enumeration is complete independently of source scan\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-4}

```ts
get inspected(): number;
```

Source candidates examined this call, including nonmatches\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-5}

```ts
get isComplete(): boolean;
```

Whether both independently bounded sections are complete\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### principalUniverseDigest {#principaluniversedigest}

#### Get Signature {#get-signature-6}

```ts
get principalUniverseDigest(): string;
```

Principal\-universe identity from the same owner\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### recordAnchor {#recordanchor}

#### Get Signature {#get-signature-7}

```ts
get recordAnchor(): 
  | AuthoringSourceLocation
  | null;
```

Copy an owning import\-path or extension record location, when available\.
Null does not establish subject absence; named references remain separate\.

# Errors {#errors}

Returns a projection error if a source index cannot fit the Node ABI\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`AuthoringSourceLocation`](/pale/reference/js/interfaces/AuthoringSourceLocation)
\| `null`

-----

### semanticIrDigest {#semanticirdigest}

#### Get Signature {#get-signature-8}

```ts
get semanticIrDigest(): string;
```

Semantic\-IR digest, not a substitute for exact compilation custody\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### sourceCopiedStringBytes {#sourcecopiedstringbytes}

#### Get Signature {#get-signature-9}

```ts
get sourceCopiedStringBytes(): number;
```

UTF\-8 bytes copied into occurrence and repeated record\-anchor locations\.

<Heading level={5} id="returns&#45;9" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### sourcesComplete {#sourcescomplete}

#### Get Signature {#get-signature-10}

```ts
get sourcesComplete(): boolean;
```

Whether source scan exhaustion has been proved independently of inputs\.

<Heading level={5} id="returns&#45;10" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-11}

```ts
get workspaceId(): string;
```

Workspace identity from this result's exact owner\.

<Heading level={5} id="returns&#45;11" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### belongsTo\(\) {#belongsto}

```ts
belongsTo(workspace: PortableWorkspaceCompilation): boolean;
```

Check whether this result came from this same compilation, not merely an equal digest\.

#### Parameters {#parameters}

<Heading level={5} id="workspace" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-12}

`boolean`

-----

### continuation\(\) {#continuation}

```ts
continuation(): 
  | PortableWorkspaceSubjectInspectionCursor
  | null;
```

Retain a continuation when either section remains unfinished; otherwise null\.

#### Returns {#returns-13}

\| [`PortableWorkspaceSubjectInspectionCursor`](/pale/reference/js/classes/PortableWorkspaceSubjectInspectionCursor)
\| `null`

-----

### dependencies\(\) {#dependencies}

```ts
dependencies(): WorkspaceCausalStep[];
```

Copy this page's direct inputs in compiler proof\-digest order\.

#### Returns {#returns-14}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep)\[\]

-----

### occurrences\(\) {#occurrences}

```ts
occurrences(): AuthoringOccurrence[];
```

Copy direct named source matches with their compiler\-assigned roles\.

# Errors {#errors-1}

Returns a projection error if a source index cannot fit the Node ABI\.

#### Returns {#returns-15}

[`AuthoringOccurrence`](/pale/reference/js/interfaces/AuthoringOccurrence)\[\]

-----

### root\(\) {#root}

```ts
root(): WorkspaceCausalStep | null;
```

Copy the selected root, or return null for an unselected subject\.

#### Returns {#returns-16}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep) \| `null`

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Copy the full subject originally supplied to this inspection\.

#### Returns {#returns-17}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
