---
title: "Type Alias: RecipientQualifiedOrganizationSourceMapping"
---

<a id="type&#45;alias&#45;recipientqualifiedorganizationsourcemapping"></a>

```ts
type RecipientQualifiedOrganizationSourceMapping = 
  | {
  kind: "unmapped-record";
}
  | {
  continuation:   | RecipientQualifiedOrganizationSourceCursor
     | null;
  inspected: number;
  kind: "named";
  occurrences: AuthoringOccurrence[];
};
```

Exact source mapping without a supplied\-input continuation\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "unmapped-record";
}
```

-----

### Type Literal {#type-literal-1}

```ts
{
  continuation:   | RecipientQualifiedOrganizationSourceCursor
     | null;
  inspected: number;
  kind: "named";
  occurrences: AuthoringOccurrence[];
}
```

#### continuation {#continuation}

```ts
continuation: 
  | RecipientQualifiedOrganizationSourceCursor
  | null;
```

Null only after this source scan is complete\.

#### inspected {#inspected}

```ts
inspected: number;
```

Source candidates examined, including nonmatches\.

#### kind {#kind}

```ts
kind: "named";
```

#### occurrences {#occurrences}

```ts
occurrences: AuthoringOccurrence[];
```

Compiler\-owned source occurrences\.
