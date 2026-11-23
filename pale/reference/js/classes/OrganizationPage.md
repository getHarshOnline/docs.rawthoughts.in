---
title: "Class: OrganizationPage"
---

<a id="class&#45;organizationpage"></a>

Bounded record results with compilation coordinates and an optional continuation\.

## Accessors {#accessors}

### admissionEvidenceDigest {#admissionevidencedigest}

#### Get Signature {#get-signature}

```ts
get admissionEvidenceDigest(): string;
```

Admission\-evidence digest retained by the producing compilation\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature-1}

```ts
get copiedStringBytes(): number;
```

UTF\-8 bytes charged to this SDK query's copied\-string budget\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### endpointLookup {#endpointlookup}

#### Get Signature {#get-signature-2}

```ts
get endpointLookup(): 
  | OrganizationEndpointLookup
  | null;
```

Cumulative endpoint lookup, or null for enumeration and incident queries\.
Input selection and effective state remain separately typed facts\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`OrganizationEndpointLookup`](/pale/reference/js/enumerations/OrganizationEndpointLookup)
\| `null`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-3}

```ts
get inspected(): number;
```

Record cells visited to produce this page\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-4}

```ts
get isComplete(): boolean;
```

Whether organization enumeration is exhausted\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### organizationSelected {#organizationselected}

#### Get Signature {#get-signature-5}

```ts
get organizationSelected(): boolean;
```

Whether the compilation selected an organization document\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### principalUniverseDigest {#principaluniversedigest}

#### Get Signature {#get-signature-6}

```ts
get principalUniverseDigest(): string;
```

Principal\-universe digest of the producing compilation\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### semanticIrDigest {#semanticirdigest}

#### Get Signature {#get-signature-7}

```ts
get semanticIrDigest(): string;
```

Semantic IR digest of the producing compilation\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-8}

```ts
get workspaceId(): string;
```

Workspace that owns the compiled organization\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### belongsTo\(\) {#belongsto}

```ts
belongsTo(owner: PortableWorkspaceCompilation): boolean;
```

Exact producing compilation, never a digest\-only comparison\.

#### Parameters {#parameters}

<Heading level={5} id="owner" className="scroll-mt-(--scroll-mt)">owner</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-9}

`boolean`

-----

### continuation\(\) {#continuation}

```ts
continuation(): OrganizationCursor | null;
```

Null only when the SDK established enumeration exhaustion\.

#### Returns {#returns-10}

[`OrganizationCursor`](/pale/reference/js/classes/OrganizationCursor) \| `null`

-----

### entries\(\) {#entries}

```ts
entries(): OrganizationEntry[];
```

Independent retained entries; no cursor is needed to keep terminal results alive\.

#### Returns {#returns-11}

[`OrganizationEntry`](/pale/reference/js/classes/OrganizationEntry)\[\]
