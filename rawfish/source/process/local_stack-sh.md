---
title: "process/local_stack.sh"
noindex: true
---

```sh
#!/usr/bin/env bash
# RawFish local-stack orchestrator.
#
# One command. Spins up the full local demo:
#   * native Ollama on the host (Metal-accelerated; this is why we
#     don't containerise Ollama on a Mac)
#   * Neo4j Community in Docker (data persisted in a named volume)
#   * RawFish backend + frontend in Docker (loopback-bound)
#
# Usage:
#   bash process/local_stack.sh up        # bring everything up
#   bash process/local_stack.sh down      # stop containers (keep data)
#   bash process/local_stack.sh purge     # stop + drop Neo4j volume
#   bash process/local_stack.sh status    # show what's running
#   bash process/local_stack.sh logs      # tail container logs
#   bash process/local_stack.sh pull      # only pull / refresh Ollama models
#   bash process/local_stack.sh restart   # down + up
#
# First run:
#   1. Copy .env.local.template -> .env.local
#   2. Set NEO4J_PASSWORD + SECRET_KEY in .env.local
#   3. bash process/local_stack.sh up
#
# Exit codes: 0 on success, non-zero on any boot step failure.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
COMPOSE_FILE="$REPO_ROOT/docker-compose.local.yml"
ENV_FILE="$REPO_ROOT/.env.local"
ENV_TEMPLATE="$REPO_ROOT/.env.local.template"

# ANSI helpers (only when stdout is a tty)
if [ -t 1 ]; then
  C_GREEN=$'\e[32m'; C_RED=$'\e[31m'; C_YELLOW=$'\e[33m'; C_BLUE=$'\e[34m'
  C_BOLD=$'\e[1m'; C_RESET=$'\e[0m'
else
  C_GREEN=""; C_RED=""; C_YELLOW=""; C_BLUE=""; C_BOLD=""; C_RESET=""
fi
say()  { printf "%s%s%s\n" "$C_BLUE" "$*" "$C_RESET"; }
ok()   { printf "%s✓ %s%s\n" "$C_GREEN" "$*" "$C_RESET"; }
warn() { printf "%s! %s%s\n" "$C_YELLOW" "$*" "$C_RESET"; }
die()  { printf "%s✗ %s%s\n" "$C_RED" "$*" "$C_RESET" 1>&2; exit 1; }

# --- env loading ---
require_env_file() {
  if [ ! -f "$ENV_FILE" ]; then
    warn ".env.local not found at $ENV_FILE"
    say  "Creating it from the template. Edit it before re-running."
    cp "$ENV_TEMPLATE" "$ENV_FILE"
    die "Edit $ENV_FILE -- set NEO4J_PASSWORD and SECRET_KEY -- then re-run."
  fi
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
  [ -n "${NEO4J_PASSWORD:-}" ] && [ "$NEO4J_PASSWORD" != "CHANGE-ME-to-any-non-empty-string" ] || \
    die "NEO4J_PASSWORD in .env.local is unset or still the template placeholder."
  [ -n "${SECRET_KEY:-}" ] && [ ${#SECRET_KEY} -ge 32 ] || \
    die "SECRET_KEY in .env.local must be at least 32 characters. Generate with: python3 -c 'import secrets; print(secrets.token_hex(32))'"
}

# --- ollama on the host ---
ensure_ollama_host() {
  command -v ollama >/dev/null 2>&1 || \
    die "Native Ollama not found. Install from https://ollama.com/download (required for Metal GPU acceleration on Apple Silicon)."
  if ! curl -fsS --max-time 2 http://localhost:11434/api/tags >/dev/null 2>&1; then
    say "Starting native Ollama in the background..."
    nohup ollama serve >/tmp/rawfish-ollama.log 2>&1 &
    local tries=0
    until curl -fsS --max-time 2 http://localhost:11434/api/tags >/dev/null 2>&1; do
      tries=$((tries + 1))
      if [ "$tries" -gt 30 ]; then
        die "Ollama did not come up within 30s. Check /tmp/rawfish-ollama.log"
      fi
      sleep 1
    done
  fi
  ok "Ollama listening at http://localhost:11434"
}

pull_ollama_models() {
  local need_chat="${RAWFISH_LLM_MODEL:-qwen3-coder:30b}"
  local need_embed="${OPENAI_EMBEDDING_MODEL:-nomic-embed-text}"
  local need_rerank="${OPENAI_RERANKING_MODEL:-$need_chat}"
  local installed
  installed="$(ollama list 2>/dev/null | awk 'NR>1 {print $1}')"
  for model in "$need_chat" "$need_embed" "$need_rerank"; do
    if echo "$installed" | grep -Fxq "$model"; then
      ok "Ollama model already present: $model"
    else
      say "Pulling Ollama model: $model (this can take a while on first run)..."
      ollama pull "$model" || die "ollama pull $model failed"
      ok "Pulled $model"
    fi
  done
}

# --- docker stack ---
ensure_docker() {
  command -v docker >/dev/null 2>&1 || die "Docker is required."
  docker compose version >/dev/null 2>&1 || die "docker compose v2 is required."
  docker info >/dev/null 2>&1 || die "Docker daemon is not running. Start Docker Desktop."
}

compose() {
  docker compose --env-file "$ENV_FILE" -f "$COMPOSE_FILE" "$@"
}

# --- post-up smoke check ---
wait_for_backend() {
  say "Waiting for RawFish backend health endpoint..."
  local tries=0
  until curl -fsS --max-time 2 http://localhost:5001/health >/dev/null 2>&1; do
    tries=$((tries + 1))
    if [ "$tries" -gt 60 ]; then
      warn "Backend did not pass /health within 60s; check 'bash process/local_stack.sh logs'."
      return 1
    fi
    sleep 1
  done
  ok "Backend healthy at http://localhost:5001/health"
}

probe_frontend() {
  if curl -fsS --max-time 4 -o /dev/null -w "%{http_code}" http://localhost:3000/ | grep -q 200; then
    ok "Frontend reachable at http://localhost:3000/"
  else
    warn "Frontend not yet responding on :3000; give it a few more seconds."
  fi
}

probe_ollama_model() {
  #: Real JSON-mode probe -- 4 checks that mirror RawFish's exact
  #: call pattern (response_format=json_object, schema in system
  #: prompt, predictor-refusal contract). Exit 0 = green, 1 = a
  #: hard check failed (block the demo), 2 = only the warning-only
  #: predictor-refusal check flagged leaks (warn but proceed; RawFish's
  #: language guard catches leaks downstream).
  local rc=0
  python3 "$REPO_ROOT/process/probe_llm_json_mode.py" || rc=$?
  case "$rc" in
    0) ok "JSON-mode probe: all hard checks pass" ;;
    2) warn "JSON-mode probe: hard checks pass; predictor-refusal check flagged leaks (language guard will catch them, but a different model may behave better)" ;;
    *)
       die "JSON-mode probe FAILED. RawFish's report generation will not produce parseable JSON against this model. Edit RAWFISH_LLM_MODEL in .env.local and re-run 'make pull-models' + 'make up'. Suggested swap-in candidates are listed in .env.local.template (qwen3-coder:30b, gemma3:27b, mistral-small:24b-instruct-2501-q4_K_M, llama3.3:70b-instruct-q4_K_M).";;
  esac
}

print_banner() {
  cat <<EOF

${C_BOLD}=== RawFish local stack is up ===${C_RESET}

  Frontend cockpit:      ${C_GREEN}http://localhost:3000/${C_RESET}
  Backend catalog:       ${C_GREEN}http://localhost:5001/api/sim/use-cases/creator/catalog${C_RESET}
  Neo4j browser:         ${C_GREEN}http://localhost:7474${C_RESET}   (user: neo4j)
  Ollama (native):       ${C_GREEN}http://localhost:11434${C_RESET}

  Active chat model:     ${C_BOLD}${RAWFISH_LLM_MODEL:-qwen3-coder:30b}${C_RESET}
  Active embed model:    ${C_BOLD}${OPENAI_EMBEDDING_MODEL:-nomic-embed-text}${C_RESET}
  ZEP_MODE:              ${C_BOLD}graphiti${C_RESET} (real Neo4j round-trip; zero mock fixtures)

  Tear down:             ${C_YELLOW}bash process/local_stack.sh down${C_RESET}
  Tail logs:             ${C_YELLOW}bash process/local_stack.sh logs${C_RESET}

EOF
}

# --- subcommands ---
cmd_up() {
  ensure_docker
  require_env_file
  ensure_ollama_host
  pull_ollama_models
  say "Building + starting the docker compose stack (neo4j + rawfish)..."
  compose up -d --build
  wait_for_backend || true
  probe_frontend
  probe_ollama_model
  print_banner
}

cmd_down() {
  ensure_docker
  if [ -f "$ENV_FILE" ]; then
    compose down --remove-orphans
  else
    docker compose -f "$COMPOSE_FILE" down --remove-orphans 2>/dev/null || true
  fi
  ok "RawFish containers stopped. Neo4j data volume preserved."
  say "(Native Ollama on the host is left running. Stop it with: pkill -f 'ollama serve')"
}

cmd_purge() {
  cmd_down
  if [ -f "$ENV_FILE" ]; then
    compose down -v --remove-orphans
  else
    docker compose -f "$COMPOSE_FILE" down -v --remove-orphans 2>/dev/null || true
  fi
  ok "Neo4j data volume dropped. Next 'up' starts from a clean graph."
}

cmd_status() {
  ensure_docker
  compose ps 2>/dev/null || warn "compose stack not running"
  echo ""
  if curl -fsS --max-time 1 http://localhost:11434/api/tags >/dev/null 2>&1; then
    ok "Native Ollama: running on :11434"
  else
    warn "Native Ollama: NOT running"
  fi
}

cmd_logs() {
  ensure_docker
  compose logs -f --tail=200
}

cmd_pull() {
  require_env_file
  ensure_ollama_host
  pull_ollama_models
}

cmd_restart() {
  cmd_down
  cmd_up
}

case "${1:-up}" in
  up)       cmd_up ;;
  down)     cmd_down ;;
  purge)    cmd_purge ;;
  status)   cmd_status ;;
  logs)     cmd_logs ;;
  pull)     cmd_pull ;;
  restart)  cmd_restart ;;
  -h|--help|help)
    sed -n '1,30p' "$0"
    ;;
  *)
    die "Unknown command: $1. Run 'bash process/local_stack.sh help'."
    ;;
esac
```
