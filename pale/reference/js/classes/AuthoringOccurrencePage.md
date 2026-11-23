---
title: "Class: AuthoringOccurrencePage"
---

<a id="class&#45;authoringoccurrencepage"></a>

Matching occurrences and scan progress from the retained compiler index\.

An empty page can be incomplete\. Row limits combine with one fixed ceiling
over copied source labels and field names\.

## Accessors {#accessors}

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature}

```ts
get copiedStringBytes(): number;
```

UTF\-8 bytes copied into returned source labels and field names\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### inspected {#inspected}

#### Get Signature {#get-signature-1}

```ts
get inspected(): number;
```

Index entries examined on this page, including nonmatches\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### isComplete {#iscomplete}

#### Get Signature {#get-signature-2}

```ts
get isComplete(): boolean;
```

Whether the scan proved exhaustion of the retained index\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`boolean`

## Methods {#methods}

### continuation\(\) {#continuation}

```ts
continuation(): 
  | AuthoringOccurrencePageCursor
  | null;
```

Share the continuation, or return `null` after proven exhaustion\.

#### Returns {#returns-3}

\| [`AuthoringOccurrencePageCursor`](/pale/reference/js/classes/AuthoringOccurrencePageCursor)
\| `null`

-----

### occurrences\(\) {#occurrences}

```ts
occurrences(): AuthoringOccurrence[];
```

Copy matching locations and roles in compiler source/path order\.

# Errors {#errors}

Returns a projection error if a source index exceeds the Node path ABI\.

#### Returns {#returns-4}

[`AuthoringOccurrence`](/pale/reference/js/interfaces/AuthoringOccurrence)\[\]
