---
title: "Type Alias: EffectiveProfileResponsibility"
---

<a id="type&#45;alias&#45;effectiveprofileresponsibility"></a>

```ts
type EffectiveProfileResponsibility = 
  | {
  kind: "communication";
}
  | {
  kind: "organizational-work";
}
  | {
  kind: "crm-business-state";
}
  | {
  kind: "engineering-execution";
}
  | {
  kind: "context-memory";
}
  | {
  kind: "terminal-harness-execution";
}
  | {
  kind: "native-event-publication";
}
  | {
  kind: "native-effect-read-back";
}
  | {
  contractId: string;
  kind: "extension";
  namespaceId: string;
  schemaId: string;
  schemaSha256: string;
};
```

Assigned responsibility with required pin fields only for an extension\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "communication";
}
```

-----

### Type Literal {#type-literal-1}

```ts
{
  kind: "organizational-work";
}
```

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "crm-business-state";
}
```

-----

### Type Literal {#type-literal-3}

```ts
{
  kind: "engineering-execution";
}
```

-----

### Type Literal {#type-literal-4}

```ts
{
  kind: "context-memory";
}
```

-----

### Type Literal {#type-literal-5}

```ts
{
  kind: "terminal-harness-execution";
}
```

-----

### Type Literal {#type-literal-6}

```ts
{
  kind: "native-event-publication";
}
```

-----

### Type Literal {#type-literal-7}

```ts
{
  kind: "native-effect-read-back";
}
```

-----

### Type Literal {#type-literal-8}

```ts
{
  contractId: string;
  kind: "extension";
  namespaceId: string;
  schemaId: string;
  schemaSha256: string;
}
```

#### contractId {#contractid}

```ts
contractId: string;
```

Extension contract identity\.

#### kind {#kind}

```ts
kind: "extension";
```

#### namespaceId {#namespaceid}

```ts
namespaceId: string;
```

Governing vocabulary namespace\.

#### schemaId {#schemaid}

```ts
schemaId: string;
```

Exact admitted schema member\.

#### schemaSha256 {#schemasha256}

```ts
schemaSha256: string;
```

Digest of the exact schema bytes\.
