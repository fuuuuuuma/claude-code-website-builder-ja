#!/usr/bin/env python3
"""GPT Image 2.0（gpt-image-2）で Webサイトの背景/装飾/OG画像などを 1 枚生成する最小スクリプト。

Claude Code から呼ぶ前提。OpenAI Images API を直接叩く（標準ライブラリのみ・依存なし）。

前提:
  export OPENAI_API_KEY=sk-...        # 必須（OpenAI Developers のキー）

使い方:
  python3 scripts/gen_image.py --prompt "Webサイトのヒーロー背景。文字は入れない。..." \
      --size 1536x1024 --out assets/hero.png

サイズ:
  gpt-image-2 は 1024x1536（縦）などに対応。幅・高さは 16 の倍数、アスペクト比 1:3〜3:1。
  横長ヒーローは 1536x1024、正方形 1024x1024、縦 1024x1536 などが目安。

注意:
  - パラメータは OpenAI Images API に準拠。仕様変更時は body を調整する。
  - 画像内の日本語テキストは高精度だが、生成後に誤字・崩れを必ず目視すること。
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-2"


def generate(prompt: str, size: str, out: str, quality: str) -> None:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("OPENAI_API_KEY が未設定です。`export OPENAI_API_KEY=...` を実行してください。")

    payload = {"model": MODEL, "prompt": prompt, "size": size, "n": 1}
    if quality and quality != "auto":
        payload["quality"] = quality
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"API エラー {e.code}: {e.read().decode('utf-8', 'ignore')[:600]}")
    except urllib.error.URLError as e:
        sys.exit(f"接続エラー: {e}")

    item = (data.get("data") or [{}])[0]
    if item.get("b64_json"):
        img = base64.b64decode(item["b64_json"])
    elif item.get("url"):
        with urllib.request.urlopen(item["url"], timeout=300) as r:
            img = r.read()
    else:
        sys.exit(f"画像データを取得できませんでした: {json.dumps(data)[:400]}")

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "wb") as f:
        f.write(img)
    print(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate one website image with GPT Image 2.0")
    ap.add_argument("--prompt", required=True, help="画像生成プロンプト")
    ap.add_argument("--size", default="1536x1024", help="例 1536x1024 / 1024x1024 / 1024x1536")
    ap.add_argument("--out", required=True, help="保存先パス（例 assets/hero.png）")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high", "auto"])
    args = ap.parse_args()
    generate(args.prompt, args.size, args.out, args.quality)
