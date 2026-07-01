# CREDITS / クレジット

**claude-code-web-builder-ja** は、優れた先行オープンソースと公式ドキュメントの考え方を土台に、
「Claude Code で壁打ち → ループで自走 → サブエージェントQA → Webサイトを公開」する配布キットとして
日本語ファーストに再構成した派生版です。原典に深く感謝します。

本キットの収録物と原典の対応:

| 本キット | 由来・参考 | 作者 | ライセンス |
|---|---|---|---|
| `skills/site-grilling`（壁打ち） | [GrillMe / grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) | Matt Pocock | MIT |
| `.claude/commands/site-goal`（/site-goal ループ） | [goal-setter-skill](https://github.com/gotalab/goal-setter-skill) ／ [makeloop](https://github.com/usedhonda/makeloop) | gotalab ／ usedhonda | MIT |
| `reference/loops.md`（ループ入門） | [Getting Started with Loops](https://claude.com/blog/getting-started-with-loops)（Anthropic・2026-06-30） | Delba de Oliveira, Michael Segner | 記事（引用・参照） |
| `reference/components.md`（部品カタログ） | [Material 3 Components](https://m3.material.io/components)（部品の分類を参照） | Google | 記事（参照） |
| `skills/site-builder`（サイト生成） | 「画像で見た目・HTMLで機能」＋セマンティックHTMLの2段ワークフロー（手法を参考に独自再構成） | — | 独自実装 |

変更点の概要: 名称・説明・手順の全面リブランド、日本語ファースト化、**Webサイト制作向けへの特化**、
壁打ち→/site-goalループ→サイト生成→QA を 1 つの Claude Code ワークフローへ統合。中核の発想は原典の設計を尊重しています。
原典のアイコン等のブランド資産は含めていません。

---

## 1) GrillMe / grilling （`site-grilling` の土台）

- リポジトリ: https://github.com/mattpocock/skills
- 該当: `skills/productivity/grill-me` ／ `skills/productivity/grilling`
- 作者: Matt Pocock ／ ライセンス: MIT

「容赦ない一問一答で計画・設計を研ぐ（質問は一度に1つ・各問に推奨案を添える・決定木を1枝ずつ降りる）」
という壁打ちの作法を、Webサイト制作の仕様詰めに再構成して使わせていただきました。

```
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 2) goal-setter-skill ／ makeloop （`goal-loop` の土台）

- goal-setter-skill: https://github.com/gotalab/goal-setter-skill — 作者 gotalab — MIT
- makeloop: https://github.com/usedhonda/makeloop — 作者 usedhonda — MIT

「検証ターゲットとフィードバックループを固定する `/goal` 契約」と「検証ゲート・状態・停止条件を備えた
本物のループ」という、ループエンジニアリングの作法を土台にしています。

```
MIT License

Copyright (c) 2026 gotalab
Copyright (c) 2026 usedhonda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 3) 参照した公式ドキュメント（引用・出典）

- **Getting Started with Loops** — Anthropic（Claude）Blog・2026-06-30・Delba de Oliveira / Michael Segner
  https://claude.com/blog/getting-started-with-loops
- **Material 3 — Components** — Google（部品の分類・名称を参照）
  https://m3.material.io/components

これらは記事・仕様であり、本文をコピーせず、考え方・分類を参照して日本語で再構成しています。

---

## 4) 「画像で見た目・HTMLで機能」ワークフロー （`site-builder` の参考）

特定の単一OSS由来ではなく、「画像で見た目を作り、HTMLでCTA・リンク・フォームを機能化する」
2段ワークフローの考え方を参考に、本キット向けに独自実装しています。

---

## 本キット独自部分

- 再構成・日本語化・Webサイト特化・統合・ブランディング: 河村風真 (fuuuuuuma)
- ライセンス: MIT（[LICENSE](LICENSE)）
- 自由に使って、改変して、配ってかまいません。原典の著作権表示（本ファイル）だけ一緒に残してください。
