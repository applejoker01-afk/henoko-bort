# 辺野古ボート転覆事故 報道検証サイト

2026年3月16日に発生した辺野古ボート転覆事故の真相究明と再発防止のための情報集約サイトです。

## 🌐 サイト構成

```
henoko-bort/
├── index.html              # トップページ（最新情報）
├── timeline.html           # 時系列詳細
├── archive.html            # アーカイブ一覧
├── search.html             # 検索ページ
├── summary/                # AI要約
│   ├── index.html
│   └── YYYY-MM-DD.html
├── archive/                # 月別アーカイブ
├── data/                   # データファイル
│   ├── timeline.json
│   ├── latest.json
│   ├── news-latest.json
│   ├── youtube-latest.json
│   └── summaries/
├── scripts/                # 自動化スクリプト
│   ├── fetch_news.py
│   ├── fetch_youtube.py
│   └── generate_summary.py
├── assets/                 # CSS/JS
└── .github/workflows/      # GitHub Actions
```

## 🚀 セットアップ手順

### 1. GitHubにアップロード

```bash
# このフォルダの内容をすべてリポジトリにコピー
# https://github.com/applejoker01-afk/henoko-bort
```

### 2. GitHub Pages の設定

1. リポジトリの **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: main, /(root)
4. **Save** をクリック

### 3. API キーの設定

#### Claude API キー（必須）

1. https://console.anthropic.com/ でAPIキーを取得
2. リポジトリの **Settings** → **Secrets and variables** → **Actions**
3. **New repository secret** をクリック
4. Name: `ANTHROPIC_API_KEY`
5. Value: 取得したAPIキー
6. **Add secret** をクリック

#### YouTube API キー（推奨）

1. https://console.cloud.google.com/ でAPIキーを取得
2. **YouTube Data API v3** を有効化
3. Settings → Secrets で `YOUTUBE_API_KEY` を追加

### 4. GitHub Actions の有効化

1. **Settings** → **Actions** → **General**
2. **Workflow permissions** を **Read and write permissions** に設定
3. **Save**

## 🔄 自動更新の仕組み

毎日午前9時（JST）に以下が自動実行されます：

1. **ニュース取得** - 産経新聞、読売新聞などのRSSから関連記事を取得
2. **YouTube動画取得** - ニッポンジャーナル、おはよう寺ちゃんなどから関連動画を取得
3. **AI要約生成** - Claude APIで日次要約を作成
4. **サイト更新** - すべてのデータを反映

## 💰 コスト

| 項目 | 月額 |
|------|------|
| GitHub Pages | 無料 |
| GitHub Actions | 無料（パブリックリポジトリ） |
| YouTube Data API | 無料（10,000ユニット/日） |
| **Claude API** | **約$5-10/月** |
| **合計** | **約$5-10/月** |

## 📝 手動更新

時系列データを追加する場合：

1. `data/timeline.json` を編集
2. 新しいイベントを `events` 配列に追加
3. コミット & プッシュ

## 🛠️ カスタマイズ

### キーワードの変更

`scripts/fetch_news.py` の `KEYWORDS` を編集

### 監視チャンネルの追加

`scripts/fetch_youtube.py` の `CHANNELS` を編集

### CSSのカスタマイズ

`assets/css/style.css` を編集

## 📞 サポート

問題が発生した場合は、リポジトリのIssueで報告してください。

## ライセンス

このサイトのコードはMITライセンスです。
記事の内容については各情報源の著作権に従ってください。

---

**武石知華さんのご冥福をお祈り申し上げます**
