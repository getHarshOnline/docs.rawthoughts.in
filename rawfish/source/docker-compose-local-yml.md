---
title: "docker-compose.local.yml"
noindex: true
---

```yml
# Local-stack compose file.
#
# Brings up the full RawFish demo against:
#   * Neo4j Community  (in this compose; data persisted via named volume)
#   * RawFish backend + frontend  (in this compose; bound to loopback)
#   * Native Ollama on the host  (NOT in this compose; see below)
#
# WHY NATIVE OLLAMA ON MAC:
#   Docker Desktop on macOS runs Linux containers inside a VM (lima /
#   QEMU). That VM cannot reach the host's Metal / MPS GPU, so an
#   Ollama container on Apple Silicon falls back to CPU-only inference
#   -- 5-10x slower than a native install. For a usable demo on an M4
#   Max, Ollama MUST run natively. The RawFish + Neo4j containers
#   reach Ollama at ``host.docker.internal:11434`` (Docker Desktop
#   resolves this to the host loopback).
#
# Bring the stack up with:
#   bash process/local_stack.sh up
#
# Or directly:
#   docker compose -f docker-compose.local.yml up -d
#
# Tear down with:
#   bash process/local_stack.sh down
#
# Ports (all loopback-bound; the hygiene gate
# check_docker_compose_loopback.sh enforces this):
#   3000  -- RawFish frontend (Vite preview of built bundle)
#   5001  -- RawFish backend
#   7474  -- Neo4j HTTP browser
#   7687  -- Neo4j Bolt
#   11434 -- Ollama (native on host)

services:
  neo4j:
    image: neo4j:5-community
    container_name: rawfish-local-neo4j
    ports:
      - "127.0.0.1:7474:7474"
      - "127.0.0.1:7687:7687"
    environment:
      NEO4J_AUTH: "neo4j/${NEO4J_PASSWORD:?NEO4J_PASSWORD must be set; do not use the dev default for any non-local environment}"
      NEO4J_ACCEPT_LICENSE_AGREEMENT: "yes"
      # Generous heap (4 GB) and page cache (2 GB) for local work; adjust down
      # for smaller machines.
      NEO4J_server_memory_heap_initial__size: "4G"
      NEO4J_server_memory_heap_max__size: "4G"
      NEO4J_server_memory_pagecache_size: "2G"
    volumes:
      - rawfish-local-neo4j-data:/data
      - rawfish-local-neo4j-logs:/logs
    healthcheck:
      test:
        - "CMD-SHELL"
        - "pass=\"$${NEO4J_AUTH#neo4j/}\"; cypher-shell -u neo4j -p \"$$pass\" 'RETURN 1' || exit 1"
      interval: 10s
      timeout: 5s
      retries: 12
      start_period: 30s
    restart: unless-stopped

  rawfish:
    # Build the same image the root docker-compose.yml does so the
    # bundled frontend + uv-locked backend stay in lockstep with the
    # rest of the repo. ``--build`` is the default on first run.
    build:
      context: .
      args:
        VITE_API_KEY: ${VITE_API_KEY:-}
        # Local compose runs the image with AUTH_ENABLED=false, so the
        # frontend bundle does not need a baked request key. The root
        # production compose path keeps the Dockerfile's strict default.
        ALLOW_EMPTY_VITE_API_KEY: "true"
    image: rawfish-local:latest
    container_name: rawfish-local-app
    depends_on:
      neo4j:
        condition: service_healthy
    ports:
      - "127.0.0.1:3000:3000"
      - "127.0.0.1:5001:5001"
    environment:
      # --- Auth + boot ---
      AUTH_ENABLED: "false"
      SECRET_KEY: "${SECRET_KEY:?SECRET_KEY must be set to a 32+ char string}"
      FLASK_PORT: "5001"
      FLASK_ENV: "development"
      # The host publish is still loopback-only; this bind is internal
      # to the container so Docker can forward 127.0.0.1:5001 on the host.
      RAWFISH_BACKEND_BIND: "0.0.0.0:5001"
      OASIS_SIMULATION_DATA_DIR: "/app/backend/uploads"

      # --- RawFish provider-router LLM (Ollama via host) ---
      RAWFISH_LLM_PROVIDER_MODE: "${RAWFISH_LLM_PROVIDER_MODE:-local_ollama}"
      RAWFISH_LLM_PROVIDER: "${RAWFISH_LLM_PROVIDER:-}"
      RAWFISH_LLM_API_KEY: "${RAWFISH_LLM_API_KEY:-}"
      # Host-side scripts use RAWFISH_LLM_BASE_URL=http://localhost:11434/v1.
      # Containers need Docker's host gateway name to reach native Ollama.
      RAWFISH_LLM_BASE_URL: "${RAWFISH_CONTAINER_LLM_BASE_URL:-http://host.docker.internal:11434/v1}"
      RAWFISH_LLM_MODEL: "${RAWFISH_LLM_MODEL:-hf.co/unsloth/gemma-4-31B-it-GGUF:Q4_K_M}"
      RAWFISH_LLM_READINESS_TIMEOUT_SEC: "${RAWFISH_LLM_READINESS_TIMEOUT_SEC:-10}"
      RAWFISH_LLM_GENERATION_TIMEOUT_SEC: "${RAWFISH_LLM_GENERATION_TIMEOUT_SEC:-120}"
      RAWFISH_LLM_MAX_RETRIES: "${RAWFISH_LLM_MAX_RETRIES:-1}"
      LLM_JSON_MODE: "${LLM_JSON_MODE:-loose}"
      POLICY_MAX_TOKENS_REPORT: "${POLICY_MAX_TOKENS_REPORT:-16384}"
      POLICY_MAX_TOKENS_ONTOLOGY: "${POLICY_MAX_TOKENS_ONTOLOGY:-8192}"

      # --- Audience store: Graphiti against local Neo4j ---
      ZEP_MODE: "graphiti"
      NEO4J_URI: "bolt://neo4j:7687"
      NEO4J_USER: "neo4j"
      NEO4J_PASSWORD: "${NEO4J_PASSWORD}"

      # --- Graphiti's own local client (separate from RawFish provider router) ---
      OPENAI_API_KEY: "${OPENAI_API_KEY:-local-graphiti-key}"
      OPENAI_BASE_URL: "${RAWFISH_CONTAINER_OPENAI_BASE_URL:-http://host.docker.internal:11434/v1}"
      OPENAI_MODEL: "${OPENAI_MODEL:-hf.co/unsloth/gemma-4-31B-it-GGUF:Q4_K_M}"
      OPENAI_EMBEDDING_MODEL: "${OPENAI_EMBEDDING_MODEL:-nomic-embed-text}"
      OPENAI_EMBEDDING_DIM: "${OPENAI_EMBEDDING_DIM:-768}"
      OPENAI_RERANKING_MODEL: "${OPENAI_RERANKING_MODEL:-hf.co/unsloth/gemma-4-31B-it-GGUF:Q4_K_M}"
    extra_hosts:
      # Make host.docker.internal resolvable on Linux Docker (it's
      # automatic on Docker Desktop for Mac, but the explicit entry
      # makes the file work cross-platform).
      - "host.docker.internal:host-gateway"
    volumes:
      - ./backend/uploads:/app/backend/uploads
      - rawfish-local-runner-state:/app/backend/run_state
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "curl -fsS http://127.0.0.1:5001/health || exit 1"]
      interval: 15s
      timeout: 5s
      retries: 10
      start_period: 45s

volumes:
  rawfish-local-neo4j-data:
  rawfish-local-neo4j-logs:
  rawfish-local-runner-state:
```
