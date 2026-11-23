---
title: "Type Alias: EffectiveProfileSelection"
---

<a id="type&#45;alias&#45;effectiveprofileselection"></a>

```ts
type EffectiveProfileSelection = 
  | {
  contentDigest: string;
  kind: "package";
  packageId: string;
  version: string;
}
  | {
  attestorId: string;
  contentDigest: string;
  kind: "normative-pack";
  packId: string;
  version: string;
}
  | {
  kind: "semantic-resource";
  repositoryId: string;
  resourceId: string;
  resourceKind: EffectiveProfileResourceKind;
}
  | {
  kind: "run-policy";
  runPolicyId: string;
}
  | {
  activationPathCount: number;
  activationRootCount: number;
  additionalRootCount: number;
  executionWorkspaceId: string;
  kind: "session";
}
  | {
  actionId: string;
  eventId: string;
  kind: "lifecycle";
  lifecycleId: string;
}
  | {
  authorityRootId: string;
  kind: "authority-root";
}
  | {
  authorityCoordinate: string;
  kind: "disclosure-ceiling";
};
```

Exact compiler\-selected coordinate, narrowed by its literal `kind`\.

Every field belongs to its selected variant and is required\. These copied
outputs describe configuration; they do not admit sources or authorize effects\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  contentDigest: string;
  kind: "package";
  packageId: string;
  version: string;
}
```

#### contentDigest {#contentdigest}

```ts
contentDigest: string;
```

Exact Package release digest\.

#### kind {#kind}

```ts
kind: "package";
```

#### packageId {#packageid}

```ts
packageId: string;
```

Package identity\.

#### version {#version}

```ts
version: string;
```

Selected Package version\.

-----

### Type Literal {#type-literal-1}

```ts
{
  attestorId: string;
  contentDigest: string;
  kind: "normative-pack";
  packId: string;
  version: string;
}
```

#### attestorId {#attestorid}

```ts
attestorId: string;
```

Attestor owning the release statement\.

#### contentDigest {#contentdigest-1}

```ts
contentDigest: string;
```

Exact Pack release digest\.

#### kind {#kind-1}

```ts
kind: "normative-pack";
```

#### packId {#packid}

```ts
packId: string;
```

Normative Pack identity\.

#### version {#version-1}

```ts
version: string;
```

Selected Pack version\.

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "semantic-resource";
  repositoryId: string;
  resourceId: string;
  resourceKind: EffectiveProfileResourceKind;
}
```

#### kind {#kind-2}

```ts
kind: "semantic-resource";
```

#### repositoryId {#repositoryid}

```ts
repositoryId: string;
```

Logical repository receiving the resource\.

#### resourceId {#resourceid}

```ts
resourceId: string;
```

Owner\-qualified resource identity\.

#### resourceKind {#resourcekind}

```ts
resourceKind: EffectiveProfileResourceKind;
```

Selected semantic resource family\.

-----

### Type Literal {#type-literal-3}

```ts
{
  kind: "run-policy";
  runPolicyId: string;
}
```

#### kind {#kind-3}

```ts
kind: "run-policy";
```

#### runPolicyId {#runpolicyid}

```ts
runPolicyId: string;
```

Exact run\-policy identity\.

-----

### Type Literal {#type-literal-4}

```ts
{
  activationPathCount: number;
  activationRootCount: number;
  additionalRootCount: number;
  executionWorkspaceId: string;
  kind: "session";
}
```

#### activationPathCount {#activationpathcount}

```ts
activationPathCount: number;
```

Activation\-path count, including zero\.

#### activationRootCount {#activationrootcount}

```ts
activationRootCount: number;
```

Activation\-root count, including zero\.

#### additionalRootCount {#additionalrootcount}

```ts
additionalRootCount: number;
```

Additional\-root count, including zero\.

#### executionWorkspaceId {#executionworkspaceid}

```ts
executionWorkspaceId: string;
```

Execution workspace owning the selection\.

#### kind {#kind-4}

```ts
kind: "session";
```

-----

### Type Literal {#type-literal-5}

```ts
{
  actionId: string;
  eventId: string;
  kind: "lifecycle";
  lifecycleId: string;
}
```

#### actionId {#actionid}

```ts
actionId: string;
```

Lifecycle action identity\.

#### eventId {#eventid}

```ts
eventId: string;
```

Lifecycle event identity\.

#### kind {#kind-5}

```ts
kind: "lifecycle";
```

#### lifecycleId {#lifecycleid}

```ts
lifecycleId: string;
```

Lifecycle behavior identity\.

-----

### Type Literal {#type-literal-6}

```ts
{
  authorityRootId: string;
  kind: "authority-root";
}
```

#### authorityRootId {#authorityrootid}

```ts
authorityRootId: string;
```

Exact authority\-root identity\.

#### kind {#kind-6}

```ts
kind: "authority-root";
```

-----

### Type Literal {#type-literal-7}

```ts
{
  authorityCoordinate: string;
  kind: "disclosure-ceiling";
}
```

#### authorityCoordinate {#authoritycoordinate}

```ts
authorityCoordinate: string;
```

Exact authority coordinate\.

#### kind {#kind-7}

```ts
kind: "disclosure-ceiling";
```
