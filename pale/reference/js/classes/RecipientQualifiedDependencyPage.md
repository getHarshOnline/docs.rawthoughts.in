---
title: "Class: RecipientQualifiedDependencyPage"
---

<a id="class&#45;recipientqualifieddependencypage"></a>

Admitted direct dependencies with an authority\-bound continuation\.

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

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature-1}

```ts
get copiedStringBytes(): number;
```

UTF\-8 bytes copied into proof steps\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

## Methods {#methods}

### continuation\(\) {#continuation}

```ts
continuation(): 
  | RecipientQualifiedDependencyCursor
  | null;
```

Resume only through the same qualified comparison owner\.

#### Returns {#returns-2}

\| [`RecipientQualifiedDependencyCursor`](/pale/reference/js/classes/RecipientQualifiedDependencyCursor)
\| `null`

-----

### dependencies\(\) {#dependencies}

```ts
dependencies(): WorkspaceCausalStep[];
```

Copy direct proof inputs\.

#### Returns {#returns-3}

[`WorkspaceCausalStep`](/pale/reference/js/classes/WorkspaceCausalStep)\[\]
