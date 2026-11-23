---
title: "Class: Pale"
---

<a id="class&#45;pale"></a>

Native PaleJS handle over the complete eligible Pale façade\.

## Constructors {#constructors}

### Constructor {#constructor}

```ts
new Pale(): Pale;
```

Verify embedded contracts and construct the native façade\.

# Errors {#errors}

Returns the stable initialization code and message when the embedded
contract bundle contradicts the compiled façade\.

#### Returns {#returns}

`Pale`

## Accessors {#accessors}

### capabilityIds {#capabilityids}

#### Get Signature {#get-signature}

```ts
get capabilityIds(): string[];
```

Return the API\-owned Node eligibility set in stable order\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`\[\]

## Methods {#methods}

### admitDiagnostic\(\) {#admitdiagnostic}

```ts
admitDiagnostic(bytes: Buffer): Buffer;
```

Admit canonical `diagnostic.v1` bytes and return the same bytes\.

# Errors {#errors-1}

Returns a native error with separate `diagnostic` bytes when the input
is not the canonical initial\-v1 diagnostic contract\.

#### Parameters {#parameters}

<Heading level={5} id="bytes" className="scroll-mt-(--scroll-mt)">bytes</Heading>

`Buffer`

#### Returns {#returns-2}

`Buffer`

-----

### admitLocalMaterializationRun\(\) {#admitlocalmaterializationrun}

```ts
admitLocalMaterializationRun(compilation: LocalOneShotCompilation, request: LocalMaterializationAdmissionRequest): LocalMaterializationAdmittedRun;
```

Admit saved plans and target effects without writing\.

# Errors {#errors-2}

Returns a native error with separate `diagnostic` bytes when directory
spelling, saved\-plan equality, observations, or Git\-local preparation fails\.

#### Parameters {#parameters-1}

<Heading level={5} id="compilation" className="scroll-mt-(--scroll-mt)">compilation</Heading>

[`LocalOneShotCompilation`](/pale/reference/js/classes/LocalOneShotCompilation)

<Heading level={5} id="request" className="scroll-mt-(--scroll-mt)">request</Heading>

[`LocalMaterializationAdmissionRequest`](/pale/reference/js/interfaces/LocalMaterializationAdmissionRequest)

#### Returns {#returns-3}

[`LocalMaterializationAdmittedRun`](/pale/reference/js/classes/LocalMaterializationAdmittedRun)

-----

### admitOneShotSavedPlan\(\) {#admitoneshotsavedplan}

```ts
admitOneShotSavedPlan(rebuilt: OneShotBoundPlan, savedBytes: Buffer): OneShotAdmittedPlan;
```

Admit saved bytes against one freshly rebuilt bound plan\.

Exact equality and plan identity remain API\-owned\. Success creates an
admission proof only; it performs no filesystem mutation\.

# Errors {#errors-3}

Returns a host\-shape error if the bound plan was already consumed, or a
native error with separate `diagnostic` bytes when saved\-plan admission
rejects the supplied bytes\.

#### Parameters {#parameters-2}

<Heading level={5} id="rebuilt" className="scroll-mt-(--scroll-mt)">rebuilt</Heading>

[`OneShotBoundPlan`](/pale/reference/js/classes/OneShotBoundPlan)

<Heading level={5} id="savedbytes" className="scroll-mt-(--scroll-mt)">savedBytes</Heading>

`Buffer`

#### Returns {#returns-4}

[`OneShotAdmittedPlan`](/pale/reference/js/interfaces/OneShotAdmittedPlan)

-----

### admitRepositoryNativeActions\(\) {#admitrepositorynativeactions}

```ts
admitRepositoryNativeActions(
   bytes: Buffer, 
   profileDigest: string, 
   instanceDigest: string, 
   repositoryId: string
): AdmittedRepositoryActions;
```

Admit one repository\-bound pure\-action catalog\.

# Errors {#errors-4}

Returns a native error with separate `diagnostic` bytes when catalog,
context, ordering, or registry parity fails admission\.

#### Parameters {#parameters-3}

<Heading level={5} id="bytes&#45;1" className="scroll-mt-(--scroll-mt)">bytes</Heading>

`Buffer`

<Heading level={5} id="profiledigest" className="scroll-mt-(--scroll-mt)">profileDigest</Heading>

`string`

<Heading level={5} id="instancedigest" className="scroll-mt-(--scroll-mt)">instanceDigest</Heading>

`string`

<Heading level={5} id="repositoryid" className="scroll-mt-(--scroll-mt)">repositoryId</Heading>

`string`

#### Returns {#returns-5}

[`AdmittedRepositoryActions`](/pale/reference/js/classes/AdmittedRepositoryActions)

-----

### admitResidentHook\(\) {#admitresidenthook}

```ts
admitResidentHook(request: ResidentHookRequest): ResidentHookAdmission;
```

Admit one repository\-hook request without selecting or invoking a carrier\.

# Errors {#errors-5}

Returns a native error with separate `diagnostic` bytes when routing,
identity, lifecycle\-event, provider\-binding, or payload admission fails\.

#### Parameters {#parameters-4}

<Heading level={5} id="request&#45;1" className="scroll-mt-(--scroll-mt)">request</Heading>

[`ResidentHookRequest`](/pale/reference/js/interfaces/ResidentHookRequest)

#### Returns {#returns-6}

[`ResidentHookAdmission`](/pale/reference/js/classes/ResidentHookAdmission)

-----

### authoringIngressLimits\(\) {#authoringingresslimits}

```ts
authoringIngressLimits(sourceClass: AuthoringIngressClass): AuthoringIngressLimits;
```

Return the application\-owned capture ceilings for one source class\.

# Errors {#errors-6}

Returns an internal projection error if the API document\-count ceiling
cannot be represented by the Node `uint32` ABI\.

#### Parameters {#parameters-5}

<Heading level={5} id="sourceclass" className="scroll-mt-(--scroll-mt)">sourceClass</Heading>

[`AuthoringIngressClass`](/pale/reference/js/enumerations/AuthoringIngressClass)

#### Returns {#returns-7}

[`AuthoringIngressLimits`](/pale/reference/js/interfaces/AuthoringIngressLimits)

-----

### bindOneShotMachineEffects\(\) {#bindoneshotmachineeffects}

```ts
bindOneShotMachineEffects(candidate: OneShotPlanCandidate, effects: Buffer<ArrayBufferLike>[]): OneShotBoundPlan;
```

Bind canonical machine\-local effect candidates into one complete plan\.

The API consumes `candidate` once and owns validation and deterministic
ordering\. This method performs no host observation or native effect\.

# Errors {#errors-7}

Returns a host\-shape error if the candidate was already consumed, or a
native error with separate `diagnostic` bytes when API admission rejects
a supplied machine\-local effect\.

#### Parameters {#parameters-6}

<Heading level={5} id="candidate" className="scroll-mt-(--scroll-mt)">candidate</Heading>

[`OneShotPlanCandidate`](/pale/reference/js/classes/OneShotPlanCandidate)

<Heading level={5} id="effects" className="scroll-mt-(--scroll-mt)">effects</Heading>

`Buffer`\<`ArrayBufferLike`\>\[\]

#### Returns {#returns-8}

[`OneShotBoundPlan`](/pale/reference/js/classes/OneShotBoundPlan)

-----

### captureLocalNativeActionRequest\(\) {#capturelocalnativeactionrequest}

```ts
captureLocalNativeActionRequest(request: LocalNativeActionInputRequest): CapturedNativeActionRequest;
```

Read one confined local file into a path\-free action request\.

# Errors {#errors-8}

Returns a native error with separate `diagnostic` bytes when the root,
confined relative path, file type, or byte ceiling is rejected\.

#### Parameters {#parameters-7}

<Heading level={5} id="request&#45;2" className="scroll-mt-(--scroll-mt)">request</Heading>

[`LocalNativeActionInputRequest`](/pale/reference/js/interfaces/LocalNativeActionInputRequest)

#### Returns {#returns-9}

[`CapturedNativeActionRequest`](/pale/reference/js/classes/CapturedNativeActionRequest)

-----

### commitConfigurationImprovementPreview\(\) {#commitconfigurationimprovementpreview}

```ts
commitConfigurationImprovementPreview(explanation: ConfigurationImprovementExplanation, prepared: PreparedConfigurationImprovementPreview): ConfigurationImprovementPreview;
```

Consume a prepared preview and the exact explanation that prepared it\.

# Errors {#errors-9}

Consumed host arguments are rejected before either remaining handle is
taken\. The API rejects equal\-coordinate but foreign explanation owners;
once called, both inputs are consumed even when that check fails\.

#### Parameters {#parameters-8}

<Heading level={5} id="explanation" className="scroll-mt-(--scroll-mt)">explanation</Heading>

[`ConfigurationImprovementExplanation`](/pale/reference/js/classes/ConfigurationImprovementExplanation)

<Heading level={5} id="prepared" className="scroll-mt-(--scroll-mt)">prepared</Heading>

[`PreparedConfigurationImprovementPreview`](/pale/reference/js/classes/PreparedConfigurationImprovementPreview)

#### Returns {#returns-10}

[`ConfigurationImprovementPreview`](/pale/reference/js/classes/ConfigurationImprovementPreview)

-----

### comparePortableWorkspaces\(\) {#compareportableworkspaces}

```ts
comparePortableWorkspaces(prior: PortableWorkspaceCompilation, current: PortableWorkspaceCompilation): WorkspaceComparison;
```

Compare two admitted portable workspace handles\.

# Errors {#errors-10}

Returns a native error with separate `diagnostic` bytes when the
workspaces cannot form one valid comparison coordinate\.

#### Parameters {#parameters-9}

<Heading level={5} id="prior" className="scroll-mt-(--scroll-mt)">prior</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="current" className="scroll-mt-(--scroll-mt)">current</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-11}

[`WorkspaceComparison`](/pale/reference/js/classes/WorkspaceComparison)

-----

### compiledInterfaceIdentity\(\) {#compiledinterfaceidentity}

```ts
compiledInterfaceIdentity(): CompiledInterfaceIdentity;
```

Report compiled SDK and interface claims without reading an executable\.

The record establishes neither executable\-byte identity nor resident state\.

# Errors {#errors-11}

Returns a native error with separate `diagnostic` bytes if the embedded
runtime schema or canonical record is incoherent\.

#### Returns {#returns-12}

[`CompiledInterfaceIdentity`](/pale/reference/js/interfaces/CompiledInterfaceIdentity)

-----

### compileEffectiveProfile\(\) {#compileeffectiveprofile}

```ts
compileEffectiveProfile(workspace: PortableWorkspaceCompilation, request: EffectiveProfileCompilationRequest): EffectiveProfileCompilation;
```

Compile one selected effective profile over an admitted workspace\.

# Errors {#errors-12}

Returns a native `Error` whose message is the canonical diagnostic
summary and whose `diagnostic` property carries exact structured bytes\.

#### Parameters {#parameters-10}

<Heading level={5} id="workspace" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="request&#45;3" className="scroll-mt-(--scroll-mt)">request</Heading>

[`EffectiveProfileCompilationRequest`](/pale/reference/js/interfaces/EffectiveProfileCompilationRequest)

#### Returns {#returns-13}

[`EffectiveProfileCompilation`](/pale/reference/js/classes/EffectiveProfileCompilation)

-----

### compileLocalOneShot\(\) {#compilelocaloneshot}

```ts
compileLocalOneShot(request: LocalOneShotCompilationRequest): LocalOneShotCompilation;
```

Resolve, stably capture, and compile one local workspace selection\.

# Errors {#errors-13}

Returns a native error with separate `diagnostic` bytes when the host
locator, source capture, selectors, or canonical compiler rejects input\.

#### Parameters {#parameters-11}

<Heading level={5} id="request&#45;4" className="scroll-mt-(--scroll-mt)">request</Heading>

[`LocalOneShotCompilationRequest`](/pale/reference/js/interfaces/LocalOneShotCompilationRequest)

#### Returns {#returns-14}

[`LocalOneShotCompilation`](/pale/reference/js/classes/LocalOneShotCompilation)

-----

### compileOneShot\(\) {#compileoneshot}

```ts
compileOneShot(request: OneShotCompilationRequest): Promise<OneShotCompilation>;
```

Compile captured sources on the Node\-API worker pool, returning a promise\.

All source buffers are copied into owned API inputs before this call
returns\. Mutating or collecting the caller's buffers or façade cannot
change the queued compilation\. Admission and rendering run off the
JavaScript thread; only result/diagnostic projection returns to it\.

# Errors {#errors-14}

Rejects the promise with the canonical API diagnostic when captured
source or context fails admission\. Host argument decoding or queue
submission may fail before work starts\. No abort mechanism is exposed\.

#### Parameters {#parameters-12}

<Heading level={5} id="request&#45;5" className="scroll-mt-(--scroll-mt)">request</Heading>

[`OneShotCompilationRequest`](/pale/reference/js/interfaces/OneShotCompilationRequest)

#### Returns {#returns-15}

`Promise`\<[`OneShotCompilation`](/pale/reference/js/classes/OneShotCompilation)\>

-----

### compilePortableWorkspace\(\) {#compileportableworkspace}

```ts
compilePortableWorkspace(request: PortableWorkspaceRequest): PortableWorkspaceCompilation;
```

Compile one path\-free workspace source batch\.

# Errors {#errors-15}

Returns a native error with separate `diagnostic` bytes when source or
workspace meaning fails API\-owned admission\.

#### Parameters {#parameters-13}

<Heading level={5} id="request&#45;6" className="scroll-mt-(--scroll-mt)">request</Heading>

[`PortableWorkspaceRequest`](/pale/reference/js/interfaces/PortableWorkspaceRequest)

#### Returns {#returns-16}

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

-----

### contractBundleIdentity\(\) {#contractbundleidentity}

```ts
contractBundleIdentity(): ContractBundleIdentity;
```

Inspect the complete embedded public\-contract bundle coordinate\.

#### Returns {#returns-17}

[`ContractBundleIdentity`](/pale/reference/js/interfaces/ContractBundleIdentity)

-----

### contractSchema\(\) {#contractschema}

```ts
contractSchema(schemaId: string): ContractSchema;
```

Look up one façade\-selected generated schema\.

# Errors {#errors-16}

Returns a native error with the canonical summary and separate
`diagnostic` bytes when the identity is not selected\.

#### Parameters {#parameters-14}

<Heading level={5} id="schemaid" className="scroll-mt-(--scroll-mt)">schemaId</Heading>

`string`

#### Returns {#returns-18}

[`ContractSchema`](/pale/reference/js/interfaces/ContractSchema)

-----

### diagnoseConfigurationImprovement\(\) {#diagnoseconfigurationimprovement}

```ts
diagnoseConfigurationImprovement(stage: ConfigurationImprovementEvaluation): ConfigurationImprovementDiagnosis;
```

Derive the canonical change\-root and impact proof\.

# Errors {#errors-17}

Returns consumed\-handle misuse or the API\-owned rejection diagnostic\.
The input stage is consumed on both success and API rejection\.

#### Parameters {#parameters-15}

<Heading level={5} id="stage" className="scroll-mt-(--scroll-mt)">stage</Heading>

[`ConfigurationImprovementEvaluation`](/pale/reference/js/classes/ConfigurationImprovementEvaluation)

#### Returns {#returns-19}

[`ConfigurationImprovementDiagnosis`](/pale/reference/js/classes/ConfigurationImprovementDiagnosis)

-----

### evaluateConfigurationImprovement\(\) {#evaluateconfigurationimprovement}

```ts
evaluateConfigurationImprovement(stage: ConfigurationImprovementProposal): ConfigurationImprovementEvaluation;
```

Admit the captured candidate through the canonical compiler\.

# Errors {#errors-18}

Returns consumed\-handle misuse or the API\-owned rejection diagnostic\.
The input stage is consumed on both success and API rejection\.

#### Parameters {#parameters-16}

<Heading level={5} id="stage&#45;1" className="scroll-mt-(--scroll-mt)">stage</Heading>

[`ConfigurationImprovementProposal`](/pale/reference/js/classes/ConfigurationImprovementProposal)

#### Returns {#returns-20}

[`ConfigurationImprovementEvaluation`](/pale/reference/js/classes/ConfigurationImprovementEvaluation)

-----

### explainConfigurationImprovement\(\) {#explainconfigurationimprovement}

```ts
explainConfigurationImprovement(inspection: ConfigurationImprovementInspection, profile: EffectiveProfileCompilation): ConfigurationImprovementExplanation;
```

Consume inspection and bind its exact effective\-profile explanation\.

# Errors {#errors-19}

Returns a host error for consumed custody or the canonical API
diagnostic for a different admitted frontier\. Inspection is consumed\.

#### Parameters {#parameters-17}

<Heading level={5} id="inspection" className="scroll-mt-(--scroll-mt)">inspection</Heading>

[`ConfigurationImprovementInspection`](/pale/reference/js/classes/ConfigurationImprovementInspection)

<Heading level={5} id="profile" className="scroll-mt-(--scroll-mt)">profile</Heading>

[`EffectiveProfileCompilation`](/pale/reference/js/classes/EffectiveProfileCompilation)

#### Returns {#returns-21}

[`ConfigurationImprovementExplanation`](/pale/reference/js/classes/ConfigurationImprovementExplanation)

-----

### inspectConfigurationImprovement\(\) {#inspectconfigurationimprovement}

```ts
inspectConfigurationImprovement(baseline: PortableWorkspaceCompilation): ConfigurationImprovementInspection;
```

Capture one admitted baseline without compiling or mutating it\.

#### Parameters {#parameters-18}

<Heading level={5} id="baseline" className="scroll-mt-(--scroll-mt)">baseline</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-22}

[`ConfigurationImprovementInspection`](/pale/reference/js/classes/ConfigurationImprovementInspection)

-----

### inspectLocalControlStore\(\) {#inspectlocalcontrolstore}

```ts
inspectLocalControlStore(request: LocalControlStorageInspectionRequest): LocalControlStorageInspection;
```

Classify an exact local control store without creation, repair or sidecars\.

This synchronous native call returns physical facts, not a resident
status, writer admission, or runtime\-readiness report\.

# Errors {#errors-20}

Throws the canonical API diagnostic for invalid coordinates, unsafe
confinement or host inspection failure\. Persistent byte contradictions
instead produce \[`LocalControlStorageStateKind::Rejected`\]\.

#### Parameters {#parameters-19}

<Heading level={5} id="request&#45;7" className="scroll-mt-(--scroll-mt)">request</Heading>

[`LocalControlStorageInspectionRequest`](/pale/reference/js/classes/LocalControlStorageInspectionRequest)

#### Returns {#returns-23}

[`LocalControlStorageInspection`](/pale/reference/js/classes/LocalControlStorageInspection)

-----

### inspectLocalMaterializationReconciliation\(\) {#inspectlocalmaterializationreconciliation}

```ts
inspectLocalMaterializationReconciliation(run: LocalMaterializationAdmittedRun): LocalMaterializationReconciliation;
```

Inspect bounded read\-back after an outcome\-unknown settlement\.

# Errors {#errors-21}

Returns a native error with separate `diagnostic` bytes when the run is
not unknown or retained receipt/ownership evidence cannot be observed\.

#### Parameters {#parameters-20}

<Heading level={5} id="run" className="scroll-mt-(--scroll-mt)">run</Heading>

[`LocalMaterializationAdmittedRun`](/pale/reference/js/classes/LocalMaterializationAdmittedRun)

#### Returns {#returns-24}

[`LocalMaterializationReconciliation`](/pale/reference/js/interfaces/LocalMaterializationReconciliation)

-----

### inspectLocalPackageDistribution\(\) {#inspectlocalpackagedistribution}

```ts
inspectLocalPackageDistribution(request: LocalPackageDistributionRequest): PackageDistributionInspection;
```

Inspect Package releases selected by one local workspace entry\.

# Errors {#errors-22}

Returns a native error with separate `diagnostic` bytes when local
selection, bounded Package capture, or Package admission fails\.

#### Parameters {#parameters-21}

<Heading level={5} id="request&#45;8" className="scroll-mt-(--scroll-mt)">request</Heading>

[`LocalPackageDistributionRequest`](/pale/reference/js/interfaces/LocalPackageDistributionRequest)

#### Returns {#returns-25}

[`PackageDistributionInspection`](/pale/reference/js/interfaces/PackageDistributionInspection)

-----

### inspectLocalRepositoryStatus\(\) {#inspectlocalrepositorystatus}

```ts
inspectLocalRepositoryStatus(compilation: LocalOneShotCompilation, repositoryId: string): LocalRepositoryStatus;
```

Compare one local repository with its admitted desired projection\.

# Errors {#errors-23}

Returns a native error with separate `diagnostic` bytes when selection,
lineage, baseline, Git authority, or comparison admission fails\.

#### Parameters {#parameters-22}

<Heading level={5} id="compilation&#45;1" className="scroll-mt-(--scroll-mt)">compilation</Heading>

[`LocalOneShotCompilation`](/pale/reference/js/classes/LocalOneShotCompilation)

<Heading level={5} id="repositoryid&#45;1" className="scroll-mt-(--scroll-mt)">repositoryId</Heading>

`string`

#### Returns {#returns-26}

[`LocalRepositoryStatus`](/pale/reference/js/interfaces/LocalRepositoryStatus)

-----

### inspectPackageDistribution\(\) {#inspectpackagedistribution}

```ts
inspectPackageDistribution(documents: CompilationDocument[]): PackageDistributionInspection;
```

Inspect captured Package release coordinates without reading a lock\.

# Errors {#errors-24}

Returns a native error with separate `diagnostic` bytes when logical
labels, finite source bounds, manifests, or source inventories fail the
API\-owned Package admission path\.

#### Parameters {#parameters-23}

<Heading level={5} id="documents" className="scroll-mt-(--scroll-mt)">documents</Heading>

[`CompilationDocument`](/pale/reference/js/interfaces/CompilationDocument)\[\]

#### Returns {#returns-27}

[`PackageDistributionInspection`](/pale/reference/js/interfaces/PackageDistributionInspection)

-----

### inspectPortableWorkspaceAuthoring\(\) {#inspectportableworkspaceauthoring}

```ts
inspectPortableWorkspaceAuthoring(
   workspace: PortableWorkspaceCompilation, 
   sourceLabel: string, 
   path: AuthoringPathSegment[]
): AuthoringInspection;
```

Inspect generated grammar facts retained by an admitted workspace\.

# Errors {#errors-25}

Returns a native `Error` carrying the API\-owned canonical diagnostic for
an oversized path or incoherent generated authoring metadata\.

#### Parameters {#parameters-24}

<Heading level={5} id="workspace&#45;1" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="sourcelabel" className="scroll-mt-(--scroll-mt)">sourceLabel</Heading>

`string`

<Heading level={5} id="path" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringPathSegment`](/pale/reference/js/classes/AuthoringPathSegment)\[\]

