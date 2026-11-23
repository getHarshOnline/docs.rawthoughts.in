---
title: "Class: WorkspaceImpactPage"
---

<a id="class&#45;workspaceimpactpage"></a>

One bounded page of the complete impact partition\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy the SDK's sealed canonical page without reconstructing its entries\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### entries {#entries}

#### Get Signature {#get-signature-1}

```ts
get entries(): WorkspaceImpact[];
```

Copy canonically ordered impact entries without exposing retained state\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceImpact`](/pale/reference/js/classes/WorkspaceImpact)\[\]

-----

### nextOffset {#nextoffset}

#### Get Signature {#get-signature-2}

```ts
get nextOffset(): number | undefined;
```

Exact next offset, or no value at the terminal page\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `undefined`
