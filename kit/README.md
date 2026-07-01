# claude-code-web-builder-ja — ループで完璧なWebサイトを作る Claude Codeキット

> **これは何**：Claude Code に渡すと、**いきなり作らず「壁打ち」から始まり**、`/site-goal` ループと
> **サブエージェント採点**（必要なら**ウルトラコード＝マルチエージェント並列**）で「各観点100点」になるまで作り込み、
> **ボタンの押した先まで動く**Webサイトを、**公開まで**面倒みる配布キット（プレゼント）です。
> ランタイムは **Claude Code**（画像は OpenAI API の `gpt-image-2`＝`scripts/gen_image.py`・要 `OPENAI_API_KEY`）。

このキットは、YouTube「ClaudeCodeチャンネル」の解説回
**「ループで完璧なWebサイトを1発生成」** の配布物です。

---

## 3行でわかる

- **1発で完璧は狙わない。** 「合格の定義」と「採点役（サブエージェント）」を用意して**ループ**で仕上げる。
- **側だけ作らない。** 全ボタン・全リンク・全フォームの「押した先」まで動かす。
- **Simple is the best。** 目的1つ・CTA1つに絞る。要素を足しすぎない。

---

## 使い方（3ステップ）

1. **開く**：このフォルダを **Claude Code で開く**（ルートで `claude`／IDE拡張）。Claude Code が `CLAUDE.md` を自動で読む。
2. **話しかける**：「**サイト作って**」。いきなり作らず、**壁打ち（一問一答）** が始まり `site-spec.md` が固まる。
3. **回す**：**`/site-goal`** を実行。3体以上のサブエージェントが各観点100点まで採点＋修正し（**ウルトラコードで並列も可**）、
   最後に **GitHub Pages / Vercel** を聞いて**公開**する。

> 接続（画像生成・デプロイ）は [`reference/connections.md`](reference/connections.md)。マルチエージェントは [`reference/ultracode.md`](reference/ultracode.md)。

---

## 4フェーズ

```
① 壁打ち(site-grilling) → ② /site-goalループ → ③ サイト生成(site-builder) → ④ デプロイ(人間確認後)
   仕様を固める            各観点100点まで自走       機能する導線まで作る         GitHub/Vercel
```

---

## Claude Code だからできること（ウルトラコード）

- **`/goal`（本キットは `/site-goal`）**：合格条件を決めて自走。**サブエージェント（`Task`）** で maker ≠ checker の採点。
- **ウルトラコード（Workflow）**：採点役を**マルチエージェントで並列**に走らせて徹底検証（山場だけ・トークン多め）。
- **スキル / フック / `/code-review`（ウルトラ版はクラウドのマルチエージェントレビュー）/ `/loop`・`/schedule`**。
- くわしくは [`reference/ultracode.md`](reference/ultracode.md)。

---

## 収録物

| パス | 中身 |
|---|---|
| `CLAUDE.md` | Claude Code が自動で読む背骨（黄金ルール・4フェーズ） |
| `.claude/skills/site-grilling/` | 壁打ち（GrillMe 方式・一問一答）＋ `references/question-bank.md` |
| `.claude/skills/site-builder/` | サイト生成（機能する導線まで）＋ `references/qa-checklist.md`・`shareable-prompts.md` |
| `.claude/commands/site-goal.md` | **`/site-goal`**（closed ループ・各観点100点まで自走） |
| `scripts/gen_image.py` | 画像生成（OpenAI API・`gpt-image-2`・要 `OPENAI_API_KEY`） |
| `design-systems/` | **DESIGN.md 30選**（配色・フォント・型の正典。1枚選んで `:root` 固定） |
| `reference/loops.md` | ループ入門（なぜループ／`/goal`／検証ゲート） |
| `reference/ultracode.md` | **ウルトラコード**（並列マルチエージェント・subagent・skills・hooks・/code-review） |
| `reference/site-playbook.md` | サイト作りのコツ（構成・CTA・「側だけダメ」・Simple is best） |
| `reference/components.md` | コンポーネントの種類（Material 3 準拠の部品辞書） |
| `reference/graphics-animation.md` | グラフィック/アニメ/機能の**名称とプロンプト** |
| `reference/reference-sites.md` | 参考Webサイト集（トンマナの当て先） |
| `reference/connections.md` | 接続（OpenAI API 画像生成・GitHub/Vercel） |
| `CREDITS.md` / `LICENSE` | 謝辞（GrillMe・goal-setter・makeloop・Loops記事）／ MIT |

---

## 由来・ライセンス

壁打ちは **GrillMe / grilling**（MIT・Matt Pocock）、ループは **goal-setter / makeloop**（MIT）と
Anthropic の [Getting Started with Loops](https://claude.com/blog/getting-started-with-loops) 由来。
くわしくは [CREDITS.md](CREDITS.md)。本キットは **MIT**（[LICENSE](LICENSE)）—— 自由に使い・改変し・配ってOK。原典表示だけ残してください。
