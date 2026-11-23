---
title: "Type Alias: EffectiveProfileEntryDetail"
---

<a id="type&#45;alias&#45;effectiveprofileentrydetail"></a>

```ts
type EffectiveProfileEntryDetail = 
  | {
  kind: "declared-selection";
  selection: EffectiveProfileDeclaredSelection;
}
  | {
  authorityCeiling: EffectiveProfileEffectClass[];
  contractId: string;
  executionPathId: string;
  kind: "responsibility";
  participant: EffectiveProfileParticipant;
  reasonSteps: EffectiveProfilePathReason[];
  responsibilities: EffectiveProfileResponsibility[];
  subject: WorkspaceSubjectValue;
}
  | {
  kind: "selection";
  selection: EffectiveProfileSelection;
}
  | {
  forbiddenCapabilities: string[];
  forbiddenEffects: EffectiveProfileEffectClass[];
  kind: "capability-narrowing";
  permittedCapabilities: string[];
  permittedEffects: EffectiveProfileEffectClass[];
}
  | {
  contributors: string[];
  forbiddenCapabilities: string[];
  forbiddenEffects: EffectiveProfileEffectClass[];
  kind: "governing-ceiling";
  permittedCapabilities: string[];
  permittedEffects: EffectiveProfileEffectClass[];
  policies: string[];
  scope: string;
  subjectResource: string;
}
  | {
  accessCeiling: EffectiveProfileRepositoryAccess;
  kind: "repository";
  materializationOrder: number;
  repositoryId: string;
}
  | {
  kind: "provider-repository";
  nativeRealization: EffectiveProfileNativeRealization;
  nativeRepositoryCoordinate: string;
  providerBindingId: string;
  repositoryId: string;
}
  | {
  capabilityCeiling: string[];
  effectCeiling: EffectiveProfileEffectClass[];
  experiencePathId: string;
  kind: "execution-path";
  nativeRealization: EffectiveProfileNativeRealization;
  providerBindingIds: string[];
  reasonSteps: EffectiveProfilePathReason[];
  responsibilityContractIds: string[];
  responsibilityPathIdentity: string;
  selectionId: string;
  subject: WorkspaceSubjectValue;
  terminalProviderBinding:   | EffectiveProfileProviderBindingRef
     | null;
  workDelegationEdgeIds: string[];
}
  | {
  exposure: OperationExposure;
  kind: "operation";
  nativeRealization: EffectiveProfileNativeRealization;
  operationId: string;
  repositoryId: string;
}
  | {
  capabilityId: string;
  effectClass: EffectiveProfileEffectClass;
  kind: "capability";
  nativeRealization: EffectiveProfileNativeRealization;
  operationId: string;
  providerDisposition: EffectiveProfileProviderDisposition;
  repositoryId: string;
  requirementDisposition: RequirementDisposition;
  requirementId: string;
}
  | {
  kind: "machine-realization";
  machineId: string;
  realization: EffectiveProfileNativeRealization;
}
  | {
  finding: EffectiveProfileFinding;
  kind: "finding";
};
```

Exact payload of one profile row, narrowed by its `kind` in JavaScript\.

Only fields belonging to the selected variant are present\. The terminal
provider reference is intrinsically nullable; empty lists remain lists\.

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

Exact declared selector\.

-----

### Type Literal {#type-literal-1}

```ts
{
  authorityCeiling: EffectiveProfileEffectClass[];
  contractId: string;
  executionPathId: string;
  kind: "responsibility";
  participant: EffectiveProfileParticipant;
  reasonSteps: EffectiveProfilePathReason[];
  responsibilities: EffectiveProfileResponsibility[];
  subject: WorkspaceSubjectValue;
}
```

#### authorityCeiling {#authorityceiling}

```ts
authorityCeiling: EffectiveProfileEffectClass[];
```

Admitted effect ceiling, not execution permission\.

#### contractId {#contractid}

```ts
contractId: string;
```

Responsibility contract identity\.

#### executionPathId {#executionpathid}

```ts
executionPathId: string;
```

Selected execution path\.

#### kind {#kind-1}

```ts
kind: "responsibility";
```

#### participant {#participant}

```ts
participant: EffectiveProfileParticipant;
```

Participant bounded by this contract\.

#### reasonSteps {#reasonsteps}

```ts
reasonSteps: EffectiveProfilePathReason[];
```

Ordered causal reasons\.

#### responsibilities {#responsibilities}

```ts
responsibilities: EffectiveProfileResponsibility[];
```

Assigned responsibilities in owner\-provided order\.

#### subject {#subject}

```ts
subject: WorkspaceSubjectValue;
```

