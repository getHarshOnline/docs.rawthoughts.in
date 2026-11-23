---
title: "Class: EffectiveProfileCompilation"
---

<a id="class&#45;effectiveprofilecompilation"></a>

Opaque admitted profile phase; garbage collection has no semantic effect\.

## Accessors {#accessors}

### compositionPlanDigest {#compositionplandigest}

#### Get Signature {#get-signature}

```ts
get compositionPlanDigest(): string;
```

Identity of the neutral composition proof\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### executionWorkspaceId {#executionworkspaceid}

#### Get Signature {#get-signature-1}

```ts
get executionWorkspaceId(): string;
```

Selected logical execution workspace\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### instanceDigest {#instancedigest}

#### Get Signature {#get-signature-2}

```ts
get instanceDigest(): string;
```

Canonical identity of the admitted private machine projection\.

This is a compilation coordinate, not machine\-readiness evidence\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### packageSemanticIrDigest {#packagesemanticirdigest}

#### Get Signature {#get-signature-3}

```ts
get packageSemanticIrDigest(): string;
```

Identity of the admitted Package semantic closure\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### profileDigest {#profiledigest}

#### Get Signature {#get-signature-4}

```ts
get profileDigest(): string;
```

Canonical identity of the complete portable profile\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### projectId {#projectid}

#### Get Signature {#get-signature-5}

```ts
get projectId(): string;
```

Selected logical project\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-6}

```ts
get workspaceId(): string;
```

Principal workspace owning the effective profile\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### authoringOccurrences\(\) {#authoringoccurrences}

```ts
authoringOccurrences(
   identity: AuthoringIdentity, 
   maximumInspected: number, 
   maximumReturned: number, 
   after?: 
  | AuthoringOccurrencePageCursor
  | null
): AuthoringOccurrencePage;
```

Find occurrences in the retained workspace and private profile sources\.

Limits must be integers from 0 through 65535\. Zero selects 64; the SDK
caps each limit at 256\. Resume with the same identity and raw limits on
this exact compilation\. Results grant no additional disclosure authority\.

# Errors {#errors}

Invalid numeric inputs produce `InvalidArg`\. An unlike continuation
produces an error carrying the canonical API diagnostic\.

#### Parameters {#parameters}

<Heading level={5} id="identity" className="scroll-mt-(--scroll-mt)">identity</Heading>

[`AuthoringIdentity`](/pale/reference/js/classes/AuthoringIdentity)

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`AuthoringOccurrencePageCursor`](/pale/reference/js/classes/AuthoringOccurrencePageCursor)
\| `null`

#### Returns {#returns-7}

[`AuthoringOccurrencePage`](/pale/reference/js/classes/AuthoringOccurrencePage)

-----

### coordinates\(\) {#coordinates}

```ts
coordinates(): EffectiveProfileCoordinates;
```

Return the exact semantic coordinate batch shared by every page\.

#### Returns {#returns-8}

[`EffectiveProfileCoordinates`](/pale/reference/js/interfaces/EffectiveProfileCoordinates)

-----

### explain\(\) {#explain}

```ts
explain(handle: string): 
  | EffectiveProfileExplanation
  | null;
```

Explain one exact profile row retained by this compilation\.

`None` means the well\-formed handle belongs to another profile
coordinate; it is not converted into a fabricated current result\.

# Errors {#errors-1}

Returns an invalid\-argument error unless `handle` is one lowercase
hexadecimal SHA\-256 representation\.

#### Parameters {#parameters-1}

<Heading level={5} id="handle" className="scroll-mt-(--scroll-mt)">handle</Heading>

`string`

#### Returns {#returns-9}

\| [`EffectiveProfileExplanation`](/pale/reference/js/interfaces/EffectiveProfileExplanation)
\| `null`

-----

### inspect\(\) {#inspect}

```ts
inspect(
   section: EffectiveProfileSection, 
   offset: number, 
   limit: number
): EffectiveProfilePage;
```

Project one bounded page without reparsing or recompiling\.

