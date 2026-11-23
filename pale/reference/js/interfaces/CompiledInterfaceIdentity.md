---
title: "Interface: CompiledInterfaceIdentity"
---

<a id="interface&#45;compiledinterfaceidentity"></a>

Compiled SDK and interface claims, not resident state or process health\.

## Properties {#properties}

### arch {#arch}

```ts
arch: string;
```

Architecture identity compiled for this process\.

-----

### canonicalBytes {#canonicalbytes}

```ts
canonicalBytes: Buffer;
```

Canonical JCS executable\-identity record\.

-----

### durablePublication {#durablepublication}

```ts
durablePublication: DurablePublicationMechanism;
```

Durable\-publication implementation compiled for this process\.

-----

### os {#os}

```ts
os: string;
```

Operating\-system identity compiled for this process\.

-----

### protocol {#protocol}

```ts
protocol: string;
```

Interface protocol compiled into this addon\.

-----

### version {#version}

```ts
version: string;
```

SDK package version compiled into this addon\.
