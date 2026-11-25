---
title: "Workspace compilation"
---

<a id="workspace&#45;compilation"></a>

A workspace is the configuration that declares one publication or several connected ones: their sites, brands, content sources and Themes, in a root `gazette.toml` plus any files it lists under `includes`\. Run `gazette check` in a publication folder to check that configuration and its pages before rendering\. The command line and MCP use the same SDK check\. For a configuration buffer alone, use `gazette check --stdin`\. The commands below call the executable as `"$GAZETTE"`, the path [the install guide](/gazette/install#what-a-build-needs) sets; if `gazette` is on your `PATH`, use that instead\.

<a id="find&#45;the&#45;configuration&#45;you&#45;need"></a>

| I need to… | Start here |
| --- | --- |
| Check a TOML buffer and get a field location | [Try the two\-site example](#check-a-complete-small-workspace) |
| Load a workspace spread across several files | [Load an explicit file set](#explicit-modular-workspace-documents) |
| Bind and inspect a project source | [Choose and read workspace sources](/gazette/workspace-sources) |
| Set publishers, contacts, and destinations | [Configure publication identity and delivery](/gazette/workspace-publications) |
| Add a Theme, browser capability or page template | [Compose themes and site resources](/gazette/workspace-presentation) |
| Choose what appears in indexes and machine\-readable outputs | [Configure navigation and discovery](/gazette/workspace-discovery) |

To create and preview a publication, follow [Your first publication](https://rawthoughts.in/gazette/first-publication/)\. For the roles of configuration, compilation and rendering, see [Gazette architecture](/gazette/architecture)\.

## Check a complete small workspace {#check-a-complete-small-workspace}

Save this as `workspace-example.toml`\. Both sites name one explicitly declared publisher; they remain distinct sites even though that reference is shared\. The brand supplies each publication's public base so routed content can resolve its addresses\.

```toml
[[principals]]
id = 'owner:writer'
kind = 'person'

[[sites]]
id = 'site:notes'
publisher = 'owner:writer'
deployable = false

[[sites]]
id = 'site:research'
publisher = 'owner:writer'
deployable = false

[[brands]]
id = 'brand:field-notes'
name = 'Field Notes'

[[brands.publications]]
site = 'site:notes'
public_base_url = 'https://notes.example/'

[[brands.publications]]
site = 'site:research'
public_base_url = 'https://research.example/'
```

With a [built Gazette executable](/gazette/install#what-a-build-needs), check the supplied bytes:

```sh
"$GAZETTE" check --stdin < workspace-example.toml
```

The JSON result contains the resolved workspace and a digest of the supplied text\. The example addresses configure route resolution; no request is sent to them\. This input has no content or Theme source and creates no files or served site\. Change one publisher to `owner:missing` and the complete check fails with a native reference diagnostic instead of returning a partially resolved workspace\.

An integration can also locate the explicit `deployable` declaration:

```sh
"$GAZETTE" check --stdin --origin '{"kind":"site","identity":"site:notes","field":["deployable"]}' < workspace-example.toml
```

The returned span addresses the original UTF\-8 bytes\. Defaults do not acquire invented source positions\. The [JavaScript SDK example](/gazette/sdk/js/overview#check-a-configuration-and-locate-a-field) shows the same check and source lookup embedded in an application\.

## Choose what the check reads {#configuration-inputs-and-boundaries}

Run `gazette check` from the publication folder or any folder beneath it\. Gazette searches upward for `gazette.toml`, stopping at the repository boundary\. Choose a different folder with `--workspace-root /path/to/publication`; `--workspace-file other.toml` selects another root document there\. An invalid selected workspace fails instead of falling back to another one\.

A local check reads the declared sources, checks page structure and references, and returns `workspace_location`, `checked_sites` and `diagnostics`\. Problems also appear one per line on standard error, with their source file and position when available\. A failed check exits unsuccessfully while retaining its diagnostic report on standard output\. Checking does not render a Theme, run a typesetter or publish\. A workspace without content has configuration to check but no pages\.

To choose a fallback for folders that have no workspace, run `gazette config set workspace /path/to/publication`\. Gazette saves the absolute selection in `$XDG_CONFIG_HOME/gazette/config.json`, or `$HOME/.config/gazette/config.json` when XDG configuration is unset\. An explicit request takes priority, followed by a client folder, the process start folder, then this saved default\. The result names the source of the choice\. Finding a local workspace never changes the saved default\.

Standard input is read only with `--stdin` or a mode that explicitly requests an input, such as `check build --local` or `--retained-math-stdin`\. Use `gazette check --stdin < workspace.toml` for a detached configuration\-only check\. It returns the resolved configuration and source digest, without reading page sources\. Empty input is checked as supplied text; it does not select a local workspace\.

Use `gazette check build --local` when you also want to validate the site build\. It takes the same `gazette-local-publication-set/1` JSON as `render-sites`, reads the declared files and runs the renderer without keeping a stage\. See [Render publications locally](/gazette/local-rendering#local-site-sets) for the recipe\.

In a build or preview request, choose a `workspace.kind`:

| Kind | Input |
| --- | --- |
| `supplied` | One complete TOML buffer |
| `local` | Absolute root, document path relative to that root, and independent loader limits |

Both compile the workspace once\. Build, preview, qualification and preparation use that compilation and keep its source information in the result\. Gazette reads the source when the request calls for it\. It does not add file reads, rendering or release to a workspace\-only check\.

Unsupported fields fail the check\. The schema covers pinned sources, Themes, plugin activation, capability\-provider bindings, resources and field origins\. Before the first release, the workspace format has no compatibility promise\.

For a site with its own brand, use the [single site block](/gazette/workspace-publications#a-site-with-its-own-brand)\. [Shared publication settings](/gazette/workspace-publications#shared-publication-settings) let sites inherit declared workspace and publisher defaults while retaining their individual overrides\.

## Explicit modular workspace documents {#explicit-modular-workspace-documents}

Put `includes` in the root workspace file when you want to keep configuration in several files:

```toml
# gazette.toml
includes = ["principals.toml", "sites/notes.toml"]
```

List every required file relative to that root\. An include cannot add another include\. Gazette reads the listed files and rejects missing, duplicate, extra, linked, special, changing or case\-aliased paths\. It does not scan siblings or fall back to another workspace\. Gazette first reads the root to learn which files to capture, then checks that those root bytes still agree when it reads the complete set\.

Every file uses the same schema\. List declarations combine, but a workspace\-level singleton table belongs to only one file\. A duplicate identity or conflicting reference fails the same way it would in a single file\. An include never overrides a declaration just because it appears later\.

Use the Rust SDK's `configuration::load_workspace(root, workspace_path, limits)` or run the CLI:

```console
"$GAZETTE" check workspace /absolute/config-root --workspace gazette.toml --allow-read
```

In MCP, call `load_workspace` with the absolute root, root\-relative `EntryPath`, read permission and limits\. The CLI and MCP report the document inventory and compiled result\. Each document gets its own path and digest\. The set has a version\-framed digest in path order\. An origin query returns the declaring file, its digest and the span in that file\.

For a standalone buffer, supply `source` to MCP `check_workspace` or use `gazette check --stdin`\. A detached buffer cannot load includes or resolve workspace\-relative source roots because it has no containing directory\. To check pages as well, use the native workspace selection described above\.

## Name the objects and their references {#identity-and-references}

- Keys are opaque, case\-sensitive `namespace:local` values with nonempty parts and no whitespace/control characters\. Their declaration proves no identity\.
- A publisher must explicitly reference a declared person or organization\. Authors, brands, contacts and controllers are not fallback publishers\.
- At least one site is required\. Projects without placements remain in the complete desired state\. Omitted declarations are not recovered from a store\.
- A rendered placement requires a `documents` source reference and logical target\. Disabled placements may omit that binding; any supplied binding still resolves\. Source selections are shared declarations, not inferred from project names\.
- Duplicate keys, conflicting identity forms, duplicate site/project placements and unresolved references fail the entire compilation\. Independent semantic failures accumulate deterministically; schema errors stop dependent resolution\.
- All state axes, placement roles and placement flags are required\. No active/public/available or deployable defaults are manufactured\. Unknown fields and enum values fail\.
- Declaration order does not change resolved topology\. Exact source identity includes comments, whitespace and order; it is not an artifact digest\.

A successful pure check means **internally resolved topology only**\. It does not certify content, verify owner facts, reconcile the registry, establish an exact source pin, bind a Theme envelope or authorize publication\. Failures produce no partial workspace on stdout and exit unsuccessfully\. Correct the declaration and rerun the complete check; no native recovery is needed because no state was changed\.

Project `lifecycle` uses `planned`, `active`, `paused`, `done` or `closed`\. It remains separate from the project's visibility and availability, and from content's `draft`, `published` or `archived` state\. Earlier project\-state spellings are rejected rather than silently translated\.

## Origins and introspection {#origins-and-introspection}

Origin queries explain which declaration supplied a value\. They inspect the same parsed workspace used by resolution; they do not load another source of truth\.

### Find where a field was declared {#exact-field-origins}

The shared compiler can retain the original syntax alongside the resolved workspace with `workspace::ParsedWorkspace::parse`\. Its `origin` operation takes one `FieldQuery`: declaration kind, exact identity and typed key/index path\. It returns the original UTF\-8 byte range and source digest\. Semantic sorting does not change the source coordinate, and source\-binding keys stay distinct from similarly named principals\. No textual name search or second TOML parser is involved\.

For the documentation\-repository declaration in [repository settings](#developer-manual-and-generated-reference-repository-settings):

```sh
"$GAZETTE" check --stdin --origin '{"kind":"brand","identity":"example:brand","field":["publications",0,"documentation_repository","path"]}' < workspace.toml
```

The whole workspace must resolve before a location is returned\. Missing or defaulted fields receive no invented origin\. Field arrays use original source order; string components are exact decoded TOML keys, not dotted paths\. The read\-only command cannot be combined with source acquisition\. These coordinates are not LSP UTF\-16 positions or ownership evidence\. Typed composition inheritance has its own [winning\-source query](#composition-origins)\. Imports and a complete override\-history view remain outside this query\. Current LSP/MCP authoring sessions project compiler\-owned declarations, references, effective values and winning origins without reparsing the workspace in an interface; see [the LSP contract](/gazette/lsp)\. Cross\-document edits, rename and formatting remain separate editor capabilities\.

### Publication origins {#publication-origins}

Publication fields have a separate `PublicationOriginQuery` with a site and typed field path\. `ParsedWorkspace::publication_origin` and `ParsedWorkspaceDocuments::publication_origin` return the winning value, its workspace\-default, publisher or site scope, and the original document coordinates\. The CLI exposes the same explanation as `gazette check --why contacts.rights --site site:notes`; see [shared publication settings](/gazette/workspace-publications#shared-publication-settings)\.

### Composition origins {#composition-origins}

Each resolved `Selected<T>` retains its winning `SelectionOrigin`\. For an effective Theme's source field:

```sh
"$GAZETTE" check --stdin --composition-origin '{"site":"example:site","field":{"kind":"theme"},"path":["source"]}' < workspace.toml
```

Use `{"kind":"plugin","package":"search-plugin"}` for plugin activation, `{"kind":"capability","capability":"publication.search/v1"}` for a capability atom, or `{"kind":"resource","resource":"module:search"}` for a resource selection\. A relative `path` such as `["provider","package"]` selects one field; an empty path selects the whole atom\. The Rust operation is `ParsedWorkspace::composition_origin` with the shared `CompositionOriginQuery`\. It follows the resolver's winner back into the original AST, preserving quoted keys, original site order, Unicode/CRLF byte coordinates and exact source digest\. Inherited values point to workspace source, never fabricated local fields\. Omitted fields still have no explicit location\. Origin queries cannot be combined with each other or source\-acquisition options\.

## Continue by task {#continue-by-task}

<a id="example"></a> <a id="acquire&#45;pinned&#45;documentation&#45;for&#45;a&#45;site"></a> <a id="materialization&#45;obligation&#45;dependency"></a> <a id="parse&#45;retained&#45;documentation"></a> <a id="resolution&#45;rules"></a> <a id="bind&#45;content&#45;to&#45;the&#45;workspace"></a>

### Choose and read workspace sources {#choose-and-read-workspace-sources}

[Choose and read workspace sources](/gazette/workspace-sources)\. Bind a project to source files, check which files Gazette will read, and inspect the parsed documents before you build\.

<a id="explicit&#45;filesystem&#45;exclusions"></a>

[Exclude paths from a local source](/gazette/workspace-sources#explicit-filesystem-exclusions)\.

<a id="publication&#45;acquisition"></a>

[Read sources for a publication](/gazette/workspace-sources#publication-acquisition)\.

<a id="brand&#45;publication&#45;settings"></a> <a id="compose&#45;owner&#45;held&#45;legal&#45;copy&#45;without&#45;duplicating&#45;it"></a> <a id="processing&#45;choices&#45;describe&#45;intent&#45;not&#45;running&#45;services"></a> <a id="plain&#45;native&#45;document&#45;defaults"></a> <a id="mount&#45;native&#45;documentation&#45;beneath&#45;an&#45;existing&#45;publication"></a> <a id="principal&#45;display&#45;names"></a> <a id="principal&#45;websites&#45;and&#45;identity&#45;references"></a> <a id="contact&#45;projection&#45;dependency"></a> <a id="independent&#45;site&#45;responsibilities"></a> <a id="developer&#45;manual&#45;and&#45;generated&#45;reference&#45;repository&#45;settings"></a> <a id="publication&#45;destination"></a>

### Configure publication identity and delivery {#configure-publication-identity-and-delivery}

[Configure publication identity and delivery](/gazette/workspace-publications)\. Set who publishes, what the site includes, and where its site or developer docs can be delivered\.

<a id="theme&#45;plugin&#45;capability&#45;provider&#45;and&#45;resource&#45;composition"></a> <a id="acquire&#45;the&#45;effective&#45;composition"></a> <a id="check&#45;captured&#45;package&#45;declarations"></a> <a id="supply&#45;declared&#45;theme&#45;inputs&#45;from&#45;a&#45;shared&#45;source"></a> <a id="validate&#45;the&#45;complete&#45;selected&#45;package&#45;set"></a> <a id="compile&#45;selected&#45;retained&#45;templates"></a> <a id="site&#45;chrome&#45;and&#45;control&#45;copy"></a> <a id="project&#45;resource&#45;destinations"></a>

### Compose themes and site resources {#compose-themes-and-site-resources}

[Compose themes and site resources](/gazette/workspace-presentation)\. Attach a Theme, choose providers and shared resources, and set presentation for a single page or the whole site\.

<a id="per&#45;content&#45;presentation&#45;selection"></a>

[Choose a template for one page](/gazette/workspace-presentation#per-content-presentation-selection)\.

<a id="taxonomy&#45;catalog&#45;and&#45;language&#45;scope"></a> <a id="generated&#45;reading&#45;indexes"></a> <a id="machine&#45;readable&#45;publication&#45;outputs"></a> <a id="preferred&#45;source&#45;invitations"></a>

### Configure navigation and discovery {#configure-navigation-and-discovery}

[Configure navigation and discovery](/gazette/workspace-discovery)\. Set which content appears in reading indexes and what the site emits for search engines and other readers\.

## Local build defaults {#local-build-defaults}

`[build]` owns the default `sites` list and `local_drafts` choice\. Optional `corpus_bytes` sets the aggregate authored\-input ceiling, including opaque assets, and `math` selects native typesetting\. Invocation overrides win; omitted settings retain Gazette's native defaults\. Execution permission stays with each call, never in this configuration\. See [local rendering](/gazette/local-rendering#local-site-sets) for the direct workspace command, math defaults and input\-size report\.

Native `gazette check` and MCP `check_workspace` use the same configured corpus ceiling without running math\. An explicit SDK `CorpusLimits.source_bytes` takes precedence, including a lower value\. Per\-document parser and source\-acquisition limits remain separate\.

### Social\-card renderer {#social-card-renderer}

An optional root\-level `social_card_renderer` binds the exact Node and browser executables used by Gazette's fixed capture helper\. Each field is a `PinnedExecutable`: an absolute `program` path and an `executable` table with the file's positive byte length, at most 256 MiB, and complete SHA\-256\. Both pins use the existing native command validation\. Neither executable is found through `PATH`, and selecting them grants no execution permission\. A renderer can set `jpeg_quality` from 1 to 100 for compressed JPEG thumbnails\. Without that selection the renderer emits PNG\.

The binding has exactly two fields, `node` and `browser`\. It accepts no caller arguments, environment, working directory, source binding or helper entrypoint\. Helper bytes are embedded engine inputs; selecting a renderer does not add a workspace source\. A split workspace may declare the binding in one included configuration document\. Two declarations fail even when equal, so document order cannot select a different executable\. Pins establish executable\-byte identity, not the identity of shared libraries, fonts or other ambient runtime inputs\.

The Theme separately declares the [social\-card recipe](/gazette/theme-reference#publication-home-social-card-recipe), including its template, dimensions and media selection\. An explicit publication link\-preview asset keeps precedence over generated output\.