#### Parameters {#parameters-2}

<Heading level={5} id="section" className="scroll-mt-(--scroll-mt)">section</Heading>

[`EffectiveProfileSection`](/pale/reference/js/enumerations/EffectiveProfileSection)

<Heading level={5} id="offset" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns-10}

[`EffectiveProfilePage`](/pale/reference/js/interfaces/EffectiveProfilePage)

-----

### inspectAuthoring\(\) {#inspectauthoring}

```ts
inspectAuthoring(sourceLabel: string, path: AuthoringPathSegment[]): AuthoringInspection;
```

Inspect generated grammar facts retained by this effective\-profile phase\.

# Errors {#errors-2}

Returns a native `Error` carrying the API\-owned canonical diagnostic for
an oversized path or incoherent generated authoring metadata\.

#### Parameters {#parameters-3}

<Heading level={5} id="sourcelabel" className="scroll-mt-(--scroll-mt)">sourceLabel</Heading>

`string`

<Heading level={5} id="path" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringPathSegment`](/pale/reference/js/classes/AuthoringPathSegment)\[\]

#### Returns {#returns-11}

[`AuthoringInspection`](/pale/reference/js/interfaces/AuthoringInspection)

-----

### inspectEffectiveAuthoring\(\) {#inspecteffectiveauthoring}

```ts
inspectEffectiveAuthoring(identity: AuthoringIdentity): EffectiveAuthoringInspection;
```

Join one compiler\-resolved identity to already retained profile rows\.

The identity's kind and value select this profile's rows; the result
carries this profile's coordinates, not an editor\-freshness claim\.

#### Parameters {#parameters-4}

<Heading level={5} id="identity&#45;1" className="scroll-mt-(--scroll-mt)">identity</Heading>

[`AuthoringIdentity`](/pale/reference/js/classes/AuthoringIdentity)

#### Returns {#returns-12}

[`EffectiveAuthoringInspection`](/pale/reference/js/interfaces/EffectiveAuthoringInspection)

-----

### inspectEffectiveAuthoringPage\(\) {#inspecteffectiveauthoringpage}

```ts
inspectEffectiveAuthoringPage(
   identity: AuthoringIdentity, 
   limit: number, 
   after?: 
  | EffectiveAuthoringContinuation
  | null
): EffectiveAuthoringPage;
```

Read another page of profile rows associated with an authoring identity\.

The row limit must be an integer from 0 through 65535\. Zero selects 64;
the SDK caps it at 256\. A continuation requires the same raw limit,
identity, and compilation\. This bound does not bound row bytes\.

# Errors {#errors-3}

Invalid numeric inputs produce `InvalidArg`\. An unlike continuation
produces an error carrying the canonical API diagnostic\.

#### Parameters {#parameters-5}

<Heading level={5} id="identity&#45;2" className="scroll-mt-(--scroll-mt)">identity</Heading>

[`AuthoringIdentity`](/pale/reference/js/classes/AuthoringIdentity)

<Heading level={5} id="limit&#45;1" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`EffectiveAuthoringContinuation`](/pale/reference/js/classes/EffectiveAuthoringContinuation)
\| `null`

#### Returns {#returns-13}

[`EffectiveAuthoringPage`](/pale/reference/js/classes/EffectiveAuthoringPage)

-----

### navigateAuthoring\(\) {#navigateauthoring}

```ts
navigateAuthoring(sourceLabel: string, path: AuthoringInstancePathSegment[]): AuthoringNavigation;
```

Resolve one source occurrence retained by this effective\-profile phase\.

#### Parameters {#parameters-6}

<Heading level={5} id="sourcelabel&#45;1" className="scroll-mt-(--scroll-mt)">sourceLabel</Heading>

`string`

<Heading level={5} id="path&#45;1" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringInstancePathSegment`](/pale/reference/js/classes/AuthoringInstancePathSegment)\[\]

#### Returns {#returns-14}

[`AuthoringNavigation`](/pale/reference/js/classes/AuthoringNavigation)
