---
title: "Class: ConfigurationImprovementInspection"
---

<a id="class&#45;configurationimprovementinspection"></a>

An admitted baseline awaiting its exact profile explanation\.

## Accessors {#accessors}

### phase {#phase}

#### Get Signature {#get-signature}

```ts
get phase(): ConfigurationImprovementPhase;
```

Current API\-owned phase\.

# Errors {#errors}

Returns a host\-argument error after this stage has been consumed\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ConfigurationImprovementPhase`](/pale/reference/js/enumerations/ConfigurationImprovementPhase)

-----

### principalUniverseDigest {#principaluniversedigest}

#### Get Signature {#get-signature-1}

```ts
get principalUniverseDigest(): string;
```

Exact baseline admitted\-universe digest\.

# Errors {#errors-1}

Returns a host error after consumption\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### workspaceId {#workspaceid}

#### Get Signature {#get-signature-2}

```ts
get workspaceId(): string;
```

Admitted principal workspace\.

# Errors {#errors-2}

Returns a host error after consumption\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