#### Returns {#returns-28}

[`AuthoringInspection`](/pale/reference/js/interfaces/AuthoringInspection)

-----

### inspectStandaloneAuthoring\(\) {#inspectstandaloneauthoring}

```ts
inspectStandaloneAuthoring(role: StandaloneAuthoringRole, path: AuthoringPathSegment[]): AuthoringInspection;
```

Inspect generated grammar facts for one standalone authoring role\.

# Errors {#errors-26}

Returns a native `Error` carrying the API\-owned canonical diagnostic for
an oversized path or incoherent generated authoring metadata\.

#### Parameters {#parameters-25}

<Heading level={5} id="role" className="scroll-mt-(--scroll-mt)">role</Heading>

[`StandaloneAuthoringRole`](/pale/reference/js/enumerations/StandaloneAuthoringRole)

<Heading level={5} id="path&#45;1" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringPathSegment`](/pale/reference/js/classes/AuthoringPathSegment)\[\]

#### Returns {#returns-29}

[`AuthoringInspection`](/pale/reference/js/interfaces/AuthoringInspection)

-----

### invokeCapturedNativeAction\(\) {#invokecapturednativeaction}

```ts
invokeCapturedNativeAction(request: CapturedNativeActionRequest): Buffer;
```

Invoke one captured request through the same pure native\-action owner\.

# Errors {#errors-27}

Returns a native error with separate `diagnostic` bytes when the action,
tagged input, or pure execution fails API\-owned admission\.

#### Parameters {#parameters-26}

<Heading level={5} id="request&#45;9" className="scroll-mt-(--scroll-mt)">request</Heading>

[`CapturedNativeActionRequest`](/pale/reference/js/classes/CapturedNativeActionRequest)

#### Returns {#returns-30}

`Buffer`

-----

### invokeNativeAction\(\) {#invokenativeaction}

```ts
invokeNativeAction(actionId: string, input: Buffer): Buffer;
```

Execute one complete tagged effect\-free native action\.

# Errors {#errors-28}

Returns a native error with separate `diagnostic` bytes when the tagged
request fails admission or pure execution\.

#### Parameters {#parameters-27}

<Heading level={5} id="actionid" className="scroll-mt-(--scroll-mt)">actionId</Heading>

`string`

<Heading level={5} id="input" className="scroll-mt-(--scroll-mt)">input</Heading>

`Buffer`

#### Returns {#returns-31}

`Buffer`

-----

### invokeNativeActionPayload\(\) {#invokenativeactionpayload}

```ts
invokeNativeActionPayload(actionId: string, payload: Buffer): Buffer;
```

Execute one carrier\-selected effect\-free native\-action payload\.

# Errors {#errors-29}

Returns a native error with separate `diagnostic` bytes when the action,
payload, or pure execution fails API\-owned admission\.

#### Parameters {#parameters-28}

<Heading level={5} id="actionid&#45;1" className="scroll-mt-(--scroll-mt)">actionId</Heading>

`string`

<Heading level={5} id="payload" className="scroll-mt-(--scroll-mt)">payload</Heading>

`Buffer`

#### Returns {#returns-32}

`Buffer`

-----

### nativeActionCatalog\(\) {#nativeactioncatalog}

```ts
nativeActionCatalog(): NativeActionDescriptor[];
```

Return the complete effect\-free native\-action descriptor batch\.

# Errors {#errors-30}

Returns a native error with separate `diagnostic` bytes if the compiled
registry contradicts its generated action contracts\.

#### Returns {#returns-33}

[`NativeActionDescriptor`](/pale/reference/js/classes/NativeActionDescriptor)\[\]

-----

### navigatePortableWorkspaceAuthoring\(\) {#navigateportableworkspaceauthoring}

```ts
navigatePortableWorkspaceAuthoring(
   workspace: PortableWorkspaceCompilation, 
   sourceLabel: string, 
   path: AuthoringInstancePathSegment[]
): AuthoringNavigation;
```

Resolve one exact source occurrence retained by an admitted workspace\.

#### Parameters {#parameters-29}

<Heading level={5} id="workspace&#45;2" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="sourcelabel&#45;1" className="scroll-mt-(--scroll-mt)">sourceLabel</Heading>

`string`

<Heading level={5} id="path&#45;2" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringInstancePathSegment`](/pale/reference/js/classes/AuthoringInstancePathSegment)\[\]

