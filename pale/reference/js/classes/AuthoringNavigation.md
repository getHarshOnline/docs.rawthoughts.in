---
title: "Class: AuthoringNavigation"
---

<a id="class&#45;authoringnavigation"></a>

Retained semantic\-navigation result from one admitted compilation\.

## Accessors {#accessors}

### alternativesTruncated {#alternativestruncated}

#### Get Signature {#get-signature}

```ts
get alternativesTruncated(): boolean;
```

Whether the API completion ceiling omitted identities\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

-----

### occurrenceRole {#occurrencerole}

#### Get Signature {#get-signature-1}

```ts
get occurrenceRole(): 
  | AuthoringOccurrenceRole
  | null;
```

Exact semantic role of the queried occurrence\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

\| [`AuthoringOccurrenceRole`](/pale/reference/js/enumerations/AuthoringOccurrenceRole)
\| `null`

-----

### referencesTruncated {#referencestruncated}

#### Get Signature {#get-signature-2}

```ts
get referencesTruncated(): boolean;
```

Whether the API reference ceiling omitted occurrences\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

## Methods {#methods}

### alternatives\(\) {#alternatives}

```ts
alternatives(): AuthoringIdentity[];
```

Same\-namespace identities eligible for value completion\.

#### Returns {#returns-3}

[`AuthoringIdentity`](/pale/reference/js/classes/AuthoringIdentity)\[\]

-----

### definition\(\) {#definition}

```ts
definition(): 
  | AuthoringSourceLocation
  | null;
```

Canonical definition retained by the compilation, when one exists\.

# Errors {#errors}

Returns an internal projection error only if an API\-owned array index
cannot be represented by the Node `uint32` path ABI\.

#### Returns {#returns-4}

\| [`AuthoringSourceLocation`](/pale/reference/js/interfaces/AuthoringSourceLocation)
\| `null`

-----

### identity\(\) {#identity}

```ts
identity(): AuthoringIdentity | null;
```

Resolved identity, or `None` for a structural\-only coordinate\.

#### Returns {#returns-5}

[`AuthoringIdentity`](/pale/reference/js/classes/AuthoringIdentity) \| `null`

-----

### references\(\) {#references}

```ts
references(): AuthoringSourceLocation[];
```

Deterministically ordered retained reference locations\.

# Errors {#errors-1}

Returns an internal projection error only if an API\-owned array index
cannot be represented by the Node `uint32` path ABI\.

#### Returns {#returns-6}

[`AuthoringSourceLocation`](/pale/reference/js/interfaces/AuthoringSourceLocation)\[\]
