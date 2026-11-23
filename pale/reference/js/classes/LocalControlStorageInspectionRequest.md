---
title: "Class: LocalControlStorageInspectionRequest"
---

<a id="class&#45;localcontrolstorageinspectionrequest"></a>

Owned scope\-selected request; construction neither validates nor performs I/O\.

The root stays inside the opaque API request\. No property or debug projection
exposes it\. Validation and root confinement occur only when
\[`Pale::inspect_local_control_store`\] invokes the canonical owner\.

## Methods {#methods}

### deployment\(\) {#deployment}

```ts
static deployment(
   runtimeStateRoot: string, 
   workspaceId: string, 
   deploymentBindingRef: string, 
   deploymentBindingSha256: string, 
   logicalStoreId: string, 
   controlIncarnationId: string
): LocalControlStorageInspectionRequest;
```

Select the exact immutable deployment\-store coordinate without host access\.

#### Parameters {#parameters}

<Heading level={5} id="runtimestateroot" className="scroll-mt-(--scroll-mt)">runtimeStateRoot</Heading>

`string`

<Heading level={5} id="workspaceid" className="scroll-mt-(--scroll-mt)">workspaceId</Heading>

`string`

<Heading level={5} id="deploymentbindingref" className="scroll-mt-(--scroll-mt)">deploymentBindingRef</Heading>

`string`

<Heading level={5} id="deploymentbindingsha256" className="scroll-mt-(--scroll-mt)">deploymentBindingSha256</Heading>

`string`

<Heading level={5} id="logicalstoreid" className="scroll-mt-(--scroll-mt)">logicalStoreId</Heading>

`string`

<Heading level={5} id="controlincarnationid" className="scroll-mt-(--scroll-mt)">controlIncarnationId</Heading>

`string`

#### Returns {#returns}

`LocalControlStorageInspectionRequest`

-----

### principal\(\) {#principal}

```ts
static principal(
   runtimeStateRoot: string, 
   principalId: string, 
   logicalStoreId: string, 
   controlIncarnationId: string
): LocalControlStorageInspectionRequest;
```

Select the exact principal trust\-store coordinate without host access\.

#### Parameters {#parameters-1}

<Heading level={5} id="runtimestateroot&#45;1" className="scroll-mt-(--scroll-mt)">runtimeStateRoot</Heading>

`string`

<Heading level={5} id="principalid" className="scroll-mt-(--scroll-mt)">principalId</Heading>

`string`

<Heading level={5} id="logicalstoreid&#45;1" className="scroll-mt-(--scroll-mt)">logicalStoreId</Heading>

`string`

<Heading level={5} id="controlincarnationid&#45;1" className="scroll-mt-(--scroll-mt)">controlIncarnationId</Heading>

`string`

#### Returns {#returns-1}

`LocalControlStorageInspectionRequest`
