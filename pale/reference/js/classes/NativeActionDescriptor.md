---
title: "Class: NativeActionDescriptor"
---

<a id="class&#45;nativeactiondescriptor"></a>

One API\-owned native\-action descriptor\.

## Accessors {#accessors}

### actionId {#actionid}

#### Get Signature {#get-signature}

```ts
get actionId(): string;
```

Exact compiled action identity\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### contractBytes {#contractbytes}

#### Get Signature {#get-signature-1}

```ts
get contractBytes(): Buffer;
```

Exact canonical action contract bytes\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### description {#description}

#### Get Signature {#get-signature-2}

```ts
get description(): string;
```

Registry\-owned concise description\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### payloadSchemaBytes {#payloadschemabytes}

#### Get Signature {#get-signature-3}

```ts
get payloadSchemaBytes(): Buffer;
```

Self\-contained payload schema bytes\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`
