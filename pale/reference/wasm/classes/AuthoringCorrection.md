---
title: "Class: AuthoringCorrection"
---

<a id="class&#45;authoringcorrection"></a>

Proposed source edit from a rejected configuration check\.

Match the expected source at the supplied path before using the replacement\.
This value preserves the compiler's proposal; it does not authorize a write\.

## Properties {#properties}

### diagnosticIdentity {#diagnosticidentity}

```ts
readonly diagnosticIdentity: string;
```

Return the identity of the rejected diagnostic, without recomputing it\.

-----

### expectedSource {#expectedsource}

```ts
readonly expectedSource: string;
```

Return the exact scalar text that must still occupy the edit range\.

-----

### replacementSource {#replacementsource}

```ts
readonly replacementSource: string;
```

Return the replacement scalar text selected by the compiler\.

-----

### sourceLabel {#sourcelabel}

```ts
readonly sourceLabel: string;
```

Return the logical label of the source to edit\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-1}

`void`

-----

### kind\(\) {#kind}

```ts
kind(): NarrowImportVisibility;
```

Return the compiler\-proved correction kind\.

#### Returns {#returns-2}

[`NarrowImportVisibility`](/pale/reference/wasm/enumerations/AuthoringCorrectionKind#narrowimportvisibility)

-----

### path\(\) {#path}

```ts
path(): AuthoringInstancePathSegment[];
```

Return the ordered field and array\-index steps to the source value\.

#### Returns {#returns-3}

[`AuthoringInstancePathSegment`](/pale/reference/wasm/classes/AuthoringInstancePathSegment)\[\]

-----

### proofSubject\(\) {#proofsubject}

```ts
proofSubject(): AuthoringIdentity;
```

Return the semantic subject that proves this correction\.

#### Returns {#returns-4}

[`AuthoringIdentity`](/pale/reference/wasm/classes/AuthoringIdentity)
