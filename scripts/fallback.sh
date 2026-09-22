#!/usr/bin/env bash
# Baut jeden Demo-Stand einmal nach _build/fallback/<tag>/.
# Damit lässt sich auf der Bühne auf fertiges HTML ausweichen, falls ein Build klemmt.
set -euo pipefail

cd "$(dirname "$0")/.."

TAGS=$(git tag --list 'stand-*' | sort)
if [ -z "$TAGS" ]; then
  echo "Keine Stände gefunden (git tag stand-*)."
  exit 1
fi

AUSGANG=$(git rev-parse --abbrev-ref HEAD)
mkdir -p _build/fallback

for TAG in $TAGS; do
  echo "== $TAG =="
  git checkout --quiet "$TAG"
  # stand-06-bruch enthält absichtlich eine Schemaverletzung, deshalb kein -W.
  uv run sphinx-build -q -b html handbuch "_build/fallback/$TAG" || true
done

git checkout --quiet "$AUSGANG"
echo "Fertig: _build/fallback/"
