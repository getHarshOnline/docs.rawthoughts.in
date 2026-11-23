---
title: "Class: WebMcpError"
---

<a id="class&#45;webmcperror"></a>

## Extends {#extends}

- `Error`

## Constructors {#constructors}

### Constructor {#constructor}

> **new WebMcpError**\(`code`: `string`, `cause?`: `unknown`\): `WebMcpError`

Retains the supplied cause value; it is not an ErrorOptions object to unwrap\.

#### Parameters {#parameters}

<Heading level={5} id="code" className="scroll-mt-(--scroll-mt)">code</Heading>

`string`

<Heading level={5} id="cause" className="scroll-mt-(--scroll-mt)">cause?</Heading>

`unknown`

#### Returns {#returns}

`WebMcpError`

#### Overrides {#overrides}

`Error.constructor`

## Properties {#properties}

### cause? {#cause-1}

> `optional` **cause?**: `unknown`

#### Inherited from {#inherited-from}

`Error.cause`

-----

### code {#code-1}

> `readonly` **code**: `string`

-----

### message {#message}

> **message**: `string`

#### Inherited from {#inherited-from-1}

`Error.message`

-----

### name {#name}

> **name**: `string`

#### Inherited from {#inherited-from-2}

`Error.name`

-----

### stack? {#stack}

> `optional` **stack?**: `string`

#### Inherited from {#inherited-from-3}

`Error.stack`
