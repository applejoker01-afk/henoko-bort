# GitHub Desktopを使った公開手順

このガイドでは、GitHub Desktopを使ってレポートをGitHubに公開し、GitHub Pagesで一般公開する手順を説明します。

## 📋 事前準備

### 必要なもの
- ✅ GitHub Desktopがインストール済み（[ダウンロード](https://desktop.github.com/)）
- ✅ GitHubアカウント
- ✅ すべてのファイルが1つのフォルダにまとまっている

### ファイル構成の確認

ダウンロードしたファイルを以下のような構成で1つのフォルダにまとめてください：

```
henoko-media-bias-report/          ← このフォルダ名は自由に変更可
├── index.html
├── README.md
├── henoko-media-bias-report.md
├── note-article.md
├── LICENSE.md
├── .gitignore
├── data/
│   └── timeline.md
└── resources/
    └── references.md
```

---

## ステップ1: GitHub Desktopでローカルリポジトリを作成

### 1-1. GitHub Desktopを起動

GitHub Desktopアプリケーションを開きます。

### 1-2. 新しいリポジトリを作成

1. メニューバーから **「File」 > 「Add Local Repository」** をクリック
   - または **「File」 > 「New Repository」** でも可能

2. 「Create a New Repository」ウィンドウで以下を入力：
   - **Name**: `henoko-media-bias-report`（任意の名前）
   - **Description**: `思想・政治信条が報道を歪める現状に関する調査報告書`
   - **Local Path**: すでにファイルがあるフォルダを選択
   - **Initialize this repository with a README**: チェックを**外す**（すでにREADME.mdがあるため）
   - **Git Ignore**: `None`
   - **License**: `None`（すでにLICENSE.mdがあるため）

3. **「Create Repository」** をクリック

### 1-3. ファイルの確認

左側の「Changes」タブに、すべてのファイルが表示されていることを確認します。

---

## ステップ2: 初回コミット

### 2-1. コミットメッセージを入力

画面下部の入力欄に：

- **Summary（必須）**: `Initial commit: 辺野古事故と京都事件の報道比較レポート`
- **Description（任意）**: 
  ```
  - 完全版レポート作成
  - 京都事件との比較分析
  - GitHub Pages対応のindex.html作成
  ```

### 2-2. コミット実行

**「Commit to main」** ボタンをクリック

---

## ステップ3: GitHubにリポジトリを公開

### 3-1. Publishボタンをクリック

画面上部の **「Publish repository」** ボタンをクリック

### 3-2. 公開設定

「Publish Repository」ウィンドウで：

- **Name**: `henoko-media-bias-report`（変更可）
- **Description**: `思想・政治信条が報道を歪める現状に関する調査報告書`
- **Keep this code private**: チェックを**外す**（公開する）
- **Organization**: なし（個人アカウントで公開）

### 3-3. Publishを実行

**「Publish Repository」** ボタンをクリック

数秒〜数十秒で、GitHubへのアップロードが完了します。

---

## ステップ4: GitHub Pagesを有効化

### 4-1. GitHubのリポジトリページを開く

GitHub Desktopの画面上部にある **「View on GitHub」** ボタンをクリック

ブラウザでGitHubリポジトリページが開きます。

### 4-2. Settings（設定）を開く

リポジトリページの上部タブから **「Settings」** をクリック

### 4-3. Pagesの設定

1. 左サイドバーの **「Pages」** をクリック

2. 「Build and deployment」セクションで：
   - **Source**: `Deploy from a branch` を選択
   - **Branch**: `main` を選択
   - **Folder**: `/ (root)` を選択

3. **「Save」** ボタンをクリック

### 4-4. 公開URLの確認

数分後、同じページの上部に以下のようなメッセージが表示されます：

```
Your site is live at https://[あなたのユーザー名].github.io/henoko-media-bias-report/
```

このURLをクリックすると、ウェブサイトが表示されます！

---

## ステップ5: ファイルの更新方法（今後の運用）

### 5-1. ファイルを編集

ローカルのファイルを通常通りエディタで編集します。

### 5-2. GitHub Desktopで変更を確認

GitHub Desktopを開くと、左側の「Changes」タブに変更されたファイルが表示されます。

### 5-3. コミット

画面下部に変更内容を記述してコミット：

- **Summary**: `レポートを更新: 新しい情報を追加`
- **Description**: 具体的な変更内容

**「Commit to main」** をクリック

### 5-4. GitHubにプッシュ

画面上部の **「Push origin」** ボタンをクリック

数秒でGitHubに反映され、数分後にGitHub Pagesのサイトも自動更新されます。

---

## 📝 よくある質問（FAQ）

### Q1: GitHub Desktopにファイルが表示されない

**A**: 
1. フォルダの場所が正しいか確認
2. `.gitignore`で除外されていないか確認
3. GitHub Desktopでリポジトリを開き直す（File > Add Local Repository）

### Q2: Publishボタンが表示されない

**A**: 
すでにGitHubに公開済みです。「View on GitHub」ボタンからリポジトリページを確認してください。

### Q3: GitHub Pagesのサイトが表示されない

**A**: 
1. Settings > Pagesの設定が正しいか確認
2. リポジトリが公開（Public）になっているか確認（Settings > General）
3. 5〜10分待ってから再度アクセス
4. ブラウザのキャッシュをクリア（Ctrl+Shift+R または Cmd+Shift+R）

### Q4: 変更がサイトに反映されない

**A**: 
1. GitHub Desktopで「Push origin」したか確認
2. GitHubのリポジトリページで変更が反映されているか確認
3. GitHub Pagesは更新に数分かかる場合があります

### Q5: index.htmlのリンクが動かない

**A**: 
`index.html`内のリンクで、相対パスが正しいか確認してください。GitHub Pagesでは：
- ✅ `henoko-media-bias-report.md` → 正しい
- ❌ `/henoko-media-bias-report.md` → リポジトリ名が入らない

---

## 🎯 次のステップ

### noteの記事を公開

`note-article.md`の内容をnoteエディタにコピーし、以下の部分にGitHub PagesのURLを追加：

```markdown
**完全版はこちら**  
👉 https://[あなたのユーザー名].github.io/henoko-media-bias-report/
```

### SNSでシェア

公開URLをTwitter/Xなどでシェアして、より多くの人に読んでもらいましょう。

---

## 📞 サポート

問題が発生した場合：

1. GitHub Desktopのヘルプ: [https://docs.github.com/desktop](https://docs.github.com/desktop)
2. GitHub Pagesのドキュメント: [https://docs.github.com/pages](https://docs.github.com/pages)
3. GitHubのリポジトリでIssueを作成

---

**作成日**: 2026年4月22日  
**対象**: Windows / macOS 両対応
