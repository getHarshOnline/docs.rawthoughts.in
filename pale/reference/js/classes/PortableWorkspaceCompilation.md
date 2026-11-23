---
title: "Class: PortableWorkspaceCompilation"
---

<a id="class&#45;portableworkspacecompilation"></a>

Opaque admitted workspace; garbage collection has no semantic effect\.

## Accessors {#accessors}

### admissionEvidenceCount {#admissionevidencecount}

#### Get Signature {#get-signature}

```ts
get admissionEvidenceCount(): number;
```

Number of admission\-evidence records\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### admissionEvidenceDigest {#admissionevidencedigest}

#### Get Signature {#get-signature-1}

```ts
get admissionEvidenceDigest(): string;
```

Exact owner\-proof frontier digest\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### adoptedReleaseCount {#adoptedreleasecount}

#### Get Signature {#get-signature-2}

```ts
get adoptedReleaseCount(): number;
```

Number of selected adopted releases\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### derivationNodeCount {#derivationnodecount}

#### Get Signature {#get-signature-3}

```ts
get derivationNodeCount(): number;
```

Number of nodes in the derivation graph\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### derivationSourceCount {#derivationsourcecount}

#### Get Signature {#get-signature-4}

```ts
get derivationSourceCount(): number;
```

Number of source nodes in the derivation graph\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### normativePackReleaseCount {#normativepackreleasecount}

#### Get Signature {#get-signature-5}

```ts
get normativePackReleaseCount(): number;
```

Number of selected normative Pack releases\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### packageReleaseCount {#packagereleasecount}

#### Get Signature {#get-signature-6}

```ts
get packageReleaseCount(): number;
```

Number of selected Package releases\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### principalUniverseDigest {#principaluniversedigest}

#### Get Signature {#get-signature-7}

```ts
get principalUniverseDigest(): string;
```

Principal\-relative admitted\-universe digest\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### semanticIrDigest {#semanticirdigest}

#### Get Signature {#get-signature-8}

```ts
get semanticIrDigest(): string;
```

Verified semantic\-IR digest\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### sourceDocumentCount {#sourcedocumentcount}

#### Get Signature {#get-signature-9}

```ts
get sourceDocumentCount(): number;
```

Number of admitted logical source documents\.

<Heading level={5} id="returns&#45;9" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-10}

```ts
get workspaceId(): string;
```

Admitted workspace identity\.

<Heading level={5} id="returns&#45;10" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### directDependencies\(\) {#directdependencies}

```ts
directDependencies(
   subject: WorkspaceSubject, 
   limit: number, 
   after?: 
  | PortableWorkspaceDependencyCursor
  | null
): PortableWorkspaceDependencyPage;
```

Page one selected fact's direct inputs without recompilation or a graph walk\.

The limit must be an integer from 0 through 65535\. The SDK owns the
64\-input default and 256\-input cap\. Resume with the same compilation,
full subject and raw limit; equal digests or equal normalized limits
cannot replace that custody\. A missing cursor starts a new query\.
A selected fact with no inputs differs from a missing root\. The row limit
and fixed copied\-string byte ceiling do not bound time or total memory,
or admit a recipient\.

# Errors {#errors}

Invalid numbers produce `InvalidArg`\. Continuation and internal failures
retain the SDK\-owned canonical diagnostic\.

#### Parameters {#parameters}

<Heading level={5} id="subject" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="limit" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`PortableWorkspaceDependencyCursor`](/pale/reference/js/classes/PortableWorkspaceDependencyCursor)
\| `null`

#### Returns {#returns-11}

[`PortableWorkspaceDependencyPage`](/pale/reference/js/classes/PortableWorkspaceDependencyPage)

-----

### directDependents\(\) {#directdependents}

```ts
directDependents(
   subject: WorkspaceSubject, 
   maximumInspected: number, 
   maximumReturned: number, 
   after?: 
  | PortableWorkspaceDependentCursor
  | null
): PortableWorkspaceDependentPage;
```

Find one\-hop direct consumers without recompiling or building a reverse index\.

Each limit must be an integer from 0 through 65535\. The SDK applies
independent 64\-row defaults and 256\-row caps\. Every candidate is charged,
including nonmatches; empty pages can remain incomplete\. Resume with this
exact compilation, full subject and both raw limits\. A missing cursor
starts a new scan, not an implicit continuation of a completed result\.
Candidate and row limits combine with a fixed aggregate input\-comparison
ceiling\. Reaching any ceiling leaves the next candidate in the continuation\.
These bounds do not limit bytes, elapsed time or retained memory\. This
supplied\-input query admits no recipient or native\-effect authority\.

# Errors {#errors-1}

Invalid numbers produce `InvalidArg`\. Continuation and internal failures
retain the SDK\-owned canonical diagnostic\.

#### Parameters {#parameters-1}

<Heading level={5} id="subject&#45;1" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`PortableWorkspaceDependentCursor`](/pale/reference/js/classes/PortableWorkspaceDependentCursor)
\| `null`

#### Returns {#returns-12}

[`PortableWorkspaceDependentPage`](/pale/reference/js/classes/PortableWorkspaceDependentPage)

-----

### inspectOrganization\(\) {#inspectorganization}

```ts
inspectOrganization(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationCursor | null
): OrganizationPage;
```

Inspect bounded shallow organization records without another compilation\.
Raw limits reach the SDK unchanged; 0 and 257 are not silently defaulted\.
Copy budget covers SDK UTF\-8 payload only\. Keep the original cursor on error\.
This inspects caller\-supplied input, not authenticated recipient delivery\.

