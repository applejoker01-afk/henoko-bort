"""
YouTube動画の自動取得スクリプト
ニッポンジャーナル、おはよう寺ちゃんなどから関連動画を取得
"""

import json
import os
from datetime import datetime
from pathlib import Path
import requests

# YouTube Data API v3 を使用
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")

# 監視するチャンネル
CHANNELS = {
    "ニッポンジャーナル": "UCq5dLZmGuwSTPCmWGcXAGNg",  # 実際のチャンネルIDに変更
    "おはよう寺ちゃん": "UCXFiB9HInBYpD3yY52J7q4Q",   # 実際のチャンネルIDに変更
}

# キーワード
KEYWORDS = ["辺野古", "武石知華", "同志社国際", "ボート転覆"]


def search_videos(channel_id, channel_name):
    """チャンネルの最新動画から関連動画を検索"""
    if not YOUTUBE_API_KEY:
        print("⚠️ YOUTUBE_API_KEY が設定されていません")
        return []
    
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "channelId": channel_id,
        "maxResults": 20,
        "order": "date",
        "type": "video",
        "key": YOUTUBE_API_KEY
    }
    
    videos = []
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if "items" not in data:
            print(f"❌ {channel_name}: {data.get('error', {}).get('message', 'Unknown error')}")
            return []
        
        for item in data["items"]:
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            
            # キーワードフィルター
            if any(kw in title or kw in description for kw in KEYWORDS):
                video_id = item["id"]["videoId"]
                videos.append({
                    "title": title,
                    "channel": channel_name,
                    "url": f"https://www.youtube.com/watch?v={video_id}",
                    "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
                    "date": item["snippet"]["publishedAt"][:10],
                    "description": description[:200],
                    "source": "youtube"
                })
        
        print(f"  ✅ {channel_name}: {len(videos)}件の関連動画を発見")
        
    except Exception as e:
        print(f"❌ {channel_name} の取得に失敗: {e}")
    
    return videos


def main():
    print("🎥 YouTube動画取得を開始...")
    
    all_videos = []
    for channel_name, channel_id in CHANNELS.items():
        videos = search_videos(channel_id, channel_name)
        all_videos.extend(videos)
    
    # 日付順にソート
    all_videos.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    # 保存
    output_dir = Path(__file__).parent.parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    data = {
        "last_updated": datetime.now().isoformat(),
        "videos": all_videos
    }
    
    with open(output_dir / "youtube-latest.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 完了: 合計 {len(all_videos)} 件の動画を取得")


if __name__ == "__main__":
    main()