#### Returns {#returns-34}

[`AuthoringNavigation`](/pale/reference/js/classes/AuthoringNavigation)

-----

### observeEffectiveProfile\(\) {#observeeffectiveprofile}

```ts
observeEffectiveProfile(compilation: EffectiveProfileCompilation): ObservationSnapshot;
```

Project an admitted effective profile into a source\-free snapshot\.

#### Parameters {#parameters-30}

<Heading level={5} id="compilation&#45;2" className="scroll-mt-(--scroll-mt)">compilation</Heading>

[`EffectiveProfileCompilation`](/pale/reference/js/classes/EffectiveProfileCompilation)

#### Returns {#returns-35}

[`ObservationSnapshot`](/pale/reference/js/classes/ObservationSnapshot)

-----

### oneShotObservationTargets\(\) {#oneshotobservationtargets}

```ts
oneShotObservationTargets(compilation: OneShotCompilation, request: OneShotObservationRequest): string[];
```

Derive the exact target set a host must observe before pure planning\.

# Errors {#errors-31}

Returns a native error with separate `diagnostic` bytes when the
repository, plan kind, or claimed prior state is invalid\.

#### Parameters {#parameters-31}

<Heading level={5} id="compilation&#45;3" className="scroll-mt-(--scroll-mt)">compilation</Heading>

