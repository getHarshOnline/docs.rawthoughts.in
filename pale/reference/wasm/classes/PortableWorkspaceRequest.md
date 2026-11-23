---
title: "Class: PortableWorkspaceRequest"
---

<a id="class&#45;portableworkspacerequest"></a>

Batched source request for portable workspace compilation\.

## Constructors {#constructors}

### Constructor {#constructor}

```ts
new PortableWorkspaceRequest(root_manifest: string, documents: PortableWorkspaceDocument[]): PortableWorkspaceRequest;
```

Bind a complete document batch to its logical root manifest\.

Documents are consumed in order\. If an element is invalid, earlier
elements remain consumed and are released; later elements are untouched\.

# Errors {#errors}

Returns a native `Error` for an invalid or already consumed document\.

#### Parameters {#parameters}

<Heading level={5} id="root&#45;manifest" className="scroll-mt-(--scroll-mt)">root\_manifest</Heading>

`string`

<Heading level={5} id="documents" className="scroll-mt-(--scroll-mt)">documents</Heading>

[`PortableWorkspaceDocument`](/pale/reference/wasm/classes/PortableWorkspaceDocument)\[\]

#### Returns {#returns}

`PortableWorkspaceRequest`

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
