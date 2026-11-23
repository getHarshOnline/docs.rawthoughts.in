---
title: "Class: OneShotPlanningRequest"
---

<a id="class&#45;oneshotplanningrequest"></a>

Complete pure\-planning request\.

## Constructors {#constructors}

### Constructor {#constructor}

```ts
new OneShotPlanningRequest(
   repositoryId: string, 
   kind: OneShotPlanKind, 
   prior: OneShotPriorMaterialization, 
   baseline: BaselineEntry[]
): OneShotPlanningRequest;
```

Capture one cohesive planning request from explicit closed observations\.

#### Parameters {#parameters}

<Heading level={5} id="repositoryid" className="scroll-mt-(--scroll-mt)">repositoryId</Heading>

`string`

<Heading level={5} id="kind" className="scroll-mt-(--scroll-mt)">kind</Heading>

[`OneShotPlanKind`](/pale/reference/js/enumerations/OneShotPlanKind)

<Heading level={5} id="prior" className="scroll-mt-(--scroll-mt)">prior</Heading>

[`OneShotPriorMaterialization`](/pale/reference/js/classes/OneShotPriorMaterialization)

<Heading level={5} id="baseline" className="scroll-mt-(--scroll-mt)">baseline</Heading>

[`BaselineEntry`](/pale/reference/js/classes/BaselineEntry)\[\]

#### Returns {#returns}

`OneShotPlanningRequest`
