---
title: "Class: PortableWorkspaceDocument"
---

<a id="class&#45;portableworkspacedocument"></a>

One logical workspace document captured entirely in host memory\.

## Constructors {#constructors}

### Constructor {#constructor}

```ts
new PortableWorkspaceDocument(label: string, bytes: Uint8Array): PortableWorkspaceDocument;
```

Capture a logical relative label and its complete bytes without I/O\.

#### Parameters {#parameters}

<Heading level={5} id="label" className="scroll-mt-(--scroll-mt)">label</Heading>

`string`

<Heading level={5} id="bytes" className="scroll-mt-(--scroll-mt)">bytes</Heading>

`Uint8Array`

#### Returns {#returns}

`PortableWorkspaceDocument`

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns-1}

`void`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-2}

`void`
