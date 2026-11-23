---
title: "Type Alias: OrganizationSourceMapping"
---

<a id="type&#45;alias&#45;organizationsourcemapping"></a>

```ts
type OrganizationSourceMapping = 
  | {
  kind: "unmapped-record";
}
  | {
  continuation:   | OrganizationSourceCursor
     | null;
  inspected: number;
  kind: "named";
  occurrences: AuthoringOccurrence[];
};
```

Exact source mapping with nullable continuation, distinct from unmapped records\.

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
  continuation:   | OrganizationSourceCursor
     | null;
  inspected: number;
  kind: "named";
  occurrences: AuthoringOccurrence[];
}
```

#### continuation {#continuation}

```ts
continuation: 
  | OrganizationSourceCursor
  | null;
```

Exact retained continuation or null after exhaustion\.

#### inspected {#inspected}

```ts
inspected: number;
```

Source candidates visited, including nonmatches\.

#### kind {#kind}

```ts
kind: "named";
```

#### occurrences {#occurrences}

```ts
occurrences: AuthoringOccurrence[];
```

Compiler\-assigned source paths and roles\.
