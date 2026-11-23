---
title: "Class: DiagnosticProjection"
---

<a id="class&#45;diagnosticprojection"></a>

Typed unadmitted candidate forwarded to \[`DiagnosticProjection`\]\.

## Constructors {#constructors}

### Constructor {#constructor}

```ts
new DiagnosticProjection(
   code: string, 
   stage: DiagnosticStage, 
   disposition: DiagnosticDisposition, 
   summary: string, 
   retry: DiagnosticRetry, 
   effect: DiagnosticEffectCertainty
): DiagnosticProjection;
```

Start one complete owner classification; API admission remains fallible\.

#### Parameters {#parameters}

<Heading level={5} id="code" className="scroll-mt-(--scroll-mt)">code</Heading>

`string`

<Heading level={5} id="stage" className="scroll-mt-(--scroll-mt)">stage</Heading>

[`DiagnosticStage`](/pale/reference/wasm/enumerations/DiagnosticStage)

<Heading level={5} id="disposition" className="scroll-mt-(--scroll-mt)">disposition</Heading>

[`DiagnosticDisposition`](/pale/reference/wasm/enumerations/DiagnosticDisposition)

<Heading level={5} id="summary" className="scroll-mt-(--scroll-mt)">summary</Heading>

`string`

<Heading level={5} id="retry" className="scroll-mt-(--scroll-mt)">retry</Heading>

[`DiagnosticRetry`](/pale/reference/wasm/enumerations/DiagnosticRetry)

<Heading level={5} id="effect" className="scroll-mt-(--scroll-mt)">effect</Heading>

[`DiagnosticEffectCertainty`](/pale/reference/wasm/enumerations/DiagnosticEffectCertainty)

#### Returns {#returns}

`DiagnosticProjection`

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

-----

### setCauses\(\) {#setcauses}

```ts
setCauses(causes: string[], omitted: number): void;
```

Attach bounded ordered cause messages and an exact omission count\.

# Errors {#errors}

Returns a native `Error` when the omitted count is not a JavaScript
number representing an integer from zero through `u32::MAX`\.

#### Parameters {#parameters-1}

<Heading level={5} id="causes" className="scroll-mt-(--scroll-mt)">causes</Heading>

`string`\[\]

<Heading level={5} id="omitted" className="scroll-mt-(--scroll-mt)">omitted</Heading>

`number`

#### Returns {#returns-3}

`void`

-----

### setHelp\(\) {#sethelp}

```ts
setHelp(help: string[]): void;
```

Attach ordered recovery suggestions\.

#### Parameters {#parameters-2}

<Heading level={5} id="help" className="scroll-mt-(--scroll-mt)">help</Heading>

`string`\[\]

#### Returns {#returns-4}

`void`

-----

### setSubject\(\) {#setsubject}

```ts
setSubject(kind: string, identity: string): void;
```

Attach the principally affected typed identity\.

#### Parameters {#parameters-3}

<Heading level={5} id="kind" className="scroll-mt-(--scroll-mt)">kind</Heading>

`string`

<Heading level={5} id="identity" className="scroll-mt-(--scroll-mt)">identity</Heading>

`string`

#### Returns {#returns-5}

`void`
