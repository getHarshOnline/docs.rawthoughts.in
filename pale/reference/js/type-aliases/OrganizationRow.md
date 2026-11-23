---
title: "Type Alias: OrganizationRow"
---

<a id="type&#45;alias&#45;organizationrow"></a>

```ts
type OrganizationRow = 
  | {
  axes: OrganizationAxes;
  interval: OrganizationInterval;
  kind: "scope";
  scope: OrganizationScopeRef;
  state: OrganizationFactState;
}
  | {
  axes: OrganizationAxes;
  interval: OrganizationInterval;
  kind: "organization";
  organization: OrganizationRef;
  scope: OrganizationScopeRef;
  state: OrganizationFactState;
}
  | {
  axes: OrganizationAxes;
  group: OrganizationGroupRef;
  interval: OrganizationInterval;
  kind: "group";
  organization: OrganizationRef;
  state: OrganizationFactState;
}
  | {
  axes: OrganizationAxes;
  interval: OrganizationInterval;
  kind: "discipline-tree";
  organization: OrganizationRef;
  state: OrganizationFactState;
  tree: OrganizationTreeRef;
}
  | {
  axes: OrganizationAxes;
  disciplineTree: OrganizationTreeRef | null;
  group: OrganizationGroupRef | null;
  interval: OrganizationInterval;
  kind: "role";
  organization: OrganizationRef;
  role: OrganizationRoleRef;
  roleClass: string;
  state: OrganizationFactState;
}
  | {
  interval: OrganizationInterval;
  issuer: string;
  kind: "occupant-binding";
  occupant: string;
  role: OrganizationRoleRef;
  state: OrganizationFactState;
}
  | {
  interval: OrganizationInterval;
  issuer: string;
  kind: "provider-binding";
  provider: string;
  role: OrganizationRoleRef;
  state: OrganizationFactState;
}
  | {
  handle: string;
  interval: OrganizationInterval;
  issuer: string;
  kind: "communication-actor";
  provider: string;
  state: OrganizationFactState;
}
  | {
  disclosure: OrganizationDisclosure;
  interval: OrganizationInterval;
  issuer: string;
  kind: "leadership";
  state: OrganizationFactState;
  topic: string;
}
  | {
  class: OrganizationRelationClass;
  from: OrganizationNode;
  interval: OrganizationInterval;
  issuer: string;
  kind: "relation";
  locality: OrganizationRelationLocality;
  relationId: string;
  state: OrganizationFactState;
  to: OrganizationNode;
}
  | {
  axes: OrganizationAxes;
  interval: OrganizationInterval;
  kind: "object";
  namespace: string;
  objectClass: string;
  objectId: string;
  organization: OrganizationRef;
  scope: OrganizationScopeRef;
  state: OrganizationFactState;
}
  | {
  accountableRoleClass: string;
  interval: OrganizationInterval;
  issuer: string;
  kind: "population-rule";
  objectClass: string;
  state: OrganizationFactState;
}
  | {
  alignmentRelation: string;
  escalationResolver: OrganizationRoleRef | null;
  holder: OrganizationRoleRef;
  interval: OrganizationInterval;
  issuer: string;
  kind: "group-lens";
  lens: string;
  profileId: string;
  reviewOwner: OrganizationRoleRef | null;
  state: OrganizationFactState;
}
  | {
  consumerAcceptance: OrganizationEvidenceRequirement;
  contract: OrganizationServiceRef;
  contractOwner: string;
  disclosure: OrganizationDisclosure;
  effect: OrganizationEffectCeiling;
  interval: OrganizationInterval;
  kind: "service";
  modelUsePermitted: boolean;
  nativeReadBack: OrganizationEvidenceRequirement;
  paleSettlement: OrganizationEvidenceRequirement;
  providerAcceptance: OrganizationEvidenceRequirement;
  providerCompletion: OrganizationEvidenceRequirement;
  retentionSeconds: bigint;
  state: OrganizationFactState;
}
  | {
  class: OrganizationProjectionClass;
  disclosure: OrganizationDisclosure;
  interval: OrganizationInterval;
  kind: "native-projection";
  nativeOwner: string;
  projectionId: string;
  state: OrganizationFactState;
  subject: OrganizationNode;
}
  | {
  disclosure: OrganizationDisclosure;
  inspectionId: string;
  kind: "inspection";
  principal: string;
  viewProvider: string | null;
}
  | {
  class: OrganizationDerivedClass;
  from: OrganizationNode;
  interval: OrganizationInterval;
  issuer: string;
  kind: "derived-relation";
  source: OrganizationDerivedSource;
  state: OrganizationFactState;
  to: OrganizationNode;
}
  | {
  kind: "responsibility";
  record: OrganizationResponsibility;
};
```

