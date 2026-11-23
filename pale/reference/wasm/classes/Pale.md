---
title: "Class: Pale"
---

<a id="class&#45;pale"></a>

Portable effect\-free Pale façade for browser, editor, and plugin\-UI hosts\.

## Constructors {#constructors}

### Constructor {#constructor}

```ts
new Pale(): Pale;
```

Verify embedded contracts and construct an effect\-free façade\.

# Errors {#errors}

Returns the stable initialization code and message when the embedded
contract bundle contradicts the compiled façade\.

#### Returns {#returns}

`Pale`

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns-1}

`void`

-----

### admitDiagnostic\(\) {#admitdiagnostic}

```ts
admitDiagnostic(bytes: Uint8Array): Uint8Array;
```

Admit exact canonical `diagnostic.v1` bytes and return the same bytes\.

# Errors {#errors-1}

Returns a native `Error` with separate structured `diagnostic` data when
the input is not the canonical initial\-v1 diagnostic contract\.

#### Parameters {#parameters}

<Heading level={5} id="bytes" className="scroll-mt-(--scroll-mt)">bytes</Heading>

`Uint8Array`

#### Returns {#returns-2}

`Uint8Array`

-----

### authoringIngressLimits\(\) {#authoringingresslimits}

```ts
authoringIngressLimits(_class: AuthoringIngressClass): AuthoringIngressLimits;
```

Return API\-owned ingress ceilings for one authoring custody class\.

#### Parameters {#parameters-1}

<Heading level={5} id="class" className="scroll-mt-(--scroll-mt)">\_class</Heading>

[`AuthoringIngressClass`](/pale/reference/wasm/enumerations/AuthoringIngressClass)

#### Returns {#returns-3}

[`AuthoringIngressLimits`](/pale/reference/wasm/classes/AuthoringIngressLimits)

-----

### capabilityIdsJson\(\) {#capabilityidsjson}

```ts
capabilityIdsJson(): string;
```

List the API\-owned WASM capabilities as pretty\-printed JSON\.

#### Returns {#returns-4}

`string`

-----

### comparePortableWorkspaces\(\) {#compareportableworkspaces}

```ts
comparePortableWorkspaces(prior: PortableWorkspaceCompilation, current: PortableWorkspaceCompilation): PortableWorkspaceComparison;
```

Compare two admitted path\-free workspace handles\.

# Errors {#errors-2}

Returns a native `Error` with separate structured `diagnostic` data when
the workspaces cannot form one valid comparison coordinate\.

#### Parameters {#parameters-2}

<Heading level={5} id="prior" className="scroll-mt-(--scroll-mt)">prior</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/wasm/classes/PortableWorkspaceCompilation)

<Heading level={5} id="current" className="scroll-mt-(--scroll-mt)">current</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/wasm/classes/PortableWorkspaceCompilation)

#### Returns {#returns-5}

[`PortableWorkspaceComparison`](/pale/reference/wasm/classes/PortableWorkspaceComparison)

-----

### compilePortableWorkspace\(\) {#compileportableworkspace}

```ts
compilePortableWorkspace(request: PortableWorkspaceRequest): PortableWorkspaceCompilation;
```

Consume and compile one complete path\-free workspace source batch\.

# Errors {#errors-3}

Returns a native `Error` with separate structured `diagnostic` data when
source or workspace meaning fails API\-owned admission\. An invalid or
already consumed request returns a native `Error` without a diagnostic\.

#### Parameters {#parameters-3}

<Heading level={5} id="request" className="scroll-mt-(--scroll-mt)">request</Heading>

[`PortableWorkspaceRequest`](/pale/reference/wasm/classes/PortableWorkspaceRequest)

#### Returns {#returns-6}

[`PortableWorkspaceCompilation`](/pale/reference/wasm/classes/PortableWorkspaceCompilation)

-----

### contractBundleIdentity\(\) {#contractbundleidentity}

```ts
contractBundleIdentity(): ContractBundleIdentity;
```

Inspect the complete embedded public\-contract bundle coordinate\.

#### Returns {#returns-7}

[`ContractBundleIdentity`](/pale/reference/wasm/classes/ContractBundleIdentity)

-----

### contractSchema\(\) {#contractschema}

```ts
contractSchema(schema_id: string): ContractSchema;
```

Look up one façade\-selected generated schema by registry identity\.

# Errors {#errors-4}

Returns a native `Error` whose message is the canonical summary and
whose `diagnostic` property carries the complete record\.

#### Parameters {#parameters-4}

<Heading level={5} id="schema&#45;id" className="scroll-mt-(--scroll-mt)">schema\_id</Heading>

`string`

#### Returns {#returns-8}

[`ContractSchema`](/pale/reference/wasm/classes/ContractSchema)

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-9}

`void`

-----

### inspectStandaloneAuthoring\(\) {#inspectstandaloneauthoring}

```ts
inspectStandaloneAuthoring(role: StandaloneAuthoringRole, path: AuthoringPathSegment[]): AuthoringInspection;
```

Inspect generated facts for one explicitly selected standalone grammar\.
Path elements are consumed in order; failure releases the converted
prefix and leaves later elements untouched\.

# Errors {#errors-5}

