"""
ニュース記事の自動取得スクリプト
産経新聞、読売新聞などのRSSフィードから関連記事を取得
"""

import json
import os
import re
from datetime import datetime, timedelta
import feedparser
import requests
from pathlib import Path

# キーワード
KEYWORDS = ["辺野古", "武石知華", "同志社国際", "ボート転覆", "不屈", "平和丸"]

# RSSフィード一覧
RSS_FEEDS = {
    "sankei": "https://www.sankei.com/rss/news/affairs.xml",
    "yomiuri": "https://www.yomiuri.co.jp/rss/yol/main.xml",
    "okinawa-times": "https://www.okinawatimes.co.jp/feed",
    "ryukyu-shimpo": "https://ryukyushimpo.jp/feed",
}

# noteのRSS
NOTE_RSS = "https://note.com/beloved_tomoka/rss"


def is_relevant(text):
    """記事が関連するかチェック"""
    if not text:
        return False
    return any(keyword in text for keyword in KEYWORDS)


def fetch_rss_news(source, url):
    """RSSフィードから関連記事を取得"""
    articles = []
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            title = entry.get('title', '')
            summary = entry.get('summary', '')
            
            if is_relevant(title) or is_relevant(summary):
                published = entry.get('published_parsed')
                date_str = ''
                if published:
                    date_str = datetime(*published[:6]).strftime('%Y-%m-%d')
                
                articles.append({
                    "title": title,
                    "source": source,
                    "url": entry.get('link', ''),
                    "date": date_str,
                    "excerpt": re.sub(r'<[^>]+>', '', summary)[:200],
                })
    except Exception as e:
        print(f"❌ {source}の取得に失敗: {e}")
    
    return articles


def fetch_note_articles():
    """noteの記事を取得"""
    articles = []
    try:
        feed = feedparser.parse(NOTE_RSS)
        for entry in feed.entries[:10]:  # 最新10件
            published = entry.get('published_parsed')
            date_str = ''
            if published:
                date_str = datetime(*published[:6]).strftime('%Y-%m-%d')
            
            articles.append({
                "title": entry.get('title', ''),
                "source": "note",
                "author": "辺野古ボート転覆事故遺族メモ",
                "url": entry.get('link', ''),
                "date": date_str,
                "excerpt": re.sub(r'<[^>]+>', '', entry.get('summary', ''))[:200],
            })
    except Exception as e:
        print(f"❌ noteの取得に失敗: {e}")
    
    return articles


def fetch_all_news():
    """すべてのニュースを取得"""
    print("📰 ニュース取得を開始...")
    
    all_articles = []
    
    # 各RSSフィードから取得
    for source, url in RSS_FEEDS.items():
        print(f"  - {source} を取得中...")
        articles = fetch_rss_news(source, url)
        all_articles.extend(articles)
        print(f"    ✅ {len(articles)}件の関連記事を発見")
    
    # noteから取得
    print(f"  - note を取得中...")
    note_articles = fetch_note_articles()
    all_articles.extend(note_articles)
    print(f"    ✅ {len(note_articles)}件の記事を発見")
    
    # 日付順にソート（新しい順）
    all_articles.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    return all_articles


def save_news(articles, output_path):
    """ニュースをJSONに保存"""
    data = {
        "last_updated": datetime.now().isoformat(),
        "articles": articles
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"💾 {len(articles)}件のニュースを保存: {output_path}")


def main():
    output_dir = Path(__file__).parent.parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    articles = fetch_all_news()
    save_news(articles, output_dir / "news-latest.json")
    
    print(f"✅ 完了: 合計 {len(articles)} 件の記事を取得")


if __name__ == "__main__":
    main()
