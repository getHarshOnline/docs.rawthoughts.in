---
title: "Type Alias: EffectiveProfileDeclaredSelection"
---

<a id="type&#45;alias&#45;effectiveprofiledeclaredselection"></a>

```ts
type EffectiveProfileDeclaredSelection = 
  | {
  kind: "resource";
  resourceKind: EffectiveProfileResourceKind;
  selector: EffectiveProfileDeclaredSelector;
}
  | {
  axis: EffectiveProfileModeAxis;
  kind: "mode-default";
  resourceId: string;
};
```

Copied admitted declaration, distinct from its expanded effective selection\.
Required variant fields do not admit sources or authorize effects\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "resource";
  resourceKind: EffectiveProfileResourceKind;
  selector: EffectiveProfileDeclaredSelector;
}
```

#### kind {#kind}

```ts
kind: "resource";
```

#### resourceKind {#resourcekind}

```ts
resourceKind: EffectiveProfileResourceKind;
```

Semantic family selected by the enclosing declaration\.

#### selector {#selector}

```ts
selector: EffectiveProfileDeclaredSelector;
```

Unexpanded declared selector\.

-----

### Type Literal {#type-literal-1}

```ts
{
  axis: EffectiveProfileModeAxis;
  kind: "mode-default";
  resourceId: string;
}
```

#### axis {#axis}

```ts
axis: EffectiveProfileModeAxis;
```

Orthogonal mode dimension\.

#### kind {#kind-1}

```ts
kind: "mode-default";
```

#### resourceId {#resourceid}

```ts
resourceId: string;
```

Exact declared run\-mode resource\.
