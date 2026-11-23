---
title: "Type Alias: EffectiveProfileExplanationEvidence"
---

<a id="type&#45;alias&#45;effectiveprofileexplanationevidence"></a>

```ts
type EffectiveProfileExplanationEvidence = 
  | {
  kind: "declared-selection";
  selection: EffectiveProfileDeclaredSelection;
}
  | {
  contractId: string;
  executionPathId: string;
  kind: "responsibility";
  reasonSteps: EffectiveProfilePathReason[];
}
  | {
  kind: "effective-selection";
  selection: EffectiveProfileSelection;
}
  | {
  kind: "execution-path";
  reasonSteps: EffectiveProfilePathReason[];
  selectionId: string;
}
  | {
  exposure: OperationExposure;
  kind: "operation-classification";
  nativeRealization: EffectiveProfileNativeRealization;
}
  | {
  kind: "capability-classification";
  nativeRealization: EffectiveProfileNativeRealization;
  providerDisposition: EffectiveProfileProviderDisposition;
  requirementDisposition: RequirementDisposition;
}
  | {
  finding: EffectiveProfileFinding;
  kind: "finding-classification";
}
  | {
  kind: "machine-realization";
  realization: EffectiveProfileNativeRealization;
}
  | {
  kind: "configuration";
};
```

Exact SDK evidence copied into a discriminated output value\.

Ordered reason lists, including empty lists, are preserved\. Configuration
does not authorize effects or establish machine/process readiness\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "declared-selection";
  selection: EffectiveProfileDeclaredSelection;
}
```

#### kind {#kind}

```ts
kind: "declared-selection";
```

#### selection {#selection}

```ts
selection: EffectiveProfileDeclaredSelection;
```

Normalized unexpanded selection\.

-----

### Type Literal {#type-literal-1}

```ts
{
  contractId: string;
  executionPathId: string;
  kind: "responsibility";
  reasonSteps: EffectiveProfilePathReason[];
}
```

#### contractId {#contractid}

```ts
contractId: string;
```

Exact responsibility contract\.

#### executionPathId {#executionpathid}

```ts
executionPathId: string;
```

Selected path carrying the contract\.

#### kind {#kind-1}

```ts
kind: "responsibility";
```

#### reasonSteps {#reasonsteps}

```ts
reasonSteps: EffectiveProfilePathReason[];
```

Ordered composition reasons, possibly empty\.

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "effective-selection";
  selection: EffectiveProfileSelection;
}
```

#### kind {#kind-2}

```ts
kind: "effective-selection";
```

#### selection {#selection-1}

```ts
selection: EffectiveProfileSelection;
```

Exact selected coordinate\.

-----

### Type Literal {#type-literal-3}

```ts
{
  kind: "execution-path";
  reasonSteps: EffectiveProfilePathReason[];
  selectionId: string;
}
```

#### kind {#kind-3}

```ts
kind: "execution-path";
```

#### reasonSteps {#reasonsteps-1}

```ts
reasonSteps: EffectiveProfilePathReason[];
```

Ordered composition reasons, possibly empty\.

#### selectionId {#selectionid}

```ts
selectionId: string;
```

Stable selected\-path identity\.

-----

### Type Literal {#type-literal-4}

```ts
{
  exposure: OperationExposure;
  kind: "operation-classification";
  nativeRealization: EffectiveProfileNativeRealization;
}
```

#### exposure {#exposure}

```ts
exposure: OperationExposure;
```

Application\-owned exposure\.

#### kind {#kind-4}

```ts
kind: "operation-classification";
```

#### nativeRealization {#nativerealization}

```ts
nativeRealization: EffectiveProfileNativeRealization;
```

Independently qualified native evidence\.

-----

### Type Literal {#type-literal-5}

```ts
{
  kind: "capability-classification";
  nativeRealization: EffectiveProfileNativeRealization;
  providerDisposition: EffectiveProfileProviderDisposition;
  requirementDisposition: RequirementDisposition;
}
```

#### kind {#kind-5}

```ts
kind: "capability-classification";
```

#### nativeRealization {#nativerealization-1}

```ts
nativeRealization: EffectiveProfileNativeRealization;
```

Independently qualified native evidence\.

#### providerDisposition {#providerdisposition}

```ts
providerDisposition: EffectiveProfileProviderDisposition;
```

Private provider\-selection outcome\.

#### requirementDisposition {#requirementdisposition}

```ts
requirementDisposition: RequirementDisposition;
```

Portable requirement outcome\.

-----

### Type Literal {#type-literal-6}

```ts
{
  finding: EffectiveProfileFinding;
  kind: "finding-classification";
}
```

#### finding {#finding}

```ts
finding: EffectiveProfileFinding;
```

Structured finding without added inference\.

#### kind {#kind-6}

```ts
kind: "finding-classification";
```

-----

### Type Literal {#type-literal-7}

```ts
{
  kind: "machine-realization";
  realization: EffectiveProfileNativeRealization;
}
```

#### kind {#kind-7}

```ts
kind: "machine-realization";
```

#### realization {#realization}

```ts
realization: EffectiveProfileNativeRealization;
```

Independent native\-evidence state\.

-----

### Type Literal {#type-literal-8}

```ts
{
  kind: "configuration";
}
```
