---
title: "Interface: WebMcpDocument"
---

<a id="interface&#45;webmcpdocument"></a>

Only the native registration subset this module consumes; no browser API polyfill\.

## Properties {#properties}

### modelContext? {#modelcontext}

> `readonly` `optional` **modelContext?**: \{ `registerTool`\(`tool`: \{ `annotations`: \{ `consequentialHint`: `false`; `readOnlyHint`: `true`; `untrustedContentHint`: `true`; \}; `description`: `string`; `inputSchema`: `object`; `name`: [`ReadOnlyTool`](/gazette/javascript/webmcp/type-aliases/ReadOnlyTool); `execute`\(`input`: `object`, `options`: \{ `signal`: `AbortSignal`; \}\): `Promise`\<[`Json`](/gazette/javascript/search/type-aliases/Json)\>; \}, `options`: \{ `signal`: `AbortSignal`; \}\): `Promise`\<`void`\>; \}

#### registerTool\(\) {#registertool}

> **registerTool**\(`tool`: \{ `annotations`: \{ `consequentialHint`: `false`; `readOnlyHint`: `true`; `untrustedContentHint`: `true`; \}; `description`: `string`; `inputSchema`: `object`; `name`: [`ReadOnlyTool`](/gazette/javascript/webmcp/type-aliases/ReadOnlyTool); `execute`\(`input`: `object`, `options`: \{ `signal`: `AbortSignal`; \}\): `Promise`\<[`Json`](/gazette/javascript/search/type-aliases/Json)\>; \}, `options`: \{ `signal`: `AbortSignal`; \}\): `Promise`\<`void`\>

<Heading level={5} id="parameters" className="scroll-mt-(--scroll-mt)">Parameters</Heading>

<Heading level={6} id="tool" className="scroll-mt-(--scroll-mt)">tool</Heading>

<Heading level={6} id="annotations" className="scroll-mt-(--scroll-mt)">annotations</Heading>

\{ `consequentialHint`: `false`; `readOnlyHint`: `true`; `untrustedContentHint`: `true`; \}

<Heading level={6} id="annotations&#45;consequentialhint" className="scroll-mt-(--scroll-mt)">annotations\.consequentialHint</Heading>

`false`

<Heading level={6} id="annotations&#45;readonlyhint" className="scroll-mt-(--scroll-mt)">annotations\.readOnlyHint</Heading>

`true`

<Heading level={6} id="annotations&#45;untrustedcontenthint" className="scroll-mt-(--scroll-mt)">annotations\.untrustedContentHint</Heading>

`true`

<Heading level={6} id="description" className="scroll-mt-(--scroll-mt)">description</Heading>

`string`

<Heading level={6} id="inputschema" className="scroll-mt-(--scroll-mt)">inputSchema</Heading>

`object`

<Heading level={6} id="name" className="scroll-mt-(--scroll-mt)">name</Heading>

[`ReadOnlyTool`](/gazette/javascript/webmcp/type-aliases/ReadOnlyTool)

<Heading level={6} id="execute" className="scroll-mt-(--scroll-mt)">execute</Heading>

\(`input`: `object`, `options`: \{ `signal`: `AbortSignal`; \}\) \=\> `Promise`\<[`Json`](/gazette/javascript/search/type-aliases/Json)\>

<Heading level={6} id="options" className="scroll-mt-(--scroll-mt)">options</Heading>

<Heading level={6} id="signal" className="scroll-mt-(--scroll-mt)">signal</Heading>

`AbortSignal`

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`Promise`\<`void`\>
