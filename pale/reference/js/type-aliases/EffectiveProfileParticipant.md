---
title: "Type Alias: EffectiveProfileParticipant"
---

<a id="type&#45;alias&#45;effectiveprofileparticipant"></a>

```ts
type EffectiveProfileParticipant = 
  | {
  interfaceId: string;
  kind: "interface";
}
  | {
  applicationId: string;
  kind: "application";
}
  | {
  engineId: string;
  kind: "engine";
}
  | {
  capabilityId: string;
  kind: "capability";
}
  | {
  kind: "terminal-leaf";
  terminalLeafId: string;
}
  | {
  kind: "plugin";
  pluginId: string;
}
  | {
  kind: "skill";
  skillId: string;
};
```

Exact participant identity, narrowed by its `kind` in JavaScript\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  interfaceId: string;
  kind: "interface";
}
```

#### interfaceId {#interfaceid}

```ts
interfaceId: string;
```

Interface identity\.

#### kind {#kind}

```ts
kind: "interface";
```

-----

### Type Literal {#type-literal-1}

```ts
{
  applicationId: string;
  kind: "application";
}
```

#### applicationId {#applicationid}

```ts
applicationId: string;
```

Application identity\.

#### kind {#kind-1}

```ts
kind: "application";
```

-----

### Type Literal {#type-literal-2}

```ts
{
  engineId: string;
  kind: "engine";
}
```

#### engineId {#engineid}

```ts
engineId: string;
```

Stable identity carried by the `engine` wire variant\.

#### kind {#kind-2}

```ts
kind: "engine";
```

-----

### Type Literal {#type-literal-3}

```ts
{
  capabilityId: string;
  kind: "capability";
}
```

#### capabilityId {#capabilityid}

```ts
capabilityId: string;
```

Capability identity\.

#### kind {#kind-3}

```ts
kind: "capability";
```

-----

### Type Literal {#type-literal-4}

```ts
{
  kind: "terminal-leaf";
  terminalLeafId: string;
}
```

#### kind {#kind-4}

```ts
kind: "terminal-leaf";
```

#### terminalLeafId {#terminalleafid}

```ts
terminalLeafId: string;
```

Terminal\-leaf identity\.

-----

### Type Literal {#type-literal-5}

```ts
{
  kind: "plugin";
  pluginId: string;
}
```

#### kind {#kind-5}

```ts
kind: "plugin";
```

#### pluginId {#pluginid}

```ts
pluginId: string;
```

Plugin identity\.

-----

### Type Literal {#type-literal-6}

```ts
{
  kind: "skill";
  skillId: string;
}
```

#### kind {#kind-6}

```ts
kind: "skill";
```

#### skillId {#skillid}

```ts
skillId: string;
```

Skill identity\.
