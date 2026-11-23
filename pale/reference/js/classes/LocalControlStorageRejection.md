---
title: "Class: LocalControlStorageRejection"
---

<a id="class&#45;localcontrolstoragerejection"></a>

A persistent rejection whose version detail exists only for a newer schema\.

## Accessors {#accessors}

### kind {#kind}

#### Get Signature {#get-signature}

```ts
get kind(): LocalControlStorageRejectionKind;
```

Exact API\-owned persistent contradiction\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`LocalControlStorageRejectionKind`](/pale/reference/js/enumerations/LocalControlStorageRejectionKind)

-----

### observedVersion {#observedversion}

#### Get Signature {#get-signature-1}

```ts
get observedVersion(): number | null;
```

Observed schema version, or absent for every non\-version rejection\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `null`

-----

### supportedVersion {#supportedversion}

#### Get Signature {#get-signature-2}

```ts
get supportedVersion(): number | null;
```

Greatest supported schema version, only for a newer\-version rejection\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number` \| `null`
