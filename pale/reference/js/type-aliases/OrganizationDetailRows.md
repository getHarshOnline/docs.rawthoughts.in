---
title: "Type Alias: OrganizationDetailRows"
---

<a id="type&#45;alias&#45;organizationdetailrows"></a>

```ts
type OrganizationDetailRows = 
  | {
  kind: "axis-resources";
  values: string[];
}
  | {
  kind: "leadership-participants";
  values: OrganizationRoleRef[];
}
  | {
  kind: "leadership-scopes";
  values: OrganizationScopeRef[];
}
  | {
  kind: "communication-resolutions";
  values: OrganizationCommunicationResolution[];
}
  | {
  kind: "communication-closure";
  values: OrganizationNode[];
}
  | {
  kind: "lens-standards";
  values: string[];
}
  | {
  kind: "lens-conditions";
  values: string[];
}
  | {
  kind: "lens-rights";
  values: OrganizationLensRight[];
}
  | {
  kind: "service-assignments";
  values: OrganizationServiceAssignment[];
}
  | {
  kind: "assignment-stewards";
  values: string[];
}
  | {
  kind: "assignment-pods";
  values: string[];
}
  | {
  kind: "service-rights";
  values: string[];
}
  | {
  kind: "service-controllers";
  values: string[];
}
  | {
  kind: "service-authorities";
  values: string[];
}
  | {
  kind: "native-references";
  values: string[];
}
  | {
  kind: "inspection-coordinates";
  values: OrganizationInspectionCoordinate[];
}
  | {
  kind: "inspection-states";
  values: OrganizationFactState[];
}
  | {
  kind: "responsibility-selections";
  values: OrganizationStructuralSelection[];
}
  | {
  kind: "responsibility-residences";
  values: OrganizationResidence[];
}
  | {
  kind: "responsibility-projections";
  values: OrganizationResponsibilityProjection[];
}
  | {
  kind: "projection-references";
  values: string[];
}
  | {
  kind: "responsibility-genealogy";
  values: OrganizationGenealogyLink[];
}
  | {
  kind: "genealogy-responsibilities";
  values: string[];
}
  | {
  kind: "genealogy-projections";
  values: string[];
}
  | {
  kind: "genealogy-occurrences";
  values: string[];
};
```

Closed structural section payloads; each variant retains its exact owning meaning\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  kind: "axis-resources";
  values: string[];
}
```

#### kind {#kind}

```ts
kind: "axis-resources";
```

#### values {#values}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-1}

```ts
{
  kind: "leadership-participants";
  values: OrganizationRoleRef[];
}
```

#### kind {#kind-1}

```ts
kind: "leadership-participants";
```

#### values {#values-1}

```ts
values: OrganizationRoleRef[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-2}

```ts
{
  kind: "leadership-scopes";
  values: OrganizationScopeRef[];
}
```

#### kind {#kind-2}

```ts
kind: "leadership-scopes";
```

#### values {#values-2}

```ts
values: OrganizationScopeRef[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-3}

```ts
{
  kind: "communication-resolutions";
  values: OrganizationCommunicationResolution[];
}
```

#### kind {#kind-3}

```ts
kind: "communication-resolutions";
```

#### values {#values-3}

```ts
values: OrganizationCommunicationResolution[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-4}

```ts
{
  kind: "communication-closure";
  values: OrganizationNode[];
}
```

#### kind {#kind-4}

```ts
kind: "communication-closure";
```

#### values {#values-4}

```ts
values: OrganizationNode[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-5}

```ts
{
  kind: "lens-standards";
  values: string[];
}
```

#### kind {#kind-5}

```ts
kind: "lens-standards";
```

#### values {#values-5}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-6}

```ts
{
  kind: "lens-conditions";
  values: string[];
}
```

#### kind {#kind-6}

```ts
kind: "lens-conditions";
```

#### values {#values-6}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-7}

```ts
{
  kind: "lens-rights";
  values: OrganizationLensRight[];
}
```

#### kind {#kind-7}

```ts
kind: "lens-rights";
```

#### values {#values-7}

```ts
values: OrganizationLensRight[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-8}

