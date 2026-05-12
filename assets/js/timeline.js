// ============================================
// タイムライン表示
// ============================================

let timelineData = [];

// データ読み込み
async function loadTimelineData() {
    try {
        const response = await fetch('/data/timeline.json');
        const data = await response.json();
        timelineData = data.events || [];
        return timelineData;
    } catch (error) {
        console.error('タイムラインデータの読み込みに失敗しました:', error);
        return [];
    }
}

// 経過日数計算
function calculateDaysSince(dateStr) {
    const eventDate = new Date(dateStr);
    const accidentDate = new Date('2026-03-16');
    const diff = Math.floor((eventDate - accidentDate) / (1000 * 60 * 60 * 24));
    return diff;
}

// 日付フォーマット
function formatDate(dateStr) {
    const date = new Date(dateStr);
    const days = ['日', '月', '火', '水', '木', '金', '土'];
    return `${date.getFullYear()}年${date.getMonth() + 1}月${date.getDate()}日（${days[date.getDay()]}）`;
}

// タイムライン描画
function renderTimeline(events, containerId = 'timeline-container') {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    // 日付順（新しい順）にソート
    const sorted = [...events].sort((a, b) => new Date(b.date) - new Date(a.date));
    
    container.innerHTML = `
        <div class="timeline">
            ${sorted.map(event => `
                <div class="timeline-item ${event.critical ? 'critical' : ''}">
                    <div class="timeline-date">${formatDate(event.date)}</div>
                    <div class="timeline-days">事故から${calculateDaysSince(event.date)}日目</div>
                    <div class="timeline-content">
                        <h3>${event.icon || '📌'} ${event.title}</h3>
                        ${event.source ? `<span class="source">${getSourceName(event.source)}</span>` : ''}
                        ${event.content || ''}
                        ${event.url ? `<p style="margin-top: 1rem;"><a href="${event.url}" target="_blank" class="btn btn-primary">詳細を見る →</a></p>` : ''}
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

// 情報源名取得
function getSourceName(source) {
    const sources = {
        'sankei': '📰 産経新聞',
        'yomiuri': '📰 読売新聞',
        'mainichi': '📰 毎日新聞',
        'asahi': '📰 朝日新聞',
        'okinawa-times': '📰 沖縄タイムス',
        'ryukyu-shimpo': '📰 琉球新報',
        'youtube': '🎥 YouTube',
        'x-post': '🐦 X (Twitter)',
        'note': '📝 note',
        'official': '🏛️ 公的機関',
        'other': '📌 その他'
    };
    return sources[source] || source;
}

// 初期化
document.addEventListener('DOMContentLoaded', async () => {
    const events = await loadTimelineData();
    renderTimeline(events);
});
