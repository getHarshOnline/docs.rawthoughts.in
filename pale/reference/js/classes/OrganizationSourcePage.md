---
title: "Class: OrganizationSourcePage"
---

<a id="class&#45;organizationsourcepage"></a>

Source matches or an unmapped record, with the queried record retained\.

## Accessors {#accessors}

### copiedStringBytes {#copiedstringbytes}

#### Get Signature {#get-signature}

```ts
get copiedStringBytes(): number;
```

SDK copied UTF\-8 payload, excluding repeated getters and allocation overhead\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

`number`

-----

### mapping {#mapping}

#### Get Signature {#get-signature-1}

```ts
get mapping(): OrganizationSourceMapping;
```

Copy the SDK source result without deriving identity from labels\.

# Errors {#errors}

Preserves existing source projection errors when an index cannot fit Node\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationSourceMapping`](/pale/reference/js/type-aliases/OrganizationSourceMapping)

-----

### record {#record}

#### Get Signature {#get-signature-2}

```ts
get record(): OrganizationRecordHandle;
```

Actual independently retained record, including unmapped/empty results\.

<Heading level={5} id="returns&#45;2" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`OrganizationRecordHandle`](/pale/reference/js/classes/OrganizationRecordHandle)
