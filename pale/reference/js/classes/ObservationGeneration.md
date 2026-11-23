---
title: "Class: ObservationGeneration"
---

<a id="class&#45;observationgeneration"></a>

Owned generation coordinate with variant\-specific accessors\.

## Accessors {#accessors}

### activeGenerationDigest {#activegenerationdigest}

#### Get Signature {#get-signature}

```ts
get activeGenerationDigest(): string | null;
```

Return the active digest for a resident generation, when selected\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### compositionPlanDigest {#compositionplandigest}

#### Get Signature {#get-signature-1}

```ts
get compositionPlanDigest(): string | null;
```

Return the composition proof digest that binds an effective profile's causal paths\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### controlIncarnationId {#controlincarnationid}

#### Get Signature {#get-signature-2}

```ts
get controlIncarnationId(): string | null;
```

Return the authority\-store incarnation for a resident generation\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### controlStoreId {#controlstoreid}

#### Get Signature {#get-signature-3}

```ts
get controlStoreId(): string | null;
```

Return the stable authority\-store identity for a resident generation\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### instanceDigest {#instancedigest}

#### Get Signature {#get-signature-4}

```ts
get instanceDigest(): string | null;
```

Return the machine\-resolved instance digest for an effective profile\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### kind {#kind}

#### Get Signature {#get-signature-5}

```ts
get kind(): ObservationGenerationKind;
```

Return the closed generation kind\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationGenerationKind`](/pale/reference/js/enumerations/ObservationGenerationKind)

-----

### profileDigest {#profiledigest}

#### Get Signature {#get-signature-6}

```ts
get profileDigest(): string | null;
```

Return the profile digest for an effective\-profile generation\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`