[`OneShotCompilation`](/pale/reference/js/classes/OneShotCompilation)

<Heading level={5} id="request&#45;10" className="scroll-mt-(--scroll-mt)">request</Heading>

[`OneShotObservationRequest`](/pale/reference/js/classes/OneShotObservationRequest)

#### Returns {#returns-36}

`string`\[\]

-----

### oneShotSummary\(\) {#oneshotsummary}

```ts
oneShotSummary(compilation: OneShotCompilation): OneShotSummary;
```

Return the flat binding\-safe summary of one admitted compilation\.

#### Parameters {#parameters-32}

<Heading level={5} id="compilation&#45;4" className="scroll-mt-(--scroll-mt)">compilation</Heading>

[`OneShotCompilation`](/pale/reference/js/classes/OneShotCompilation)

#### Returns {#returns-37}

[`OneShotSummary`](/pale/reference/js/interfaces/OneShotSummary)

-----

### planLocalOneShot\(\) {#planlocaloneshot}

```ts
planLocalOneShot(compilation: LocalOneShotCompilation, request: LocalOneShotPlanRequest): LocalOneShotPlan;
```

Reconstruct one complete local plan from trusted observations\.

# Errors {#errors-32}

Returns a native error with separate `diagnostic` bytes when repository,
lineage, baseline, Git authority, or plan admission fails\.

