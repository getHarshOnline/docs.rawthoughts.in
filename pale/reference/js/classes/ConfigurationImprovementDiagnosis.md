---
title: "Class: ConfigurationImprovementDiagnosis"
---

<a id="class&#45;configurationimprovementdiagnosis"></a>

A diagnosed candidate awaiting a complete immutable preview\.

## Accessors {#accessors}

### derivationReceiptDigest {#derivationreceiptdigest}

#### Get Signature {#get-signature}

```ts
get derivationReceiptDigest(): string;
```

Exact canonical derivation receipt identity\.

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
