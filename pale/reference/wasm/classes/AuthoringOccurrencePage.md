---
title: "Class: AuthoringOccurrencePage"
---

<a id="class&#45;authoringoccurrencepage"></a>

Matching occurrences and scan progress from the retained compiler index\.

An empty page can be incomplete\. Row limits combine with one fixed ceiling
over copied source labels and field names\.

## Properties {#properties}

### copiedStringBytes {#copiedstringbytes}

```ts
readonly copiedStringBytes: number;
```

UTF\-8 bytes copied into returned source labels and field names\.

-----

### inspected {#inspected}

```ts
readonly inspected: number;
```

Index entries examined, including nonmatches\.

-----

### isComplete {#iscomplete}

```ts
readonly isComplete: boolean;
```

Whether the scan proved exhaustion of the retained index\.

## Methods {#methods}

### \[dispose\]\(\) {#dispose}

```ts
[dispose](): void;
```

#### Returns {#returns}

`void`

-----

### continuation\(\) {#continuation}

```ts
continuation(): 
  | AuthoringOccurrencePageCursor
  | undefined;
```

Share the continuation, or return `undefined` after proven exhaustion\.

Each call creates an independently owned handle\. Resuming consumes that
handle; callers can retain another copy when they need to retry a query\.

#### Returns {#returns-1}

\| [`AuthoringOccurrencePageCursor`](/pale/reference/wasm/classes/AuthoringOccurrencePageCursor)
\| `undefined`

-----

### free\(\) {#free}

```ts
free(): void;
```

#### Returns {#returns-2}

`void`

-----

### occurrences\(\) {#occurrences}

```ts
occurrences(): AuthoringOccurrence[];
```

Copy matching occurrences in compiler source/path order\.

#### Returns {#returns-3}

[`AuthoringOccurrence`](/pale/reference/wasm/classes/AuthoringOccurrence)\[\]
