---
title: "Class: RecipientQualifiedWorkspaceInspection"
---

<a id="class&#45;recipientqualifiedworkspaceinspection"></a>

Opaque recipient\-qualified access to one retained workspace\.

Only an application or resident route can return this handle\. JavaScript
cannot construct or copy its authority\.

## Methods {#methods}

### associateProfileObservation\(\) {#associateprofileobservation}

```ts
associateProfileObservation(snapshot: ObservationSnapshot, profile: EffectiveProfileCompilation): ObservationProfileAssociationResult;
```

Associate an observation only after recipient authority is current\.

# Errors {#errors}

Returns an authority or aggregate\-budget failure\. Coordinate and source
refusals remain values on the returned association result\.

#### Parameters {#parameters}

<Heading level={5} id="snapshot" className="scroll-mt-(--scroll-mt)">snapshot</Heading>

[`ObservationSnapshot`](/pale/reference/js/classes/ObservationSnapshot)

<Heading level={5} id="profile" className="scroll-mt-(--scroll-mt)">profile</Heading>

[`EffectiveProfileCompilation`](/pale/reference/js/classes/EffectiveProfileCompilation)

#### Returns {#returns}

[`ObservationProfileAssociationResult`](/pale/reference/js/classes/ObservationProfileAssociationResult)

-----

### inspectOrganization\(\) {#inspectorganization}

```ts
inspectOrganization(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: 
  | RecipientQualifiedOrganizationCursor
  | null
): RecipientQualifiedOrganizationPage;
```

Page admitted organization records\. Every continuation is re\-authorized\.

# Errors {#errors-1}

Returns an authority, budget, custody, or SDK projection failure\.

#### Parameters {#parameters-1}

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedOrganizationCursor`](/pale/reference/js/classes/RecipientQualifiedOrganizationCursor)
\| `null`

#### Returns {#returns-1}

[`RecipientQualifiedOrganizationPage`](/pale/reference/js/classes/RecipientQualifiedOrganizationPage)

-----

### inspectOrganizationEndpoint\(\) {#inspectorganizationendpoint}

```ts
inspectOrganizationEndpoint(
   endpoint: OrganizationNode, 
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: 
  | RecipientQualifiedOrganizationCursor
  | null
): RecipientQualifiedOrganizationPage;
```

Find one endpoint after recipient admission\.

# Errors {#errors-2}

Returns an authority, selector, budget, custody, or projection failure\.

#### Parameters {#parameters-2}

<Heading level={5} id="endpoint" className="scroll-mt-(--scroll-mt)">endpoint</Heading>

[`OrganizationNode`](/pale/reference/js/type-aliases/OrganizationNode)

<Heading level={5} id="maximuminspected&#45;1" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;1" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;1" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedOrganizationCursor`](/pale/reference/js/classes/RecipientQualifiedOrganizationCursor)
\| `null`

#### Returns {#returns-2}

[`RecipientQualifiedOrganizationPage`](/pale/reference/js/classes/RecipientQualifiedOrganizationPage)

-----

### inspectOrganizationIncidentRelations\(\) {#inspectorganizationincidentrelations}

```ts
inspectOrganizationIncidentRelations(
   endpoint: OrganizationNode, 
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: 
  | RecipientQualifiedOrganizationCursor
  | null
): RecipientQualifiedOrganizationPage;
```

Page admitted relations incident to one endpoint\.

# Errors {#errors-3}

Returns an authority, selector, budget, custody, or projection failure\.

#### Parameters {#parameters-3}

<Heading level={5} id="endpoint&#45;1" className="scroll-mt-(--scroll-mt)">endpoint</Heading>

[`OrganizationNode`](/pale/reference/js/type-aliases/OrganizationNode)

<Heading level={5} id="maximuminspected&#45;2" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;2" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;2" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;2" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedOrganizationCursor`](/pale/reference/js/classes/RecipientQualifiedOrganizationCursor)
\| `null`

#### Returns {#returns-3}

[`RecipientQualifiedOrganizationPage`](/pale/reference/js/classes/RecipientQualifiedOrganizationPage)

-----

### inspectOrganizationIncidentServices\(\) {#inspectorganizationincidentservices}

```ts
inspectOrganizationIncidentServices(
   scope: OrganizationScopeRef, 
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: 
  | RecipientQualifiedOrganizationCursor
  | null
): RecipientQualifiedOrganizationPage;
```

Page admitted services incident to one scope\.

# Errors {#errors-4}

Returns an authority, selector, budget, custody, or projection failure\.

#### Parameters {#parameters-4}

<Heading level={5} id="scope" className="scroll-mt-(--scroll-mt)">scope</Heading>

[`OrganizationScopeRef`](/pale/reference/js/interfaces/OrganizationScopeRef)

<Heading level={5} id="maximuminspected&#45;3" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;3" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;3" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;3" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedOrganizationCursor`](/pale/reference/js/classes/RecipientQualifiedOrganizationCursor)
\| `null`

#### Returns {#returns-4}

[`RecipientQualifiedOrganizationPage`](/pale/reference/js/classes/RecipientQualifiedOrganizationPage)

-----

### inspectOrganizationSources\(\) {#inspectorganizationsources}

```ts
inspectOrganizationSources(
   record: RecipientQualifiedOrganizationRecordHandle, 
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: 
  | RecipientQualifiedOrganizationSourceCursor
  | null
): RecipientQualifiedOrganizationSourcePage;
```

Read source evidence for an admitted record\. Every continuation is re\-authorized\.

# Errors {#errors-5}

Returns an authority, budget, custody, or projection failure\.

#### Parameters {#parameters-5}

<Heading level={5} id="record" className="scroll-mt-(--scroll-mt)">record</Heading>

[`RecipientQualifiedOrganizationRecordHandle`](/pale/reference/js/classes/RecipientQualifiedOrganizationRecordHandle)

<Heading level={5} id="maximuminspected&#45;4" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;4" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;4" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;4" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`RecipientQualifiedOrganizationSourceCursor`](/pale/reference/js/classes/RecipientQualifiedOrganizationSourceCursor)
\| `null`

#### Returns {#returns-5}

[`RecipientQualifiedOrganizationSourcePage`](/pale/reference/js/classes/RecipientQualifiedOrganizationSourcePage)

-----

### summary\(\) {#summary}

```ts
summary(): RecipientQualifiedWorkspaceSummary;
```

Identity\-and\-count projection of the retained workspace\.

# Errors {#errors-6}

Returns an authority or aggregate\-budget failure before projection\.

#### Returns {#returns-6}

[`RecipientQualifiedWorkspaceSummary`](/pale/reference/js/classes/RecipientQualifiedWorkspaceSummary)
