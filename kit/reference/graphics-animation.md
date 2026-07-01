# グラフィック・アニメーション・機能 — 名称とプロンプト

「こういう見た目/動きにしたい」を**正式名称で知っておくと、AI に一言で頼める**。
下の「頼み方（プロンプト）」はそのままコピペして使える短い指示。**盛りすぎない**（Simple is the best）。
アニメは `prefers-reduced-motion` で止める前提で。

---

## A. グラフィック / 背景（静的な見た目）

| 名称（EN / JP） | どんな見た目 | 頼み方（プロンプト） |
|---|---|---|
| Gradient mesh（メッシュグラデ） | 複数色がにじむ背景 | 「ヒーロー背景をやわらかいメッシュグラデ（brand→accent）にして」 |
| Aurora / blob（オーロラ・ブロブ） | 有機的な光のにじみ | 「背景にゆっくり動くブロブ（accent系・低彩度）を1つ」 |
| Glassmorphism（すりガラス） | 半透明＋ぼかしのカード | 「カードをすりガラス（背景ぼかし＋薄い枠）にして」 |
| Noise / grain（ノイズ） | 質感を足す粒子 | 「背景に薄いグレインを重ねてのっぺり感を消して」 |
| Dot / line grid（ドット格子） | 規則的な点/線 | 「セクション背景に薄いドット格子（line色）を敷いて」 |
| Gradient border（グラデ枠） | 縁が光るカード | 「強調カードだけグラデ枠（brand→accent）に」 |
| Bento grid（ベント―） | 大小タイルの一覧 | 「特徴をベントーグリッド（大1＋小4）で並べて」 |

## B. アニメーション（動き）

| 名称（EN / JP） | どんな動き | 頼み方（プロンプト） | よく使う道具 |
|---|---|---|---|
| Scroll reveal（スクロール出現） | 下からふわっと表示 | 「各セクションをスクロールで下からフェードイン（stagger）」 | IntersectionObserver / AOS / GSAP |
| Parallax（パララックス） | 背景と前景で速度差 | 「ヒーロー背景を軽いパララックスに（やりすぎない）」 | GSAP / Lenis |
| Sticky scroll（固定追従） | 文字が固定で図が進む | 「使い方セクションを sticky scroll に」 | GSAP ScrollTrigger |
| Marquee（流れる帯） | ロゴ等が横に流れる | 「ロゴ群を無限マーキーで横スクロール」 | CSS / Swiper |
| Count-up（数字カウント） | 0→数値へ増える | 「実績数字を画面内でカウントアップ」 | JS |
| Typewriter（タイプ） | 文字が打たれる | 「ヒーロー見出しをタイプライター風に」 | JS |
| Hover tilt（ホバー傾き） | カードが傾く | 「カードにホバーで軽い3D傾き」 | vanilla-tilt |
| Magnetic button（吸着） | ボタンがカーソルに寄る | 「一次CTAをマグネティックに（弱め）」 | JS |
| Image reveal（画像リビール） | マスクで現れる | 「画像をマスクでリビール表示」 | GSAP / Framer Motion |
| Page / view transition | ページ切替の演出 | 「ページ遷移に View Transitions を」 | View Transitions API |
| Kinetic typography | 文字が動く演出 | 「見出しをキネティックタイポで強調」 | GSAP |
| Lottie（軽量アニメ） | ベクターアニメ再生 | 「ヒーローに軽いLottieアニメを1つ」 | Lottie |

> ライブラリ早見: **GSAP / ScrollTrigger**（本格アニメ）、**Framer Motion**（React）、**Lenis**（なめらかスクロール）、
> **AOS**（お手軽出現）、**Swiper**（カルーセル/マーキー）、**Three.js / Spline**（3D）、**Lottie**（ベクターアニメ）、**tsParticles**（粒子）。

## C. 機能（触れる仕掛け）

| 名称 | 何をする | 頼み方（プロンプト） |
|---|---|---|
| Dark mode toggle | 明暗切替 | 「ダークモード切替を付けて（設定を保存）」 |
| Sticky header | 追従ヘッダー | 「スクロールで縮む固定ヘッダーに」 |
| Smooth scroll / anchor | 滑らか移動 | 「ナビのリンクを該当セクションへスムーススクロール」 |
| Hamburger menu | スマホメニュー | 「スマホはハンバーガーメニューに」 |
| Accordion / Tabs | 開閉・切替 | 「FAQをアコーディオン、機能をタブで」 |
| Modal / Lightbox | 重ねて表示 | 「画像はライトボックス、未定リンクは準備中モーダル」 |
| Carousel / Slider | 横送り | 「お客様の声をカルーセルに（矢印＋ドット）」 |
| Filter / Search | 絞り込み | 「事例を種類で絞り込めるフィルタを」 |
| Form validation | 入力チェック | 「フォームに必須・形式チェックとエラー表示」 |
| Toast / Snackbar | 一時通知 | 「送信成功をトーストで知らせる」 |
| Back-to-top | 上へ戻る | 「右下に『上へ戻る』ボタン（出現は下スクロール時）」 |
| Skeleton loader | 読込表示 | 「重い画像はスケルトンで読込表示」 |
| Cookie banner | 同意バー | 「必要なら Cookie 同意バーを（計測時）」 |

---

## 使うときの原則
- **足しすぎない。** 動き・装飾は「目的（CTA）に効くもの」だけ。迷ったら減らす。
- **重くしない。** 3Dや大量パーティクルは速度と相談（Lighthouse≥90を死守）。
- **止められるように。** すべてのアニメは `prefers-reduced-motion: reduce` で無効化。
- **側だけにしない。** 見た目の演出より先に、リンク/ボタン/フォームの「押した先」を動かす。
