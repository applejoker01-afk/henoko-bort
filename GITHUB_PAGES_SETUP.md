# GitHub Pagesの設定ガイド

このリポジトリをGitHub Pagesでウェブサイトとして公開する手順です。

## 手順

### 1. GitHubリポジトリにプッシュ

まず、すべてのファイルをGitHubリポジトリにプッシュしてください：

```bash
git init
git add .
git commit -m "Initial commit: 辺野古事故と京都事件の報道比較レポート"
git remote add origin https://github.com/[あなたのユーザー名]/henoko-media-bias-report.git
git branch -M main
git push -u origin main
```

### 2. GitHub Pagesを有効化

1. GitHubリポジトリのページにアクセス
2. 「Settings」タブをクリック
3. 左サイドバーの「Pages」をクリック
4. 「Source」セクションで以下を選択：
   - Branch: `main`
   - Folder: `/ (root)`
5. 「Save」をクリック

### 3. 公開URLの確認

数分後、以下のURLでサイトが公開されます：

```
https://[あなたのユーザー名].github.io/henoko-media-bias-report/
```

### 4. カスタムドメインの設定（オプション）

独自ドメインを使用したい場合：

1. GitHub Pages設定ページの「Custom domain」に独自ドメインを入力
2. DNSプロバイダーでCNAMEレコードを設定
3. 「Enforce HTTPS」にチェック

## ファイル構成の確認

GitHub Pagesでは、以下の優先順位でトップページが決定されます：

1. `index.html`（最優先）← **このファイルが存在するので、これがトップページになります**
2. `index.md`
3. `README.md`

## トラブルシューティング

### サイトが表示されない場合

1. GitHub Pagesの設定が正しいか確認
2. リポジトリが公開（Public）になっているか確認
3. GitHub Actionsのビルドログを確認（Settings > Pages > Build and deployment）

### CSSが読み込まれない場合

- `index.html`内のCSSは`<style>`タグ内に直接記述されているため、外部CSSファイルは不要です
- フォントはGoogle Fontsから読み込まれています（インターネット接続が必要）

## メタデータの更新

`index.html`の以下の部分を必要に応じて更新してください：

```html
<title>思想・政治信条が報道を歪める現状 - 辺野古事故と京都事件の比較調査</title>
<meta name="description" content="...">
<meta name="keywords" content="...">
```

## SNSシェア対応（オプション）

OGP（Open Graph Protocol）タグを追加すると、SNSでのシェア時に見栄えが良くなります。

`index.html`の`<head>`内に以下を追加：

```html
<!-- OGP -->
<meta property="og:title" content="思想・政治信条が報道を歪める現状">
<meta property="og:description" content="辺野古事故と京都事件の報道比較調査">
<meta property="og:type" content="website">
<meta property="og:url" content="https://[あなたのユーザー名].github.io/henoko-media-bias-report/">
<meta property="og:image" content="https://[あなたのユーザー名].github.io/henoko-media-bias-report/og-image.png">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="思想・政治信条が報道を歪める現状">
<meta name="twitter:description" content="辺野古事故と京都事件の報道比較調査">
<meta name="twitter:image" content="https://[あなたのユーザー名].github.io/henoko-media-bias-report/og-image.png">
```

## アクセス解析（オプション）

Google Analyticsなどを設定する場合は、`index.html`の`</head>`の直前に追加してください。

---

**公開後は、noteの記事内でGitHub PagesのURLを共有してください！**
