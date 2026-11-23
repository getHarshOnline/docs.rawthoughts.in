---
title: "Class: AuthoringInspection"
---

<a id="class&#45;authoringinspection"></a>

Complete source\-role and schema\-derived response for one authoring request\.

## Properties {#properties}

### definition {#definition}

```ts
readonly definition: string | undefined;
```

Return the selected named definition for a shared grammar\.

-----

### schemaId {#schemaid}

```ts
readonly schemaId: string | undefined;
```

Return the selected grammar descriptor identity\.

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

### node\(\) {#node}

```ts
node(): AuthoringNodeFact | undefined;
```

Return structural facts only when the state is available\.

#### Returns {#returns-2}

[`AuthoringNodeFact`](/pale/reference/wasm/classes/AuthoringNodeFact) \| `undefined`

-----

### state\(\) {#state}

```ts
state(): AuthoringInspectionState;
```

Return availability for the exact request\.

#### Returns {#returns-3}

[`AuthoringInspectionState`](/pale/reference/wasm/enumerations/AuthoringInspectionState)
