---
title: "Class: RecipientQualifiedWorkspaceSummary"
---

<a id="class&#45;recipientqualifiedworkspacesummary"></a>

Identity\-and\-count projection of a recipient\-qualified workspace\.

## Accessors {#accessors}

### admissionEvidenceCount {#admissionevidencecount}

#### Get Signature {#get-signature}

```ts
get admissionEvidenceCount(): number;
```

Owner\-proof records consumed at admission\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### admissionEvidenceDigest {#admissionevidencedigest}

#### Get Signature {#get-signature-1}

```ts
get admissionEvidenceDigest(): string;
```

Admission\-evidence identity\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### adoptedReleaseCount {#adoptedreleasecount}

#### Get Signature {#get-signature-2}

```ts
get adoptedReleaseCount(): number;
```

Adopted module releases in the admitted closure\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature-3}

```ts
get canonicalBytes(): Buffer;
```

Complete API\-owned canonical summary bytes\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### derivationNodeCount {#derivationnodecount}

#### Get Signature {#get-signature-4}

```ts
get derivationNodeCount(): number;
```

Retained causal derivation nodes\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### derivationSourceCount {#derivationsourcecount}

#### Get Signature {#get-signature-5}

```ts
get derivationSourceCount(): number;
```

Retained causal source coordinates\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### normativePackReleaseCount {#normativepackreleasecount}

#### Get Signature {#get-signature-6}

```ts
get normativePackReleaseCount(): number;
```

Attestor\-scoped normative\-Pack releases in the admitted closure\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### packageReleaseCount {#packagereleasecount}

#### Get Signature {#get-signature-7}

```ts
get packageReleaseCount(): number;
```

Package releases in the admitted closure\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### principalUniverseDigest {#principaluniversedigest}

#### Get Signature {#get-signature-8}

```ts
get principalUniverseDigest(): string;
```

Principal\-relative universe identity\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### semanticIrDigest {#semanticirdigest}

#### Get Signature {#get-signature-9}

```ts
get semanticIrDigest(): string;
```

Semantic identity\.

<Heading level={5} id="returns&#45;9" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### sourceDocumentCount {#sourcedocumentcount}

#### Get Signature {#get-signature-10}

```ts
get sourceDocumentCount(): number;
```

Source documents consumed at ingress\.

<Heading level={5} id="returns&#45;10" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-11}

```ts
get workspaceId(): string;
```

Workspace identity\.

<Heading level={5} id="returns&#45;11" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
