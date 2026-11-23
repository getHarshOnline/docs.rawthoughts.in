---
title: "Class: RecipientQualifiedWorkspaceComparisonInspection"
---

<a id="class&#45;recipientqualifiedworkspacecomparisoninspection"></a>

Opaque recipient\-qualified access to one exact workspace comparison\.

Only an application or resident route can return this handle\. JavaScript
cannot construct or copy its authority\.

## Methods {#methods}

### changeRoots\(\) {#changeroots}

```ts
changeRoots(offset: number, limit: number): WorkspaceChangeRootPage;
```

Project one admitted change\-root page\.

# Errors {#errors}

Returns an authority or aggregate\-budget failure\.

#### Parameters {#parameters}

<Heading level={5} id="offset" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns}

[`WorkspaceChangeRootPage`](/pale/reference/js/classes/WorkspaceChangeRootPage)

-----

### comparesExactInspections\(\) {#comparesexactinspections}

```ts
comparesExactInspections(prior: RecipientQualifiedWorkspaceInspection, current: RecipientQualifiedWorkspaceInspection): boolean;
```

Test whether this comparison retains these exact qualified inspections\.

This proves SDK custody only\. It does not recheck recipient authority,
disclosure, freshness, or the shared inspection budget\.

#### Parameters {#parameters-1}

<Heading level={5} id="prior" className="scroll-mt-(--scroll-mt)">prior</Heading>

[`RecipientQualifiedWorkspaceInspection`](/pale/reference/js/classes/RecipientQualifiedWorkspaceInspection)

<Heading level={5} id="current" className="scroll-mt-(--scroll-mt)">current</Heading>

[`RecipientQualifiedWorkspaceInspection`](/pale/reference/js/classes/RecipientQualifiedWorkspaceInspection)

#### Returns {#returns-1}

`boolean`

-----

### compareSubject\(\) {#comparesubject}

```ts
compareSubject(subject: WorkspaceSubject): WorkspaceSubjectComparison;
```

Compare one exact subject after fresh admission\.

# Errors {#errors-1}

Returns an authority or aggregate\-budget failure\.

#### Parameters {#parameters-2}

<Heading level={5} id="subject" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

#### Returns {#returns-2}

[`WorkspaceSubjectComparison`](/pale/reference/js/classes/WorkspaceSubjectComparison)

-----

### contributingRoots\(\) {#contributingroots}

```ts
contributingRoots(
   subject: WorkspaceSubject, 
   limit: number, 
   after?: 
  | RecipientQualifiedContributingRootsCursor
  | null
): RecipientQualifiedContributingRootsPage;
```

Page admitted roots that contribute to one subject\.

# Errors {#errors-2}

Returns an authority, budget, custody, or projection failure\.

#### Parameters {#parameters-3}

<Heading level={5} id="subject&#45;1" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="limit&#45;1" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedContributingRootsCursor`](/pale/reference/js/classes/RecipientQualifiedContributingRootsCursor)
\| `null`

#### Returns {#returns-3}

[`RecipientQualifiedContributingRootsPage`](/pale/reference/js/classes/RecipientQualifiedContributingRootsPage)

-----

### correspondOrganizationRecord\(\) {#correspondorganizationrecord}

```ts
correspondOrganizationRecord(
   selectedSide: OrganizationComparisonSide, 
   selected: RecipientQualifiedOrganizationRecordHandle, 
   maximumInspected: number, 
   maximumCopiedBytes: number, 
   after?: 
  | RecipientQualifiedOrganizationCorrespondenceCursor
  | null
): RecipientQualifiedOrganizationCorrespondence;
```

Find one admitted organization record on the other comparison side\.

# Errors {#errors-3}

Returns an authority, budget, custody, or projection failure\.

#### Parameters {#parameters-4}

<Heading level={5} id="selectedside" className="scroll-mt-(--scroll-mt)">selectedSide</Heading>

[`OrganizationComparisonSide`](/pale/reference/js/enumerations/OrganizationComparisonSide)

<Heading level={5} id="selected" className="scroll-mt-(--scroll-mt)">selected</Heading>

[`RecipientQualifiedOrganizationRecordHandle`](/pale/reference/js/classes/RecipientQualifiedOrganizationRecordHandle)

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedOrganizationCorrespondenceCursor`](/pale/reference/js/classes/RecipientQualifiedOrganizationCorrespondenceCursor)
\| `null`

#### Returns {#returns-4}

