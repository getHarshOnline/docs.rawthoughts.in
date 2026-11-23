---
title: "Enumeration: OrganizationResponsibilityLifecycle"
---

<a id="enumeration&#45;organizationresponsibilitylifecycle"></a>

Lifecycle asserted by the responsibility author, not newly verified by inspection\.

## Enumeration Members {#enumeration-members}

### AcceptedTarget {#acceptedtarget}

```ts
AcceptedTarget: 1;
```

Accepted future semantic target\.

-----

### Candidate {#candidate}

```ts
Candidate: 3;
```

Candidate design, not accepted ABI status\.

-----

### ConfigurationOpen {#configurationopen}

```ts
ConfigurationOpen: 5;
```

Private population remains open\.

-----

### EvidenceGated {#evidencegated}

```ts
EvidenceGated: 6;
```

Evidence must close before use\.

-----

### Historical {#historical}

```ts
Historical: 7;
```

Historical evidence only\.

-----

### ImplementationOpen {#implementationopen}

```ts
ImplementationOpen: 4;
```

Implementation remains open\.

-----

### OwnerDesiredConfiguration {#ownerdesiredconfiguration}

```ts
OwnerDesiredConfiguration: 2;
```

Principal\-owner desired configuration\.

-----

### Rejected {#rejected}

```ts
Rejected: 8;
```

Rejected proposition retained as genealogy\.

-----

### VerifiedCurrent {#verifiedcurrent}

```ts
VerifiedCurrent: 0;
```

Author asserts verified current owner truth\.
