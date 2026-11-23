---
title: "Class: AuthoringIdentity"
---

<a id="class&#45;authoringidentity"></a>

Opaque API\-owned semantic identity eligible for effective\-profile joining\.

## Accessors {#accessors}

### authoredValue {#authoredvalue}

#### Get Signature {#get-signature}

```ts
get authoredValue(): string;
```

Exact TOML scalar spelling valid in the reference scope\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### kind {#kind}

#### Get Signature {#get-signature-1}

```ts
get kind(): AuthoringIdentityKind;
```

Non\-interchangeable semantic namespace\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`AuthoringIdentityKind`](/pale/reference/js/enumerations/AuthoringIdentityKind)

-----

### value {#value}

#### Get Signature {#get-signature-2}

```ts
get value(): string;
```

Canonical compiler\-owned display form\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
