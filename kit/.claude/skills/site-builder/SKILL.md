---
name: site-builder
description: 固まったサイト仕様(site-spec.md)から、DESIGN.mdで見た目を固定し、セマンティックHTML/CSS/JSで組み、ボタン・リンク・フォームの「押した先」まで機能化して、GPT Image 2.0で画像/背景を補い、サブエージェントQAで各観点100点までループしてデプロイまで行う。「側だけ」で止めない。
---

# site-builder — Webサイトビルダー（DESIGN.md → 機能するHTML → QA → デプロイ）

> 「**見た目は DESIGN.md と画像で、機能は HTML/CSS/JS で**」。見た目だけの“ガワ”で終わらせず、
> **導線（押した先）まで動かす**のが本キットの肝。謝辞は [CREDITS.md](../../../CREDITS.md)。

## 前提

`site-grilling` の壁打ちで `site-spec.md`（サイト仕様）が固まっていること。固まっていなければ先に `site-grilling` に戻る。
コピー・構成・CTA・**各導線のリンク先**は `site-spec.md` が正。ここで創作しない。

## 流れ（4 フェーズ）

```
Phase 1 見た目を固定(DESIGN.md) → Phase 2 機能するHTMLを組む → Phase 3 サブエージェントQA(100点) → Phase 4 デプロイ(人間確認後)
```

### Phase 1 — 見た目を固定する（DESIGN.md ＋ 画像）
- `design-systems/` から DESIGN.md を **1 枚選び**、その `:root{}`（色トークン）と見出しフォントを固定する。
  途中で色を足さない（トークン外の色使用は QA で減点）。
- 参考サイト（`reference/reference-sites.md` で決めた URL）を**トンマナの当て先**にする。レイアウトのコピーではない。
- 使うコンポーネントは `reference/components.md` から選ぶ。やりたい動き/装飾は `reference/graphics-animation.md` の
  「名称＋プロンプト」で指示する。
- 画像・背景・OG画像・アイコンは **GPT Image 2.0（OpenAI API・同梱 `scripts/gen_image.py`・要 `OPENAI_API_KEY`）** で生成（接続は `reference/connections.md`）。
  **重要テキスト（見出し・価格・日付・CTA）は画像に焼き込まず HTML テキストに置く**（編集・SEO・崩れ対策）。

### Phase 2 — 機能する HTML を組む（「側だけ」で止めない）
- **セマンティック HTML**（`header/nav/main/section/footer`、見出し階層、`alt`、ラベル）で `index.html`（＋必要ページ）を作る。
- **導線を全部つなぐ** — ここが最重要:
  - `<a href>` は**実在する遷移先**（別ページ／外部URL／`#anchor`）へ。ダミー `#` を残さない。
  - `<button>` は**押したら実際に動く**（モーダル開閉・タブ切替・送信・スクロール）。
  - `<form>` は**送信先を配線**（メール `mailto:`／外部フォーム／スプレッドシート等）。未定は「準備中モーダル」（閉じる/背景/Esc）。
  - スムーススクロール、ハンバーガーメニュー、アコーディオンなど**触って反応する**まで作る。
- レスポンシブ: 390/430（スマホ）→ 768/1024（タブレット）→ PC。横スクロールを出さない。タップ領域 44px 以上。
- アクセシビリティ: フォーカスリング、キーボード操作、`prefers-reduced-motion` でアニメ抑制、コントラスト AA。
- 計測が要るなら GA4／GTM を配線（UTM）。

### Phase 3 — QA（3 体以上のサブエージェントで各観点 100 点まで）
**自己採点しない。** `/site-goal`（`.claude/commands/site-goal.md`）のループで、**3 体以上のサブエージェント**
（機能／デザイン／モバイル&速度／（任意）コピー&法規制）が各観点を 0〜100 点で採点し、
**全観点が 100 点になるまで**実行 → 検証 → 修正を繰り返す。基準は [`references/qa-checklist.md`](references/qa-checklist.md)。
- 機能チェッカーは**実機で全リンク/ボタン/モーダル/フォームを押し**、遷移先の存在・送信成立・戻れることまで確認する。
- デザイン採点が曖昧なら**参考サイトの URL を求めてよい**（当て先＝基準）。
- 定量チェック（リンク切れ0・コンソールエラー0・Lighthouse≥90・390pxで横スクロール0）を優先する。

### Phase 4 — デプロイ（GitHub / Vercel を選ばせて公開）
全観点 100 点になったら、**「GitHub Pages か Vercel か」をユーザーに質問**し、選ばれた先へデプロイする。
**完成して終わりにしない。** 接続は [`reference/connections.md`](../../../reference/connections.md)。

- **GitHub Pages**: リポジトリに push → Pages を有効化（`gh`／git）。完全無料・静的向き。
- **Vercel**: Vercel プラグイン／MCP を接続 → 「create a deployment」でプレビュー公開（または `vercel` CLI）。
- 公開後に**本番 URL が HTTP 200**・**本番でも全導線が動くこと**・計測タグの発火を確認。
  独自ドメイン・決済/フォーム実連携・本番公開は、人間の承認後に実行（自動で公開しない）。

## 出力モードの選び方
- **既定: HTML中心＋画像は補助**（テキスト・導線は HTML、背景/装飾/写真は GPT Image 2.0）。編集・SEO・レスポンシブに強い。
- **ビジュアル重視**: アート性が要る箇所だけ GPT Image 2.0 の作り込み画像を使う（重要テキストは必ず HTML に併記）。

## 配布用プロンプト
他の人にそのまま渡せる汎用プロンプト（壁打ち → /goal ループ → サイト生成 → デプロイ）は
[`references/shareable-prompts.md`](references/shareable-prompts.md)。

## やってはいけない
- 仕様が固まる前に作り始める／壁打ちを飛ばす
- **`href="#"` やダミーボタンを残す**（＝側だけ）。全導線の押した先まで動かす
- DESIGN.md のトークン外の色を足す／途中で配色を変える
- GPT Image 2.0 に重要テキストを焼き込む（後から変わる要素・長文は HTML へ）
- **自己採点で「完成」と言う**（採点はサブエージェント。全観点 100 点まで回す）
- 公開先の選択を飛ばして「完成」で止まる（必ず GitHub/Vercel を選ばせて公開まで）
- 目的に効かない要素を足す（Simple is the best）／誇張・断定保証コピー（景表法・薬機法）
