---
title: "sdk/wasm/dist/pale_wasm.d.ts"
noindex: true
---

```ts
/* tslint:disable */
/* eslint-disable */

/**
 * Proposed source edit from a rejected configuration check.
 *
 * Match the expected source at the supplied path before using the replacement.
 * This value preserves the compiler's proposal; it does not authorize a write.
 */
export class AuthoringCorrection {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return the compiler-proved correction kind.
     */
    kind(): AuthoringCorrectionKind;
    /**
     * Return the ordered field and array-index steps to the source value.
     */
    path(): AuthoringInstancePathSegment[];
    /**
     * Return the semantic subject that proves this correction.
     */
    proofSubject(): AuthoringIdentity;
    /**
     * Return the identity of the rejected diagnostic, without recomputing it.
     */
    readonly diagnosticIdentity: string;
    /**
     * Return the exact scalar text that must still occupy the edit range.
     */
    readonly expectedSource: string;
    /**
     * Return the replacement scalar text selected by the compiler.
     */
    readonly replacementSource: string;
    /**
     * Return the logical label of the source to edit.
     */
    readonly sourceLabel: string;
}

/**
 * Kind of source correction proved by the compiler.
 */
export enum AuthoringCorrectionKind {
    /**
     * Narrow an import visibility ceiling to its export's ceiling.
     */
    NarrowImportVisibility = 0,
}

/**
 * One child key offered at the selected structural path.
 */
export class AuthoringFieldFact {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return the complete bounded literal vocabulary.
     */
    allowedValues(): AuthoringLiteralFact[];
    /**
     * Return requiredness across applicable structural variants.
     */
    presence(): AuthoringFieldPresence;
    /**
     * Return all admitted structural value categories in stable order.
     */
    valueKinds(): AuthoringValueKind[];
    /**
     * Return producer documentation for this field.
     */
    readonly description: string | undefined;
    /**
     * Return the exact authored key spelling.
     */
    readonly name: string;
}

/**
 * Requiredness of one child field across structural variants.
 */
export enum AuthoringFieldPresence {
    /**
     * Every applicable variant requires the field.
     */
    Required = 0,
    /**
     * No applicable variant requires the field.
     */
    Optional = 1,
    /**
     * Requiredness depends on the selected structural variant.
     */
    VariantDependent = 2,
}

/**
 * Resolved binding-safe semantic identity.
 */
export class AuthoringIdentity {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return the non-interchangeable identity namespace.
     */
    kind(): AuthoringIdentityKind;
    /**
     * Return the exact scalar spelling valid in the reference scope.
     */
    readonly authoredValue: string;
    /**
     * Return the canonical compiler-owned display form.
     */
    readonly value: string;
}

/**
 * Closed namespace of one resolved editor-visible identity.
 */
export enum AuthoringIdentityKind {
    /**
     * Compiler-admitted source document.
     */
    SourceDocument = 0,
    /**
     * Principal-owned workspace root.
     */
    Workspace = 1,
    /**
     * Canonical project.
     */
    Project = 2,
    /**
     * Canonical execution workspace.
     */
    ExecutionWorkspace = 3,
    /**
     * Canonical repository.
     */
    Repository = 4,
    /**
     * Neutral execution-path selection.
     */
    ExecutionPath = 5,
    /**
     * Reusable workspace module.
     */
    Module = 6,
    /**
     * Immutable module release.
     */
    ModuleRelease = 7,
    /**
     * Content-addressed component.
     */
    Component = 8,
    /**
     * Named module export.
     */
    Export = 9,
    /**
     * Module-scoped namespace.
     */
    Namespace = 10,
    /**
     * Qualified declaration.
     */
    Declaration = 11,
    /**
     * Module-scoped logical resource.
     */
    Resource = 12,
    /**
     * Private run-policy declaration.
     */
    RunPolicy = 13,
    /**
     * Private lifecycle behavior.
     */
    LifecycleBehavior = 14,
    /**
     * Portable capability identity.
     */
    Capability = 15,
    /**
     * Machine-local authority root.
     */
    AuthorityRoot = 16,
    /**
     * Exact provider-binding projection.
     */
    ProviderBinding = 17,
    /**
     * Private machine binding.
     */
    Machine = 18,
    /**
     * Responsibility derivation.
     */
    ResponsibilityDerivation = 19,
    /**
     * Responsibility native projection.
     */
    ResponsibilityProjection = 20,
    /**
     * Responsibility Genealogy link.
     */
    ResponsibilityGenealogyLink = 21,
    /**
     * Qualified logical scope.
     */
    LogicalScope = 22,
    /**
     * Qualified logical organization.
     */
    LogicalOrganization = 23,
    /**
     * Qualified organizational group.
     */
    OrganizationalGroup = 24,
    /**
     * Qualified discipline tree.
     */
    DisciplineTree = 25,
    /**
     * Qualified stable organizational role.
     */
    OrganizationalRole = 26,
    /**
     * Explicit organizational occupant.
     */
    OrganizationalOccupant = 27,
    /**
     * Explicit organizational provider.
     */
    OrganizationalProvider = 28,
    /**
     * Provider-neutral communication actor.
     */
    CommunicationActor = 29,
    /**
     * Topic-scoped leadership participation.
     */
    LeadershipTopic = 30,
    /**
     * Organizational relation.
     */
    OrganizationalRelation = 31,
    /**
     * Owner-selected organizational object.
     */
    OrganizationalObject = 32,
    /**
     * Group-lens authority profile.
     */
    GroupLensProfile = 33,
    /**
     * Directional-service contract.
     */
    DirectionalService = 34,
    /**
     * Organizational native projection.
     */
    OrganizationalProjection = 35,
    /**
     * Organizational inspection.
     */
    OrganizationalInspection = 36,
    /**
     * Neutral composition participant.
     */
    CompositionParticipant = 37,
    /**
     * Composition responsibility contract.
     */
    CompositionResponsibilityContract = 38,
    /**
     * Composition participant manifest.
     */
    CompositionParticipantManifest = 39,
    /**
     * Composition provider.
     */
    CompositionProvider = 40,
    /**
     * Composition provider binding.
     */
    CompositionProviderBinding = 41,
    /**
     * Composition entry contract.
     */
    CompositionEntryContract = 42,
    /**
     * Neutral request translation.
     */
    CompositionRequestTranslation = 43,
    /**
     * Neutral result translation.
     */
    CompositionResultTranslation = 44,
    /**
     * Neutral termination contract.
     */
    CompositionTerminationContract = 45,
    /**
     * Neutral settlement contract.
     */
    CompositionSettlementContract = 46,
    /**
     * Neutral continuity contract.
     */
    CompositionContinuityContract = 47,
    /**
     * Typed neutral composition edge.
     */
    CompositionEdge = 48,
    /**
     * Selected neutral experience path.
     */
    ExperiencePath = 49,
    /**
     * Package doctrine resource.
     */
    PackageDoctrine = 50,
    /**
     * Package operation-archetype resource.
     */
    PackageOperationArchetype = 51,
    /**
     * Package operation resource.
     */
    PackageOperation = 52,
    /**
     * Package role-archetype resource.
     */
    PackageRoleArchetype = 53,
    /**
     * Package specialist-role resource.
     */
    PackageRole = 54,
    /**
     * Package stack resource.
     */
    PackageStack = 55,
    /**
     * Package run-mode resource.
     */
    PackageRunMode = 56,
    /**
     * Package policy-family resource.
     */
    PackagePolicyFamily = 57,
    /**
     * Package governing-order resource.
     */
    PackageGoverningOrder = 58,
    /**
     * Package capability-policy resource.
     */
    PackageCapabilityPolicy = 59,
    /**
     * Package tool-recipe resource.
     */
    PackageToolRecipe = 60,
    /**
     * Immutable Package identity.
     */
    Package = 61,
}

/**
 * Source-custody class whose API-owned limits protect authoring ingress.
 */
export enum AuthoringIngressClass {
    /**
     * Portable workspace-language documents.
     */
    Workspace = 0,
    /**
     * Private selections, bindings, locks, and lifecycle guidance.
     */
    Private = 1,
    /**
     * Immutable Package distribution members.
     */
    Package = 2,
}

/**
 * API-owned finite source limits for one custody class.
 */
export class AuthoringIngressLimits {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Maximum bytes retained from one logical document.
     */
    readonly maxDocumentBytes: bigint;
    /**
     * Maximum logical documents as a non-lossy JavaScript `bigint`.
     */
    readonly maxDocuments: bigint;
    /**
     * Maximum aggregate bytes retained for the custody class.
     */
    readonly maxTotalBytes: bigint;
}

/**
 * Complete source-role and schema-derived response for one authoring request.
 */
export class AuthoringInspection {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return structural facts only when the state is available.
     */
    node(): AuthoringNodeFact | undefined;
    /**
     * Return availability for the exact request.
     */
    state(): AuthoringInspectionState;
    /**
     * Return the selected named definition for a shared grammar.
     */
    readonly definition: string | undefined;
    /**
     * Return the selected grammar descriptor identity.
     */
    readonly schemaId: string | undefined;
}

/**
 * Availability of structural authoring help at one coordinate.
 */
export enum AuthoringInspectionState {
    /**
     * The generated grammar contains the selected path.
     */
    Available = 0,
    /**
     * The source is substantive text rather than TOML grammar.
     */
    TextDocument = 1,
    /**
     * The compilation does not own the requested label.
     */
    UnknownDocument = 2,
    /**
     * The structural path is outside the selected grammar.
     */
    UnknownPath = 3,
}

/**
 * One exact path step used for semantic authoring navigation.
 */
export class AuthoringInstancePathSegment {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Construct one exact field step.
     */
    static field(value: string): AuthoringInstancePathSegment;
    /**
     * Construct one exact array-member step.
     *
     * # Errors
     *
     * Returns a native `Error` when the value is not a JavaScript number
     * representing an integer from zero through `u32::MAX`.
     */
    static index(value: number): AuthoringInstancePathSegment;
    /**
     * Return the exact segment family.
     */
    kind(): AuthoringInstancePathSegmentKind;
    /**
     * Return the decoded key for a field segment.
     */
    readonly fieldValue: string | undefined;
    /**
     * Return the exact array index as a non-lossy JavaScript `bigint`.
     */
    readonly indexValue: bigint | undefined;
}

/**
 * Exact instance-path segment family.
 */
export enum AuthoringInstancePathSegmentKind {
    /**
     * Exact decoded key.
     */
    Field = 0,
    /**
     * Exact array or array-of-tables index.
     */
    Index = 1,
}

/**
 * Lossless projection of one generated TOML literal.
 */
export class AuthoringLiteral {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return the literal family.
     */
    kind(): AuthoringLiteralKind;
    /**
     * Return the Boolean member when this is a Boolean literal.
     */
    readonly booleanValue: boolean | undefined;
    /**
     * Return the signed integer member as a non-lossy JavaScript `bigint`.
     */
    readonly integerValue: bigint | undefined;
    /**
     * Return the string member when this is a string literal.
     */
    readonly stringValue: string | undefined;
}

/**
 * One allowed literal plus producer-owned documentation.
 */
export class AuthoringLiteralFact {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return the exact literal admitted by the generated node.
     */
    value(): AuthoringLiteral;
    /**
     * Return variant-specific producer documentation.
     */
    readonly description: string | undefined;
}

/**
 * Closed TOML literal family supplied by generated grammar facts.
 */
export enum AuthoringLiteralKind {
    /**
     * UTF-8 string literal.
     */
    String = 0,
    /**
     * Signed integer literal.
     */
    Integer = 1,
    /**
     * Boolean literal.
     */
    Boolean = 2,
}

/**
 * Semantic navigation result for one exact admitted occurrence.
 */
export class AuthoringNavigation {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return all bounded same-namespace completion alternatives.
     */
    alternatives(): AuthoringIdentity[];
    /**
     * Return the canonical definition when the closure contains one.
     */
    definition(): AuthoringSourceLocation | undefined;
    /**
     * Return the resolved identity, when the coordinate is semantic.
     */
    identity(): AuthoringIdentity | undefined;
    /**
     * Return the semantic role of the queried occurrence.
     */
    occurrenceRole(): AuthoringOccurrenceRole | undefined;
    /**
     * Return all retained references in deterministic order.
     */
    references(): AuthoringSourceLocation[];
    /**
     * Report whether the API ceiling omitted completion alternatives.
     */
    readonly alternativesTruncated: boolean;
    /**
     * Report whether the API ceiling omitted source references.
     */
    readonly referencesTruncated: boolean;
}

/**
 * Bounded structural facts for one authoring position.
 */
export class AuthoringNodeFact {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return the complete bounded literal vocabulary.
     */
    allowedValues(): AuthoringLiteralFact[];
    /**
     * Return every deterministic child-field fact in stable order.
     */
    fields(): AuthoringFieldFact[];
    /**
     * Return every admitted structural value category in stable order.
     */
    valueKinds(): AuthoringValueKind[];
    /**
     * Return producer documentation for this structural context.
     */
    readonly description: string | undefined;
    /**
     * Return the optional generated string format.
     */
    readonly format: string | undefined;
    /**
     * Return the inclusive collection-size upper bound as a non-lossy `bigint`.
     */
    readonly maxItems: bigint | undefined;
    /**
     * Return the inclusive string-length upper bound as a non-lossy `bigint`.
     */
    readonly maxLength: bigint | undefined;
    /**
     * Return the inclusive integer upper bound as a non-lossy `bigint`.
     */
    readonly maximum: bigint | undefined;
    /**
     * Return the inclusive collection-size lower bound as a non-lossy `bigint`.
     */
    readonly minItems: bigint | undefined;
    /**
     * Return the inclusive string-length lower bound as a non-lossy `bigint`.
     */
    readonly minLength: bigint | undefined;
    /**
     * Return the inclusive integer lower bound as a non-lossy `bigint`.
     */
    readonly minimum: bigint | undefined;
    /**
     * Return the optional generated string pattern.
     */
    readonly pattern: string | undefined;
}

/**
 * Compiler-produced location and role, without source text.
 */
export class AuthoringOccurrence {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Copy the logical source label and decoded field/index path.
     */
    location(): AuthoringSourceLocation;
    /**
     * Definition, reference, or projection role assigned by the compiler.
     */
    role(): AuthoringOccurrenceRole;
}

/**
 * Matching occurrences and scan progress from the retained compiler index.
 *
 * An empty page can be incomplete. Row limits combine with one fixed ceiling
 * over copied source labels and field names.
 */
export class AuthoringOccurrencePage {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Share the continuation, or return `undefined` after proven exhaustion.
     *
     * Each call creates an independently owned handle. Resuming consumes that
     * handle; callers can retain another copy when they need to retry a query.
     */
    continuation(): AuthoringOccurrencePageCursor | undefined;
    /**
     * Copy matching occurrences in compiler source/path order.
     */
    occurrences(): AuthoringOccurrence[];
    /**
     * UTF-8 bytes copied into returned source labels and field names.
     */
    readonly copiedStringBytes: number;
    /**
     * Index entries examined, including nonmatches.
     */
    readonly inspected: number;
    /**
     * Whether the scan proved exhaustion of the retained index.
     */
    readonly isComplete: boolean;
}

/**
 * Opaque continuation for one compilation, full identity, and pair of limits.
 *
 * The cursor retains its SDK compilation until freed or consumed. It cannot be
 * reconstructed from text and grants no permission to disclose source locations.
 */
export class AuthoringOccurrencePageCursor {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
}

/**
 * Semantic role played by one exact admitted occurrence.
 */
export enum AuthoringOccurrenceRole {
    /**
     * The occurrence establishes the canonical definition.
     */
    Definition = 0,
    /**
     * The occurrence resolves to a separate definition.
     */
    Reference = 1,
    /**
     * The occurrence carries a content-bearing projection.
     */
    Projection = 2,
}

/**
 * One structural path step supplied by a tolerant host parser.
 */
export class AuthoringPathSegment {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Construct one structural array-item step.
     */
    static arrayItem(): AuthoringPathSegment;
    /**
     * Construct one exact field step.
     */
    static field(value: string): AuthoringPathSegment;
}

/**
 * Exact source label and path supplied by the compiler, including on rejection.
 */
export class AuthoringSourceLocation {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return the complete exact instance path in stable order.
     */
    path(): AuthoringInstancePathSegment[];
    /**
     * Return the compiler logical source label.
     */
    readonly sourceLabel: string;
}

/**
 * Structural value category admitted by one generated node.
 */
export enum AuthoringValueKind {
    /**
     * Boolean value.
     */
    Boolean = 0,
    /**
     * Signed integer value.
     */
    Integer = 1,
    /**
     * UTF-8 string value.
     */
    String = 2,
    /**
     * Ordered array value.
     */
    Array = 3,
    /**
     * TOML table or inline-table value.
     */
    Table = 4,
}

/**
 * Exact embedded bundle coordinate, with only JavaScript-safe integers.
 */
export class ContractBundleIdentity {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Number of schemas in the embedded bundle.
     */
    readonly memberCount: number;
    /**
     * RFC 8785 descriptor-manifest digest.
     */
    readonly schemaManifestSha256: string;
    /**
     * Domain-separated active schema-set digest.
     */
    readonly schemaSetSha256: string;
}

/**
 * One selected generated schema and its exact bytes.
 */
export class ContractSchema {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Copy the exact raw schema into one owned `Uint8Array`.
     */
    bytes(): Uint8Array;
    /**
     * Descriptor-registry identity used for lookup.
     */
    readonly registryId: string;
    /**
     * SHA-256 of the exact raw schema bytes.
     */
    readonly schemaSha256: string;
    /**
     * Canonical schema URI.
     */
    readonly schemaUri: string;
    /**
     * Wire identity carried by standalone documents, when one exists.
     */
    readonly wireSchemaId: string | undefined;
}

/**
 * WebAssembly representation of API-owned [`DiagnosticDisposition`].
 */
export enum DiagnosticDisposition {
    /**
     * Runtime prerequisite failure.
     */
    OperationalFailure = 0,
    /**
     * Input or authored meaning requires correction.
     */
    InvalidInput = 1,
    /**
     * Current admitted state blocks the request.
     */
    Blocked = 2,
    /**
     * Pale application invariant failure.
     */
    InternalFailure = 3,
    /**
     * An external effect may have occurred and requires reconciliation.
     */
    EffectOutcomeUnknown = 4,
}

/**
 * WebAssembly representation of API-owned [`DiagnosticEffectCertainty`].
 */
export enum DiagnosticEffectCertainty {
    /**
     * No external-effect boundary exists.
     */
    NotApplicable = 0,
    /**
     * The effect boundary is proven not to have started.
     */
    NotStarted = 1,
    /**
     * Owner evidence confirms the effect and result.
     */
    Confirmed = 2,
    /**
     * Available evidence cannot establish whether the external effect occurred.
     */
    OutcomeUnknown = 3,
}

/**
 * Typed unadmitted candidate forwarded to [`DiagnosticProjection`].
 */
export class DiagnosticProjection {
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Start one complete owner classification; API admission remains fallible.
     */
    constructor(code: string, stage: DiagnosticStage, disposition: DiagnosticDisposition, summary: string, retry: DiagnosticRetry, effect: DiagnosticEffectCertainty);
    /**
     * Attach bounded ordered cause messages and an exact omission count.
     *
     * # Errors
     *
     * Returns a native `Error` when the omitted count is not a JavaScript
     * number representing an integer from zero through `u32::MAX`.
     */
    setCauses(causes: string[], omitted: number): void;
    /**
     * Attach ordered recovery suggestions.
     */
    setHelp(help: string[]): void;
    /**
     * Attach the principally affected typed identity.
     */
    setSubject(kind: string, identity: string): void;
}

/**
 * WebAssembly representation of API-owned [`DiagnosticRetry`].
 */
export enum DiagnosticRetry {
    /**
     * No retry instruction is established.
     */
    NotIndicated = 0,
    /**
     * Retry after correcting input or authored meaning.
     */
    AfterCorrection = 1,
    /**
     * Retry after admitted state changes.
     */
    AfterStateChange = 2,
    /**
     * Reconcile evidence before deciding whether to retry.
     */
    ReconcileFirst = 3,
}

/**
 * WebAssembly representation of API-owned [`DiagnosticStage`].
 */
export enum DiagnosticStage {
    /**
     * External input admission.
     */
    InputAdmission = 0,
    /**
     * Generated contract validation.
     */
    ContractValidation = 1,
    /**
     * Owner-specific semantic admission.
     */
    SemanticAdmission = 2,
    /**
     * Package source loading.
     */
    PackageLoading = 3,
    /**
     * Workspace source loading.
     */
    WorkspaceLoading = 4,
    /**
     * Compiler resolution or sealing.
     */
    Compilation = 5,
    /**
     * Generated-surface rendering.
     */
    Rendering = 6,
    /**
     * Operation admission.
     */
    OperationAdmission = 7,
    /**
     * Resident generation or durable transition admission.
     */
    ResidentAdmission = 8,
    /**
     * Resident recovery and safe-continuation proof.
     */
    ResidentRecovery = 9,
    /**
     * Effect-free planning.
     */
    Planning = 10,
    /**
     * Materialization or reconciliation.
     */
    Materialization = 11,
    /**
     * Pure native-action computation.
     */
    NativeAction = 12,
    /**
     * External prerequisite observation.
     */
    HostObservation = 13,
    /**
     * Other Pale application invariant.
     */
    Internal = 14,
}

/**
 * One effect-free native-action descriptor owned by the API registry.
 */
export class NativeActionDescriptor {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Copy the exact canonical action contract into one `Uint8Array`.
     */
    contractBytes(): Uint8Array;
    /**
     * Copy the self-contained payload schema into one `Uint8Array`.
     */
    payloadSchemaBytes(): Uint8Array;
    /**
     * Exact compiled action identity.
     */
    readonly actionId: string;
    /**
     * Registry-owned concise action description.
     */
    readonly description: string;
}

/**
 * Portable effect-free Pale façade for browser, editor, and plugin-UI hosts.
 */
export class Pale {
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Admit exact canonical `diagnostic.v1` bytes and return the same bytes.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data when
     * the input is not the canonical initial-v1 diagnostic contract.
     */
    admitDiagnostic(bytes: Uint8Array): Uint8Array;
    /**
     * Return API-owned ingress ceilings for one authoring custody class.
     */
    authoringIngressLimits(_class: AuthoringIngressClass): AuthoringIngressLimits;
    /**
     * List the API-owned WASM capabilities as pretty-printed JSON.
     */
    capabilityIdsJson(): string;
    /**
     * Compare two admitted path-free workspace handles.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data when
     * the workspaces cannot form one valid comparison coordinate.
     */
    comparePortableWorkspaces(prior: PortableWorkspaceCompilation, current: PortableWorkspaceCompilation): PortableWorkspaceComparison;
    /**
     * Consume and compile one complete path-free workspace source batch.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data when
     * source or workspace meaning fails API-owned admission. An invalid or
     * already consumed request returns a native `Error` without a diagnostic.
     */
    compilePortableWorkspace(request: PortableWorkspaceRequest): PortableWorkspaceCompilation;
    /**
     * Inspect the complete embedded public-contract bundle coordinate.
     */
    contractBundleIdentity(): ContractBundleIdentity;
    /**
     * Look up one façade-selected generated schema by registry identity.
     *
     * # Errors
     *
     * Returns a native `Error` whose message is the canonical summary and
     * whose `diagnostic` property carries the complete record.
     */
    contractSchema(schema_id: string): ContractSchema;
    /**
     * Inspect generated facts for one explicitly selected standalone grammar.
     * Path elements are consumed in order; failure releases the converted
     * prefix and leaves later elements untouched.
     *
     * # Errors
     *
     * Returns a native `Error` carrying the API-owned canonical diagnostic when
     * the path exceeds its bound or generated authoring metadata is incoherent.
     * An invalid or already consumed element returns a native `Error` without
     * an API diagnostic.
     */
    inspectStandaloneAuthoring(role: StandaloneAuthoringRole, path: AuthoringPathSegment[]): AuthoringInspection;
    /**
     * Execute one complete tagged effect-free native-action request.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data when
     * the tagged request fails admission or pure execution.
     */
    invokeNativeAction(action_id: string, input_bytes: Uint8Array): Uint8Array;
    /**
     * Execute one carrier-selected effect-free native-action payload.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data when
     * the action, payload, or pure execution fails API-owned admission.
     */
    invokeNativeActionPayload(action_id: string, payload_bytes: Uint8Array): Uint8Array;
    /**
     * Return the complete effect-free native-action catalog as one batch.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data if
     * the compiled registry contradicts its action contracts.
     */
    nativeActionCatalog(): NativeActionDescriptor[];
    /**
     * Verify embedded contracts and construct an effect-free façade.
     *
     * # Errors
     *
     * Returns the stable initialization code and message when the embedded
     * contract bundle contradicts the compiled façade.
     */
    constructor();
    /**
     * Consume one typed classification and admit it through the diagnostic owner.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data when
     * the projection cannot be admitted or canonically encoded. An invalid or
     * already consumed handle returns a native `Error` without a diagnostic.
     */
    projectDiagnostic(projection: DiagnosticProjection): Uint8Array;
    /**
     * Validate one explicitly typed source without selecting project context.
     *
     * # Errors
     *
     * Returns a native `Error` with the API-owned canonical diagnostic when
     * label, resource, syntax, or contract admission fails.
     */
    validateAuthoringDocument(role: StandaloneAuthoringRole, source_label: string, bytes: Uint8Array): void;
    /**
     * Structurally validate and canonicalize one selected contract document.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data when
     * the schema identity or document fails API-owned admission.
     */
    validateContractDocument(schema_id: string, bytes: Uint8Array): ValidatedContractDocument;
}

/**
 * Opaque comparison and retained proof owner for two workspace handles.
 */
export class PortableWorkspaceComparison {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Project one bounded page of exact change roots.
     *
     * Offset and limit must be JavaScript numbers representing exact integers.
     * The offset range is `0..=u32::MAX`; the limit range is `0..=u16::MAX`.
     * Invalid values return a host error instead of being coerced.
     *
     * # Errors
     *
     * Returns a native `Error` when either page coordinate is not an exact
     * integer in its declared range.
     */
    changeRoots(offset: number, limit: number): WorkspaceChangeRootPage;
    /**
     * Compare the typed outputs for one full subject identity.
     *
     * Membership is separate from equality and dependency impact. A valid
     * subject from another compilation can be absent from both sides.
     * This synchronous call copies up to two facts and encodes the answer;
     * it does not provide a fixed byte or elapsed-time bound.
     *
     * A valid supplied subject handle is consumed. Use the result's `subject()`
     * method to obtain a new copy for another query.
     *
     * # Errors
     *
     * Returns a host error for a missing, freed, or wrong-class subject without
     * retaining a borrow of this comparison.
     */
    compareSubject(subject: WorkspaceSubject): WorkspaceSubjectComparison;
    /**
     * Explain a full subject identity against this retained comparison.
     *
     * A valid subject from another compilation is accepted. If this pair does
     * not contain it, the answer is `NotPresent`, not an identity error.
     *
     * # Errors
     *
     * Returns a native `Error` with separate structured `diagnostic` data if
     * admitted proof contradicts its comparison identities or causal invariants.
     */
    explain(subject: WorkspaceSubject): WorkspaceExplanation;
    /**
     * Project one bounded page of the complete impact partition.
     *
     * Offset and limit must be JavaScript numbers representing exact integers.
     * The offset range is `0..=u32::MAX`; the limit range is `0..=u16::MAX`.
     * Invalid values return a host error instead of being coerced.
     *
     * # Errors
     *
     * Returns a native `Error` when either page coordinate is not an exact
     * integer in its declared range.
     */
    impacts(offset: number, limit: number): WorkspaceImpactPage;
    /**
     * Number of current subjects reachable from a root.
     */
    readonly affectedCount: number;
    /**
     * Number of exact source-change roots.
     */
    readonly changeRootCount: number;
    /**
     * Principal-relative current universe digest.
     */
    readonly currentPrincipalUniverseDigest: string;
    /**
     * Current semantic-IR digest.
     */
    readonly currentSemanticIrDigest: string;
    /**
     * Principal-relative predecessor universe digest.
     */
    readonly priorPrincipalUniverseDigest: string;
    /**
     * Predecessor semantic-IR digest.
     */
    readonly priorSemanticIrDigest: string;
    /**
     * Domain-separated identity of the verified derivation receipt.
     */
    readonly receiptDigest: string;
    /**
     * Number of current subjects outside every root closure.
     */
    readonly unaffectedCount: number;
}

/**
 * Opaque admitted portable workspace; dropping it has no semantic effect.
 */
export class PortableWorkspaceCompilation {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Find occurrences of a compiler-produced identity without recompiling.
     *
     * Limits must be numbers representing integers from 0 through 65535. The
     * SDK treats zero as 64 and caps values above 256. Resume on this exact
     * compilation with the same identity and raw limits. Empty pages can continue.
     * Omit the continuation for a first page; a supplied null or invalid handle
     * is an error, not a request to restart.
     *
     * After receiver and identity validation, a supplied continuation is consumed
     * even if limit validation or the SDK query fails. Obtain another handle
     * from its page before retrying.
     *
     * # Errors
     *
     * Invalid limits or handles produce a host error, without coercion. An unlike
     * continuation returns the canonical API diagnostic through the existing
     * diagnostic projection.
     */
    authoringOccurrences(identity: AuthoringIdentity, maximum_inspected: number, maximum_returned: number, after?: AuthoringOccurrencePageCursor): AuthoringOccurrencePage;
    /**
     * Return all bounded cardinalities in one exact JSON object.
     */
    countsJson(): string;
    /**
     * Inspect generated grammar retained by this admitted portable workspace.
     * Path elements are consumed in order; failure releases the converted
     * prefix and leaves later elements untouched.
     *
     * # Errors
     *
     * Returns a native `Error` carrying the API-owned canonical diagnostic when
     * the path exceeds its bound or generated authoring metadata is incoherent.
     * An invalid or already consumed element returns a native `Error` without
     * an API diagnostic.
     */
    inspectAuthoring(source_label: string, path: AuthoringPathSegment[]): AuthoringInspection;
    /**
     * Resolve one exact occurrence through this workspace's canonical linker.
     *
     * Path elements are consumed in order. On failure, earlier elements remain
     * consumed and are released; later elements are untouched.
     *
     * # Errors
     * Returns a native `Error` for an invalid or already consumed path element.
     */
    navigateAuthoring(source_label: string, path: AuthoringInstancePathSegment[]): AuthoringNavigation;
    /**
     * Number of admission-evidence records.
     */
    readonly admissionEvidenceCount: number;
    /**
     * Exact owner-proof frontier consumed by admission.
     */
    readonly admissionEvidenceDigest: string;
    /**
     * Number of adopted releases.
     */
    readonly adoptedReleaseCount: number;
    /**
     * Number of derivation nodes.
     */
    readonly derivationNodeCount: number;
    /**
     * Number of derivation sources.
     */
    readonly derivationSourceCount: number;
    /**
     * Number of normative Pack releases.
     */
    readonly normativePackReleaseCount: number;
    /**
     * Number of Package releases.
     */
    readonly packageReleaseCount: number;
    /**
     * Principal-relative admitted-universe digest.
     */
    readonly principalUniverseDigest: string;
    /**
     * Verified semantic-IR digest.
     */
    readonly semanticIrDigest: string;
    /**
     * Number of admitted source documents.
     */
    readonly sourceDocumentCount: number;
    /**
     * Workspace identity declared by the admitted root manifest.
     */
    readonly workspaceId: string;
}

/**
 * One logical workspace document captured entirely in host memory.
 */
export class PortableWorkspaceDocument {
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Capture a logical relative label and its complete bytes without I/O.
     */
    constructor(label: string, bytes: Uint8Array);
}

/**
 * Batched source request for portable workspace compilation.
 */
export class PortableWorkspaceRequest {
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Bind a complete document batch to its logical root manifest.
     *
     * Documents are consumed in order. If an element is invalid, earlier
     * elements remain consumed and are released; later elements are untouched.
     *
     * # Errors
     * Returns a native `Error` for an invalid or already consumed document.
     */
    constructor(root_manifest: string, documents: PortableWorkspaceDocument[]);
}

/**
 * Explicit standalone grammar role selected by a WebAssembly host.
 */
export enum StandaloneAuthoringRole {
    /**
     * Root portable workspace manifest.
     */
    WorkspaceManifest = 0,
    /**
     * Reusable workspace module.
     */
    WorkspaceModule = 1,
    /**
     * Workspace-language primitive declarations.
     */
    WorkspaceLanguagePrimitives = 2,
    /**
     * Responsibility derivation declarations.
     */
    ResponsibilityDerivation = 3,
    /**
     * Organization-to-responsibility translation declarations.
     */
    OrganizationalTranslation = 4,
    /**
     * Experience-composition declarations.
     */
    ExperienceComposition = 5,
    /**
     * Exact module-resolution lock.
     */
    WorkspaceResolutionLock = 6,
    /**
     * Exact workspace-universe lock.
     */
    WorkspaceUniverseLock = 7,
    /**
     * Private capability and operation bindings.
     */
    Capabilities = 8,
    /**
     * Private machine realization and authority-root bindings.
     */
    MachineBinding = 9,
    /**
     * Exact admitted distribution identities.
     */
    DistributionLock = 10,
    /**
     * Package manifest and resource inventory.
     */
    PackageManifest = 11,
    /**
     * Package doctrine declarations.
     */
    PackageDoctrine = 12,
    /**
     * Package operation declarations.
     */
    PackageOperations = 13,
    /**
     * Package role declarations.
     */
    PackageRoles = 14,
    /**
     * Package stack declarations.
     */
    PackageStacks = 15,
    /**
     * Package run-mode declarations.
     */
    PackageRunModes = 16,
    /**
     * Package policy-family declaration.
     */
    PackagePolicyFamily = 17,
    /**
     * Package governing-order declaration.
     */
    PackageGoverningOrder = 18,
    /**
     * Package capability-policy declaration.
     */
    PackageCapabilityPolicy = 19,
    /**
     * Package tool-recipe declaration.
     */
    PackageToolRecipe = 20,
}

/**
 * Canonical result of structural document validation.
 */
export class ValidatedContractDocument {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Copy the RFC 8785 document bytes into one owned `Uint8Array`.
     */
    readonly canonicalBytes: Uint8Array;
    /**
     * Admitted descriptor-registry identity.
     */
    readonly schemaId: string;
    /**
     * SHA-256 of the schema that admitted the document.
     */
    readonly schemaSha256: string;
}

/**
 * One complete typed fact on a shortest causal path.
 */
export class WorkspaceCausalStep {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Exact produced fact.
     */
    fact(): WorkspaceFact;
    /**
     * Exact provenance.
     */
    provenance(): WorkspaceProvenance;
    /**
     * Deterministic rule.
     */
    rule(): WorkspaceDerivationRule;
    /**
     * Semantic subject.
     */
    subject(): WorkspaceSubject;
    /**
     * Exact proof-node digest.
     */
    readonly nodeDigest: string;
}

/**
 * Closed source transition.
 */
export enum WorkspaceChangeKind {
    /**
     * Added fact.
     */
    Added = 0,
    /**
     * Modified fact.
     */
    Modified = 1,
    /**
     * Removed fact.
     */
    Removed = 2,
}

/**
 * One exact source-change root from a verified comparison receipt.
 */
export class WorkspaceChangeRoot {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Exact current fact, absent only for a removed root.
     */
    currentFact(): WorkspaceFact | undefined;
    /**
     * Closed transition.
     */
    kind(): WorkspaceChangeKind;
    /**
     * Exact predecessor fact, absent only for an added root.
     */
    priorFact(): WorkspaceFact | undefined;
    /**
     * Clone the typed subject for inspection or explanation.
     */
    subject(): WorkspaceSubject;
    /**
     * Content address of the exact root.
     */
    readonly rootDigest: string;
}

/**
 * One bounded page of exact change roots.
 */
export class WorkspaceChangeRootPage {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Copy the SDK's exact canonical page without reconstructing typed entries.
     */
    canonicalBytes(): Uint8Array;
    /**
     * Consume the page and return its owned entries in canonical order.
     */
    intoEntries(): WorkspaceChangeRoot[];
    /**
     * Next exact offset, or `undefined` at the end.
     */
    readonly nextOffset: number | undefined;
}

/**
 * Closed deterministic derivation rule.
 */
export enum WorkspaceDerivationRule {
    /**
     * Source admission.
     */
    SourceAdmission = 0,
    /**
     * Component admission.
     */
    ComponentAdmission = 1,
    /**
     * Module sealing.
     */
    ModuleSealing = 2,
    /**
     * Declaration linking.
     */
    DeclarationLinking = 3,
    /**
     * Import linking.
     */
    ImportLinking = 4,
    /**
     * Extension application.
     */
    ExtensionApplication = 5,
    /**
     * Policy composition.
     */
    PolicyComposition = 6,
    /**
     * Responsibility lowering.
     */
    ResponsibilityLowering = 7,
    /**
     * Organizational translation.
     */
    OrganizationalTranslation = 8,
    /**
     * Experience composition.
     */
    ExperienceComposition = 9,
    /**
     * Resource selection.
     */
    ResourceSelection = 10,
    /**
     * Resolution locking.
     */
    ResolutionLocking = 11,
    /**
     * Universe locking.
     */
    UniverseLocking = 12,
    /**
     * Semantic-IR sealing.
     */
    SemanticIrSealing = 13,
}

/**
 * Deterministic causal explanation for one comparison subject.
 */
export class WorkspaceExplanation {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Copy the SDK's exact canonical explanation, including its causal witness.
     */
    canonicalBytes(): Uint8Array;
    /**
     * Proof DAG frontier, when affected.
     */
    frontier(): WorkspaceExplanationFrontier | undefined;
    /**
     * Deterministically selected root, when affected.
     */
    root(): WorkspaceChangeRoot | undefined;
    /**
     * Exact query outcome.
     */
    state(): WorkspaceExplanationState;
    /**
     * Complete shortest typed proof sequence.
     */
    steps(): WorkspaceCausalStep[];
    /**
     * Clone the typed query subject.
     */
    subject(): WorkspaceSubject;
}

/**
 * Proof DAG frontier.
 */
export enum WorkspaceExplanationFrontier {
    /**
     * Predecessor DAG.
     */
    Predecessor = 0,
    /**
     * Current DAG.
     */
    Current = 1,
}

/**
 * Closed explanation state.
 */
export enum WorkspaceExplanationState {
    /**
     * Subject absent.
     */
    NotPresent = 0,
    /**
     * Present and unaffected.
     */
    Unaffected = 1,
    /**
     * Present with a witness.
     */
    Affected = 2,
}

/**
 * Lossless typed fact projection for a root or causal step.
 */
export class WorkspaceFact {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Closed fact family.
     */
    kind(): WorkspaceFactKind;
    /**
     * Source byte length.
     */
    readonly byteLen: number | undefined;
    /**
     * Closure digest.
     */
    readonly closureDigest: string | undefined;
    /**
     * Component digest.
     */
    readonly componentDigest: string | undefined;
    /**
     * Module digest.
     */
    readonly moduleDigest: string | undefined;
    /**
     * Resolution-lock digest.
     */
    readonly resolutionDigest: string | undefined;
    /**
     * Source digest.
     */
    readonly sourceDigest: string | undefined;
    /**
     * Source path.
     */
    readonly sourcePath: string | undefined;
    /**
     * Import-surface digest.
     */
    readonly surfaceDigest: string | undefined;
    /**
     * Universe-lock digest.
     */
    readonly universeDigest: string | undefined;
    /**
     * Value digest.
     */
    readonly valueDigest: string | undefined;
    /**
     * Workspace semantic-IR digest.
     */
    readonly workspaceSemanticIrDigest: string | undefined;
}

/**
 * Closed derivation-fact family.
 */
export enum WorkspaceFactKind {
    /**
     * Source content.
     */
    SourceContent = 0,
    /**
     * Component.
     */
    Component = 1,
    /**
     * Module.
     */
    Module = 2,
    /**
     * Declaration.
     */
    Declaration = 3,
    /**
     * Import surface.
     */
    ImportSurface = 4,
    /**
     * Extension.
     */
    Extension = 5,
    /**
     * Effective policy.
     */
    EffectivePolicy = 6,
    /**
     * Responsibility closure.
     */
    ResponsibilityClosure = 7,
    /**
     * Organizational-translation closure.
     */
    OrganizationalTranslationClosure = 8,
    /**
     * Experience composition.
     */
    ExperienceComposition = 9,
    /**
     * Resource.
     */
    Resource = 10,
    /**
     * Resolution lock.
     */
    ResolutionLock = 11,
    /**
     * Universe lock.
     */
    UniverseLock = 12,
    /**
     * Semantic IR.
     */
    SemanticIr = 13,
}

/**
 * One current subject in the complete reachability partition.
 */
export class WorkspaceImpact {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Root-backed reachability classification.
     */
    state(): WorkspaceImpactState;
    /**
     * Clone the typed subject for inspection or explanation.
     */
    subject(): WorkspaceSubject;
    /**
     * Exact count of roots whose closure reaches this subject.
     */
    readonly contributingRootCount: number;
}

/**
 * One bounded page of the complete impact partition.
 */
export class WorkspaceImpactPage {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Copy the SDK's exact canonical page without reconstructing typed entries.
     */
    canonicalBytes(): Uint8Array;
    /**
     * Consume the page and return its owned entries in canonical order.
     */
    intoEntries(): WorkspaceImpact[];
    /**
     * Next exact offset, or `undefined` at the end.
     */
    readonly nextOffset: number | undefined;
}

/**
 * Closed impact classification.
 */
export enum WorkspaceImpactState {
    /**
     * Root-reachable.
     */
    Affected = 0,
    /**
     * Outside every root closure.
     */
    Unaffected = 1,
}

/**
 * Lossless provenance projection for one causal step.
 */
export class WorkspaceProvenance {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Closed provenance family.
     */
    kind(): WorkspaceProvenanceKind;
    /**
     * Selected export identity.
     */
    readonly exportId: string | undefined;
    /**
     * Extension namespace identity.
     */
    readonly extensionNamespaceId: string | undefined;
    /**
     * Importer module identity.
     */
    readonly importerModuleId: string | undefined;
    /**
     * Local namespace identity.
     */
    readonly localNamespaceId: string | undefined;
    /**
     * Selected module digest.
     */
    readonly moduleDigest: string | undefined;
    /**
     * Module or extension owner identity.
     */
    readonly moduleId: string | undefined;
    /**
     * Selected release identity.
     */
    readonly releaseId: string | undefined;
    /**
     * Direct source identity.
     */
    readonly sourceId: string | undefined;
    /**
     * Upstream namespace identity.
     */
    readonly sourceNamespaceId: string | undefined;
    /**
     * Extension target declaration identity.
     */
    readonly targetDeclarationId: string | undefined;
    /**
     * Extension target namespace identity.
     */
    readonly targetNamespaceId: string | undefined;
    /**
     * Upstream module identity.
     */
    readonly upstreamModuleId: string | undefined;
    /**
     * Upstream release identity.
     */
    readonly upstreamReleaseId: string | undefined;
}

/**
 * Closed provenance family.
 */
export enum WorkspaceProvenanceKind {
    /**
     * Direct source.
     */
    Source = 0,
    /**
     * Selected module release.
     */
    ModuleRelease = 1,
    /**
     * Resolved import.
     */
    Import = 2,
    /**
     * Workspace extension.
     */
    Extension = 3,
    /**
     * Compiler aggregate.
     */
    Compilation = 4,
}

/**
 * Opaque typed subject coordinate emitted by verified comparison evidence.
 */
export class WorkspaceSubject {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Return the closed coordinate family.
     */
    kind(): WorkspaceSubjectKind;
    /**
     * Component identity, when this is a component subject.
     */
    readonly componentId: string | undefined;
    /**
     * Local declaration identity, when carried by this subject.
     */
    readonly declarationId: string | undefined;
    /**
     * Namespace of a declaration-like subject.
     */
    readonly declarationNamespaceId: string | undefined;
    /**
     * Selected export identity, when carried.
     */
    readonly exportId: string | undefined;
    /**
     * Extension namespace identity, when carried.
     */
    readonly extensionNamespaceId: string | undefined;
    /**
     * Importer module identity, when carried.
     */
    readonly importerModuleId: string | undefined;
    /**
     * Importer-local namespace identity, when carried.
     */
    readonly localNamespaceId: string | undefined;
    /**
     * Module identity, when this is a module subject.
     */
    readonly moduleId: string | undefined;
    /**
     * Owning module for declaration-like subjects.
     */
    readonly ownerModuleId: string | undefined;
    /**
     * Resource identity, when carried.
     */
    readonly resourceId: string | undefined;
    /**
     * Receipt-local source identity, when this is a source subject.
     */
    readonly sourceId: string | undefined;
    /**
     * Upstream namespace identity, when carried.
     */
    readonly sourceNamespaceId: string | undefined;
    /**
     * Upstream module identity, when carried.
     */
    readonly upstreamModuleId: string | undefined;
    /**
     * Upstream release identity, when carried.
     */
    readonly upstreamReleaseId: string | undefined;
    /**
     * Workspace identity, when this is the complete workspace subject.
     */
    readonly workspaceId: string | undefined;
}

/**
 * Owned SDK answer for one subject, not another retained compilation.
 *
 * The receipt joins the parent comparison's prior/current identities. This
 * result and copied facts remain usable after the parent is freed. Free each
 * returned handle when finished; no handle grants disclosure or effect authority.
 */
export class WorkspaceSubjectComparison {
    private constructor();
    free(): void;
    [Symbol.dispose](): void;
    /**
     * Copy the SDK's exact canonical bytes without parsing or re-encoding them.
     */
    canonicalBytes(): Uint8Array;
    /**
     * Return equality only for shared membership; otherwise return no value.
     *
     * An affected subject can still have equal outputs.
     */
    comparison(): WorkspaceValueComparison | undefined;
    /**
     * Copy the current fact for current-only or shared membership.
     *
     * Returns no handle for absent or prior-only membership.
     */
    currentFact(): WorkspaceFact | undefined;
    /**
     * Identify which sides contain a value, without deriving equality.
     */
    membership(): WorkspaceSubjectMembership;
    /**
     * Copy the predecessor fact for prior-only or shared membership.
     *
     * Returns no handle for absent or current-only membership.
     */
    priorFact(): WorkspaceFact | undefined;
    /**
     * Copy the full subject, including all compound identity fields.
     */
    subject(): WorkspaceSubject;
    /**
     * Identity of the parent comparison that produced this answer.
     */
    readonly receiptDigest: string;
}

/**
 * Closed workspace-subject family.
 */
export enum WorkspaceSubjectKind {
    /**
     * Logical source.
     */
    Source = 0,
    /**
     * Semantic component.
     */
    Component = 1,
    /**
     * Selected module.
     */
    Module = 2,
    /**
     * Declaration.
     */
    Declaration = 3,
    /**
     * Import path.
     */
    Import = 4,
    /**
     * Extension rule.
     */
    Extension = 5,
    /**
     * Effective policy.
     */
    Policy = 6,
    /**
     * Responsibility closure.
     */
    ResponsibilityClosure = 7,
    /**
     * Organizational-translation closure.
     */
    OrganizationalTranslationClosure = 8,
    /**
     * Experience composition.
     */
    ExperienceComposition = 9,
    /**
     * Selected resource.
     */
    Resource = 10,
    /**
     * Resolution lock.
     */
    ResolutionLock = 11,
    /**
     * Universe lock.
     */
    UniverseLock = 12,
    /**
     * Whole workspace.
     */
    Workspace = 13,
}

/**
 * Subject membership in the comparison's predecessor and current compilations.
 */
export enum WorkspaceSubjectMembership {
    /**
     * Neither compilation contains the subject.
     */
    Absent = 0,
    /**
     * Only the predecessor contains the subject.
     */
    PriorOnly = 1,
    /**
     * Only the current compilation contains the subject.
     */
    CurrentOnly = 2,
    /**
     * Both compilations contain the subject.
     */
    Shared = 3,
}

/**
 * Equality of shared compiler outputs, independent of dependency impact.
 */
export enum WorkspaceValueComparison {
    /**
     * Both typed outputs are equal.
     */
    Equal = 0,
    /**
     * The typed outputs differ.
     */
    Changed = 1,
}
```
