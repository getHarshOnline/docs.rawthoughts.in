---
title: "Class: WorkspaceChangeRootPage"
---

<a id="class&#45;workspacechangerootpage"></a>

One bounded page of change roots\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy the SDK's sealed canonical page without rebuilding its entries\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### entries {#entries}

#### Get Signature {#get-signature-1}

```ts
get entries(): WorkspaceChangeRoot[];
```

Copy canonically ordered root entries\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceChangeRoot`](/pale/reference/js/classes/WorkspaceChangeRoot)\[\]

-----

### nextOffset {#nextoffset}

#### Get Signature {#get-signature-2}

```ts
get nextOffset(): number | undefined;
```

Exact next offset, or no value at the terminal page\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `undefined`
