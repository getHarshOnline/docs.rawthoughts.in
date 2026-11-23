---
title: "Class: OrganizationRecordHandle"
---

<a id="class&#45;organizationrecordhandle"></a>

Retain one record for detail and source queries; see \[`OrganizationCursor`\] for custody\.

## Accessors {#accessors}

### workspaceId {#workspaceid}

#### Get Signature {#get-signature}

```ts
get workspaceId(): string;
```

Actual retained workspace coordinate\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### axisResources\(\) {#axisresources}

```ts
axisResources(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned axis resources section of this exact parent\.

# Errors {#errors}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters}

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-1}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### belongsTo\(\) {#belongsto}

```ts
belongsTo(owner: PortableWorkspaceCompilation): boolean;
```

Exact producing compilation, not equal\-value reconstructed source\.

#### Parameters {#parameters-1}

<Heading level={5} id="owner" className="scroll-mt-(--scroll-mt)">owner</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-2}

`boolean`

-----

### communicationResolutions\(\) {#communicationresolutions}

```ts
communicationResolutions(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned communication resolutions section of this exact parent\.

# Errors {#errors-1}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-2}

<Heading level={5} id="maximuminspected&#45;1" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;1" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;1" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-3}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### inspectionCoordinates\(\) {#inspectioncoordinates}

```ts
inspectionCoordinates(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned inspection coordinates section of this exact parent\.

# Errors {#errors-2}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-3}

<Heading level={5} id="maximuminspected&#45;2" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;2" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;2" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;2" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-4}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### inspectionStates\(\) {#inspectionstates}

```ts
inspectionStates(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned inspection states section of this exact parent\.

# Errors {#errors-3}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-4}

<Heading level={5} id="maximuminspected&#45;3" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;3" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;3" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;3" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-5}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### leadershipParticipants\(\) {#leadershipparticipants}

```ts
leadershipParticipants(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned leadership participants section of this exact parent\.

# Errors {#errors-4}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-5}

<Heading level={5} id="maximuminspected&#45;4" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;4" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;4" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;4" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-6}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### leadershipScopes\(\) {#leadershipscopes}

```ts
leadershipScopes(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned leadership scopes section of this exact parent\.

# Errors {#errors-5}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-6}

<Heading level={5} id="maximuminspected&#45;5" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;5" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;5" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;5" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-7}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### lensConditions\(\) {#lensconditions}

```ts
lensConditions(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned lens conditions section of this exact parent\.

# Errors {#errors-6}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-7}

<Heading level={5} id="maximuminspected&#45;6" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;6" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;6" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;6" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-8}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### lensRights\(\) {#lensrights}

```ts
lensRights(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned lens rights section of this exact parent\.

# Errors {#errors-7}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-8}

<Heading level={5} id="maximuminspected&#45;7" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;7" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;7" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;7" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-9}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### lensStandards\(\) {#lensstandards}

```ts
lensStandards(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned lens standards section of this exact parent\.

# Errors {#errors-8}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-9}

<Heading level={5} id="maximuminspected&#45;8" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;8" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;8" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;8" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-10}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### nativeReferences\(\) {#nativereferences}

```ts
nativeReferences(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned native references section of this exact parent\.

# Errors {#errors-9}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-10}

<Heading level={5} id="maximuminspected&#45;9" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;9" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;9" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;9" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-11}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### responsibilityGenealogy\(\) {#responsibilitygenealogy}

```ts
responsibilityGenealogy(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned responsibility genealogy section of this exact parent\.

# Errors {#errors-10}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-11}

<Heading level={5} id="maximuminspected&#45;10" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;10" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;10" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;10" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-12}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### responsibilityProjections\(\) {#responsibilityprojections}

```ts
responsibilityProjections(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned responsibility projections section of this exact parent\.

# Errors {#errors-11}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-12}

<Heading level={5} id="maximuminspected&#45;11" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;11" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;11" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;11" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-13}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### responsibilityResidences\(\) {#responsibilityresidences}

```ts
responsibilityResidences(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned responsibility residences section of this exact parent\.

# Errors {#errors-12}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-13}

<Heading level={5} id="maximuminspected&#45;12" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;12" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;12" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;12" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-14}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### responsibilitySelections\(\) {#responsibilityselections}

```ts
responsibilitySelections(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned responsibility selections section of this exact parent\.

# Errors {#errors-13}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-14}

<Heading level={5} id="maximuminspected&#45;13" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;13" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;13" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;13" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-15}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### sameRecord\(\) {#samerecord}

```ts
sameRecord(other: OrganizationRecordHandle): boolean;
```

Exact retained owner and record, including handles issued by independent pages\.
Equal values in another compilation do not identify the same record handle\.

#### Parameters {#parameters-15}

<Heading level={5} id="other" className="scroll-mt-(--scroll-mt)">other</Heading>

`OrganizationRecordHandle`

#### Returns {#returns-16}

`boolean`

-----

### serviceAssignments\(\) {#serviceassignments}

```ts
serviceAssignments(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned service assignments section of this exact parent\.

# Errors {#errors-14}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-16}

<Heading level={5} id="maximuminspected&#45;14" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;14" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;14" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;14" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-17}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### serviceAuthorities\(\) {#serviceauthorities}

```ts
serviceAuthorities(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned service authorities section of this exact parent\.

# Errors {#errors-15}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-17}

<Heading level={5} id="maximuminspected&#45;15" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;15" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;15" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;15" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-18}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### serviceControllers\(\) {#servicecontrollers}

```ts
serviceControllers(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned service controllers section of this exact parent\.

# Errors {#errors-16}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-18}

<Heading level={5} id="maximuminspected&#45;16" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;16" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;16" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;16" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-19}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### serviceRights\(\) {#servicerights}

```ts
serviceRights(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned service rights section of this exact parent\.

# Errors {#errors-17}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-19}

<Heading level={5} id="maximuminspected&#45;17" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;17" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;17" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;17" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-20}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### sources\(\) {#sources}

```ts
sources(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationSourceCursor | null
): OrganizationSourcePage;
```

Page exact source occurrences and roles; unmapped is not absent source\.
Empty named pages can continue\. All original limits bind continuation\.

# Errors {#errors-18}

Numeric coercion rejects before the SDK; SDK diagnostics remain unchanged\.

#### Parameters {#parameters-20}

<Heading level={5} id="maximuminspected&#45;18" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;18" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;18" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;18" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationSourceCursor`](/pale/reference/js/classes/OrganizationSourceCursor) \| `null`

#### Returns {#returns-21}

[`OrganizationSourcePage`](/pale/reference/js/classes/OrganizationSourcePage)
