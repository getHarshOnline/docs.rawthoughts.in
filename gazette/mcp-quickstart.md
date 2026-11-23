---
title: "Connect a Gazette MCP client"
---

<a id="connect&#45;a&#45;gazette&#45;mcp&#45;client"></a>

Start Gazette locally and send a configuration check from your own MCP client\. You’ll get back a resolved workspace with one site\. To connect Codex or Claude Code and work on a publication, use [Work with an agent](https://rawthoughts.in/gazette/work-with-an-agent/)\.

## Connect a local client {#connect-a-local-client}

<Steps>

<Step title="Start the server" id="gazette-layout-0">

Configure your client to start the local Gazette executable with the `mcp` argument\.

```sh
/absolute/path/to/gazette mcp
```

Use standard input and output for the protocol\. Send logs to standard error\. Keep the process and its input stream open while the client is connected\. If you need an executable, [build Gazette](/gazette/install#what-a-build-needs) first\.

Starting the server does not read a workspace\. Each tool call supplies its source text or the local sources it is allowed to read\.

</Step>

<Step title="Initialize the connection" id="gazette-layout-1">

Send `initialize` and wait for the server to return the negotiated protocol version\. Then send `notifications/initialized`\. If your client uses the stateless protocol, skip this step and use the stateless example below\.

```json
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-11-25","capabilities":{},"clientInfo":{"name":"publication-integration","version":"0.1.0"}}}
```

```json
{"jsonrpc":"2.0","method":"notifications/initialized"}
```

Write each JSON object on its own line\. Keep standard input open between messages\.

</Step>

<Step title="Discover the tools" id="gazette-layout-2">

In the initialized session, send this request and find `check_workspace` in `result.tools`\. Its input schema describes the `source` field used in the next step\.

```json
{"jsonrpc":"2.0","id":2,"method":"tools/list"}
```

For a stateless client, include the same protocol metadata as in the stateless example below\. [Tool discovery](/gazette/mcp#discovery-and-acceptance) covers filtering and pagination\.

</Step>

</Steps>

## Make a complete supplied\-input call {#make-a-complete-supplied-input-call}

Call `check_workspace` with the configuration inline\. Use the tab for your client’s connection\. This example works without a workspace directory or a publishing account\.

<CodeGroup>

```json Initialized client
{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"check_workspace","arguments":{"source":"principals=[{id='owner:writer',kind='person'}]\nsites=[{id='site:notes',publisher='owner:writer',deployable=false}]\n"}}}
```

```json Stateless client
{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"_meta":{"io.modelcontextprotocol/protocolVersion":"2026-07-28","io.modelcontextprotocol/clientCapabilities":{}},"name":"check_workspace","arguments":{"source":"principals=[{id='owner:writer',kind='person'}]\nsites=[{id='site:notes',publisher='owner:writer',deployable=false}]\n"}}}
```

</CodeGroup>

Look for `result.isError: false` and `result.structuredContent.workspace.sites["site:notes"]`\. It should show `owner:writer` as publisher and `deployable: false`\. The result also includes the source SHA\-256\.

Change only the publisher value to `owner:missing` and send the call again with a new request ID\. Expect a tool result with `isError: true` and a diagnostic about the missing principal\. A malformed JSON\-RPC request instead returns a protocol error\. See [Results and uncertain delivery](/gazette/mcp#results-and-uncertain-delivery) for client error handling\.

## Check your own publication {#check-your-own-publication}

When the example works, call `check_workspace` again without `source`\. Pass `workspace` as the absolute path of a publication folder or workspace file, or omit it to use the folder your client opened:

```json
{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"check_workspace","arguments":{"workspace":"/absolute/path/to/publication"}}}
```

Unlike the supplied\-input call, this reads the workspace's declared sources and checks every page\. The result reports `workspace_location`, `checked_sites` and `diagnostics`; each diagnostic names its file and line, so fix that source and call again\. Nothing is rendered or published\. [Choose what the check reads](/gazette/workspace#configuration-inputs-and-boundaries) explains how Gazette finds a folder\.

When you finish, close the server’s standard input\.

## Continue from the example {#continue-from-the-example}

- [Choose an operation](/gazette/mcp#find-an-operation-contract) to see what each call reads, changes and returns\.
- [Work with an agent](https://rawthoughts.in/gazette/work-with-an-agent/) to review a publication, edit a note and open a preview\.
