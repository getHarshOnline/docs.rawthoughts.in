---
title: "Class: AdmittedRepositoryActions"
---

<a id="class&#45;admittedrepositoryactions"></a>

Repository\-bound admitted action selection\.

## Accessors {#accessors}

### instanceDigest {#instancedigest}

#### Get Signature {#get-signature}

```ts
get instanceDigest(): string;
```

Exact instance digest carried by the admitted catalog\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### profileDigest {#profiledigest}

#### Get Signature {#get-signature-1}

```ts
get profileDigest(): string;
```

Exact profile digest carried by the admitted catalog\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### repositoryId {#repositoryid}

#### Get Signature {#get-signature-2}

```ts
get repositoryId(): string;
```

Exact repository identity carried by the admitted catalog\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

## Methods {#methods}

### descriptors\(\) {#descriptors}

```ts
descriptors(): NativeActionDescriptor[];
```

Clone the stable selected descriptors as one batch\.

#### Returns {#returns-3}

[`NativeActionDescriptor`](/pale/reference/js/classes/NativeActionDescriptor)\[\]
