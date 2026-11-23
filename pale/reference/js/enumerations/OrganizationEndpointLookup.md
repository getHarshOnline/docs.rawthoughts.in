---
title: "Enumeration: OrganizationEndpointLookup"
---

<a id="enumeration&#45;organizationendpointlookup"></a>

Record\-membership evidence, separate from effective state and native readiness\.

## Enumeration Members {#enumeration-members}

### ExternalReference {#externalreference}

```ts
ExternalReference: 3;
```

An owner\-native reference, not an invented local record\.

-----

### Found {#found}

```ts
Found: 1;
```

This or an earlier page found a record or binding witness\.

-----

### NotFound {#notfound}

```ts
NotFound: 2;
```

The relevant scan ended without a local record\.

-----

### SearchIncomplete {#searchincomplete}

```ts
SearchIncomplete: 0;
```

No match yet; the scan can continue\.