#### Parameters {#parameters-33}

<Heading level={5} id="compilation&#45;5" className="scroll-mt-(--scroll-mt)">compilation</Heading>

[`LocalOneShotCompilation`](/pale/reference/js/classes/LocalOneShotCompilation)

<Heading level={5} id="request&#45;11" className="scroll-mt-(--scroll-mt)">request</Heading>

[`LocalOneShotPlanRequest`](/pale/reference/js/interfaces/LocalOneShotPlanRequest)

#### Returns {#returns-38}

[`LocalOneShotPlan`](/pale/reference/js/classes/LocalOneShotPlan)

-----

### planOneShot\(\) {#planoneshot}

```ts
planOneShot(compilation: OneShotCompilation, request: OneShotPlanningRequest): OneShotPlanCandidate;
```

Construct one deterministic plan candidate without host effects\.

# Errors {#errors-33}

Returns a host\-shape error for an incomplete baseline tuple, or a native
error with separate `diagnostic` bytes when planning rejects the claim\.

#### Parameters {#parameters-34}

<Heading level={5} id="compilation&#45;6" className="scroll-mt-(--scroll-mt)">compilation</Heading>

[`OneShotCompilation`](/pale/reference/js/classes/OneShotCompilation)

<Heading level={5} id="request&#45;12" className="scroll-mt-(--scroll-mt)">request</Heading>

