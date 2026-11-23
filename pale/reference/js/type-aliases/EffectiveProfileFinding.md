---
title: "Type Alias: EffectiveProfileFinding"
---

<a id="type&#45;alias&#45;effectiveprofilefinding"></a>

```ts
type EffectiveProfileFinding = 
  | {
  kind: "native-realization-unknown";
  machineId: string;
}
  | {
  kind: "operation-unbound";
  operationId: string;
  repositoryId: string;
}
  | {
  capabilityId: string;
  disposition: RequirementDisposition;
  kind: "requirement";
  operationId: string;
  repositoryId: string;
  requirementId: string;
};
```

Copied application finding with only the selected variant's required fields\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "native-realization-unknown";
  machineId: string;
}
```

#### kind {#kind}

```ts
kind: "native-realization-unknown";
```

#### machineId {#machineid}

```ts
machineId: string;
```

Selected private machine\-binding identity\.

-----

### Type Literal {#type-literal-1}

```ts
{
  kind: "operation-unbound";
  operationId: string;
  repositoryId: string;
}
```

#### kind {#kind-1}

```ts
kind: "operation-unbound";
```

#### operationId {#operationid}

```ts
operationId: string;
```

Owner\-qualified operation identity\.

#### repositoryId {#repositoryid}

```ts
repositoryId: string;
```

Logical repository containing the occurrence\.

-----

### Type Literal {#type-literal-2}

```ts
{
  capabilityId: string;
  disposition: RequirementDisposition;
  kind: "requirement";
  operationId: string;
  repositoryId: string;
  requirementId: string;
}
```

#### capabilityId {#capabilityid}

```ts
capabilityId: string;
```

Portable capability identity\.

#### disposition {#disposition}

```ts
disposition: RequirementDisposition;
```

Independent portable requirement outcome\.

#### kind {#kind-2}

```ts
kind: "requirement";
```

#### operationId {#operationid-1}

```ts
operationId: string;
```

Owner\-qualified operation identity\.

#### repositoryId {#repositoryid-1}

```ts
repositoryId: string;
```

Logical repository containing the occurrence\.

#### requirementId {#requirementid}

```ts
requirementId: string;
```

Requirement identity local to the operation\.