Copied causal selector, not an admitted comparison handle\.

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "selection";
  selection: EffectiveProfileSelection;
}
```

#### kind {#kind-2}

```ts
kind: "selection";
```

#### selection {#selection-1}

```ts
selection: EffectiveProfileSelection;
```

Exact selected value\.

-----

### Type Literal {#type-literal-3}

```ts
{
  forbiddenCapabilities: string[];
  forbiddenEffects: EffectiveProfileEffectClass[];
  kind: "capability-narrowing";
  permittedCapabilities: string[];
  permittedEffects: EffectiveProfileEffectClass[];
}
```

#### forbiddenCapabilities {#forbiddencapabilities}

```ts
forbiddenCapabilities: string[];
```

Explicitly forbidden capabilities\.

#### forbiddenEffects {#forbiddeneffects}

```ts
forbiddenEffects: EffectiveProfileEffectClass[];
```

Explicitly forbidden effect classes\.

#### kind {#kind-3}

```ts
kind: "capability-narrowing";
```

#### permittedCapabilities {#permittedcapabilities}

```ts
permittedCapabilities: string[];
```

Retained capabilities in owner\-provided order\.

#### permittedEffects {#permittedeffects}

```ts
permittedEffects: EffectiveProfileEffectClass[];
```

Retained effect classes\.

-----

### Type Literal {#type-literal-4}

```ts
{
  contributors: string[];
  forbiddenCapabilities: string[];
  forbiddenEffects: EffectiveProfileEffectClass[];
  kind: "governing-ceiling";
  permittedCapabilities: string[];
  permittedEffects: EffectiveProfileEffectClass[];
  policies: string[];
  scope: string;
  subjectResource: string;
}
```

#### contributors {#contributors}

```ts
contributors: string[];
```

Canonical contributors in owner\-provided order\.

#### forbiddenCapabilities {#forbiddencapabilities-1}

```ts
forbiddenCapabilities: string[];
```

Capabilities forbidden by the meet\.

#### forbiddenEffects {#forbiddeneffects-1}

```ts
forbiddenEffects: EffectiveProfileEffectClass[];
```

Effects forbidden by the meet\.

#### kind {#kind-4}

```ts
kind: "governing-ceiling";
```

#### permittedCapabilities {#permittedcapabilities-1}

```ts
permittedCapabilities: string[];
```

Capabilities retained by the meet\.

#### permittedEffects {#permittedeffects-1}

```ts
permittedEffects: EffectiveProfileEffectClass[];
```

Effects retained by the meet\.

#### policies {#policies}

```ts
policies: string[];
```

Exact policies whose bodies were met\.

#### scope {#scope}

```ts
scope: string;
```

Semantic scope of the meet\.

#### subjectResource {#subjectresource}

```ts
subjectResource: string;
```

Governed Package resource\.

-----

### Type Literal {#type-literal-5}

```ts
{
  accessCeiling: EffectiveProfileRepositoryAccess;
  kind: "repository";
  materializationOrder: number;
  repositoryId: string;
}
```

#### accessCeiling {#accessceiling}

```ts
accessCeiling: EffectiveProfileRepositoryAccess;
```

Admitted access ceiling, not effect authorization\.

#### kind {#kind-5}

```ts
kind: "repository";
```

#### materializationOrder {#materializationorder}

```ts
materializationOrder: number;
```

Zero\-based materialization order\.

#### repositoryId {#repositoryid}

```ts
repositoryId: string;
```

Logical repository identity\.

-----

### Type Literal {#type-literal-6}

```ts
{
  kind: "provider-repository";
  nativeRealization: EffectiveProfileNativeRealization;
  nativeRepositoryCoordinate: string;
  providerBindingId: string;
  repositoryId: string;
}
```

#### kind {#kind-6}

```ts
kind: "provider-repository";
```

#### nativeRealization {#nativerealization}

```ts
nativeRealization: EffectiveProfileNativeRealization;
```

Separately qualified native evidence\.

#### nativeRepositoryCoordinate {#nativerepositorycoordinate}

```ts
nativeRepositoryCoordinate: string;
```

Opaque native coordinate, not a local path assertion\.

#### providerBindingId {#providerbindingid}

```ts
providerBindingId: string;
```

Selected provider\-binding locator\.

#### repositoryId {#repositoryid-1}

```ts
repositoryId: string;
```

Logical repository identity\.

-----

### Type Literal {#type-literal-7}

```ts
{
  capabilityCeiling: string[];
  effectCeiling: EffectiveProfileEffectClass[];
  experiencePathId: string;
  kind: "execution-path";
  nativeRealization: EffectiveProfileNativeRealization;
  providerBindingIds: string[];
  reasonSteps: EffectiveProfilePathReason[];
  responsibilityContractIds: string[];
  responsibilityPathIdentity: string;
  selectionId: string;
  subject: WorkspaceSubjectValue;
  terminalProviderBinding:   | EffectiveProfileProviderBindingRef
     | null;
  workDelegationEdgeIds: string[];
}
```

#### capabilityCeiling {#capabilityceiling}

```ts
capabilityCeiling: string[];
```

Admitted capability ceiling\.

#### effectCeiling {#effectceiling}

```ts
effectCeiling: EffectiveProfileEffectClass[];
```

Admitted effect ceiling\.

#### experiencePathId {#experiencepathid}

```ts
experiencePathId: string;
```

Selected experience path\.

#### kind {#kind-7}

```ts
kind: "execution-path";
```

#### nativeRealization {#nativerealization-1}

```ts
nativeRealization: EffectiveProfileNativeRealization;
```

Separately qualified native evidence\.

#### providerBindingIds {#providerbindingids}

```ts
providerBindingIds: string[];
```

Explicit provider bindings required by this path\.

#### reasonSteps {#reasonsteps-1}

```ts
reasonSteps: EffectiveProfilePathReason[];
```

Ordered causal reasons\.

#### responsibilityContractIds {#responsibilitycontractids}

```ts
responsibilityContractIds: string[];
```

Consumed responsibility contracts in owner\-provided order\.

#### responsibilityPathIdentity {#responsibilitypathidentity}

```ts
responsibilityPathIdentity: string;
```

Exact responsibility\-path identity\.

#### selectionId {#selectionid}

```ts
selectionId: string;
```

Stable path selection identity\.

#### subject {#subject-1}

```ts
subject: WorkspaceSubjectValue;
```

Copied causal selector, not an admitted comparison handle\.

#### terminalProviderBinding {#terminalproviderbinding}

```ts
terminalProviderBinding: 
  | EffectiveProfileProviderBindingRef
  | null;
