---
title: "Class: RecipientQualifiedOrganizationCorrespondence"
---

<a id="class&#45;recipientqualifiedorganizationcorrespondence"></a>

One admitted cross\-generation organization lookup\.

## Accessors {#accessors}

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature}

```ts
get copiedStringBytes(): number;
```

UTF\-8 row bytes copied for a match\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-1}

```ts
get inspected(): number;
```

Other\-side candidates examined\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### selected {#selected}

#### Get Signature {#get-signature-2}

```ts
get selected(): RecipientQualifiedOrganizationRecordHandle;
```

Retain the admitted selected record\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`RecipientQualifiedOrganizationRecordHandle`](/pale/reference/js/classes/RecipientQualifiedOrganizationRecordHandle)

-----

### selectedSide {#selectedside}

#### Get Signature {#get-signature-3}

```ts
get selectedSide(): OrganizationComparisonSide;
```

Side that supplied the selected record\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationComparisonSide`](/pale/reference/js/enumerations/OrganizationComparisonSide)

-----

### state {#state}

#### Get Signature {#get-signature-4}

```ts
get state(): RecipientQualifiedOrganizationCorrespondenceState;
```

Copy the bounded search state\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`RecipientQualifiedOrganizationCorrespondenceState`](/pale/reference/js/type-aliases/RecipientQualifiedOrganizationCorrespondenceState)
