---
title: "Interface: LocalOneShotPlanCounts"
---

<a id="interface&#45;localoneshotplancounts"></a>

Flat transition counts derived from one complete local plan\.

## Properties {#properties}

### adopt {#adopt}

```ts
adopt: number;
```

Number of explicit adoption transitions\.

-----

### baseline {#baseline}

```ts
baseline: number;
```

Number of observed repository targets\.

-----

### create {#create}

```ts
create: number;
```

Number of create transitions\.

-----

### deferredEffects {#deferredeffects}

```ts
deferredEffects: number;
```

Number of deliberately deferred effects\.

-----

### delete {#delete}

```ts
delete: number;
```

Number of deletion transitions\.

-----

### machineLocalEffects {#machinelocaleffects}

```ts
machineLocalEffects: number;
```

Number of bound machine\-local effects\.

-----

### operations {#operations}

```ts
operations: number;
```

Number of repository\-surface operations\.

-----

### splice {#splice}

```ts
splice: number;
```

Number of managed\-block splice transitions\.

-----

### totalOperations {#totaloperations}

```ts
totalOperations: number;
```

Total repository\-surface and machine\-local operations\.

-----

### unchanged {#unchanged}

```ts
unchanged: number;
```

Number of unchanged surfaces\.

-----

### update {#update}

```ts
update: number;
```

Number of replacement transitions\.
