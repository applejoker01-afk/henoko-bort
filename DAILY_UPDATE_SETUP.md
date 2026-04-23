# 毎日更新システム設定ガイド

このガイドでは、辺野古ボート転覆事故の情報を毎日更新するために構築した自動化システムの設定方法を説明します。

## 📋 目次

1. [システムの概要](#システムの概要)
2. [初期設定](#初期設定)
3. [自動化の仕組み](#自動化の仕組み)
4. [日々の運用方法](#日々の運用方法)
5. [トラブルシューティング](#トラブルシューティング)

---

## システムの概要

### 🎯 目的

- 辺野古ボート転覆事故に関する情報を継続的に追跡
- 報道の偏りや「報道しない自由」を記録
- 遺族の発信を正確に保存
- 真相究明のための証拠保全

### 🛠️ 主な機能

1. **毎日自動でテンプレート生成** - GitHub Actionsが毎朝9時に更新テンプレートを作成
2. **Issueによるリマインダー** - 毎日の更新タスクをIssueで管理
3. **情報源チェックリスト** - 確認すべきメディアや機関を網羅
4. **週次サマリー** - 1週間の動きを総括
5. **コミュニティ貢献** - 誰でも情報提供や更新に参加可能

---

## 初期設定

### ステップ1: リポジトリの公開

GitHubリポジトリを**Public**（公開）に設定してください。

1. リポジトリのSettings > General
2. 一番下の「Danger Zone」
3. 「Change repository visibility」で「Make public」

**重要**: GitHub Actionsは公開リポジトリで無料で使用できます。

### ステップ2: GitHub Actionsの有効化

1. リポジトリのSettings > Actions > General
2. 「Actions permissions」で「Allow all actions and reusable workflows」を選択
3. 「Workflow permissions」で「Read and write permissions」を選択
4. 「Save」をクリック

### ステップ3: Labelsの作成

リポジトリのIssuesページで以下のLabelsを作成：

1. `daily-update` (色: #0075ca) - 毎日の更新タスク
2. `reminder` (色: #fbca04) - リマインダー
3. `new-info` (色: #7057ff) - 新しい情報
4. `needs-verification` (色: #d93f0b) - 要確認
5. `misinformation` (色: #b60205) - 誤報・デマ
6. `urgent` (色: #d93f0b) - 緊急

### ステップ4: ファイル構造の確認

以下のファイル構造になっているか確認：

```
henoko-media-bias-report/
├── .github/
│   ├── workflows/
│   │   └── daily-reminder.yml          # 自動化ワークフロー
│   └── ISSUE_TEMPLATE/
│       ├── new-information.md          # 情報提供テンプレート
│       └── misinformation-report.md    # 誤報報告テンプレート
├── updates/
│   ├── README.md                       # 更新履歴の索引
│   ├── SOURCES.md                      # 情報源チェックリスト
│   ├── WEEKLY_SUMMARY_TEMPLATE.md      # 週次サマリーテンプレート
│   └── 2026-04/
│       └── 2026-04-22.md              # 日次更新ファイル
├── CONTRIBUTING.md                     # 貢献ガイドライン
└── README.md                           # メインREADME
```

---

## 自動化の仕組み

### GitHub Actions ワークフローの動作

#### ファイル: `.github/workflows/daily-reminder.yml`

**実行タイミング:**
- 毎日午前9時（日本時間）
- 手動実行も可能

**実行内容:**
1. 今日の日付を取得（日本時間）
2. 今日の更新ファイルが存在するかチェック
3. なければテンプレートを自動生成
4. Issueを作成してリマインダー通知

**生成されるファイル:**
- `updates/YYYY-MM/YYYY-MM-DD.md`

**生成されるIssue:**
- タイトル: `📅 YYYY年MM月DD日 の情報更新リマインダー`
- ラベル: `daily-update`, `reminder`

### テンプレートの内容

自動生成されるテンプレートには以下が含まれます：

- ✅ 報道・メディア情報のチェックリスト
- ✅ 公的機関の発表確認欄
- ✅ 関係機関の動き記録欄
- ✅ 遺族の発信確認欄
- ✅ SNS・世論の動向記録欄
- ✅ 統計データの更新欄
- ✅ 今日のまとめ欄

---

## 日々の運用方法

### 毎朝のルーティン（所要時間: 30-60分）

#### 1. Issueの確認（5分）

1. GitHubリポジトリのIssuesタブを開く
2. 今日の日付のリマインダーIssueを確認
3. チェックリストを参照

#### 2. 情報源の確認（20-30分）

`updates/SOURCES.md`のチェックリストに従って情報を収集：

**最優先（毎日）:**
- [ ] 遺族のnote
- [ ] 産経新聞
- [ ] 読売新聞
- [ ] coki
- [ ] 沖縄タイムス
- [ ] 琉球新報
- [ ] 第11管区海上保安本部
- [ ] 文部科学省

#### 3. 更新ファイルの編集（15-20分）

##### 方法A: GitHub Web上で直接編集（簡単）

1. `updates/YYYY-MM/YYYY-MM-DD.md`を開く
2. 鉛筆アイコン（Edit）をクリック
3. 情報を追加・更新
4. 下部の「Commit changes」でコミット

##### 方法B: GitHub Desktopで編集（詳細）

1. GitHub Desktopでリポジトリを開く
2. エディタで `updates/YYYY-MM/YYYY-MM-DD.md`を編集
3. 変更を保存
4. GitHub Desktopでコミット
5. 「Push origin」でGitHubに反映

#### 4. Issueのクローズ（1分）

更新が完了したら、リマインダーIssueをクローズ

### 週末のルーティン（所要時間: 2-3時間）

#### 日曜日: 週次サマリーの作成

1. `WEEKLY_SUMMARY_TEMPLATE.md`をコピー
2. `updates/YYYY-MM/week-XX.md`として保存
3. 今週の日次更新を参照して週次サマリーを作成
4. 統計データを集計
5. 主要な動きを総括

---

## 手動での情報提供

### 他の人が情報を提供する方法

#### 方法1: Issueで情報提供（推奨）

1. [Issues](../../issues/new)を開く
2. 「新しい情報の提供」テンプレートを選択
3. フォームに記入
4. Submit

→ 管理者が確認して更新ファイルに反映

#### 方法2: Pull Requestで直接編集

1. リポジトリをフォーク
2. 更新ファイルを編集
3. Pull Requestを作成

→ 管理者がレビュー後にマージ

---

## トラブルシューティング

### Q1: GitHub Actionsが動作しない

**原因:**
- リポジトリがPrivateになっている
- GitHub Actionsが無効になっている
- Workflow permissionsが不足

**解決方法:**
1. Settings > Actions > Generalを確認
2. 「Allow all actions」が選択されているか確認
3. 「Read and write permissions」が有効か確認

### Q2: Issueが自動作成されない

**原因:**
- ワークフローのエラー
- Labelが存在しない

**解決方法:**
1. Actionsタブでワークフローの実行履歴を確認
2. エラーメッセージを読む
3. 必要なLabelを作成

### Q3: テンプレートが生成されない

**原因:**
- すでにファイルが存在する
- ワークフローの権限不足

**解決方法:**
1. `updates/YYYY-MM/YYYY-MM-DD.md`が存在するか確認
2. 存在しなければ、手動で実行: Actions > 毎日の情報更新リマインダー > Run workflow

### Q4: 更新が反映されない

**原因:**
- コミット忘れ
- プッシュ忘れ

**解決方法:**
1. GitHub Desktopで「Push origin」をクリック
2. GitHubのリポジトリページで変更が反映されているか確認

---

## 高度な設定（オプション）

### 通知の設定

GitHub Actionsの実行結果を通知で受け取る：

1. GitHubのSettings > Notifications
2. 「Actions」の通知を有効化
3. メールまたはWebで通知を受信

### 自動化のカスタマイズ

`.github/workflows/daily-reminder.yml`を編集して：

- 実行時刻の変更（cron設定）
- Issueの内容のカスタマイズ
- 通知先の追加

### RSSフィード

GitHub Issuesには自動的にRSSフィードが生成されます：

```
https://github.com/[ユーザー名]/henoko-media-bias-report/issues.atom
```

RSSリーダーに登録すると、新しいIssueを自動チェックできます。

---

## セキュリティとプライバシー

### 重要な注意事項

- ❌ 遺族の個人情報（住所、電話番号など）は絶対に記載しない
- ❌ GitHubに個人的な認証情報（APIキーなど）をコミットしない
- ✅ 遺族が公開している情報のみを扱う
- ✅ 情報源を必ず明記

### 誤ってコミットした場合

1. すぐにファイルを削除
2. 新しいコミットで上書き
3. 必要に応じてGitHubサポートに連絡

---

## サポート・質問

### ヘルプが必要な場合

1. [CONTRIBUTING.md](CONTRIBUTING.md)を確認
2. [Issues](../../issues)で質問
3. [Discussions](../../discussions)で議論（有効な場合）

### 連絡先

- **作成者:** としひで
- **GitHub:** このリポジトリのIssues
- **note:** （必要に応じて記載）

---

## まとめ

このシステムにより：

✅ 毎日自動的に更新テンプレートが生成される
✅ 情報源を漏れなくチェックできる
✅ 誰でも情報提供や更新に参加できる
✅ 長期的な記録が維持される
✅ 真相究明のための証拠が保全される

**継続は力なり。毎日の小さな更新が、大きな真実を明らかにします。**

---

**最終更新:** 2026年4月22日  
**作成者:** としひで  
**バージョン:** 1.0
