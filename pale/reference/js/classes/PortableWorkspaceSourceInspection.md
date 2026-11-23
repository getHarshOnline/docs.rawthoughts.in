---
title: "Class: PortableWorkspaceSourceInspection"
---

<a id="class&#45;portableworkspacesourceinspection"></a>

A source answer retaining the exact compilation that supplied it\.

Equal semantic digests can accompany different unselected source inputs\.
Garbage collection releases the shared compiler handle, not native state\.
This inspection grants neither source disclosure nor execution permission\.

## Accessors {#accessors}

### location {#location}

#### Get Signature {#get-signature}

```ts
get location(): AuthoringSourceLocation;
```

Requested location, including when no occurrence was found\.

# Errors {#errors}

Returns a projection error if an array index exceeds the Node path ABI\.

<Heading level={5} id="returns" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`AuthoringSourceLocation`](/pale/reference/js/interfaces/AuthoringSourceLocation)

-----

### state {#state}

#### Get Signature {#get-signature-1}

```ts
get state(): PortableWorkspaceSourceState;
```

Direct named meaning and selected\-proof membership from the compiler\.

<Heading level={5} id="returns&#45;1" className="scroll-mt-(--scroll-mt)">Returns</Heading>

[`PortableWorkspaceSourceState`](/pale/reference/js/enumerations/PortableWorkspaceSourceState)

## Methods {#methods}

### belongsTo\(\) {#belongsto}

```ts
belongsTo(workspace: PortableWorkspaceCompilation): boolean;
```

Match the exact retained compilation, not merely its semantic digests\.

#### Parameters {#parameters}

<Heading level={5} id="workspace" className="scroll-mt-(--scroll-mt)">workspace</Heading>

[`PortableWorkspaceCompilation`](/pale/reference/js/classes/PortableWorkspaceCompilation)

#### Returns {#returns-2}

`boolean`

-----

### occurrence\(\) {#occurrence}

```ts
occurrence(): AuthoringOccurrence | null;
```

Copy the location and role; absent only for `NoOccurrence`\.

# Errors {#errors-1}

Returns a projection error if an array index exceeds the Node path ABI\.

#### Returns {#returns-3}

[`AuthoringOccurrence`](/pale/reference/js/interfaces/AuthoringOccurrence) \| `null`

-----

### subject\(\) {#subject}

```ts
subject(): WorkspaceSubject | null;
```

Copy the full subject for `Unselected` or `Selected`; otherwise `null`\.

#### Returns {#returns-4}

[`WorkspaceSubject`](/pale/reference/js/classes/WorkspaceSubject) \| `null`
