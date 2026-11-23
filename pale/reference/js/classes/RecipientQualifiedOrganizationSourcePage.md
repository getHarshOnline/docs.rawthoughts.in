---
title: "Class: RecipientQualifiedOrganizationSourcePage"
---

<a id="class&#45;recipientqualifiedorganizationsourcepage"></a>

Exact admitted source evidence for one qualified record\.

## Accessors {#accessors}

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature}

```ts
get copiedStringBytes(): number;
```

UTF\-8 source\-location bytes copied into this page\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### mapping {#mapping}

#### Get Signature {#get-signature-1}

```ts
get mapping(): RecipientQualifiedOrganizationSourceMapping;
```

Copy the exact source mapping and qualified continuation\.

# Errors {#errors}

Returns a projection failure if a source index cannot fit the Node ABI\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`RecipientQualifiedOrganizationSourceMapping`](/pale/reference/js/type-aliases/RecipientQualifiedOrganizationSourceMapping)

-----

### record {#record}

#### Get Signature {#get-signature-2}

```ts
get record(): RecipientQualifiedOrganizationRecordHandle;
```

Exact admitted record that supplied this page\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`RecipientQualifiedOrganizationRecordHandle`](/pale/reference/js/classes/RecipientQualifiedOrganizationRecordHandle)
