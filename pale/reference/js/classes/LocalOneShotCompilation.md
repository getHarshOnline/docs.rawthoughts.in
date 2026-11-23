---
title: "Class: LocalOneShotCompilation"
---

<a id="class&#45;localoneshotcompilation"></a>

Opaque local compilation retaining API\-private host capabilities\.

The handle itself grants no plan admission, mutation, runtime activation,
or resident authority\. JavaScript can pass it only to the explicit local
operations exposed by \[`Pale`\]\.

## Methods {#methods}

### summary\(\) {#summary}

```ts
summary(): OneShotSummary;
```

Return the same bounded summary projected by captured one\-shot compilation\.

#### Returns {#returns}

[`OneShotSummary`](/pale/reference/js/interfaces/OneShotSummary)
