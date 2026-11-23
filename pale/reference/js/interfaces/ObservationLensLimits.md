---
title: "Interface: ObservationLensLimits"
---

<a id="interface&#45;observationlenslimits"></a>

Work and copy limits for one observation\-lens step\.

A returned cursor binds these limits to the exact snapshot and filter\.
Reaching a limit does not prove that later subjects are absent\.

## Properties {#properties}

### maximumCausalPathLookups {#maximumcausalpathlookups}

```ts
maximumCausalPathLookups: number;
```

Maximum retained causal paths this step can look up\.

-----

### maximumCausalSteps {#maximumcausalsteps}

```ts
maximumCausalSteps: number;
```

Maximum causal steps this step can copy\.

-----

### maximumCopiedStringBytes {#maximumcopiedstringbytes}

```ts
maximumCopiedStringBytes: number;
```

Maximum UTF\-8 string bytes this step can copy\.

-----

### maximumInspected {#maximuminspected}

```ts
maximumInspected: number;
```

Maximum subjects this step can inspect\.

-----

### maximumNodes {#maximumnodes}

```ts
maximumNodes: number;
```

Maximum lens nodes this step can copy\.
