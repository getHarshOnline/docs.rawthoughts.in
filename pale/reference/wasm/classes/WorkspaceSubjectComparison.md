---
title: "Class: WorkspaceSubjectComparison"
---

<a id="class&#45;workspacesubjectcomparison"></a>

Owned SDK answer for one subject, not another retained compilation\.

The receipt joins the parent comparison's prior/current identities\. This
result and copied facts remain usable after the parent is freed\. Free each
returned handle when finished; no handle grants disclosure or effect authority\.

## Properties {#properties}

### receiptDigest {#receiptdigest}

```ts
readonly receiptDigest: string;
```

Identity of the parent comparison that produced this answer\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### canonicalBytes\(\) {#canonicalbytes}

```ts
canonicalBytes(): Uint8Array;
```

Copy the SDK's exact canonical bytes without parsing or re\-encoding them\.

#### Returns {#returns-1}

`Uint8Array`

-----

### comparison\(\) {#comparison}

```ts
comparison(): 
  | WorkspaceValueComparison
  | undefined;
```

Return equality only for shared membership; otherwise return no value\.

An affected subject can still have equal outputs\.

#### Returns {#returns-2}

\| [`WorkspaceValueComparison`](/pale/reference/wasm/enumerations/WorkspaceValueComparison)
\| `undefined`

-----

### currentFact\(\) {#currentfact}

```ts
currentFact(): WorkspaceFact | undefined;
```

Copy the current fact for current\-only or shared membership\.

Returns no handle for absent or prior\-only membership\.

#### Returns {#returns-3}

[`WorkspaceFact`](/pale/reference/wasm/classes/WorkspaceFact) \| `undefined`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-4}

`void`

-----

### membership\(\) {#membership}

```ts
membership(): WorkspaceSubjectMembership;
```

Identify which sides contain a value, without deriving equality\.

#### Returns {#returns-5}

[`WorkspaceSubjectMembership`](/pale/reference/wasm/enumerations/WorkspaceSubjectMembership)

-----

### priorFact\(\) {#priorfact}

```ts
priorFact(): WorkspaceFact | undefined;
```

Copy the predecessor fact for prior\-only or shared membership\.

Returns no handle for absent or current\-only membership\.

#### Returns {#returns-6}

[`WorkspaceFact`](/pale/reference/wasm/classes/WorkspaceFact) \| `undefined`

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Copy the full subject, including all compound identity fields\.

#### Returns {#returns-7}

[`WorkspaceSubject`](/pale/reference/wasm/classes/WorkspaceSubject)
