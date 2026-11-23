---
title: "Class: OrganizationResponsibility"
---

<a id="class&#45;organizationresponsibility"></a>

Shallow responsibility header with independent attributed answers\.

Kept in one allocation when held by \[`OrganizationRow`\], so its complete
attribution payload does not determine every other row's inline size\.
The copied\-string budget excludes this allocation and allocator overhead\.

## Accessors {#accessors}

### consumerAcceptance {#consumeracceptance}

#### Get Signature {#get-signature}

```ts
get consumerAcceptance(): OrganizationConsumerAcceptanceAnswer;
```

Independent consumer\-local consequence acceptance requirement\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationConsumerAcceptanceAnswer`](/pale/reference/js/type-aliases/OrganizationConsumerAcceptanceAnswer)

-----

### derivationId {#derivationid}

#### Get Signature {#get-signature-1}

```ts
get derivationId(): string;
```

Exact responsibility derivation identity\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### lifecycle {#lifecycle}

#### Get Signature {#get-signature-2}

```ts
get lifecycle(): OrganizationResponsibilityLifecycle;
```

Lifecycle asserted by the author; not reverified by this query\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationResponsibilityLifecycle`](/pale/reference/js/enumerations/OrganizationResponsibilityLifecycle)

-----

### nativeResult {#nativeresult}

#### Get Signature {#get-signature-3}

```ts
get nativeResult(): OrganizationNativeReadBackAnswer;
```

Independent supplied native\-result/read\-back requirement or omission\.

<Heading level={5} id="returns&#45;3" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationNativeReadBackAnswer`](/pale/reference/js/type-aliases/OrganizationNativeReadBackAnswer)

-----

### paleSettlement {#palesettlement}

#### Get Signature {#get-signature-4}

```ts
get paleSettlement(): OrganizationSettlementAnswer;
```

Independent Pale obligation\-settlement requirement\.

<Heading level={5} id="returns&#45;4" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationSettlementAnswer`](/pale/reference/js/type-aliases/OrganizationSettlementAnswer)

-----

### placement {#placement}

#### Get Signature {#get-signature-5}

```ts
get placement(): OrganizationPlacementAnswer;
```

Actual supplied placement or explicit attributed omission\.

<Heading level={5} id="returns&#45;5" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationPlacementAnswer`](/pale/reference/js/type-aliases/OrganizationPlacementAnswer)

-----

### provenance {#provenance}

#### Get Signature {#get-signature-6}

```ts
get provenance(): OrganizationAttribution;
```

Original complete\-record source/owner attribution\.

<Heading level={5} id="returns&#45;6" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationAttribution`](/pale/reference/js/interfaces/OrganizationAttribution)

-----

### providerAcceptance {#provideracceptance}

#### Get Signature {#get-signature-7}

```ts
get providerAcceptance(): OrganizationProviderAcceptanceAnswer;
```

Independent provider\-local acceptance requirement\.

<Heading level={5} id="returns&#45;7" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationProviderAcceptanceAnswer`](/pale/reference/js/type-aliases/OrganizationProviderAcceptanceAnswer)

-----

### providerCompletion {#providercompletion}

#### Get Signature {#get-signature-8}

```ts
get providerCompletion(): OrganizationProviderCompletionAnswer;
```

Independent provider\-local completion requirement\.

<Heading level={5} id="returns&#45;8" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationProviderCompletionAnswer`](/pale/reference/js/type-aliases/OrganizationProviderCompletionAnswer)
