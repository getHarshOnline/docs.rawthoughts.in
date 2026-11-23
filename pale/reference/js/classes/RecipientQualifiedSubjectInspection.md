---
title: "Class: RecipientQualifiedSubjectInspection"
---

<a id="class&#45;recipientqualifiedsubjectinspection"></a>

Admitted proof and source evidence with an authority\-bound continuation\.

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

### dependencyCopiedStringBytes {#dependencycopiedstringbytes}

#### Get Signature {#get-signature-1}

```ts
get dependencyCopiedStringBytes(): number;
```

UTF\-8 bytes copied into proof steps\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-2}

```ts
get inspected(): number;
```

Source candidates examined by this call\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### sourceCopiedStringBytes {#sourcecopiedstringbytes}

#### Get Signature {#get-signature-3}

```ts
get sourceCopiedStringBytes(): number;
```

UTF\-8 bytes copied into source locations\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

## Methods {#methods}

### continuation\(\) {#continuation}

```ts
continuation(): 
  | RecipientQualifiedSubjectInspectionCursor
  | null;
```

Resume only through the same qualified comparison owner\.

#### Returns {#returns-4}

\| [`RecipientQualifiedSubjectInspectionCursor`](/pale/reference/js/classes/RecipientQualifiedSubjectInspectionCursor)
\| `null`

-----

### dependencies\(\) {#dependencies}

```ts
dependencies(): WorkspaceCausalStep[];
```

Copy this page's direct proof inputs\.

#### Returns {#returns-5}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep)\[\]

-----

### occurrences\(\) {#occurrences}

```ts
occurrences(): AuthoringOccurrence[];
```

Copy exact named source occurrences\.

# Errors {#errors}

Returns a projection error if a source index cannot fit the Node ABI\.

#### Returns {#returns-6}

[`AuthoringOccurrence`](/pale/reference/js/interfaces/AuthoringOccurrence)\[\]
