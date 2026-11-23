---
title: "Interfaces"
---

<a id="interfaces"></a>

Use the connection that fits your application\. The CLI works from a shell, standalone MCP gives agents tools to inspect and review workspace configuration, and LSP gives editors feedback on Pale declarations\. ACP conducts a coding\-agent turn\. A2A can hand work to a resident through an authenticated connection\. Shared operations use the same Rust SDK\.

To embed Pale in your process, [choose an SDK](/pale/sdks)\. For workspace inspection or installing repository guidance, follow the [product guides](https://rawthoughts.in/pale/)\.

## Choose a connection {#choose-a-connection}

| When you need to | Use | What the caller supplies |
| --- | --- | --- |
| Inspect configuration, plan repository guidance or apply a reviewed file update from a shell | `pale`\. [Build the CLI](/pale/getting-started#build-the-command-line-tool), then see the [command reference](/pale/interfaces/cli)\. | A command and its inputs\. Read results from standard output and diagnostics from standard error\. |
| Let an agent inspect captured sources or review a proposed change | `pale-mcp`\. See [MCP framing and discovery](/pale/mcp#connect-and-discover)\. | A stdio client that supports the documented protocol revision, and the sources to review\. Check the handshake before relying on a launch entry\. |
| Diagnose and navigate Pale configuration while editing | `pale-lsp`\. See [LSP source capture and synchronization](/pale/interfaces/lsp) and the [VS Code integration](/pale/integrations/vscode)\. | Pale configuration documents\. VS Code starts one server per workspace folder and exposes the Profile Explorer\. |
| Send one prompt through a connected coding agent | `pale-acp`\. See [ACP deadlines, updates and cancellation](/pale/interfaces/acp)\. | Connected input and output streams\. The caller starts the agent\. Pale negotiates ACP v1, creates a session and conducts one prompt turn per call\. |
| Inspect a `Delegate` handle or manage delegated work | `pale-a2a`\. See the [A2A integration](/pale/interfaces/a2a)\. | A handle for inspection, or an authenticated resident attachment to start, advance, observe or cancel work\. The caller arranges the connection\. |

MCP calls the CLI's dispatcher in the same process and works from the sources supplied to the call\. It has no automatic access to an editor's unsaved buffers\. LSP supplies diagnostics, completion, hover, navigation and configuration review for Pale declarations\. Use a language server for the project's own language to inspect its code\.

The ACP conductor ends after one turn\. For a later prompt, arrange another call\. A2A needs a caller\-supplied connection for resident operations\. Discovery and installation are the caller's responsibility\.

## Connect a resident explicitly {#connect-a-resident-explicitly}

A trusted embedding application can supply `ResidentAttachment` to an interface that accepts it\. Its carrier authenticates the resident\. Its response policy checks signatures, changes to who can act and the proofs that prevent replay of an older state\. The [Rust SDK](/pale/sdk/rust#choose-portable-native-or-resident-operations) describes those types\.

Ordinary CLI and MCP sessions start without a resident\. If a resident call loses its response, the operation may still be running\. Observe or reconcile it before retrying\.
