# 接続ガイド — connections（Claude Code 前提）

このキットは **Claude Code** で使う前提。サイトを作り始める前に、(1) 渡し方、(2) 画像生成、(3) デプロイ の
接続を確認しておく。**画像生成は OpenAI API（gpt-image-2）を使うので `OPENAI_API_KEY` が必要**。出典は末尾。

---

## 0. キットの渡し方（Claude Code）
- このフォルダ（リポジトリ）を **Claude Code で開く**（ルートで `claude` を起動、または IDE 拡張で開く）。
- Claude Code は**作業前にプロジェクト直下の `CLAUDE.md` を自動で読む**。
- 「サイト作って」と話しかけると、`CLAUDE.md` に従って**プランモードで壁打ち**から始まる。
- 壁打ち・ビルドのスキルは `.claude/skills/`、ループは `/site-goal`（`.claude/commands/site-goal.md`）。
  マルチエージェント（ウルトラコード）は `reference/ultracode.md`。

---

## 1. 画像生成（GPT Image 2.0 = gpt-image-2）
Claude Code は画像生成を内蔵しないので、**OpenAI Images API** を呼んで GPT Image 2.0 で生成する。同梱の `scripts/gen_image.py` を使う。

| 方法 | 接続 | 向いている場面 |
|---|---|---|
| **A. OpenAI API（推奨・既定）** | `export OPENAI_API_KEY=sk-...` → `python3 scripts/gen_image.py --prompt "..." --size 1536x1024 --out assets/hero.png`。モデルは `gpt-image-2` | 既定。背景・装飾・OG画像 |
| **B. Runway MCP コネクタ** | `claude mcp add runway https://mcp.runwayml.com/mcp`。GPT Images 2.0 / Gen-4.5 / Seedance / Kling など | 別モデル・動画も |
| **C. HiggsField MCP コネクタ** | `claude mcp add` で HiggsField の MCP を接続し `generate_image` | コネクタ運用の代替 |

- 用途は**ヒーロー背景・装飾・写真・OG画像・アイコン**。**重要テキスト（見出し・価格・日付・CTA）は焼き込まず HTML** に置く。
- サイズは横長 `1536x1024`・正方形 `1024x1024`・縦 `1024x1536` 等（16 の倍数・アスペクト 1:3〜3:1）。出力は `assets/` に保存。
- MCP コネクタは `claude mcp add <name> <url|cmd>`、またはプロジェクトの `.mcp.json` で追加。

---

## 2. デプロイ（GitHub Pages か Vercel）
静的サイトは **GitHub Pages** か **Vercel**。Claude Code は Bash を実行できるので、CLI かコネクタで公開まで進められる。

| 先 | 接続（推奨） | 向いている場面 |
|---|---|---|
| **GitHub Pages（無料・シンプル）** | `gh` ／ git で push → Pages を有効化 | 完全無料・静的で十分なとき |
| **Vercel** | `vercel` CLI（`npm i -g vercel` → `vercel deploy`）、または `claude mcp add vercel https://mcp.vercel.com` を接続して「create a deployment」 | プレビューURL・独自ドメイン・表示が速い |

**公開（デプロイ）＝取り消せない外部公開**なので、実行は **必ず人間が確認してから**（自動で公開しない）。
公開後は本番 URL が HTTP 200 を返すこと・**本番でも全導線が動くこと**・計測タグの発火を確認する。

---

## まとめ（最短ルート）
1. **渡す**: Claude Code でこのフォルダを開く →「サイト作って」。
2. **壁打ち→ループ**: 仕様を固め、`/site-goal` で各観点100点まで自走（採点はウルトラコードで並列も可）。
3. **画像**: `OPENAI_API_KEY` を設定 → `scripts/gen_image.py`（gpt-image-2）。**デプロイ**: GitHub Pages か `vercel` → 人間確認して公開。

---

## 出典
- GPT Image 2 Model（gpt-image-2・サイズ・任意解像度）｜OpenAI API — https://developers.openai.com/api/docs/models/gpt-image-2
- Image generation｜OpenAI API — https://developers.openai.com/api/docs/guides/image-generation
- Connect to local & remote MCP servers（`claude mcp add`）｜Claude Docs — https://docs.claude.com/en/docs/claude-code/mcp
- Use Vercel's MCP server / `vercel` CLI deploy｜Vercel — https://vercel.com/docs/agent-resources/vercel-mcp
- GitHub Pages ドキュメント — https://docs.github.com/pages
