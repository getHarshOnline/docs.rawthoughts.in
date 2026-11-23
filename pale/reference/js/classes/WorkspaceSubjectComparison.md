---
title: "Class: WorkspaceSubjectComparison"
---

<a id="class&#45;workspacesubjectcomparison"></a>

Owned comparison of one subject, with the SDK's exact canonical bytes\.

The receipt identifies the parent comparison\. Its existing summary supplies
the prior/current universe and semantic identities\. This answer is not a
new receipt, a compilation handle or evidence of native state\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy the API\-owned projection without parsing or re\-encoding it\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### receiptDigest {#receiptdigest}

#### Get Signature {#get-signature-1}

```ts
get receiptDigest(): string;
```

Identity of the parent comparison that produced this answer\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### values {#values}

#### Get Signature {#get-signature-2}

```ts
get values(): WorkspaceSubjectValues;
```

Copy membership and values without deriving equality in JavaScript\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceSubjectValues`](/pale/reference/js/type-aliases/WorkspaceSubjectValues)

## Methods {#methods}

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Copy the full subject, including compound identity fields\.

#### Returns {#returns-3}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