Shallow copied records from the existing eighteen\-family owner\.

These public values can be copied or constructed as observations, but no
query accepts them as authority or reconstructs an opaque record handle\.
Nested collections are intentionally accessed through their owning handle\.

## Union Members {#union-members}

### Type Literal {#type-literal}

```ts
{
  axes: OrganizationAxes;
  interval: OrganizationInterval;
  kind: "scope";
  scope: OrganizationScopeRef;
  state: OrganizationFactState;
}
```

#### axes {#axes}

```ts
axes: OrganizationAxes;
```

Independent owner, controller, authority and disclosure observations; resources are queried separately\.

#### interval {#interval}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### kind {#kind}

```ts
kind: "scope";
```

#### scope {#scope}

```ts
scope: OrganizationScopeRef;
```

Exact namespace\-qualified logical scope\.

#### state {#state}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-1}

```ts
{
  axes: OrganizationAxes;
  interval: OrganizationInterval;
  kind: "organization";
  organization: OrganizationRef;
  scope: OrganizationScopeRef;
  state: OrganizationFactState;
}
```

#### axes {#axes-1}

```ts
axes: OrganizationAxes;
```

Independent owner, controller, authority and disclosure observations; resources are queried separately\.

#### interval {#interval-1}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### kind {#kind-1}

```ts
kind: "organization";
```

#### organization {#organization}

```ts
organization: OrganizationRef;
```

Exact namespace\-qualified organization association\.

#### scope {#scope-1}

```ts
scope: OrganizationScopeRef;
```

Exact namespace\-qualified logical scope\.

#### state {#state-1}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-2}

```ts
{
  axes: OrganizationAxes;
  group: OrganizationGroupRef;
  interval: OrganizationInterval;
  kind: "group";
  organization: OrganizationRef;
  state: OrganizationFactState;
}
```

#### axes {#axes-2}

```ts
axes: OrganizationAxes;
```

Independent owner, controller, authority and disclosure observations; resources are queried separately\.

#### group {#group}

```ts
group: OrganizationGroupRef;
```

Actual group association; not substituted for the discipline tree\.

#### interval {#interval-2}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### kind {#kind-2}

```ts
kind: "group";
```

#### organization {#organization-1}

```ts
organization: OrganizationRef;
```

Exact namespace\-qualified organization association\.

#### state {#state-2}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-3}

```ts
{
  axes: OrganizationAxes;
  interval: OrganizationInterval;
  kind: "discipline-tree";
  organization: OrganizationRef;
  state: OrganizationFactState;
  tree: OrganizationTreeRef;
}
```

#### axes {#axes-3}

```ts
axes: OrganizationAxes;
```

Independent owner, controller, authority and disclosure observations; resources are queried separately\.

#### interval {#interval-3}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### kind {#kind-3}

```ts
kind: "discipline-tree";
```

#### organization {#organization-2}

```ts
organization: OrganizationRef;
```

Exact namespace\-qualified organization association\.

#### state {#state-3}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

#### tree {#tree}

```ts
tree: OrganizationTreeRef;
```

Exact namespace\-qualified discipline tree\.

-----

### Type Literal {#type-literal-4}

```ts
{
  axes: OrganizationAxes;
  disciplineTree: OrganizationTreeRef | null;
  group: OrganizationGroupRef | null;
  interval: OrganizationInterval;
  kind: "role";
  organization: OrganizationRef;
  role: OrganizationRoleRef;
  roleClass: string;
  state: OrganizationFactState;
}
```

#### axes {#axes-4}

```ts
axes: OrganizationAxes;
```

Independent owner, controller, authority and disclosure observations; resources are queried separately\.

#### disciplineTree {#disciplinetree}

```ts
disciplineTree: OrganizationTreeRef | null;
```

Actual optional tree association, independently of group\.

#### group {#group-1}

```ts
group: OrganizationGroupRef | null;
```

Actual group association; not substituted for the discipline tree\.

#### interval {#interval-4}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### kind {#kind-4}

```ts
kind: "role";
```

#### organization {#organization-3}

```ts
organization: OrganizationRef;
```

Exact namespace\-qualified organization association\.

