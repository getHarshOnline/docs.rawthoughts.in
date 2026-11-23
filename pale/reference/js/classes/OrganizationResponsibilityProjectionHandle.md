---
title: "Class: OrganizationResponsibilityProjectionHandle"
---

<a id="class&#45;organizationresponsibilityprojectionhandle"></a>

Query one responsibility projection's members; see \[`OrganizationCursor`\] for custody\.

## Methods {#methods}

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
