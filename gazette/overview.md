---
title: "Gazette developer guide"
---

<a id="gazette&#45;developer&#45;guide"></a>

Gazette publishes a body of thought from the whole to its parts, and makes that structure what readers, search, feeds, JSON\-LD and `llms.txt` index\. This guide is for developers who build an editor integration, extend a Theme or embed Gazette in an application: the Rust compiler resolves content, relationships and addresses once for the CLI, agent server, editors and SDKs\. Among the products [RawThoughts](https://rawthoughts.in/) builds, Gazette carries approved work outward, and it works as a product of its own\.

To write and preview a publication, start with [Your first publication](https://rawthoughts.in/gazette/first-publication/)\.

## Start with your integration {#start-with-your-integration}

<CardGroup>

<Card href="&#47;gazette&#47;install&#35;what&#45;a&#45;build&#45;needs" title="Build Gazette" id="gazette-layout-0">

Compile the executable and continue with a publication or integration\.

</Card>

<Card href="&#47;gazette&#47;architecture" title="Understand the architecture" id="gazette-layout-1">

Follow a content change from source files through the compiler to its outputs\.

</Card>

<Card href="&#47;gazette&#47;mcp&#45;quickstart" title="Connect an MCP client" id="gazette-layout-2">

Start the local server and check a workspace from your client\.

</Card>

<Card href="&#47;gazette&#47;sdk&#47;js&#47;overview&#35;check&#45;a&#45;configuration&#45;and&#45;locate&#45;a&#45;field" title="Use the JavaScript SDK" id="gazette-layout-3">

Check a complete configuration from Node and locate a field in its source\.

</Card>

</CardGroup>

[Publications built with Gazette](/gazette/previews) shows six live sites and the Theme each uses\.

## Extend Gazette {#extend-gazette}

| You are building | Read |
| --- | --- |
| Editor support | [LSP](/gazette/lsp), [VS Code](/gazette/vscode) |
| A theme or component | [Theme contract](/gazette/theme-reference), [Tera](/gazette/tera) |
| Browser search and other browser features | [Browser SDK](/gazette/sdk/js/browser), [capability bindings](/gazette/browser-capabilities) |
| A developer\-documentation build | [Mintlify integration](/gazette/mintlify), [documentation generators](/gazette/documentation-generators) |
| Delivery or recovery tooling | [Release operations](/gazette/releasing), [store](/gazette/store), [recovery](/gazette/recovery) |

## Look up a contract {#look-up-a-contract}

[Workspace configuration](/gazette/workspace) covers how to validate the setup, read its sources and choose a Theme\. The [content model](/gazette/content-model) explains pages, collections, journeys and authorship\. Use [Markdown](/gazette/markdown), [page resources](/gazette/page-resources) and [notebooks](/gazette/notebooks) for the supported source formats\.

Use [local rendering](/gazette/local-rendering) to build or inspect site files and [preview](/gazette/preview) to serve them locally\. See [routing](/gazette/routing), [links and crossings](/gazette/links-and-crossings), [feeds](/gazette/feeds), [JSON\-LD](/gazette/json-ld) and [deployment files](/gazette/deployment-output) for what Gazette emits\. To update a configured destination, follow [output materialization](/gazette/output-materialization)\.

Integrations that prepare public output also need [policy checks](/gazette/policy-checks), [disclosure checks](/gazette/output-disclosure) and [delivery observation](/gazette/delivery)\. These operations are separate from ordinary analysis and rendering\.

Use `gazette schema` to print a declaration schema, and `gazette <command> --help` for command inputs and permissions\.

Gazette is licensed under the GNU Affero General Public License, version 3 or later\. See [LICENSE](/gazette/source/LICENSE) and the [distribution notices](/gazette/install#generate-distribution-notices)\.
