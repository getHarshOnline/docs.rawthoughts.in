---
title: "Class: ConfigurationImprovementEvaluation"
---

<a id="class&#45;configurationimprovementevaluation"></a>

An admitted candidate awaiting the canonical impact proof\.

## Accessors {#accessors}

### candidateInstanceDigest {#candidateinstancedigest}

#### Get Signature {#get-signature}

```ts
get candidateInstanceDigest(): string;
```

Exact candidate instance digest from admitted candidate compilation\.

# Errors {#errors}

Returns a host error after consumption\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidatePrincipalUniverseDigest {#candidateprincipaluniversedigest}

#### Get Signature {#get-signature-1}

```ts
get candidatePrincipalUniverseDigest(): string;
```

Exact candidate principal universe digest from admitted candidate compilation\.

# Errors {#errors-1}

Returns a host error after consumption\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### candidateProfileDigest {#candidateprofiledigest}

#### Get Signature {#get-signature-2}

```ts
get candidateProfileDigest(): string;
```

Exact candidate profile digest from admitted candidate compilation\.

# Errors {#errors-2}

Returns a host error after consumption\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### phase {#phase}

#### Get Signature {#get-signature-3}

```ts
get phase(): ConfigurationImprovementPhase;
```

Current API\-owned phase\.

# Errors {#errors-3}

Returns a host\-argument error after this stage has been consumed\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementPhase`](/pale/reference/js/enumerations/ConfigurationImprovementPhase)
