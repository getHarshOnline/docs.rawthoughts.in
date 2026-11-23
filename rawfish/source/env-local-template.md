---
title: ".env.local.template"
noindex: true
---

```template
# RawFish local-stack env template.
#
# Copy to .env.local, then set NEO4J_PASSWORD and SECRET_KEY before
# running `make up`.

AUTH_ENABLED=false
SECRET_KEY=CHANGE-ME-to-a-32-plus-char-random-string-via-secrets-token-hex
FLASK_PORT=5001

# RawFish report-generator provider. This default uses native Ollama on
# the host and requires no external credentials.
RAWFISH_LLM_PROVIDER_MODE=local_ollama
RAWFISH_LLM_PROVIDER=
RAWFISH_LLM_API_KEY=
RAWFISH_LLM_BASE_URL=http://localhost:11434/v1
# Optional container override for `make up`. Leave empty unless your
# Docker host gateway differs from Docker Desktop's host.docker.internal.
RAWFISH_CONTAINER_LLM_BASE_URL=
RAWFISH_LLM_MODEL=qwen3-coder:30b
RAWFISH_LLM_READINESS_TIMEOUT_SEC=10
RAWFISH_LLM_GENERATION_TIMEOUT_SEC=120
RAWFISH_LLM_MAX_RETRIES=1

LLM_JSON_MODE=loose
POLICY_MAX_TOKENS_REPORT=16384
POLICY_MAX_TOKENS_ONTOLOGY=8192

IDEMPOTENCY_WAIT_SECONDS=5
IDEMPOTENCY_CLAIM_TTL_SECONDS=900

# Audience store: Graphiti against local Neo4j in Docker.
ZEP_MODE=graphiti
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=CHANGE-ME-to-any-non-empty-string

# Graphiti's own local client. These names come from Graphiti's client
# library; they are separate from RawFish provider-router settings.
OPENAI_API_KEY=local-graphiti-key
OPENAI_BASE_URL=http://localhost:11434/v1
# Optional container override for Graphiti's local client inside Docker.
RAWFISH_CONTAINER_OPENAI_BASE_URL=
OPENAI_MODEL=qwen3-coder:30b
OPENAI_EMBEDDING_MODEL=nomic-embed-text
OPENAI_EMBEDDING_DIM=768
OPENAI_RERANKING_MODEL=qwen3-coder:30b

# Frontend build-arg, only relevant for auth-enabled production builds.
# The local compose stack runs AUTH_ENABLED=false and permits this to be empty.
VITE_API_KEY=
```
