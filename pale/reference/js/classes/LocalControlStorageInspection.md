---
title: "Class: LocalControlStorageInspection"
---

<a id="class&#45;localcontrolstorageinspection"></a>

Opaque physical result, independent of writer, resident and native readiness\.

Optional details are tied to the retained closed API state, never supplied
by JavaScript\. The result contains no runtime root or database connection\.

## Accessors {#accessors}

### kind {#kind}

#### Get Signature {#get-signature}

```ts
get kind(): LocalControlStoreKind;
```

Store class implied by the exact inspected scope\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`LocalControlStoreKind`](/pale/reference/js/enumerations/LocalControlStoreKind)

-----

### rejection {#rejection}

#### Get Signature {#get-signature-1}

```ts
get rejection(): 
  | LocalControlStorageRejection
  | null;
```

Persistent contradiction only for \[`LocalControlStorageStateKind::Rejected`\];
not an API transport failure\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`LocalControlStorageRejection`](/pale/reference/js/classes/LocalControlStorageRejection)
\| `null`

-----

### state {#state}

#### Get Signature {#get-signature-2}

```ts
get state(): LocalControlStorageStateKind;
```

Physical classification only; \[`LocalControlStorageStateKind::Ready`\]
never grants authority\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`LocalControlStorageStateKind`](/pale/reference/js/enumerations/LocalControlStorageStateKind)

-----

### unresolved {#unresolved}

#### Get Signature {#get-signature-3}

```ts
get unresolved(): 
  | LocalControlStorageProfileRequirement[]
  | null;
```

Requirements only for \[`LocalControlStorageStateKind::ProfileUnselected`\],
preserving source\-owned order\.

Absence means a different physical state, not an admitted profile\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`LocalControlStorageProfileRequirement`](/pale/reference/js/enumerations/LocalControlStorageProfileRequirement)\[\]
\| `null`
