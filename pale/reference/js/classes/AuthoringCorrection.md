---
title: "Class: AuthoringCorrection"
---

<a id="class&#45;authoringcorrection"></a>

Copied compiler\-proved edit, not permission to change a source document\.

Callers must match the exact expected source before applying a replacement\.
Caught errors still require ordinary JavaScript narrowing; `instanceof AuthoringCorrection` identifies a native correction member, not write authority\.

## Accessors {#accessors}

### diagnosticIdentity {#diagnosticidentity}

#### Get Signature {#get-signature}

```ts
get diagnosticIdentity(): string;
```

Identity of the exact rejected diagnostic\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### expectedSource {#expectedsource}

#### Get Signature {#get-signature-1}

```ts
get expectedSource(): string;
```

Exact source spelling that must still exist before any edit\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### kind {#kind}

#### Get Signature {#get-signature-2}

```ts
get kind(): NarrowImportVisibility;
```

Compiler\-proved correction class\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`NarrowImportVisibility`](/pale/reference/js/enumerations/AuthoringCorrectionKind#narrowimportvisibility)

-----

### path {#path}

#### Get Signature {#get-signature-3}

```ts
get path(): AuthoringLocationSegment[];
```

Exact decoded\-key and array\-index path\.

# Errors {#errors}

Returns a projection error if an API array index exceeds Node's `uint32` ABI\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`AuthoringLocationSegment`](/pale/reference/js/interfaces/AuthoringLocationSegment)\[\]

-----

### proofSubject {#proofsubject}

#### Get Signature {#get-signature-4}

```ts
get proofSubject(): AuthoringIdentity;
```

Retained semantic subject proving this correction, not an edit capability\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`AuthoringIdentity`](/pale/reference/js/classes/AuthoringIdentity)

-----

### replacementSource {#replacementsource}

#### Get Signature {#get-signature-5}

```ts
get replacementSource(): string;
```

Exact replacement spelling selected by the compiler\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### sourceLabel {#sourcelabel}

#### Get Signature {#get-signature-6}

```ts
get sourceLabel(): string;
```

Logical label of the edited source\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