[`RecipientQualifiedOrganizationCorrespondence`](/pale/reference/js/classes/RecipientQualifiedOrganizationCorrespondence)

-----

### directDependencies\(\) {#directdependencies}

```ts
directDependencies(
   side: OrganizationComparisonSide, 
   subject: WorkspaceSubject, 
   limit: number, 
   after?: 
  | RecipientQualifiedDependencyCursor
  | null
): RecipientQualifiedDependencyPage;
```

Read direct proof inputs from one admitted comparison side\.

# Errors {#errors-4}

Returns an authority, budget, custody, or projection failure\.

#### Parameters {#parameters-5}

<Heading level={5} id="side" className="scroll-mt-(--scroll-mt)">side</Heading>

[`OrganizationComparisonSide`](/pale/reference/js/enumerations/OrganizationComparisonSide)

<Heading level={5} id="subject&#45;2" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="limit&#45;2" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

<Heading level={5} id="after&#45;2" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedDependencyCursor`](/pale/reference/js/classes/RecipientQualifiedDependencyCursor)
\| `null`

#### Returns {#returns-5}

[`RecipientQualifiedDependencyPage`](/pale/reference/js/classes/RecipientQualifiedDependencyPage)

-----

### impacts\(\) {#impacts}

```ts
impacts(offset: number, limit: number): WorkspaceImpactPage;
```

Project one admitted impact page\.

# Errors {#errors-5}

Returns an authority or aggregate\-budget failure\.

#### Parameters {#parameters-6}

<Heading level={5} id="offset&#45;1" className="scroll-mt-(--scroll-mt)">offset</Heading>

`number`

<Heading level={5} id="limit&#45;3" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

#### Returns {#returns-6}

[`WorkspaceImpactPage`](/pale/reference/js/classes/WorkspaceImpactPage)

-----

### inspectSubject\(\) {#inspectsubject}

```ts
inspectSubject(
   side: OrganizationComparisonSide, 
   subject: WorkspaceSubject, 
   inputLimit: number, 
   maximumInspected: number, 
   maximumReturned: number, 
   after?: 
  | RecipientQualifiedSubjectInspectionCursor
  | null
): RecipientQualifiedSubjectInspection;
```

Inspect source and proof evidence on one admitted comparison side\.

# Errors {#errors-6}

Returns an authority, budget, custody, or projection failure\.

#### Parameters {#parameters-7}

<Heading level={5} id="side&#45;1" className="scroll-mt-(--scroll-mt)">side</Heading>

[`OrganizationComparisonSide`](/pale/reference/js/enumerations/OrganizationComparisonSide)

<Heading level={5} id="subject&#45;3" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="inputlimit" className="scroll-mt-(--scroll-mt)">inputLimit</Heading>

`number`

<Heading level={5} id="maximuminspected&#45;1" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="after&#45;3" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedSubjectInspectionCursor`](/pale/reference/js/classes/RecipientQualifiedSubjectInspectionCursor)
\| `null`

#### Returns {#returns-7}

[`RecipientQualifiedSubjectInspection`](/pale/reference/js/classes/RecipientQualifiedSubjectInspection)

-----

### subjects\(\) {#subjects}

```ts
subjects(limit: number, after?: 
  | RecipientQualifiedComparisonSubjectCursor
  | null): RecipientQualifiedComparisonSubjectPage;
```

Enumerate admitted subject identities across both sides\.

# Errors {#errors-7}

Returns an authority, budget, custody, or projection failure\.

#### Parameters {#parameters-8}

<Heading level={5} id="limit&#45;4" className="scroll-mt-(--scroll-mt)">limit</Heading>

`number`

<Heading level={5} id="after&#45;4" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedComparisonSubjectCursor`](/pale/reference/js/classes/RecipientQualifiedComparisonSubjectCursor)
\| `null`

#### Returns {#returns-8}

[`RecipientQualifiedComparisonSubjectPage`](/pale/reference/js/classes/RecipientQualifiedComparisonSubjectPage)

-----

### summaries\(\) {#summaries}

```ts
summaries(): RecipientQualifiedWorkspacePairSummary;
```

Identity summaries of this exact admitted pair and comparison\.

# Errors {#errors-8}

Returns an authority or aggregate\-budget failure before projection\.

#### Returns {#returns-9}

[`RecipientQualifiedWorkspacePairSummary`](/pale/reference/js/classes/RecipientQualifiedWorkspacePairSummary)
