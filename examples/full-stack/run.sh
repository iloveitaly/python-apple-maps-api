#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

pids=()

cleanup() {
  for pid in "${pids[@]:-}"; do
    kill "$pid" 2>/dev/null || true
  done
  wait 2>/dev/null || true
}
trap cleanup EXIT INT TERM

echo "starting API server on http://127.0.0.1:8765"
uv run python app/server.py &
pids+=($!)

echo "starting React frontend on http://localhost:5173"
(cd web && pnpm dev) &
pids+=($!)

wait
