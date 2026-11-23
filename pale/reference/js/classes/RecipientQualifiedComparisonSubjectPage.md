---
title: "Class: RecipientQualifiedComparisonSubjectPage"
---

<a id="class&#45;recipientqualifiedcomparisonsubjectpage"></a>

Admitted comparison subjects with an authority\-bound continuation\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy the canonical projection without opaque custody\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-1}

```ts
get inspected(): number;
```

Native entries examined by the bounded merge\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### subjectIdentityBytes {#subjectidentitybytes}

#### Get Signature {#get-signature-2}

```ts
get subjectIdentityBytes(): number;
```

UTF\-8 bytes copied from subject identities\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

## Methods {#methods}

### comparison\(\) {#comparison}

```ts
comparison(): WorkspaceComparisonSummary;
```

Copy comparison coordinates and receipt identity\.

#### Returns {#returns-3}

[`WorkspaceComparisonSummary`](/pale/reference/js/classes/WorkspaceComparisonSummary)

-----

### continuation\(\) {#continuation}

```ts
continuation(): 
  | RecipientQualifiedComparisonSubjectCursor
  | null;
```

Resume only through the same qualified comparison owner\.

#### Returns {#returns-4}

\| [`RecipientQualifiedComparisonSubjectCursor`](/pale/reference/js/classes/RecipientQualifiedComparisonSubjectCursor)
\| `null`

-----

### subjects\(\) {#subjects}

```ts
subjects(): WorkspaceSubject[];
```

Copy subject identities in canonical order\.

#### Returns {#returns-5}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)\[\]
