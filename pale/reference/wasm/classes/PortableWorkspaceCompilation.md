---
title: "Class: PortableWorkspaceCompilation"
---

<a id="class&#45;portableworkspacecompilation"></a>

Opaque admitted portable workspace; dropping it has no semantic effect\.

## Properties {#properties}

### admissionEvidenceCount {#admissionevidencecount}

```ts
readonly admissionEvidenceCount: number;
```

Number of admission\-evidence records\.

-----

### admissionEvidenceDigest {#admissionevidencedigest}

```ts
readonly admissionEvidenceDigest: string;
```

Exact owner\-proof frontier consumed by admission\.

-----

### adoptedReleaseCount {#adoptedreleasecount}

```ts
readonly adoptedReleaseCount: number;
```

Number of adopted releases\.

-----

### derivationNodeCount {#derivationnodecount}

```ts
readonly derivationNodeCount: number;
```

Number of derivation nodes\.

-----

### derivationSourceCount {#derivationsourcecount}

```ts
readonly derivationSourceCount: number;
```

Number of derivation sources\.

-----

### normativePackReleaseCount {#normativepackreleasecount}

```ts
readonly normativePackReleaseCount: number;
```

Number of normative Pack releases\.

-----

### packageReleaseCount {#packagereleasecount}

```ts
readonly packageReleaseCount: number;
```

Number of Package releases\.

-----

### principalUniverseDigest {#principaluniversedigest}

```ts
readonly principalUniverseDigest: string;
```

Principal\-relative admitted\-universe digest\.

-----

### semanticIrDigest {#semanticirdigest}

```ts
readonly semanticIrDigest: string;
```

Verified semantic\-IR digest\.

-----

### sourceDocumentCount {#sourcedocumentcount}

```ts
readonly sourceDocumentCount: number;
```

Number of admitted source documents\.

-----

### workspaceId {#workspaceid}

```ts
readonly workspaceId: string;
```

Workspace identity declared by the admitted root manifest\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### authoringOccurrences\(\) {#authoringoccurrences}

```ts
authoringOccurrences(
   identity: AuthoringIdentity, 
   maximum_inspected: number, 
   maximum_returned: number, 
   after?: AuthoringOccurrencePageCursor
): AuthoringOccurrencePage;
```

Find occurrences of a compiler\-produced identity without recompiling\.

Limits must be numbers representing integers from 0 through 65535\. The
SDK treats zero as 64 and caps values above 256\. Resume on this exact
compilation with the same identity and raw limits\. Empty pages can continue\.
Omit the continuation for a first page; a supplied null or invalid handle
is an error, not a request to restart\.

After receiver and identity validation, a supplied continuation is consumed
even if limit validation or the SDK query fails\. Obtain another handle
from its page before retrying\.

# Errors {#errors}

Invalid limits or handles produce a host error, without coercion\. An unlike
continuation returns the canonical API diagnostic through the existing
diagnostic projection\.

#### Parameters {#parameters}

<Heading level={5} id="identity" className="scroll-mt-(--scroll-mt)">identity</Heading>

[`AuthoringIdentity`](/pale/reference/wasm/classes/AuthoringIdentity)

<Heading level={5} id="maximum&#45;inspected" className="scroll-mt-(--scroll-mt)">maximum\_inspected</Heading>

`number`

<Heading level={5} id="maximum&#45;returned" className="scroll-mt-(--scroll-mt)">maximum\_returned</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`AuthoringOccurrencePageCursor`](/pale/reference/wasm/classes/AuthoringOccurrencePageCursor)

#### Returns {#returns-1}

[`AuthoringOccurrencePage`](/pale/reference/wasm/classes/AuthoringOccurrencePage)

-----

### countsJson\(\) {#countsjson}

```ts
countsJson(): string;
```

Return all bounded cardinalities in one exact JSON object\.

#### Returns {#returns-2}

`string`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-3}

`void`

-----

### inspectAuthoring\(\) {#inspectauthoring}

```ts
inspectAuthoring(source_label: string, path: AuthoringPathSegment[]): AuthoringInspection;
```

Inspect generated grammar retained by this admitted portable workspace\.
Path elements are consumed in order; failure releases the converted
prefix and leaves later elements untouched\.

# Errors {#errors-1}

Returns a native `Error` carrying the API\-owned canonical diagnostic when
the path exceeds its bound or generated authoring metadata is incoherent\.
An invalid or already consumed element returns a native `Error` without
an API diagnostic\.

#### Parameters {#parameters-1}

<Heading level={5} id="source&#45;label" className="scroll-mt-(--scroll-mt)">source\_label</Heading>

`string`

<Heading level={5} id="path" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringPathSegment`](/pale/reference/wasm/classes/AuthoringPathSegment)\[\]

#### Returns {#returns-4}

[`AuthoringInspection`](/pale/reference/wasm/classes/AuthoringInspection)

-----

### navigateAuthoring\(\) {#navigateauthoring}

```ts
navigateAuthoring(source_label: string, path: AuthoringInstancePathSegment[]): AuthoringNavigation;
```

Resolve one exact occurrence through this workspace's canonical linker\.

Path elements are consumed in order\. On failure, earlier elements remain
consumed and are released; later elements are untouched\.

# Errors {#errors-2}

Returns a native `Error` for an invalid or already consumed path element\.

#### Parameters {#parameters-2}

<Heading level={5} id="source&#45;label&#45;1" className="scroll-mt-(--scroll-mt)">source\_label</Heading>

`string`

<Heading level={5} id="path&#45;1" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringInstancePathSegment`](/pale/reference/wasm/classes/AuthoringInstancePathSegment)\[\]

#### Returns {#returns-5}

[`AuthoringNavigation`](/pale/reference/wasm/classes/AuthoringNavigation)
