---
title: "Class: OrganizationGenealogyHandle"
---

<a id="class&#45;organizationgenealogyhandle"></a>

Query one genealogy link's members; see \[`OrganizationCursor`\] for custody\.

## Methods {#methods}

### occurrences\(\) {#occurrences}

```ts
occurrences(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned occurrences section of this exact parent\.

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

### projections\(\) {#projections}

```ts
projections(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned projections section of this exact parent\.

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

-----

### responsibilities\(\) {#responsibilities}

```ts
responsibilities(
   maximumInspected: number, 
   maximumReturned: number, 
   maximumCopiedBytes: number, 
   after?: OrganizationDetailCursor | null
): OrganizationDetailPage;
```

Page the SDK\-owned responsibilities section of this exact parent\.

# Errors {#errors-2}

Invalid numeric representations reject before dispatch; SDK limit, custody,
unavailable\-section and copied\-string errors preserve their diagnostics\.

#### Parameters {#parameters-2}

<Heading level={5} id="maximuminspected&#45;2" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;2" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="maximumcopiedbytes&#45;2" className="scroll-mt-(--scroll-mt)">maximumCopiedBytes</Heading>

`number`

<Heading level={5} id="after&#45;2" className="scroll-mt-(--scroll-mt)">after?</Heading>

[`OrganizationDetailCursor`](/pale/reference/js/classes/OrganizationDetailCursor) \| `null`

#### Returns {#returns-2}

[`OrganizationDetailPage`](/pale/reference/js/classes/OrganizationDetailPage)
