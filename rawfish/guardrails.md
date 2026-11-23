---
title: "Guardrails"
---

<a id="guardrails"></a>

RawFish rejects some operations and attaches warnings to others\. A rejected request stops the operation; a warning changes how its result should be read\. Keep that difference visible when integrating a lane or changing report handling\.

## What blocks an operation {#what-blocks-an-operation}

The prototype rejects invalid request, catalog, report and manifest schemas; a catalog missing its `lane_manifest`; an unavailable selected provider; scale above the active cap; and an idempotency key reused with a different body\. Unsafe artifact ids and path traversal are refused too\.

During generation, the report must pass its schema and language check before persistence proceeds\. These checks run at particular boundaries, not continuously over every saved file\.

## What changes the interpretation {#what-changes-the-interpretation}

Numeric and comparative checks can expose gaps or demote claims\. Driver attribution is a co\-occurrence hint rather than a cause\. Missing evidence, field\-validation questions and surrogate sensitivity caveats need to stay with the result they qualify\. An unknown external model price is reported as unavailable\.

Do not turn one of these warnings into a guarantee or hide it behind a successful response\.

## Stored reports need different care {#stored-reports-need-different-care}

Stored JSON reads validate the lane's schema but do not repeat the language check or verify the recorded digest and embedded run identity\. JSON, Markdown and metadata are separate writes, so a readable JSON file can survive a later publication failure\. Integrations must preserve generation errors rather than treating HTTP 200 as completed report publication\. [Report storage](/rawfish/architecture#reports) explains that boundary\.

Creator has another limit: its deterministic runner provides no executed conversation, and its generator does not consume the evidence catalog\. A schema\-valid report and its claim labels cannot create that missing support\. The [findings guide](/rawfish/using#read-what-the-run-actually-supports) explains how readers should use the output\.

## Check source rules and runtime behavior separately {#check-source-rules-and-runtime-behavior-separately}

Static process gates reject stale routes and ids, external font fetches, empty statistical manifests and wording that makes an external provider mandatory\. [Check a change](/rawfish/runbook#maintainer-qualification) lists the commands\. Runtime tests must exercise each lane's rejection and warning paths separately\.

The [rebuild contract](/rawfish/rebuild-target) requires stronger report read\-back and settings guards than this prototype implements\.