Returns a native `Error` carrying the API\-owned canonical diagnostic when
the path exceeds its bound or generated authoring metadata is incoherent\.
An invalid or already consumed element returns a native `Error` without
an API diagnostic\.

#### Parameters {#parameters-5}

<Heading level={5} id="role" className="scroll-mt-(--scroll-mt)">role</Heading>

[`StandaloneAuthoringRole`](/pale/reference/wasm/enumerations/StandaloneAuthoringRole)

<Heading level={5} id="path" className="scroll-mt-(--scroll-mt)">path</Heading>

[`AuthoringPathSegment`](/pale/reference/wasm/classes/AuthoringPathSegment)\[\]

#### Returns {#returns-10}

[`AuthoringInspection`](/pale/reference/wasm/classes/AuthoringInspection)

-----

### invokeNativeAction\(\) {#invokenativeaction}

```ts
invokeNativeAction(action_id: string, input_bytes: Uint8Array): Uint8Array;
```

Execute one complete tagged effect\-free native\-action request\.

# Errors {#errors-6}

Returns a native `Error` with separate structured `diagnostic` data when
the tagged request fails admission or pure execution\.

#### Parameters {#parameters-6}

<Heading level={5} id="action&#45;id" className="scroll-mt-(--scroll-mt)">action\_id</Heading>

`string`

<Heading level={5} id="input&#45;bytes" className="scroll-mt-(--scroll-mt)">input\_bytes</Heading>

`Uint8Array`

#### Returns {#returns-11}

`Uint8Array`

-----

### invokeNativeActionPayload\(\) {#invokenativeactionpayload}

```ts
invokeNativeActionPayload(action_id: string, payload_bytes: Uint8Array): Uint8Array;
```

Execute one carrier\-selected effect\-free native\-action payload\.

# Errors {#errors-7}

Returns a native `Error` with separate structured `diagnostic` data when
the action, payload, or pure execution fails API\-owned admission\.

#### Parameters {#parameters-7}

<Heading level={5} id="action&#45;id&#45;1" className="scroll-mt-(--scroll-mt)">action\_id</Heading>

`string`

<Heading level={5} id="payload&#45;bytes" className="scroll-mt-(--scroll-mt)">payload\_bytes</Heading>

`Uint8Array`

#### Returns {#returns-12}

`Uint8Array`

-----

### nativeActionCatalog\(\) {#nativeactioncatalog}

```ts
nativeActionCatalog(): NativeActionDescriptor[];
```

Return the complete effect\-free native\-action catalog as one batch\.

# Errors {#errors-8}

Returns a native `Error` with separate structured `diagnostic` data if
the compiled registry contradicts its action contracts\.

#### Returns {#returns-13}

[`NativeActionDescriptor`](/pale/reference/wasm/classes/NativeActionDescriptor)\[\]

-----

### projectDiagnostic\(\) {#projectdiagnostic}

```ts
projectDiagnostic(projection: DiagnosticProjection): Uint8Array;
```

Consume one typed classification and admit it through the diagnostic owner\.

# Errors {#errors-9}

Returns a native `Error` with separate structured `diagnostic` data when
the projection cannot be admitted or canonically encoded\. An invalid or
already consumed handle returns a native `Error` without a diagnostic\.

#### Parameters {#parameters-8}

<Heading level={5} id="projection" className="scroll-mt-(--scroll-mt)">projection</Heading>

[`DiagnosticProjection`](/pale/reference/wasm/classes/DiagnosticProjection)

#### Returns {#returns-14}

`Uint8Array`

-----

### validateAuthoringDocument\(\) {#validateauthoringdocument}

```ts
validateAuthoringDocument(
   role: StandaloneAuthoringRole, 
   source_label: string, 
   bytes: Uint8Array
): void;
```

Validate one explicitly typed source without selecting project context\.

# Errors {#errors-10}

Returns a native `Error` with the API\-owned canonical diagnostic when
label, resource, syntax, or contract admission fails\.

#### Parameters {#parameters-9}

<Heading level={5} id="role&#45;1" className="scroll-mt-(--scroll-mt)">role</Heading>

[`StandaloneAuthoringRole`](/pale/reference/wasm/enumerations/StandaloneAuthoringRole)

<Heading level={5} id="source&#45;label" className="scroll-mt-(--scroll-mt)">source\_label</Heading>

`string`

<Heading level={5} id="bytes&#45;1" className="scroll-mt-(--scroll-mt)">bytes</Heading>

`Uint8Array`

#### Returns {#returns-15}

`void`

-----

### validateContractDocument\(\) {#validatecontractdocument}

```ts
validateContractDocument(schema_id: string, bytes: Uint8Array): ValidatedContractDocument;
```

Structurally validate and canonicalize one selected contract document\.

# Errors {#errors-11}

Returns a native `Error` with separate structured `diagnostic` data when
the schema identity or document fails API\-owned admission\.

#### Parameters {#parameters-10}

<Heading level={5} id="schema&#45;id&#45;1" className="scroll-mt-(--scroll-mt)">schema\_id</Heading>

`string`

<Heading level={5} id="bytes&#45;2" className="scroll-mt-(--scroll-mt)">bytes</Heading>

`Uint8Array`

#### Returns {#returns-16}

[`ValidatedContractDocument`](/pale/reference/wasm/classes/ValidatedContractDocument)
