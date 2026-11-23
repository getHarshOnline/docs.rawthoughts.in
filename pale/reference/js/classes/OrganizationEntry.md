---
title: "Class: OrganizationEntry"
---

<a id="class&#45;organizationentry"></a>

A shallow row paired with its independently retainable record handle\.

## Accessors {#accessors}

### handle {#handle}

#### Get Signature {#get-signature}

```ts
get handle(): OrganizationRecordHandle;
```

Independently retain the exact record for nested/source queries\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationRecordHandle`](/pale/reference/js/classes/OrganizationRecordHandle)

-----

### row {#row}

#### Get Signature {#get-signature-1}

```ts
get row(): OrganizationRow;
```

Copy the exact selected row payload; modifying it never mutates native custody\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationRow`](/pale/reference/js/type-aliases/OrganizationRow)
