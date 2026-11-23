---
title: "Class: OrganizationServiceAssignmentHandle"
---

<a id="class&#45;organizationserviceassignmenthandle"></a>

Query one service assignment's members; see \[`OrganizationCursor`\] for custody\.

## Methods {#methods}

### pods\(\) {#pods}

```ts
pods(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned pods section of this exact parent\.

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

#### Returns {#returns}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)

-----

### stewards\(\) {#stewards}

```ts
stewards(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned stewards section of this exact parent\.

# Errors {#errors-1}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-1}

<Heading level={5} id="maximuminspected&#45;1" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;1" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;1" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-1}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)
