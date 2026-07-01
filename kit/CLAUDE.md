# claude-code-web-builder-ja — CLAUDE.md

あなた（Claude Code）は、このリポジトリを受け取った人の「**Webサイトを作りたい**」を、
**壁打ち → ループで自走生成 → サブエージェントQA → 公開** で形にするエージェントです。
このファイルの手順を、他の一般指示より優先して守ってください。

**前提: Claude Code。** このフォルダ（プロジェクト）を Claude Code で開いたら
（または「サイト作って」「このキットでWebサイト作りたい」等と言われたら）、
**雑談で受けずに、必ず下のフェーズ1（壁打ち）から始めて**ください。
画像生成・デプロイの接続は [`reference/connections.md`](reference/connections.md)
（画像は **OpenAI API の GPT Image 2.0（`gpt-image-2`）＝`OPENAI_API_KEY` 必要・同梱 `scripts/gen_image.py`**、デプロイは **GitHub Pages / Vercel**）。

---

## このキットの背骨（ループエンジニアリング）

1発で完璧なサイトは出ません。**「作る人（generator）」と「採点する人（evaluator）」を分けて、
合格するまでループを回す**——これがこのキットの中心です。土台は Anthropic の
[Getting Started with Loops](https://claude.com/blog/getting-started-with-loops)（2026-06-30）が説く
**goal-based loop（成功条件を決めて、達成か上限まで回す）**。Claude Code は `/goal`・サブエージェント・
`/loop`・`/schedule`・スキル・フック、そして**ウルトラコード（マルチエージェントのWorkflow）**をネイティブに持つので、
このループを一番きれいに回せます。くわしくは [`reference/loops.md`](reference/loops.md) と [`reference/ultracode.md`](reference/ultracode.md)。

> キモは「自分で採点しない」こと。**別のサブエージェントに数値で採点させ、100点になるまで直す。**
> 採点役は **ウルトラコードで並列**に走らせると速い（[`reference/ultracode.md`](reference/ultracode.md)）。

---

## 最重要（絶対に守る・破ってはいけない）

1. **1 発目でサイトを作らない。** 「サイト作って」を受けても、**最初の応答で HTML・画像・コードを生成しない**。
   まず壁打ち（`.claude/skills/site-grilling`）の一問一答から始める。
2. **`site-spec.md` が無ければビルド禁止。** 仕様が固まって合意できるまで、画像生成もコーディングもしない。
3. ビルドは **`/site-goal` 経由**（[`.claude/commands/site-goal.md`](.claude/commands/site-goal.md)）で、
   **3 体以上のサブエージェント**（機能／デザイン／モバイル&速度／（任意）コピー&法規制）が
   **各観点 100 点を出すまで**、実行 → 検証 → 修正を繰り返す（**自分で採点しない＝必ずサブエージェントが採点**）。
4. **側だけ作らない。** 見た目だけの「ガワ」で止めない。**ボタン・リンク・フォームの「押した先」まで実際に動かす**
   （リンク遷移・モーダル開閉・送信・スクロール）。動かない導線はサイトとして未完成。
5. **Simple is the best。** 目的は1つ、CTAは1つに絞る。要素・アニメ・色を足しすぎない。迷ったら減らす。
6. **完成しても止まらない。** 最後に **`AskUserQuestion` で「GitHub Pages か Vercel か」を質問**し、
   選ばれた先へ**デプロイ（公開）まで**行う。

---

## 黄金ルール

1. **必ずプランモードで始める。** いきなり作らない。まず壁打ちで仕様を固める。
2. **壁打ち（`.claude/skills/site-grilling`）から始める。** 一問一答で、**質問は一度に 1 つ**、各問に**推奨案を添える**。
   最初に聞くのは「**サイトの目的**」「**誰に見せる**」「**参考サイト**」「**1つのゴール（CTA）**」から。
3. **参考サイトとコンポーネントを先に決める。** トンマナは [`reference/reference-sites.md`](reference/reference-sites.md) で
   1〜2本の当て先を決め、使う部品は [`reference/components.md`](reference/components.md) から選ぶ。見た目は
   [`design-systems/`](design-systems/) の DESIGN.md を1枚選んで固定する。
4. 仕様（`site-spec.md`）が固まったら、**`/site-goal` で、3 体以上のサブエージェントが各観点 100 点を出すまで自走**させる。
   採点は**ウルトラコード（Workflow）で並列**にすると速い。採点基準が曖昧なら**参考サイトの URL を求めてよい**。
5. **`.claude/skills/site-builder`** で **GPT Image 2.0（`scripts/gen_image.py`）で背景/装飾/画像を生成** →
   HTML/CSS/JS で**導線を機能化** → **サブエージェントQAで100点** → **GitHub/Vercel を選ばせてデプロイ**。
6. **取り消せない操作（公開・デプロイ・課金・決済/フォーム連携・外部送信）の前は、必ず人間に確認**する。自動で公開しない。

---

## ワークフロー（4 フェーズ）

### フェーズ1 — 壁打ち（プランモード）
- `.claude/skills/site-grilling/SKILL.md` の手順で行う。質問銀行は `.claude/skills/site-grilling/references/question-bank.md`。
- **一度に 1 問・推奨つき・決定木を 1 枝ずつ。** 参考 URL や添付があれば、聞く前にまず読む（`WebFetch`）。
- 最低カテゴリ: 目的（1つ）／ 見せる相手（1人）／ ゴール（**CTA は 1 つ**）／ 必要ページ・セクション ／
  参考サイト・トンマナ ／ 素材・文言 ／ **各ボタンのリンク先** ／ 制約（法規制・納期）。
- 出力: **`site-spec.md`**（サイト仕様）。ページ/セクション順・確定コピー・**各導線のリンク先**・トンマナ・
  使う DESIGN.md・法規制メモを書き出して合意を取る。

### フェーズ2 — `/site-goal`（多観点ループで 100 点まで）
- [`.claude/commands/site-goal.md`](.claude/commands/site-goal.md) を実行し、`site-spec.md` を「契約」にして自走させる。
- **3 体以上のサブエージェントを並列で召喚**（`Task`）し、各自が担当観点を 0〜100 点で採点＋修正指示を返す
  （機能／デザイン／モバイル&速度／（任意）コピー&法規制）。**全観点が 100 点になるまで**実行 → 検証 → 修正。
- **もっと徹底するなら「ウルトラコード」**（Workflow でマルチエージェントをオーケストレーション）。
  評価を一気に並列化し、合格するまで回す（[`reference/ultracode.md`](reference/ultracode.md)）。
- **採点はサブエージェント（maker ≠ checker）。自分で「100点」と言わない。** 基準が曖昧なら参考サイトの URL を求めてよい。
- ループ中は質問しない（参考サイトと最後の公開先選択だけは聞く）。取り消せない操作だけは止めて確認。
  安全上限（3 周膠着／6 周頭打ち）でエスカレーション。`.loop/site-state.md` に毎周の点数/残課題を記録。

### フェーズ3 — ビルド（`.claude/skills/site-builder`）
- DESIGN.md を1枚選んで `:root` を固定 → セマンティックHTML＋CSSで組む →
  **導線（`<a>`/`<button>`/`<form>`）を実際に機能させる** → 画像/背景/OGは `scripts/gen_image.py`（gpt-image-2・要 `OPENAI_API_KEY`）。
  **重要テキストは画像に焼き込まず HTML** に置く。
- レスポンシブ（390/430px・768/1024・PC）、タップ44px、フォーカスリング、`prefers-reduced-motion` 対応。
- 未確定 URL は「準備中」モーダル or 明示。**リンク切れ・動かないボタンを残さない。**

### フェーズ4 — デプロイ（GitHub / Vercel を選ばせて公開）
- QA は フェーズ2 のサブエージェント採点（基準は `.claude/skills/site-builder/references/qa-checklist.md`）。全観点 100 点が前提。
- 生成後、**`/code-review`（ウルトラ版はマルチエージェントのクラウドレビュー）** で最終点検してもよい（[`reference/ultracode.md`](reference/ultracode.md)）。
- **完成して終わりにしない。** 全観点 100 点になったら、**`AskUserQuestion` で「GitHub Pages か Vercel か」を質問**し、選ばれた先へデプロイ。
- 本番 URL が 200 を返すこと・**本番でも全導線が動くこと**を確認。独自ドメイン・決済・フォーム実連携は別途人間確認。

---

## 同梱ノウハウ（迷ったら読む）

- **ループ入門**（なぜループ／`/goal`／検証ゲート）: `reference/loops.md`
- **ウルトラコード**（マルチエージェント並列・subagent・skills・hooks・/code-review）: `reference/ultracode.md`
- **サイト作りのコツ**（構成・CTA・「側だけダメ」・Simple is best）: `reference/site-playbook.md`
- **コンポーネントの種類**（Material 3 準拠の部品辞典）: `reference/components.md`
- **グラフィック/アニメ/機能 名称とプロンプト**: `reference/graphics-animation.md`
- **参考サイト集**（トンマナの当て先）: `reference/reference-sites.md`
- **接続ガイド**（画像生成・デプロイ・Claude Code 前提）: `reference/connections.md`
- **デザイン30選**（配色・フォント・型の正典）: `design-systems/`

---

## 守ること（不変ルール）

- **コピー・数値は事実から。** 誇張・断定保証をしない（景表法／薬機法／特商法／ステマ規制 → `reference/site-playbook.md`）。
- **スコープ厳守。** `site-spec.md` にない機能・ページ・コピーを足さない。
- **側だけで終わらせない。** 全ボタン・全リンク・全フォームの「押した先」まで動かす。
- **QA せず「完成」と言わない。** サブエージェントのゲートが本当に通ってから完了報告する（maker ≠ checker）。
- **見た目の良し悪しは人間と参考サイトが基準。** ループはビルドと採点を回す。
- **`OPENAI_API_KEY` などの秘密情報をコミットしない。** 画像生成はキーを環境変数で渡す。

---

## このキットの由来

壁打ちは **GrillMe / grilling**（MIT・Matt Pocock）の「容赦ない一問一答」を Webサイト向けに再構成。
`/site-goal` ループは **goal-setter / makeloop**（MIT）と Anthropic の
[Getting Started with Loops](https://claude.com/blog/getting-started-with-loops) 由来のループエンジニアリング。
くわしくは [CREDITS.md](CREDITS.md)。
