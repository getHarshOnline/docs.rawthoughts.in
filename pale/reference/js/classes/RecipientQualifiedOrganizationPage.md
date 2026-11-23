---
title: "Class: RecipientQualifiedOrganizationPage"
---

<a id="class&#45;recipientqualifiedorganizationpage"></a>

One admitted organization page with an authority\-bound continuation\.

## Accessors {#accessors}

### admissionEvidenceDigest {#admissionevidencedigest}

#### Get Signature {#get-signature}

```ts
get admissionEvidenceDigest(): string;
```

Admission\-evidence identity of the producing compilation\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature-1}

```ts
get copiedStringBytes(): number;
```

UTF\-8 string bytes copied into this page\.

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

Cumulative endpoint state, or null for enumeration and incident queries\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`OrganizationEndpointLookup`](/pale/reference/js/enumerations/OrganizationEndpointLookup)
\| `null`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-3}

```ts
get inspected(): number;
```

Record cells visited by this query\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-4}

```ts
get isComplete(): boolean;
```

Whether the selected enumeration is complete\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### organizationSelected {#organizationselected}

#### Get Signature {#get-signature-5}

```ts
get organizationSelected(): boolean;
```

Whether organization input was selected\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### principalUniverseDigest {#principaluniversedigest}

#### Get Signature {#get-signature-6}

```ts
get principalUniverseDigest(): string;
```

Principal\-relative universe identity\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### semanticIrDigest {#semanticirdigest}

#### Get Signature {#get-signature-7}

```ts
get semanticIrDigest(): string;
```

Semantic identity of the producing compilation\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-8}

```ts
get workspaceId(): string;
```

Workspace that owns this semantic result\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### continuation\(\) {#continuation}

```ts
continuation(): 
  | RecipientQualifiedOrganizationCursor
  | null;
```

Resume only through the same qualified inspection owner\.

#### Returns {#returns-9}

\| [`RecipientQualifiedOrganizationCursor`](/pale/reference/js/classes/RecipientQualifiedOrganizationCursor)
\| `null`

-----

### entries\(\) {#entries}

```ts
entries(): RecipientQualifiedOrganizationEntry[];
```

Copy the admitted rows and retain their qualified record custody\.

#### Returns {#returns-10}

[`RecipientQualifiedOrganizationEntry`](/pale/reference/js/classes/RecipientQualifiedOrganizationEntry)\[\]
