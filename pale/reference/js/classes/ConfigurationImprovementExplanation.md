---
title: "Class: ConfigurationImprovementExplanation"
---

<a id="class&#45;configurationimprovementexplanation"></a>

The exact baseline explanation retained for proposal or borrowed preparation\.

## Accessors {#accessors}

### instanceDigest {#instancedigest}

#### Get Signature {#get-signature}

```ts
get instanceDigest(): string;
```

Exact private instance digest, not native\-readiness proof\.

# Errors {#errors}

Returns a host error after consumption\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### phase {#phase}

#### Get Signature {#get-signature-1}

```ts
get phase(): ConfigurationImprovementPhase;
```

Current API\-owned phase\.

# Errors {#errors-1}

Returns a host\-argument error after this stage has been consumed\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementPhase`](/pale/reference/js/enumerations/ConfigurationImprovementPhase)

-----

### profileDigest {#profiledigest}

#### Get Signature {#get-signature-2}

```ts
get profileDigest(): string;
```

Exact baseline profile digest\.

# Errors {#errors-2}

Returns a host error after consumption\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
