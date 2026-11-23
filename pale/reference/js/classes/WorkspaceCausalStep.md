---
title: "Class: WorkspaceCausalStep"
---

<a id="class&#45;workspacecausalstep"></a>

One complete typed compiler fact with its derivation and provenance\.

## Accessors {#accessors}

### nodeDigest {#nodedigest}

#### Get Signature {#get-signature}

```ts
get nodeDigest(): string;
```

Exact content address of this proof fact\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`string`

-----

### rule {#rule}

#### Get Signature {#get-signature-1}

```ts
get rule(): WorkspaceDerivationRule;
```

Closed deterministic compiler rule\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`WorkspaceDerivationRule`](/pale/reference/js/enumerations/WorkspaceDerivationRule)

## Methods {#methods}

### fact\(\) {#fact}

```ts
fact(): WorkspaceFact;
```

Project the exact typed fact produced by the rule\.

#### Returns {#returns-2}

[`WorkspaceFact`](/pale/reference/js/interfaces/WorkspaceFact)

-----

### provenance\(\) {#provenance}

```ts
provenance(): WorkspaceProvenance;
```

Project the exact provenance classification\.

#### Returns {#returns-3}

[`WorkspaceProvenance`](/pale/reference/js/interfaces/WorkspaceProvenance)

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject;
```

Clone the semantic subject produced at this step\.

#### Returns {#returns-4}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject)