#### role {#role}

```ts
role: OrganizationRoleRef;
```

Exact stable role, independent of its occupant/provider\.

#### roleClass {#roleclass}

```ts
roleClass: string;
```

Owner\-selected role class; its spelling grants no authority\.

#### state {#state-4}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-5}

```ts
{
  interval: OrganizationInterval;
  issuer: string;
  kind: "occupant-binding";
  occupant: string;
  role: OrganizationRoleRef;
  state: OrganizationFactState;
}
```

#### interval {#interval-5}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### issuer {#issuer}

```ts
issuer: string;
```

Owner that issued this exact fact\.

#### kind {#kind-5}

```ts
kind: "occupant-binding";
```

#### occupant {#occupant}

```ts
occupant: string;
```

Actual occupant identity, not the role or provider\.

#### role {#role-1}

```ts
role: OrganizationRoleRef;
```

Exact stable role, independent of its occupant/provider\.

#### state {#state-5}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-6}

```ts
{
  interval: OrganizationInterval;
  issuer: string;
  kind: "provider-binding";
  provider: string;
  role: OrganizationRoleRef;
  state: OrganizationFactState;
}
```

#### interval {#interval-6}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### issuer {#issuer-1}

```ts
issuer: string;
```

Owner that issued this exact fact\.

#### kind {#kind-6}

```ts
kind: "provider-binding";
```

#### provider {#provider}

```ts
provider: string;
```

Actual provider identity, not an occupant or native readiness proof\.

#### role {#role-2}

```ts
role: OrganizationRoleRef;
```

Exact stable role, independent of its occupant/provider\.

#### state {#state-6}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-7}

```ts
{
  handle: string;
  interval: OrganizationInterval;
  issuer: string;
  kind: "communication-actor";
  provider: string;
  state: OrganizationFactState;
}
```

#### handle {#handle}

```ts
handle: string;
```

Canonical provider\-native communication handle; not an authorization union\.

#### interval {#interval-7}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### issuer {#issuer-2}

```ts
issuer: string;
```

Owner that issued this exact fact\.

#### kind {#kind-7}

```ts
kind: "communication-actor";
```

#### provider {#provider-1}

```ts
provider: string;
```

Actual provider identity, not an occupant or native readiness proof\.

#### state {#state-7}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-8}

```ts
{
  disclosure: OrganizationDisclosure;
  interval: OrganizationInterval;
  issuer: string;
  kind: "leadership";
  state: OrganizationFactState;
  topic: string;
}
```

#### disclosure {#disclosure}

```ts
disclosure: OrganizationDisclosure;
```

Declared disclosure ceiling, not admitted recipient context\.

#### interval {#interval-8}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### issuer {#issuer-3}

```ts
issuer: string;
```

Owner that issued this exact fact\.

#### kind {#kind-8}

```ts
kind: "leadership";
```

#### state {#state-8}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

#### topic {#topic}

```ts
topic: string;
```

Exact topic coordinate; derived edges also require endpoints and interval\.

-----

### Type Literal {#type-literal-9}

```ts
{
  class: OrganizationRelationClass;
  from: OrganizationNode;
  interval: OrganizationInterval;
  issuer: string;
  kind: "relation";
  locality: OrganizationRelationLocality;
  relationId: string;
  state: OrganizationFactState;
  to: OrganizationNode;
}
```

#### class {#class}

```ts
class: OrganizationRelationClass;
```

Actual owner\-defined class, not a renderer style\.

#### from {#from}

```ts
from: OrganizationNode;
```

Exact typed directional source endpoint\.

#### interval {#interval-9}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### issuer {#issuer-4}

```ts
issuer: string;
```

Owner that issued this exact fact\.

#### kind {#kind-9}

```ts
kind: "relation";
```

#### locality {#locality}

```ts
locality: OrganizationRelationLocality;
```

Locality already selected by the canonical class owner\.

#### relationId {#relationid}

```ts
relationId: string;
```

Exact explicit relation identity, preserving parallel relations\.

#### state {#state-9}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

#### to {#to}

```ts
to: OrganizationNode;
```

Exact typed directional destination endpoint\.

-----

### Type Literal {#type-literal-10}

```ts
{
  axes: OrganizationAxes;
  interval: OrganizationInterval;
  kind: "object";
  namespace: string;
  objectClass: string;
  objectId: string;
  organization: OrganizationRef;
  scope: OrganizationScopeRef;
  state: OrganizationFactState;
}
```

