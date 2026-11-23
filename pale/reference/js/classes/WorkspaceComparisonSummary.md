---
title: "Class: WorkspaceComparisonSummary"
---

<a id="class&#45;workspacecomparisonsummary"></a>

Owned comparison coordinates and complete partition counts\.

This is the same API summary whether obtained from a workspace comparison
or a configuration\-improvement preview; it owns no causal graph\.

## Accessors {#accessors}

### affectedCount {#affectedcount}

#### Get Signature {#get-signature}

```ts
get affectedCount(): number;
```

Number of affected current subjects\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature-1}

```ts
get canonicalBytes(): Buffer;
```

Exact API\-owned canonical summary bytes\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### changeRootCount {#changerootcount}

#### Get Signature {#get-signature-2}

```ts
get changeRootCount(): number;
```

Exact number of change roots\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### currentPrincipalUniverseDigest {#currentprincipaluniversedigest}

#### Get Signature {#get-signature-3}

```ts
get currentPrincipalUniverseDigest(): string;
```

Exact current admitted\-universe identity\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### currentSemanticIrDigest {#currentsemanticirdigest}

#### Get Signature {#get-signature-4}

```ts
get currentSemanticIrDigest(): string;
```

Current semantic\-IR identity\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### priorPrincipalUniverseDigest {#priorprincipaluniversedigest}

#### Get Signature {#get-signature-5}

```ts
get priorPrincipalUniverseDigest(): string;
```

Exact predecessor admitted\-universe identity\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### priorSemanticIrDigest {#priorsemanticirdigest}

#### Get Signature {#get-signature-6}

```ts
get priorSemanticIrDigest(): string;
```

Predecessor semantic\-IR identity\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### receiptDigest {#receiptdigest}

#### Get Signature {#get-signature-7}

```ts
get receiptDigest(): string;
```

Canonical derivation receipt identity\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### unaffectedCount {#unaffectedcount}

#### Get Signature {#get-signature-8}

```ts
get unaffectedCount(): number;
```

Number of unaffected current subjects\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`