# Errors {#errors-2}

Nonintegral/out\-of\-representation limits are `InvalidArg`; SDK query, custody,
section and copy failures preserve the canonical diagnostic\.

#### Parameters {#parameters-2}

<Heading level={5} id="maximuminspected&#45;1" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;1" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;2" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationCursor`](/pale/reference/js/classes/OrganizationCursor) \| `null`

#### Returns {#returns-13}

[`OrganizationPage`](/pale/reference/js/classes/OrganizationPage)

-----

### inspectOrganizationEndpoint\(\) {#inspectorganizationendpoint}

```ts
inspectOrganizationEndpoint(
   endpoint: OrganizationNode, 
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationCursor | null
): OrganizationPage;
```

Find an exact endpoint or its binding witnesses in the retained compilation\.
Empty partial pages do not prove absence\. A continuation binds the original
endpoint, owner and limits\. This grants no recipient disclosure permission\.

# Errors {#errors-3}

Malformed transport values reject before the SDK\. Identifier, limit, custody
and copy\-budget failures retain the SDK diagnostic and do not advance a cursor\.

#### Parameters {#parameters-3}

<Heading level={5} id="endpoint" className="scroll-mt-(--scroll-mt)">endpoint</Heading>

[`OrganizationNode`](/pale/reference/js/type-aliases/OrganizationNode)

<Heading level={5} id="maximuminspected&#45;2" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;2" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;1" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;3" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationCursor`](/pale/reference/js/classes/OrganizationCursor) \| `null`

#### Returns {#returns-14}

[`OrganizationPage`](/pale/reference/js/classes/OrganizationPage)

-----

### inspectOrganizationIncidentRelations\(\) {#inspectorganizationincidentrelations}

```ts
inspectOrganizationIncidentRelations(
   endpoint: OrganizationNode, 
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationCursor | null
): OrganizationPage;
```

Read one\-hop explicit and already\-derived relations at either endpoint\.
The application preserves direction, intervals and parallel relations\.
This is not transitive impact, endpoint\-existence proof or native observation\.

# Errors {#errors-4}

Uses the same query limits and failure rules as \[`Self::inspect_organization_endpoint`\]\.

#### Parameters {#parameters-4}

<Heading level={5} id="endpoint&#45;1" className="scroll-mt-(--scroll-mt)">endpoint</Heading>

[`OrganizationNode`](/pale/reference/js/type-aliases/OrganizationNode)

<Heading level={5} id="maximuminspected&#45;3" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;3" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;2" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;4" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationCursor`](/pale/reference/js/classes/OrganizationCursor) \| `null`

#### Returns {#returns-15}

[`OrganizationPage`](/pale/reference/js/classes/OrganizationPage)

-----

### inspectOrganizationIncidentServices\(\) {#inspectorganizationincidentservices}

```ts
inspectOrganizationIncidentServices(
   scope: OrganizationScopeRef, 
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationCursor | null
): OrganizationPage;
```

Page directional services at an exact provider or consumer scope\.
Retains full contract direction, requirements and source/detail handles\.
Empty pages may continue; this does not prove scope existence or native readiness\.

# Errors {#errors-5}

Uses the same limit, cursor and diagnostic rules as \[`Self::inspect_organization_endpoint`\]\.

#### Parameters {#parameters-5}

<Heading level={5} id="scope" className="scroll-mt-(--scroll-mt)">scope</Heading>

[`OrganizationScopeRef`](/pale/reference/js/interfaces/OrganizationScopeRef)

<Heading level={5} id="maximuminspected&#45;4" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;4" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;3" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;5" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationCursor`](/pale/reference/js/classes/OrganizationCursor) \| `null`

#### Returns {#returns-16}

[`OrganizationPage`](/pale/reference/js/classes/OrganizationPage)

-----

### inspectSubject\(\) {#inspectsubject}

```ts
inspectSubject(
   subject: WorkspaceSubject, 
   inputLimit: number, 
   maximumInspected: number, 
   maximumReturned: number, 
   after?: 
  | PortableWorkspaceSubjectInspectionCursor
  | null
): PortableWorkspaceSubjectInspection;
```

Inspect one subject's fact, direct inputs and source evidence without recompiling\.

All limits must be integers from 0 through 65535\. The SDK applies its
64\-row defaults and 256\-row caps once\. Resume with this exact compilation,
full subject and all three raw limits\. Empty pages can remain unfinished;
completed sections do not restart\. Row limits do not bound bytes, time or
aggregate retained memory\. This supplied\-input query grants no recipient
authority and performs no source\-disclosure admission\.

# Errors {#errors-6}

Invalid numbers produce `InvalidArg`\. Continuation mismatches and internal
projection failures retain the SDK\-owned canonical diagnostic\.

#### Parameters {#parameters-6}

<Heading level={5} id="subject&#45;2" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="inputlimit" className="scroll-mt-(--scroll-mt)">inputLimit</Heading>

`number`

<Heading level={5} id="maximuminspected&#45;5" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;5" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="after&#45;6" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`PortableWorkspaceSubjectInspectionCursor`](/pale/reference/js/classes/PortableWorkspaceSubjectInspectionCursor)
\| `null`

#### Returns {#returns-17}

[`PortableWorkspaceSubjectInspection`](/pale/reference/js/classes/PortableWorkspaceSubjectInspection)
