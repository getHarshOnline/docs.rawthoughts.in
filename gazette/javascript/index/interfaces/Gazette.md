---
title: "Interface: Gazette"
---

<a id="interface&#45;gazette"></a>

Frozen synchronous API\. Native failures have JSON messages; host type errors may not\.

## Properties {#properties}

### assembleDocumentation {#assembledocumentation}

> `readonly` **assembleDocumentation**: \(`workspace`: `Uint8Array`, `site`: `string`, `options`: [`DocumentationOptions`](/gazette/javascript/index/interfaces/DocumentationOptions)\) \=\> [`DocumentationFiles`](/gazette/javascript/index/interfaces/DocumentationFiles)

Complete selected manual/reference target and native report; configured generators require independent stage/execute permissions\.

#### Parameters {#parameters}

<Heading level={5} id="workspace" className="scroll-mt-(--scroll-mt)">workspace</Heading>

`Uint8Array`

<Heading level={5} id="site" className="scroll-mt-(--scroll-mt)">site</Heading>

`string`

<Heading level={5} id="options" className="scroll-mt-(--scroll-mt)">options</Heading>

[`DocumentationOptions`](/gazette/javascript/index/interfaces/DocumentationOptions)

#### Returns {#returns}

[`DocumentationFiles`](/gazette/javascript/index/interfaces/DocumentationFiles)

-----

### checkWorkspace {#checkworkspace}

> `readonly` **checkWorkspace**: \(`source`: `Uint8Array`, `limits?`: [`ProjectionLimits`](/gazette/javascript/index/interfaces/ProjectionLimits)\) \=\> `string`

Native workspace Compilation JSON, not publication or native\-source approval\.

#### Parameters {#parameters-1}

<Heading level={5} id="source" className="scroll-mt-(--scroll-mt)">source</Heading>

`Uint8Array`

<Heading level={5} id="limits" className="scroll-mt-(--scroll-mt)">limits?</Heading>

[`ProjectionLimits`](/gazette/javascript/index/interfaces/ProjectionLimits)

#### Returns {#returns-1}

`string`

-----

### compositionOrigin {#compositionorigin}

> `readonly` **compositionOrigin**: \(`source`: `Uint8Array`, `queryJson`: `string`, `limits?`: [`ProjectionLimits`](/gazette/javascript/index/interfaces/ProjectionLimits)\) \=\> `string`

queryJson is the Rust SDK CompositionOriginQuery, preserving the winning declaration and inheritance origin\.

#### Parameters {#parameters-2}

<Heading level={5} id="source&#45;1" className="scroll-mt-(--scroll-mt)">source</Heading>

`Uint8Array`

<Heading level={5} id="queryjson" className="scroll-mt-(--scroll-mt)">queryJson</Heading>

`string`

<Heading level={5} id="limits&#45;1" className="scroll-mt-(--scroll-mt)">limits?</Heading>

[`ProjectionLimits`](/gazette/javascript/index/interfaces/ProjectionLimits)

#### Returns {#returns-2}

`string`

-----

### fieldOrigin {#fieldorigin}

> `readonly` **fieldOrigin**: \(`source`: `Uint8Array`, `queryJson`: `string`, `limits?`: [`ProjectionLimits`](/gazette/javascript/index/interfaces/ProjectionLimits)\) \=\> `string`

queryJson is the Rust SDK FieldQuery; returned spans are half\-open UTF\-8 byte ranges\.

#### Parameters {#parameters-3}

<Heading level={5} id="source&#45;2" className="scroll-mt-(--scroll-mt)">source</Heading>

`Uint8Array`

<Heading level={5} id="queryjson&#45;1" className="scroll-mt-(--scroll-mt)">queryJson</Heading>

`string`

<Heading level={5} id="limits&#45;2" className="scroll-mt-(--scroll-mt)">limits?</Heading>

[`ProjectionLimits`](/gazette/javascript/index/interfaces/ProjectionLimits)

#### Returns {#returns-3}

`string`

-----

### inspectDocument {#inspectdocument}

> `readonly` **inspectDocument**: \(`source`: `Uint8Array`, `options?`: [`DocumentOptions`](/gazette/javascript/index/interfaces/DocumentOptions)\) \=\> `string`

Native \{document, html?\} JSON; body coordinates remain relative to document\.body\_span\.

#### Parameters {#parameters-4}

<Heading level={5} id="source&#45;3" className="scroll-mt-(--scroll-mt)">source</Heading>

`Uint8Array`

<Heading level={5} id="options&#45;1" className="scroll-mt-(--scroll-mt)">options?</Heading>

[`DocumentOptions`](/gazette/javascript/index/interfaces/DocumentOptions)

#### Returns {#returns-4}

`string`

