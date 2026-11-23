---
title: "Class: OneShotPlanCandidate"
---

<a id="class&#45;oneshotplancandidate"></a>

Canonical effect\-free plan candidate and its flat transition counts\.

The private API value is linear: binding machine effects consumes it
exactly once\. The copied identity fields remain inspectable so JavaScript
garbage collection or a repeated host call cannot recreate planning
authority\.

## Accessors {#accessors}

### canonicalBytes {#canonicalbytes}

#### Get Signature {#get-signature}

```ts
get canonicalBytes(): Buffer;
```

Copy canonical `agent-surface-plan.v1` bytes\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Buffer`

-----

### deferredEffectCount {#deferredeffectcount}

#### Get Signature {#get-signature-1}

```ts
get deferredEffectCount(): number;
```

Deferred host\-effect count\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### kind {#kind}

#### Get Signature {#get-signature-2}

```ts
get kind(): OneShotPlanKind;
```

Requested plan operation\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OneShotPlanKind`](/pale/reference/js/enumerations/OneShotPlanKind)

-----

### oneShotCompilationDigest {#oneshotcompilationdigest}

#### Get Signature {#get-signature-3}

```ts
get oneShotCompilationDigest(): string;
```

One\-shot output identity used by planning\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### operationCount {#operationcount}

#### Get Signature {#get-signature-4}

```ts
get operationCount(): number;
```

Planned operation count\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### planDigest {#plandigest}

#### Get Signature {#get-signature-5}

```ts
get planDigest(): string;
```

Canonical complete\-plan digest\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### repositoryId {#repositoryid}

#### Get Signature {#get-signature-6}

```ts
get repositoryId(): string;
```

Selected logical repository\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
