---
title: "Enumeration: LocalMaterializationAction"
---

<a id="enumeration&#45;localmaterializationaction"></a>

Closed repository or machine\-local transition shown by local status\.

## Enumeration Members {#enumeration-members}

### Adopt {#adopt}

```ts
Adopt: 1;
```

Adopt matching pre\-existing bytes under explicit adoption policy\.

-----

### Create {#create}

```ts
Create: 0;
```

Create a previously absent file\.

-----

### Delete {#delete}

```ts
Delete: 3;
```

Delete a previously owned file\.

-----

### Splice {#splice}

```ts
Splice: 4;
```

Replace only Pale's managed block while preserving other bytes\.

-----

### Update {#update}

```ts
Update: 2;
```

Replace an owned file whose desired bytes changed\.