[`OneShotPlanningRequest`](/pale/reference/js/classes/OneShotPlanningRequest)

#### Returns {#returns-39}

[`OneShotPlanCandidate`](/pale/reference/js/classes/OneShotPlanCandidate)

-----

### portableWorkspaceAuthoringOccurrences\(\) {#portableworkspaceauthoringoccurrences}

```ts
portableWorkspaceAuthoringOccurrences(
   workspace: PortableWorkspaceCompilation, 
   identity: AuthoringIdentity, 
   maximumInspected: number, 
   maximumReturned: number, 
   after?: 
  | AuthoringOccurrencePageCursor
  | null
): AuthoringOccurrencePage;
```

Find occurrences of a compiler\-produced identity without recompiling\.

Limits must be integers from 0 through 65535\. Zero selects 64 and values
above 256 are capped by the SDK\. Resume with the same raw limits and
identity on this exact workspace\. An empty page can still continue\.

# Errors {#errors-34}

Invalid numeric inputs produce `InvalidArg`\. An unlike continuation
produces an error carrying the canonical API diagnostic\.

#### Parameters {#parameters-35}

<Heading level={5} id="workspace&#45;3" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="identity" className="scroll-mt-(--scroll-mt)">identity</Heading>

[`AuthoringIdentity`](/pale/reference/js/classes/AuthoringIdentity)

<Heading level={5} id="maximuminspected" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="after" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`AuthoringOccurrencePageCursor`](/pale/reference/js/classes/AuthoringOccurrencePageCursor)
\| `null`

#### Returns {#returns-40}

[`AuthoringOccurrencePage`](/pale/reference/js/classes/AuthoringOccurrencePage)

-----

### portableWorkspaceSourceSubject\(\) {#portableworkspacesourcesubject}

```ts
portableWorkspaceSourceSubject(
   workspace: PortableWorkspaceCompilation, 
   sourceLabel: string, 
   path: AuthoringInstancePathSegment[]
): PortableWorkspaceSourceInspection;
```

Read the subject directly named at one captured source location\.

The result retains this compilation even when the subject is unselected\.
It does not follow proof inputs or turn nearby names into record anchors\.

# Errors {#errors-35}

Returns the canonical API diagnostic when the path exceeds 64 segments\.

#### Parameters {#parameters-36}

<Heading level={5} id="workspace&#45;4" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="sourcelabel&#45;2" className="scroll-mt-(--scroll-mt)">sourceLabel</Heading>

`string`

