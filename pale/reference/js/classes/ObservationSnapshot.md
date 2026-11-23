---
title: "Class: ObservationSnapshot"
---

<a id="class&#45;observationsnapshot"></a>

Opaque source\-free observation snapshot\.

## Accessors {#accessors}

### cursor {#cursor}

#### Get Signature {#get-signature}

```ts
get cursor(): ObservationCursor;
```

Return the exact complete\-snapshot cursor\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationCursor`](/pale/reference/js/classes/ObservationCursor)

-----

### factCount {#factcount}

#### Get Signature {#get-signature-1}

```ts
get factCount(): number;
```

Return the retained fact count\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### omittedFactCount {#omittedfactcount}

#### Get Signature {#get-signature-2}

```ts
get omittedFactCount(): number;
```

Return the count omitted by snapshot construction\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

## Methods {#methods}

### associateProfile\(\) {#associateprofile}

```ts
associateProfile(profile: EffectiveProfileCompilation, workspace: PortableWorkspaceCompilation): ObservationProfileAssociationResult;
```

Associate this exact snapshot with an effective profile\.

The returned handle retains identity only\. It copies no profile rows,
observation facts, or causal paths\.

#### Parameters {#parameters}

<Heading level={5} id="profile" className="scroll-mt-(--scroll-mt)">profile</Heading>

[`EffectiveProfileCompilation`](/pale/reference/js/classes/EffectiveProfileCompilation)

<Heading level={5} id="workspace" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-3}

[`ObservationProfileAssociationResult`](/pale/reference/js/classes/ObservationProfileAssociationResult)

-----

### causalPath\(\) {#causalpath}

```ts
causalPath(subject: ObservationSubject): ObservationCausalPathResult;
```

Return one retained exact causal path for an API\-issued subject\.

#### Parameters {#parameters-1}

<Heading level={5} id="subject" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`ObservationSubject`](/pale/reference/js/classes/ObservationSubject)

#### Returns {#returns-4}

[`ObservationCausalPathResult`](/pale/reference/js/classes/ObservationCausalPathResult)

-----

### deltaFrom\(\) {#deltafrom}

```ts
deltaFrom(
   prior: ObservationSnapshot, 
   maximumChanges: number, 
   cancellation: ObservationCancellation
): ObservationDeltaOutcome;
```

Derive one adjacent atomic delta from an earlier API snapshot\.

#### Parameters {#parameters-2}

<Heading level={5} id="prior" className="scroll-mt-(--scroll-mt)">prior</Heading>

`ObservationSnapshot`

<Heading level={5} id="maximumchanges" className="scroll-mt-(--scroll-mt)">maximumChanges</Heading>

`number`

<Heading level={5} id="cancellation" className="scroll-mt-(--scroll-mt)">cancellation</Heading>

[`ObservationCancellation`](/pale/reference/js/enumerations/ObservationCancellation)

#### Returns {#returns-5}

[`ObservationDeltaOutcome`](/pale/reference/js/classes/ObservationDeltaOutcome)

-----

### inspectProfile\(\) {#inspectprofile}

```ts
inspectProfile(
   profile: EffectiveProfileCompilation, 
   workspace: PortableWorkspaceCompilation, 
   subject: ObservationSubject, 
   maximumInspected: number, 
   maximumReturned: number, 
   after?: 
  | ObservationProfileContinuation
  | null
): ObservationProfileResult;
```

Read profile rows for a subject from this snapshot's admitted source\.

Reuse retained profile and workspace handles; do not recompile between
pages\. Both limits are 1 to 256\. They bound examined and returned rows,
not total bytes or caller\-retained memory\. No source is parsed or written\.

#### Parameters {#parameters-3}

<Heading level={5} id="profile&#45;1" className="scroll-mt-(--scroll-mt)">profile</Heading>

[`EffectiveProfileCompilation`](/pale/reference/js/classes/EffectiveProfileCompilation)

<Heading level={5} id="workspace&#45;1" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="subject&#45;1" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`ObservationSubject`](/pale/reference/js/classes/ObservationSubject)

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`ObservationProfileContinuation`](/pale/reference/js/classes/ObservationProfileContinuation)
\| `null`

#### Returns {#returns-6}

[`ObservationProfileResult`](/pale/reference/js/classes/ObservationProfileResult)

-----

### page\(\) {#page}

```ts
page(
   filter: ObservationFilter, 
   limits: ObservationPageLimits, 
   cancellation: ObservationCancellation, 
   after?: ObservationPageCursor | null
): ObservationPageResult;
```

Query one bounded page\. A ready result can still stop before exhaustion\.

#### Parameters {#parameters-4}

<Heading level={5} id="filter" className="scroll-mt-(--scroll-mt)">filter</Heading>

[`ObservationFilter`](/pale/reference/js/classes/ObservationFilter)

<Heading level={5} id="limits" className="scroll-mt-(--scroll-mt)">limits</Heading>

[`ObservationPageLimits`](/pale/reference/js/interfaces/ObservationPageLimits)

<Heading level={5} id="cancellation&#45;1" className="scroll-mt-(--scroll-mt)">cancellation</Heading>

[`ObservationCancellation`](/pale/reference/js/enumerations/ObservationCancellation)

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`ObservationPageCursor`](/pale/reference/js/classes/ObservationPageCursor) \| `null`

#### Returns {#returns-7}

[`ObservationPageResult`](/pale/reference/js/classes/ObservationPageResult)

-----

### visualLens\(\) {#visuallens}

```ts
visualLens(
   filter: ObservationFilter, 
   limits: ObservationLensLimits, 
   includeCausalPaths: boolean, 
   cancellation: ObservationCancellation, 
   after?: ObservationLensCursor | null
): ObservationLensDisposition;
```

Build one bounded non\-authoritative lens step\.

The result carries snapshot\-bound facts and optional retained causal
paths, not layout or proof that omitted subjects are absent\.

#### Parameters {#parameters-5}

<Heading level={5} id="filter&#45;1" className="scroll-mt-(--scroll-mt)">filter</Heading>

[`ObservationFilter`](/pale/reference/js/classes/ObservationFilter)

<Heading level={5} id="limits&#45;1" className="scroll-mt-(--scroll-mt)">limits</Heading>

[`ObservationLensLimits`](/pale/reference/js/interfaces/ObservationLensLimits)

<Heading level={5} id="includecausalpaths" className="scroll-mt-(--scroll-mt)">includeCausalPaths</Heading>

`boolean`

<Heading level={5} id="cancellation&#45;2" className="scroll-mt-(--scroll-mt)">cancellation</Heading>

[`ObservationCancellation`](/pale/reference/js/enumerations/ObservationCancellation)

<Heading level={5} id="after&#45;2" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`ObservationLensCursor`](/pale/reference/js/classes/ObservationLensCursor) \| `null`

#### Returns {#returns-8}

[`ObservationLensDisposition`](/pale/reference/js/classes/ObservationLensDisposition)
