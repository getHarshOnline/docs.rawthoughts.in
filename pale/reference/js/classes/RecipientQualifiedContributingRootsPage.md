---
title: "Class: RecipientQualifiedContributingRootsPage"
---

<a id="class&#45;recipientqualifiedcontributingrootspage"></a>

Admitted contributing roots with an authority\-bound continuation\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy the canonical projection without opaque custody\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

## Methods {#methods}

### continuation\(\) {#continuation}

```ts
continuation(): 
  | RecipientQualifiedContributingRootsCursor
  | null;
```

Resume only through the same qualified comparison owner\.

#### Returns {#returns-1}

\| [`RecipientQualifiedContributingRootsCursor`](/pale/reference/js/classes/RecipientQualifiedContributingRootsCursor)
\| `null`

-----

### roots\(\) {#roots}

```ts
roots(): WorkspaceChangeRoot[];
```

Copy exact contributing roots\.

#### Returns {#returns-2}

[`WorkspaceChangeRoot`](/pale/reference/js/classes/WorkspaceChangeRoot)\[\]
