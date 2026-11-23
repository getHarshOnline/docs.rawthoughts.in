---
title: "Class: LocalMaterializationAdmittedRun"
---

<a id="class&#45;localmaterializationadmittedrun"></a>

Opaque admitted local run awaiting settlement or non\-effectful drop\.

## Accessors {#accessors}

### kind {#kind}

#### Get Signature {#get-signature}

```ts
get kind(): OneShotPlanKind;
```

Requested apply, explicit\-adoption, or removal journey\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OneShotPlanKind`](/pale/reference/js/enumerations/OneShotPlanKind)

## Methods {#methods}

### targets\(\) {#targets}

```ts
targets(): LocalMaterializationTargetAdmission[];
```

Ordered repository\-plan identities admitted before effects\.

#### Returns {#returns-1}

[`LocalMaterializationTargetAdmission`](/pale/reference/js/interfaces/LocalMaterializationTargetAdmission)\[\]