<Heading level={5} id="path&#45;3" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringInstancePathSegment`](/pale/reference/js/classes/AuthoringInstancePathSegment)\[\]

#### Returns {#returns-41}

[`PortableWorkspaceSourceInspection`](/pale/reference/js/classes/PortableWorkspaceSourceInspection)

-----

### portableWorkspaceSubjectOccurrences\(\) {#portableworkspacesubjectoccurrences}

```ts
portableWorkspaceSubjectOccurrences(
   workspace: PortableWorkspaceCompilation, 
   subject: WorkspaceSubject, 
   maximumInspected: number, 
   maximumReturned: number, 
   after?: 
  | AuthoringOccurrencePageCursor
  | null
): PortableWorkspaceSubjectOccurrences;
```

Find direct named occurrences of a full proof subject without recompiling\.

Limits must be integers from 0 through 65535\. Zero selects 64; the SDK
caps values above 256\. Resume on this compilation with the same subject
and raw limits\. Identity\-query cursors cannot resume a subject query\.
Limits count examined and returned rows, not bytes, time or retained
memory\. This supplied\-input query does not authorize source disclosure\.

# Errors {#errors-36}

Invalid numbers produce `InvalidArg`\. An unlike continuation produces
an error carrying the canonical API diagnostic before the scan begins\.

#### Parameters {#parameters-37}

<Heading level={5} id="workspace&#45;5" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="subject" className="scroll-mt-(--scroll-mt)">subject</Heading>

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)

<Heading level={5} id="maximuminspected&#45;1" className="scroll-mt-(--scroll-mt)">maximumInspected</Heading>

`number`

<Heading level={5} id="maximumreturned&#45;1" className="scroll-mt-(--scroll-mt)">maximumReturned</Heading>

`number`

<Heading level={5} id="after&#45;1" className="scroll-mt-(--scroll-mt)">after?</Heading>

\| [`AuthoringOccurrencePageCursor`](/pale/reference/js/classes/AuthoringOccurrencePageCursor)
\| `null`

#### Returns {#returns-42}

[`PortableWorkspaceSubjectOccurrences`](/pale/reference/js/classes/PortableWorkspaceSubjectOccurrences)

-----

### prepareConfigurationImprovementPreview\(\) {#prepareconfigurationimprovementpreview}

```ts
prepareConfigurationImprovementPreview(
   explanation: ConfigurationImprovementExplanation, 
   candidate: PortableWorkspaceCompilation, 
   request: ConfigurationImprovementCandidateRequest
): PreparedConfigurationImprovementPreview;
```

Prepare from an already admitted candidate while borrowing explanation\.

# Errors {#errors-37}

Returns consumed\-handle misuse or the exact API preparation diagnostic\.
Every preparation failure leaves the explanation available for retry\.

#### Parameters {#parameters-38}

<Heading level={5} id="explanation&#45;1" className="scroll-mt-(--scroll-mt)">explanation</Heading>

[`ConfigurationImprovementExplanation`](/pale/reference/js/classes/ConfigurationImprovementExplanation)

<Heading level={5} id="candidate&#45;1" className="scroll-mt-(--scroll-mt)">candidate</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

<Heading level={5} id="request&#45;13" className="scroll-mt-(--scroll-mt)">request</Heading>

[`ConfigurationImprovementCandidateRequest`](/pale/reference/js/interfaces/ConfigurationImprovementCandidateRequest)

#### Returns {#returns-43}

[`PreparedConfigurationImprovementPreview`](/pale/reference/js/classes/PreparedConfigurationImprovementPreview)

-----

### previewConfigurationImprovement\(\) {#previewconfigurationimprovement}

```ts
previewConfigurationImprovement(stage: ConfigurationImprovementDiagnosis): ConfigurationImprovementPreview;
```

Freeze the diagnosed candidate for explicit effect\-free review\.

# Errors {#errors-38}

Returns consumed\-handle misuse or the API\-owned rejection diagnostic\.
The input stage is consumed on both success and API rejection\.

#### Parameters {#parameters-39}

<Heading level={5} id="stage&#45;2" className="scroll-mt-(--scroll-mt)">stage</Heading>

[`ConfigurationImprovementDiagnosis`](/pale/reference/js/classes/ConfigurationImprovementDiagnosis)

#### Returns {#returns-44}

[`ConfigurationImprovementPreview`](/pale/reference/js/classes/ConfigurationImprovementPreview)

-----

### previewLocalConfigurationImprovement\(\) {#previewlocalconfigurationimprovement}

```ts
previewLocalConfigurationImprovement(request: LocalConfigurationImprovementRequest): Promise<ConfigurationImprovementPreview>;
```

Capture two local source roots and return a fresh effect\-free preview\.

The request is owned before returning the promise\. The worker uses the
SDK's capture and review owners; it neither resumes an editor review nor
chooses a terminal decision\. Acceptance still performs no source write\.

# Errors {#errors-39}

The promise rejects with the canonical API diagnostic for invalid
locators, capture, selection, compilation or review input\. This route
introduces no cancellation or native\-effect authority\.

#### Parameters {#parameters-40}

<Heading level={5} id="request&#45;14" className="scroll-mt-(--scroll-mt)">request</Heading>

[`LocalConfigurationImprovementRequest`](/pale/reference/js/interfaces/LocalConfigurationImprovementRequest)

#### Returns {#returns-45}

`Promise`\<[`ConfigurationImprovementPreview`](/pale/reference/js/classes/ConfigurationImprovementPreview)\>

-----

### projectDiagnostic\(\) {#projectdiagnostic}

```ts
projectDiagnostic(projection: DiagnosticProjection): Buffer;
```

Project a typed owner classification into canonical `diagnostic.v1` bytes\.

# Errors {#errors-40}

Returns a native error with separate `diagnostic` bytes when the
projection cannot be admitted or canonically encoded\.

#### Parameters {#parameters-41}

<Heading level={5} id="projection" className="scroll-mt-(--scroll-mt)">projection</Heading>

[`DiagnosticProjection`](/pale/reference/js/interfaces/DiagnosticProjection)

#### Returns {#returns-46}

`Buffer`

-----

### proposeConfigurationImprovement\(\) {#proposeconfigurationimprovement}

```ts
proposeConfigurationImprovement(explanation: ConfigurationImprovementExplanation, request: ConfigurationImprovementProposalRequest): ConfigurationImprovementProposal;
```

Consume explanation and capture candidate source without evaluating it\.

# Errors {#errors-41}

Returns consumed\-handle misuse or canonical source\-capture diagnostics\.
The explanation is consumed even if capture rejects the request\.

#### Parameters {#parameters-42}

<Heading level={5} id="explanation&#45;2" className="scroll-mt-(--scroll-mt)">explanation</Heading>

[`ConfigurationImprovementExplanation`](/pale/reference/js/classes/ConfigurationImprovementExplanation)

<Heading level={5} id="request&#45;15" className="scroll-mt-(--scroll-mt)">request</Heading>

[`ConfigurationImprovementProposalRequest`](/pale/reference/js/interfaces/ConfigurationImprovementProposalRequest)

#### Returns {#returns-47}

[`ConfigurationImprovementProposal`](/pale/reference/js/classes/ConfigurationImprovementProposal)

-----

### publishLocalOneShotPlan\(\) {#publishlocaloneshotplan}

```ts
publishLocalOneShotPlan(plan: LocalOneShotPlan, outputDirectory: string): LocalOneShotPlanPublication;
```

Publish one complete plan into a confined local directory\.

This method is the explicit native\-effect boundary for saved\-plan
publication\. Constructing the request or plan does not invoke it\.

# Errors {#errors-42}

Returns a native error with separate `diagnostic` bytes when directory
admission, retained identity, or atomic publication fails\.

#### Parameters {#parameters-43}

<Heading level={5} id="plan" className="scroll-mt-(--scroll-mt)">plan</Heading>

[`LocalOneShotPlan`](/pale/reference/js/classes/LocalOneShotPlan)

<Heading level={5} id="outputdirectory" className="scroll-mt-(--scroll-mt)">outputDirectory</Heading>

`string`

#### Returns {#returns-48}

[`LocalOneShotPlanPublication`](/pale/reference/js/interfaces/LocalOneShotPlanPublication)

-----

### residentHookTransportUnavailable\(\) {#residenthooktransportunavailable}

```ts
residentHookTransportUnavailable(admission: ResidentHookAdmission): void;
```

Reject an admitted hook explicitly when no authenticated carrier exists\.

This is the API\-owned bootstrap non\-effect projection\. It never attempts
IPC, falls back to one\-shot evaluation, or infers resident availability\.

# Errors {#errors-43}

Always returns the canonical unavailable\-carrier diagnostic as a native
error with separate `diagnostic` bytes\.

#### Parameters {#parameters-44}

<Heading level={5} id="admission" className="scroll-mt-(--scroll-mt)">admission</Heading>

[`ResidentHookAdmission`](/pale/reference/js/classes/ResidentHookAdmission)

#### Returns {#returns-49}

`void`

-----

### settleLocalMaterializationRun\(\) {#settlelocalmaterializationrun}

```ts
settleLocalMaterializationRun(run: LocalMaterializationAdmittedRun): LocalMaterializationRunResult;
```

Settle one admitted run in repository order\.

This is an explicit native\-effect boundary\. Executable identity and every
receipt slot are admitted before the first repository mutation\.

# Errors {#errors-44}

Returns a native error with separate `diagnostic` bytes for pre\-effect
rejection or outcome\-unknown settlement requiring read\-back\.

#### Parameters {#parameters-45}

<Heading level={5} id="run&#45;1" className="scroll-mt-(--scroll-mt)">run</Heading>

[`LocalMaterializationAdmittedRun`](/pale/reference/js/classes/LocalMaterializationAdmittedRun)

#### Returns {#returns-50}

[`LocalMaterializationRunResult`](/pale/reference/js/interfaces/LocalMaterializationRunResult)

-----

### validateContractDocument\(\) {#validatecontractdocument}

```ts
validateContractDocument(schemaId: string, bytes: Buffer): ValidatedContractDocument;
```

Validate and canonicalize one selected contract document\.

# Errors {#errors-45}

Returns a native error with separate `diagnostic` bytes when the schema
identity or document fails API\-owned contract admission\.

#### Parameters {#parameters-46}

<Heading level={5} id="schemaid&#45;1" className="scroll-mt-(--scroll-mt)">schemaId</Heading>

`string`

<Heading level={5} id="bytes&#45;2" className="scroll-mt-(--scroll-mt)">bytes</Heading>

`Buffer`

#### Returns {#returns-51}

[`ValidatedContractDocument`](/pale/reference/js/interfaces/ValidatedContractDocument)

-----

### validateStandaloneAuthoring\(\) {#validatestandaloneauthoring}

```ts
validateStandaloneAuthoring(
   role: StandaloneAuthoringRole, 
   sourceLabel: string, 
   bytes: Buffer
): void;
```

Validate one explicitly typed standalone authoring document\.

# Errors {#errors-46}

Returns a native error with separate `diagnostic` bytes when source
capture, TOML parsing, or API\-owned grammar admission fails\.

#### Parameters {#parameters-47}

<Heading level={5} id="role&#45;1" className="scroll-mt-(--scroll-mt)">role</Heading>

[`StandaloneAuthoringRole`](/pale/reference/js/enumerations/StandaloneAuthoringRole)

<Heading level={5} id="sourcelabel&#45;3" className="scroll-mt-(--scroll-mt)">sourceLabel</Heading>

`string`

<Heading level={5} id="bytes&#45;3" className="scroll-mt-(--scroll-mt)">bytes</Heading>

`Buffer`

#### Returns {#returns-52}

`void`

-----

### verifyCurrentExecutableBinding\(\) {#verifycurrentexecutablebinding}

```ts
verifyCurrentExecutableBinding(compilation: LocalOneShotCompilation): CompiledInterfaceIdentity;
```

Verify the current host executable against one captured workspace binding\.

This checks the Node executable, not the loaded addon's bytes\. Success
returns the compiled interface claims; it establishes no resident state
or process health and starts no service\.

# Errors {#errors-47}

Returns a native error with separate `diagnostic` bytes when no runtime
is bound or executable bytes, version, protocol, or identity disagree\.

#### Parameters {#parameters-48}

<Heading level={5} id="compilation&#45;7" className="scroll-mt-(--scroll-mt)">compilation</Heading>

[`LocalOneShotCompilation`](/pale/reference/js/classes/LocalOneShotCompilation)

#### Returns {#returns-53}

[`CompiledInterfaceIdentity`](/pale/reference/js/interfaces/CompiledInterfaceIdentity)
