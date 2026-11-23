---
title: "Class: PortableWorkspaceSubjectOccurrences"
---

<a id="class&#45;portableworkspacesubjectoccurrences"></a>

Compiler membership plus a bounded page of direct named occurrences\.

An empty incomplete page must be resumed\. The underlying cursor retains
the exact compilation, full subject, query kind, and both raw limits\.

## Accessors {#accessors}

### membership {#membership}

#### Get Signature {#get-signature}

```ts
get membership(): PortableWorkspaceSubjectMembership;
```

Selected\-proof membership; it does not summarize source\-page contents\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`PortableWorkspaceSubjectMembership`](/pale/reference/js/enumerations/PortableWorkspaceSubjectMembership)

## Methods {#methods}

### page\(\) {#page}

```ts
page(): AuthoringOccurrencePage;
```

Copy the SDK page without recompiling or restarting its scan\.

#### Returns {#returns-1}

[`AuthoringOccurrencePage`](/pale/reference/js/classes/AuthoringOccurrencePage)