```

Exact terminal binding, or null for a path without a terminal leaf\.

#### workDelegationEdgeIds {#workdelegationedgeids}

```ts
workDelegationEdgeIds: string[];
```

Traversed neutral delegation edges\.

-----

### Type Literal {#type-literal-8}

```ts
{
  exposure: OperationExposure;
  kind: "operation";
  nativeRealization: EffectiveProfileNativeRealization;
  operationId: string;
  repositoryId: string;
}
```

#### exposure {#exposure}

```ts
exposure: OperationExposure;
```

Three\-state private exposure\.

#### kind {#kind-8}

```ts
kind: "operation";
```

#### nativeRealization {#nativerealization-2}

```ts
nativeRealization: EffectiveProfileNativeRealization;
```

Independent native evidence\.

#### operationId {#operationid}

```ts
operationId: string;
```

Owner\-qualified operation identity\.

#### repositoryId {#repositoryid-2}

```ts
repositoryId: string;
```

Owning logical repository\.

-----

### Type Literal {#type-literal-9}

```ts
{
  capabilityId: string;
  effectClass: EffectiveProfileEffectClass;
  kind: "capability";
  nativeRealization: EffectiveProfileNativeRealization;
  operationId: string;
  providerDisposition: EffectiveProfileProviderDisposition;
  repositoryId: string;
  requirementDisposition: RequirementDisposition;
  requirementId: string;
}
```

#### capabilityId {#capabilityid}

```ts
capabilityId: string;
```

Portable capability identity\.

#### effectClass {#effectclass}

```ts
effectClass: EffectiveProfileEffectClass;
```

Effect required by this occurrence\.

#### kind {#kind-9}

```ts
kind: "capability";
```

#### nativeRealization {#nativerealization-3}

```ts
nativeRealization: EffectiveProfileNativeRealization;
```

Independent native evidence\.

#### operationId {#operationid-1}

```ts
operationId: string;
```

Owner\-qualified operation identity\.

#### providerDisposition {#providerdisposition}

```ts
providerDisposition: EffectiveProfileProviderDisposition;
```

Private provider disposition\.

#### repositoryId {#repositoryid-3}

```ts
repositoryId: string;
```

Owning logical repository\.

#### requirementDisposition {#requirementdisposition}

```ts
requirementDisposition: RequirementDisposition;
```

Portable configuration disposition\.

#### requirementId {#requirementid}

```ts
requirementId: string;
```

Requirement identity local to the operation\.

-----

### Type Literal {#type-literal-10}

```ts
{
  kind: "machine-realization";
  machineId: string;
  realization: EffectiveProfileNativeRealization;
}
```

#### kind {#kind-10}

```ts
kind: "machine-realization";
```

#### machineId {#machineid}

```ts
machineId: string;
```

Selected machine\-binding identity\.

#### realization {#realization}

```ts
realization: EffectiveProfileNativeRealization;
```

Machine\-specific native evidence\.

-----

### Type Literal {#type-literal-11}

```ts
{
  finding: EffectiveProfileFinding;
  kind: "finding";
}
```

#### finding {#finding}

```ts
finding: EffectiveProfileFinding;
```

Exact finding value\.

#### kind {#kind-11}

```ts
kind: "finding";
```