-----

### inspectDocumentTree {#inspectdocumenttree}

> `readonly` **inspectDocumentTree**: \(`treeJson`: `string`, `tree`: [`TreeOptions`](/gazette/javascript/index/interfaces/TreeOptions), `options?`: [`DocumentOptions`](/gazette/javascript/index/interfaces/DocumentOptions)\) \=\> `string`

Exact same complete\-tree capture, with explicit \+\+\+ framing; returns \{input, document, html?\}\.

#### Parameters {#parameters-5}

<Heading level={5} id="treejson" className="scroll-mt-(--scroll-mt)">treeJson</Heading>

`string`

<Heading level={5} id="tree" className="scroll-mt-(--scroll-mt)">tree</Heading>

[`TreeOptions`](/gazette/javascript/index/interfaces/TreeOptions)

<Heading level={5} id="options&#45;2" className="scroll-mt-(--scroll-mt)">options?</Heading>

[`DocumentOptions`](/gazette/javascript/index/interfaces/DocumentOptions)

#### Returns {#returns-5}

`string`

-----

### inspectMarkdown {#inspectmarkdown}

> `readonly` **inspectMarkdown**: \(`source`: `Uint8Array`, `options?`: [`MarkdownOptions`](/gazette/javascript/index/interfaces/MarkdownOptions)\) \=\> `string`

Native \{inspection, html?\} JSON with exact UTF\-8 source coordinates\.

#### Parameters {#parameters-6}

<Heading level={5} id="source&#45;4" className="scroll-mt-(--scroll-mt)">source</Heading>

`Uint8Array`

<Heading level={5} id="options&#45;3" className="scroll-mt-(--scroll-mt)">options?</Heading>

[`MarkdownOptions`](/gazette/javascript/index/interfaces/MarkdownOptions)

#### Returns {#returns-6}

`string`

-----

### inspectMarkdownTree {#inspectmarkdowntree}

> `readonly` **inspectMarkdownTree**: \(`treeJson`: `string`, `tree`: [`TreeOptions`](/gazette/javascript/index/interfaces/TreeOptions), `options?`: [`MarkdownOptions`](/gazette/javascript/index/interfaces/MarkdownOptions)\) \=\> `string`

Exact Rust markdown::input::Tree JSON; returns native \{input, inspection, html?\}\.

#### Parameters {#parameters-7}

<Heading level={5} id="treejson&#45;1" className="scroll-mt-(--scroll-mt)">treeJson</Heading>

`string`

<Heading level={5} id="tree&#45;1" className="scroll-mt-(--scroll-mt)">tree</Heading>

[`TreeOptions`](/gazette/javascript/index/interfaces/TreeOptions)

<Heading level={5} id="options&#45;4" className="scroll-mt-(--scroll-mt)">options?</Heading>

[`MarkdownOptions`](/gazette/javascript/index/interfaces/MarkdownOptions)

#### Returns {#returns-7}

`string`

-----

### inspectPagePackage {#inspectpagepackage}

> `readonly` **inspectPagePackage**: \(`request`: [`PagePackageRequest`](/gazette/javascript/index/interfaces/PagePackageRequest), `options?`: [`PagePackageOptions`](/gazette/javascript/index/interfaces/PagePackageOptions)\) \=\> `string`

Exact application PagePackageOwnership JSON, or JSON null for a standalone page\. Performs no native reads\.

#### Parameters {#parameters-8}

<Heading level={5} id="request" className="scroll-mt-(--scroll-mt)">request</Heading>

[`PagePackageRequest`](/gazette/javascript/index/interfaces/PagePackageRequest)

<Heading level={5} id="options&#45;5" className="scroll-mt-(--scroll-mt)">options?</Heading>

[`PagePackageOptions`](/gazette/javascript/index/interfaces/PagePackageOptions)

#### Returns {#returns-8}

`string`

-----

### inspectReleaseHistory {#inspectreleasehistory}

> `readonly` **inspectReleaseHistory**: \(`request`: `Uint8Array`, `options`: [`HistoryOptions`](/gazette/javascript/index/interfaces/HistoryOptions)\) \=\> `string`

Exact native history JSON; request selects kind, database, record\_id, optional expected\_header and native read options\. No release effects\.

#### Parameters {#parameters-9}

<Heading level={5} id="request&#45;1" className="scroll-mt-(--scroll-mt)">request</Heading>

`Uint8Array`

<Heading level={5} id="options&#45;6" className="scroll-mt-(--scroll-mt)">options</Heading>

[`HistoryOptions`](/gazette/javascript/index/interfaces/HistoryOptions)

#### Returns {#returns-9}

`string`

-----

### observeDelivery {#observedelivery}

