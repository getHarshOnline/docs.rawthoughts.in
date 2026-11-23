---
title: "Class: OneShotObservationRequest"
---

<a id="class&#45;oneshotobservationrequest"></a>

Complete effect\-free observation\-target request\.

## Constructors {#constructors}

### Constructor {#constructor}

```ts
new OneShotObservationRequest(
   repositoryId: string, 
   kind: OneShotPlanKind, 
   prior: OneShotPriorMaterialization
): OneShotObservationRequest;
```

Capture one cohesive observation\-target request\.

#### Parameters {#parameters}

<Heading level={5} id="repositoryid" className="scroll-mt-(--scroll-mt)">repositoryId</Heading>

`string`

<Heading level={5} id="kind" className="scroll-mt-(--scroll-mt)">kind</Heading>

[`OneShotPlanKind`](/pale/reference/js/enumerations/OneShotPlanKind)

<Heading level={5} id="prior" className="scroll-mt-(--scroll-mt)">prior</Heading>

[`OneShotPriorMaterialization`](/pale/reference/js/classes/OneShotPriorMaterialization)

#### Returns {#returns}

`OneShotObservationRequest`
