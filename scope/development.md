---
title: "Development"
---

<a id="development"></a>

Build the standalone Rust library before you make a change\. The current build has no context service\. Use [the architecture](/scope/concepts) to see where to add a source adapter, a storage change or a retrieval rule\.

## Building the library {#building-the-library}

You need Rust and Cargo\. Run the commands from the repository root\. The crate has no external dependencies\.

<Steps>

<Step title="Build the library" id="gazette-layout-0">

```sh
cargo build --locked --offline --manifest-path kernel/Cargo.toml
```

Cargo should finish building `scope-kernel`\. Keep `--locked` so that the command uses the repository's lockfile\.

</Step>

<Step title="Check the current test target" id="gazette-layout-1">

```sh
cargo test --locked --offline --manifest-path kernel/Cargo.toml
```

Cargo currently reports zero unit tests and zero doc tests\. This command checks that the test targets compile\.

</Step>

</Steps>

## Where a change belongs {#how-the-repository-is-laid-out}

Start in `kernel/` for library work\. It holds the crate alone today\. Admission of each source owner's snapshot arrives as one module per owner, as [Source imports](/scope/engineering/source-imports) lists the owners, each with its first admission check and test\. Keep repository, mailbox and database access with the source owners\.

A folder is created with its first operation and test, and each lives in the place below\.

| Folder | What goes there |
| --- | --- |
| `cli/` and `daemon/` | The command line \(`scope resolve`, `read`, `report-use`, `migrate`, `seed`, `optimize` and `permissions`\) and the daemon, the single writer of accepted records, with its local transport, restricted loopback bridge and the [diagnostic stream](/scope/engineering/diagnostics)\. |
| `schema/` | Storage migrations V001 to V005, run by the journaled runner on [Durability and recovery](/scope/engineering/durability-and-recovery)\. |
| `protos/` | Client transport and language definitions, generated with `buf generate` after contract validation\. |
| `bindings/python/` and `bindings/typescript/` | The Python binding, a maturin build of the kernel published as `scope-kernel`, and the TypeScript client `@rtepl/scope-client`, whose hooks and components are for React\. A Hugging Face or PyTorch integration is a possibility only if a learned scorer needs a training path\. |
| `dashboard/` | Contract tests for the diagnostic client, which a separately owned viewer renders; the stream's design is on Diagnostics\. |
| `plugins/` | Client plugins, such as the admitted browser plugin the daemon's loopback bridge serves\. |

The paper in `paper/` is separate from the service design\.

Publish schemas, a generated manifest, canonicalisation examples and contract tests in the planned `contracts/` directory\. Clients will pin that manifest by hash\. Wait for it before writing an integration\.

## Rules every change keeps {#rules-every-change-keeps}

| If you change | Keep this rule |
| --- | --- |
| Source adapters | The source owner reads the original and keeps credentials\. Scope accepts only the supplied snapshot\. |
| Stored data | Keep credentials, provider\-session material and executable credential bindings out of schemas, data, bundles, acknowledgements, logs and diagnostics\. Check that even a non\-secret source or grant reference is allowed\. |
| Retrieval | Check access and validity before searching or ranking\. A high score cannot make a source eligible or remove context the task requires\. |
| Persistence | Commit the complete change before readers can see it\. Rebuild indexes from committed records\. |
| Signed records | Canonicalise with RFC 8785, hash with SHA\-256 and sign over the contract's domain prefix\. A record's digest does not cover itself\. |
| Learning | Propose, review and release changes separately\. Production retrieval cannot rewrite its own policy\. |

<Warning>

Do not put operational data, personal records, credentials or database files in this repository\. Use synthetic examples for development\.

</Warning>

The [snapshot design](/scope/concepts#owners-hand-scope-snapshots-scope-never-reads-a-source) explains why acquisition belongs outside Scope\. For the user\-facing consequences, return to [Context for a task](https://rawthoughts.in/scope/context-for-a-task/)\.

## Contributions {#contributions}

Scope is not accepting outside contributions yet\. Each contributor must first accept the [contributor agreement](/scope/source/CLA-md), which needs legal review and a way to record acceptance before intake opens; [CONTRIBUTING\.md](/scope/source/CONTRIBUTING-md) explains it\. An accepted contribution follows the repository's licence, AGPL\-3\.0\-or\-later\. Issues are welcome\. Commercial licensing questions go to the address in the [README's licence section](/scope/repository#licence)\.