#### axes {#axes-5}

```ts
axes: OrganizationAxes;
```

Independent owner, controller, authority and disclosure observations; resources are queried separately\.

#### interval {#interval-10}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### kind {#kind-10}

```ts
kind: "object";
```

#### namespace {#namespace}

```ts
namespace: string;
```

Actual owning namespace; not discarded during projection\.

#### objectClass {#objectclass}

```ts
objectClass: string;
```

Owner\-selected object class; not inferred from a label\.

#### objectId {#objectid}

```ts
objectId: string;
```

Actual owner\-selected object identity\.

#### organization {#organization-4}

```ts
organization: OrganizationRef;
```

Exact namespace\-qualified organization association\.

#### scope {#scope-2}

```ts
scope: OrganizationScopeRef;
```

Exact namespace\-qualified logical scope\.

#### state {#state-10}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-11}

```ts
{
  accountableRoleClass: string;
  interval: OrganizationInterval;
  issuer: string;
  kind: "population-rule";
  objectClass: string;
  state: OrganizationFactState;
}
```

#### accountableRoleClass {#accountableroleclass}

```ts
accountableRoleClass: string;
```

Explicit accountable role class in the population rule\.

#### interval {#interval-11}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### issuer {#issuer-5}

```ts
issuer: string;
```

Owner that issued this exact fact\.

#### kind {#kind-11}

```ts
kind: "population-rule";
```

#### objectClass {#objectclass-1}

```ts
objectClass: string;
```

Owner\-selected object class; not inferred from a label\.

#### state {#state-11}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-12}

```ts
{
  alignmentRelation: string;
  escalationResolver: OrganizationRoleRef | null;
  holder: OrganizationRoleRef;
  interval: OrganizationInterval;
  issuer: string;
  kind: "group-lens";
  lens: string;
  profileId: string;
  reviewOwner: OrganizationRoleRef | null;
  state: OrganizationFactState;
}
```

#### alignmentRelation {#alignmentrelation}

```ts
alignmentRelation: string;
```

Existing relation that bounds the lens context\.

#### escalationResolver {#escalationresolver}

```ts
escalationResolver: OrganizationRoleRef | null;
```

Actual optional escalation resolver role\.

#### holder {#holder}

```ts
holder: OrganizationRoleRef;
```

Exact role carrying the declared lens\-scoped profile\.

#### interval {#interval-12}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### issuer {#issuer-6}

```ts
issuer: string;
```

Owner that issued this exact fact\.

#### kind {#kind-12}

```ts
kind: "group-lens";
```

#### lens {#lens}

```ts
lens: string;
```

Owner\-selected governed lens\.

#### profileId {#profileid}

```ts
profileId: string;
```

Exact group\-lens authority\-profile identity\.

#### reviewOwner {#reviewowner}

```ts
reviewOwner: OrganizationRoleRef | null;
```

Actual optional accountable review role\.

#### state {#state-12}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-13}

```ts
{
  consumerAcceptance: OrganizationEvidenceRequirement;
  contract: OrganizationServiceRef;
  contractOwner: string;
  disclosure: OrganizationDisclosure;
  effect: OrganizationEffectCeiling;
  interval: OrganizationInterval;
  kind: "service";
  modelUsePermitted: boolean;
  nativeReadBack: OrganizationEvidenceRequirement;
  paleSettlement: OrganizationEvidenceRequirement;
  providerAcceptance: OrganizationEvidenceRequirement;
  providerCompletion: OrganizationEvidenceRequirement;
  retentionSeconds: bigint;
  state: OrganizationFactState;
}
```

#### consumerAcceptance {#consumeracceptance}

```ts
consumerAcceptance: OrganizationEvidenceRequirement;
```

Independent consumer\-local consequence acceptance requirement\.

#### contract {#contract}

```ts
contract: OrganizationServiceRef;
```

Complete contract identity, including namespace and both directional scopes\.

#### contractOwner {#contractowner}

```ts
contractOwner: string;
```

Owner of the relationship/contract, not a selected provider\.

#### disclosure {#disclosure-1}

```ts
disclosure: OrganizationDisclosure;
```

Declared disclosure ceiling, not admitted recipient context\.

#### effect {#effect}

```ts
effect: OrganizationEffectCeiling;
```

Declared effect ceiling; inspection does not grant or perform an effect\.

#### interval {#interval-13}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### kind {#kind-13}

```ts
kind: "service";
```

#### modelUsePermitted {#modelusepermitted}