> `readonly` **observeDelivery**: \(`request`: `Uint8Array`, `options?`: [`DeliveryOptions`](/gazette/javascript/index/interfaces/DeliveryOptions)\) \=\> `string`

Exact native delivery Report JSON; mismatches throw the complete selected\-route report\. No publication or settlement\.

#### Parameters {#parameters-10}

<Heading level={5} id="request&#45;2" className="scroll-mt-(--scroll-mt)">request</Heading>

`Uint8Array`

<Heading level={5} id="options&#45;7" className="scroll-mt-(--scroll-mt)">options?</Heading>

[`DeliveryOptions`](/gazette/javascript/index/interfaces/DeliveryOptions)

#### Returns {#returns-10}

`string`

-----

### prepareSites {#preparesites}

> `readonly` **prepareSites**: \(`recipe`: `Uint8Array`, `options`: [`PrepareOptions`](/gazette/javascript/index/interfaces/PrepareOptions)\) \=\> `string`

Native complete report\. Errors retain partial effects or original reconciliation coordinates; never retry blindly\.

#### Parameters {#parameters-11}

<Heading level={5} id="recipe" className="scroll-mt-(--scroll-mt)">recipe</Heading>

`Uint8Array`

<Heading level={5} id="options&#45;8" className="scroll-mt-(--scroll-mt)">options</Heading>

[`PrepareOptions`](/gazette/javascript/index/interfaces/PrepareOptions)

#### Returns {#returns-11}

`string`

-----

### qualifySites {#qualifysites}

> `readonly` **qualifySites**: \(`recipe`: `Uint8Array`, `options`: [`QualificationOptions`](/gazette/javascript/index/interfaces/QualificationOptions)\) \=\> `string`

Complete native qualification report; failures never return a reduced successful set\. Lost delivery does not authorize retry\.

#### Parameters {#parameters-12}

<Heading level={5} id="recipe&#45;1" className="scroll-mt-(--scroll-mt)">recipe</Heading>

`Uint8Array`

<Heading level={5} id="options&#45;9" className="scroll-mt-(--scroll-mt)">options</Heading>

[`QualificationOptions`](/gazette/javascript/index/interfaces/QualificationOptions)

#### Returns {#returns-12}

`string`

-----

### renderSiteFiles {#rendersitefiles}

> `readonly` **renderSiteFiles**: \(`recipe`: `Uint8Array`, `options`: [`RenderOptions`](/gazette/javascript/index/interfaces/RenderOptions)\) \=\> [`PublicationFiles`](/gazette/javascript/index/interfaces/PublicationFiles)

Same complete render plus owned file bytes; no staging, CLI bridge or publication effect\.

#### Parameters {#parameters-13}

<Heading level={5} id="recipe&#45;2" className="scroll-mt-(--scroll-mt)">recipe</Heading>

`Uint8Array`

<Heading level={5} id="options&#45;10" className="scroll-mt-(--scroll-mt)">options</Heading>

[`RenderOptions`](/gazette/javascript/index/interfaces/RenderOptions)

#### Returns {#returns-13}

[`PublicationFiles`](/gazette/javascript/index/interfaces/PublicationFiles)

-----

### renderSites {#rendersites}

> `readonly` **renderSites**: \(`recipe`: `Uint8Array`, `options`: [`RenderOptions`](/gazette/javascript/index/interfaces/RenderOptions)\) \=\> `string`

Complete native inspection; incomplete sets throw the same full report without dropping siblings\.

#### Parameters {#parameters-14}

<Heading level={5} id="recipe&#45;3" className="scroll-mt-(--scroll-mt)">recipe</Heading>

`Uint8Array`

<Heading level={5} id="options&#45;11" className="scroll-mt-(--scroll-mt)">options</Heading>

[`RenderOptions`](/gazette/javascript/index/interfaces/RenderOptions)

#### Returns {#returns-14}

`string`

-----

### reviewPublication {#reviewpublication}

> `readonly` **reviewPublication**: \(`workspace`: `Uint8Array`, `site`: `string`, `options`: [`ReviewOptions`](/gazette/javascript/index/interfaces/ReviewOptions)\) \=\> `string`

Exact private native PublicationReview JSON; a digest is not approval or certification\.

#### Parameters {#parameters-15}

<Heading level={5} id="workspace&#45;1" className="scroll-mt-(--scroll-mt)">workspace</Heading>

`Uint8Array`

<Heading level={5} id="site&#45;1" className="scroll-mt-(--scroll-mt)">site</Heading>

`string`

<Heading level={5} id="options&#45;12" className="scroll-mt-(--scroll-mt)">options</Heading>

[`ReviewOptions`](/gazette/javascript/index/interfaces/ReviewOptions)

#### Returns {#returns-15}

`string`
