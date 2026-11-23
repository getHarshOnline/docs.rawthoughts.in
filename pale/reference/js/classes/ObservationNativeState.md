---
title: "Class: ObservationNativeState"
---

<a id="class&#45;observationnativestate"></a>

Native\-owner evidence without copied native payload\.

## Accessors {#accessors}

### kind {#kind}

#### Get Signature {#get-signature}

```ts
get kind(): ObservationNativeStateKind;
```

Return the closed native\-evidence kind\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`ObservationNativeStateKind`](/pale/reference/js/enumerations/ObservationNativeStateKind)

-----

### observationKind {#observationkind}

#### Get Signature {#get-signature-1}

```ts
get observationKind(): string | null;
```

Return the owner\-defined observation kind when observed\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`

-----

### ownerSystemId {#ownersystemid}

#### Get Signature {#get-signature-2}

```ts
get ownerSystemId(): string | null;
```

Return the native system retaining source truth when observed\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string` \| `null`
