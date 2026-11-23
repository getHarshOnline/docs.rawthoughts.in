---
title: "Class: EffectiveProfileEntry"
---

<a id="class&#45;effectiveprofileentry"></a>

One retained SDK row with its original opaque explanation handle\.

Values remain readable independently of the page or join that returned
them\. Explaining a handle still requires a retained matching profile\.

## Accessors {#accessors}

### detail {#detail}

#### Get Signature {#get-signature}

```ts
get detail(): EffectiveProfileEntryDetail;
```

Copy this row's exact variant payload into an output\-only value\.

Each read copies the selected payload, including its arrays\. Retain the
returned detail when inspecting several fields\. Editing the JavaScript
copy cannot change this retained row or admit a new subject or effect\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`EffectiveProfileEntryDetail`](/pale/reference/js/type-aliases/EffectiveProfileEntryDetail)

-----

### explanationHandle {#explanationhandle}

#### Get Signature {#get-signature-1}

```ts
get explanationHandle(): string;
```

Original SDK\-owned row explanation identity\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`
