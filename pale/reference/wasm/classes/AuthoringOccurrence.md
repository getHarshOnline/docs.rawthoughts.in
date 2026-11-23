---
title: "Class: AuthoringOccurrence"
---

<a id="class&#45;authoringoccurrence"></a>

Compiler\-produced location and role, without source text\.

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

### location\(\) {#location}

```ts
location(): AuthoringSourceLocation;
```

Copy the logical source label and decoded field/index path\.

#### Returns {#returns-2}

[`AuthoringSourceLocation`](/pale/reference/wasm/classes/AuthoringSourceLocation)

-----

### role\(\) {#role}

```ts
role(): AuthoringOccurrenceRole;
```

Definition, reference, or projection role assigned by the compiler\.

#### Returns {#returns-3}

[`AuthoringOccurrenceRole`](/pale/reference/wasm/enumerations/AuthoringOccurrenceRole)