```ts
{
  kind: "service-assignments";
  values: OrganizationServiceAssignment[];
}
```

#### kind {#kind-8}

```ts
kind: "service-assignments";
```

#### values {#values-8}

```ts
values: OrganizationServiceAssignment[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-9}

```ts
{
  kind: "assignment-stewards";
  values: string[];
}
```

#### kind {#kind-9}

```ts
kind: "assignment-stewards";
```

#### values {#values-9}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-10}

```ts
{
  kind: "assignment-pods";
  values: string[];
}
```

#### kind {#kind-10}

```ts
kind: "assignment-pods";
```

#### values {#values-10}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-11}

```ts
{
  kind: "service-rights";
  values: string[];
}
```

#### kind {#kind-11}

```ts
kind: "service-rights";
```

#### values {#values-11}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-12}

```ts
{
  kind: "service-controllers";
  values: string[];
}
```

#### kind {#kind-12}

```ts
kind: "service-controllers";
```

#### values {#values-12}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-13}

```ts
{
  kind: "service-authorities";
  values: string[];
}
```

#### kind {#kind-13}

```ts
kind: "service-authorities";
```

#### values {#values-13}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-14}

```ts
{
  kind: "native-references";
  values: string[];
}
```

#### kind {#kind-14}

```ts
kind: "native-references";
```

#### values {#values-14}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-15}

```ts
{
  kind: "inspection-coordinates";
  values: OrganizationInspectionCoordinate[];
}
```

#### kind {#kind-15}

```ts
kind: "inspection-coordinates";
```

#### values {#values-15}

```ts
values: OrganizationInspectionCoordinate[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-16}

```ts
{
  kind: "inspection-states";
  values: OrganizationFactState[];
}
```

#### kind {#kind-16}

```ts
kind: "inspection-states";
```

#### values {#values-16}

```ts
values: OrganizationFactState[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-17}

```ts
{
  kind: "responsibility-selections";
  values: OrganizationStructuralSelection[];
}
```

#### kind {#kind-17}

```ts
kind: "responsibility-selections";
```

#### values {#values-17}

```ts
values: OrganizationStructuralSelection[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-18}

```ts
{
  kind: "responsibility-residences";
  values: OrganizationResidence[];
}
```

#### kind {#kind-18}

```ts
kind: "responsibility-residences";
```

#### values {#values-18}

```ts
values: OrganizationResidence[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-19}

```ts
{
  kind: "responsibility-projections";
  values: OrganizationResponsibilityProjection[];
}
```

#### kind {#kind-19}

```ts
kind: "responsibility-projections";
```

#### values {#values-19}

```ts
values: OrganizationResponsibilityProjection[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-20}

```ts
{
  kind: "projection-references";
  values: string[];
}
```

#### kind {#kind-20}

```ts
kind: "projection-references";
```

#### values {#values-20}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-21}

```ts
{
  kind: "responsibility-genealogy";
  values: OrganizationGenealogyLink[];
}
```

#### kind {#kind-21}

```ts
kind: "responsibility-genealogy";
```

#### values {#values-21}

```ts
values: OrganizationGenealogyLink[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-22}

```ts
{
  kind: "genealogy-responsibilities";
  values: string[];
}
```

#### kind {#kind-22}

```ts
kind: "genealogy-responsibilities";
```

#### values {#values-22}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-23}

```ts
{
  kind: "genealogy-projections";
  values: string[];
}
```

#### kind {#kind-23}

```ts
kind: "genealogy-projections";
```

#### values {#values-23}

```ts
values: string[];
```

Exact owning variant payload\.

-----

### Type Literal {#type-literal-24}

```ts
{
  kind: "genealogy-occurrences";
  values: string[];
}
```

#### kind {#kind-24}

```ts
kind: "genealogy-occurrences";
```

#### values {#values-24}

```ts
values: string[];
```

Exact owning variant payload\.