```ts
modelUsePermitted: boolean;
```

Declared model\-use ceiling, not a dispatch decision\.

#### nativeReadBack {#nativereadback}

```ts
nativeReadBack: OrganizationEvidenceRequirement;
```

Independent native owner effect/read\-back requirement\.

#### paleSettlement {#palesettlement}

```ts
paleSettlement: OrganizationEvidenceRequirement;
```

Independent Pale obligation\-settlement requirement\.

#### providerAcceptance {#provideracceptance}

```ts
providerAcceptance: OrganizationEvidenceRequirement;
```

Independent provider\-local acceptance requirement\.

#### providerCompletion {#providercompletion}

```ts
providerCompletion: OrganizationEvidenceRequirement;
```

Independent provider\-local completion requirement\.

#### retentionSeconds {#retentionseconds}

```ts
retentionSeconds: bigint;
```

Declared retention ceiling in seconds, not a live retention receipt\.

#### state {#state-13}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

-----

### Type Literal {#type-literal-14}

```ts
{
  class: OrganizationProjectionClass;
  disclosure: OrganizationDisclosure;
  interval: OrganizationInterval;
  kind: "native-projection";
  nativeOwner: string;
  projectionId: string;
  state: OrganizationFactState;
  subject: OrganizationNode;
}
```

#### class {#class-1}

```ts
class: OrganizationProjectionClass;
```

Actual owner\-defined class, not a renderer style\.

#### disclosure {#disclosure-2}

```ts
disclosure: OrganizationDisclosure;
```

Declared disclosure ceiling, not admitted recipient context\.

#### interval {#interval-14}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### kind {#kind-14}

```ts
kind: "native-projection";
```

#### nativeOwner {#nativeowner}

```ts
nativeOwner: string;
```

Native owner retaining record/effect truth\.

#### projectionId {#projectionid}

```ts
projectionId: string;
```

Exact native\-projection identity\.

#### state {#state-14}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

#### subject {#subject}

```ts
subject: OrganizationNode;
```

Actual typed semantic subject of the desired projection\.

-----

### Type Literal {#type-literal-15}

```ts
{
  disclosure: OrganizationDisclosure;
  inspectionId: string;
  kind: "inspection";
  principal: string;
  viewProvider: string | null;
}
```

#### disclosure {#disclosure-3}

```ts
disclosure: OrganizationDisclosure;
```

Declared disclosure ceiling, not admitted recipient context\.

#### inspectionId {#inspectionid}

```ts
inspectionId: string;
```

Exact configured inspection\-contract identity\.

#### kind {#kind-15}

```ts
kind: "inspection";
```

#### principal {#principal}

```ts
principal: string;
```

Declared principal reference; no authenticated authority is inferred\.

#### viewProvider {#viewprovider}

```ts
viewProvider: string | null;
```

Optional configured view provider, not proof of availability\.

-----

### Type Literal {#type-literal-16}

```ts
{
  class: OrganizationDerivedClass;
  from: OrganizationNode;
  interval: OrganizationInterval;
  issuer: string;
  kind: "derived-relation";
  source: OrganizationDerivedSource;
  state: OrganizationFactState;
  to: OrganizationNode;
}
```

#### class {#class-2}

```ts
class: OrganizationDerivedClass;
```

Actual owner\-defined class, not a renderer style\.

#### from {#from-1}

```ts
from: OrganizationNode;
```

Exact typed directional source endpoint\.

#### interval {#interval-15}

```ts
interval: OrganizationInterval;
```

Actual effective interval, not editor or presentation time\.

#### issuer {#issuer-7}

```ts
issuer: string;
```

Owner that issued this exact fact\.

#### kind {#kind-16}

```ts
kind: "derived-relation";
```

#### source {#source}

```ts
source: OrganizationDerivedSource;
```

Complete dedicated source\-fact coordinate for this derived edge\.

#### state {#state-15}

```ts
state: OrganizationFactState;
```

Actual owner\-defined effective state, including distinct negative states\.

#### to {#to-1}

```ts
to: OrganizationNode;
```

Exact typed directional destination endpoint\.

-----

### Type Literal {#type-literal-17}

```ts
{
  kind: "responsibility";
  record: OrganizationResponsibility;
}
```

#### kind {#kind-17}

```ts
kind: "responsibility";
```

#### record {#record}

```ts
record: OrganizationResponsibility;
```

Complete shallow responsibility header, not a custody token\.
