---
title: "Class: RecipientQualifiedOrganizationRecordHandle"
---

<a id="class&#45;recipientqualifiedorganizationrecordhandle"></a>

Exact admitted organization record with no supplied\-input query method\.

## Accessors {#accessors}

### workspaceId {#workspaceid}

#### Get Signature {#get-signature}

```ts
get workspaceId(): string;
```

Workspace retained by this record\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### sameRecord\(\) {#samerecord}

```ts
sameRecord(other: RecipientQualifiedOrganizationRecordHandle): boolean;
```

Test exact record custody under one compiler owner\.

#### Parameters {#parameters}

<Heading level={5} id="other" className="scroll-mt-(--scroll-mt)">other</Heading>

`RecipientQualifiedOrganizationRecordHandle`

#### Returns {#returns-1}

`boolean`
