---
title: "Type Alias: Captured<T>"
---

<a id="type&#45;alias&#45;captured&#45;t"></a>

> **Captured**\<`T`\> \= `T` *extends* readonly `unknown`\[\] ? `{ readonly [K in keyof T]: Captured<T[K]> }` : `T` *extends* `object` ? `{ readonly [K in keyof T]: Captured<T[K]> }` : `T`

The runtime captures and deeply freezes JSON; input mutability does not escape\.

## Type Parameters {#type-parameters}

### T {#t}

`T`
