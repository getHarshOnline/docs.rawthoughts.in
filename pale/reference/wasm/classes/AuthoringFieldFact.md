---
title: "Class: AuthoringFieldFact"
---

<a id="class&#45;authoringfieldfact"></a>

One child key offered at the selected structural path\.

## Properties {#properties}

### description {#description}

```ts
readonly description: string | undefined;
```

Return producer documentation for this field\.

-----

### name {#name}

```ts
readonly name: string;
```

Return the exact authored key spelling\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### allowedValues\(\) {#allowedvalues}

```ts
allowedValues(): AuthoringLiteralFact[];
```

Return the complete bounded literal vocabulary\.

#### Returns {#returns-1}

[`AuthoringLiteralFact`](/pale/reference/wasm/classes/AuthoringLiteralFact)\[\]

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-2}

`void`

-----

### presence\(\) {#presence}

```ts
presence(): AuthoringFieldPresence;
```

Return requiredness across applicable structural variants\.

#### Returns {#returns-3}

[`AuthoringFieldPresence`](/pale/reference/wasm/enumerations/AuthoringFieldPresence)

-----

### valueKinds\(\) {#valuekinds}

```ts
valueKinds(): AuthoringValueKind[];
```

Return all admitted structural value categories in stable order\.

#### Returns {#returns-4}

[`AuthoringValueKind`](/pale/reference/wasm/enumerations/AuthoringValueKind)\[\]
