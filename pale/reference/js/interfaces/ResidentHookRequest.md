---
title: "Interface: ResidentHookRequest"
---

<a id="interface&#45;residenthookrequest"></a>

Complete native event awaiting API\-owned resident\-hook admission\.

## Properties {#properties}

### event {#event}

```ts
event: string;
```

Static lifecycle\-event identity\.

-----

### payload {#payload}

```ts
payload: Buffer;
```

Complete bounded native event payload\.

-----

### providerBinding {#providerbinding}

```ts
providerBinding: string;
```

Stable provider\-binding locator\.

-----

### providerBindingIdentity {#providerbindingidentity}

```ts
providerBindingIdentity: string;
```

Domain\-separated identity of the complete provider\-binding body\.

-----

### repository {#repository}

```ts
repository: string;
```

Logical repository identity\.

-----

### workspace {#workspace}

```ts
workspace: string;
```

Logical workspace identity\.
