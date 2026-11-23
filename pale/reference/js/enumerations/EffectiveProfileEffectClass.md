---
title: "Enumeration: EffectiveProfileEffectClass"
---

<a id="enumeration&#45;effectiveprofileeffectclass"></a>

Effect class in an admitted ceiling, not permission to execute an effect\.

## Enumeration Members {#enumeration-members}

### Compute {#compute}

```ts
Compute: 0;
```

Pure caller\-supplied computation\.

-----

### Execute {#execute}

```ts
Execute: 2;
```

Local command execution without remote write\.

-----

### Network {#network}

```ts
Network: 4;
```

Remote read\.

-----

### Publish {#publish}

```ts
Publish: 5;
```

Remote or outward\-facing write\.

-----

### Read {#read}

```ts
Read: 1;
```

Non\-mutating read\.

-----

### Write {#write}

```ts
Write: 3;
```

Local state mutation\.
