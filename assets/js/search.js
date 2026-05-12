// ============================================
// 検索機能
// ============================================

let searchData = [];
let currentFilter = 'all';

// データ読み込み
async function loadSearchData() {
    try {
        const response = await fetch('/data/timeline.json');
        const data = await response.json();
        searchData = data.events || [];
    } catch (error) {
        console.error('データの読み込みに失敗しました:', error);
    }
}

// 検索実行
function performSearch(query) {
    const lowerQuery = query.toLowerCase();
    
    let filtered = searchData.filter(item => {
        // フィルター適用
        if (currentFilter !== 'all' && item.source !== currentFilter) {
            return false;
        }
        
        // 検索クエリ
        if (!query) return true;
        
        return (
            (item.title && item.title.toLowerCase().includes(lowerQuery)) ||
            (item.content && item.content.toLowerCase().includes(lowerQuery)) ||
            (item.date && item.date.includes(lowerQuery))
        );
    });
    
    displayResults(filtered);
}

// 結果表示
function displayResults(results) {
    const container = document.getElementById('search-results');
    if (!container) return;
    
    if (results.length === 0) {
        container.innerHTML = '<p class="no-results">該当する情報が見つかりませんでした。</p>';
        return;
    }
    
    container.innerHTML = `
        <p class="result-count">${results.length}件の結果が見つかりました</p>
        ${results.map(item => `
            <div class="media-card ${item.source || ''}">
                <span class="source">${getSourceName(item.source)}</span>
                <h3><a href="${item.url || '#'}" target="_blank">${item.title}</a></h3>
                <p class="date">${item.date} (事故から${item.days_since}日目)</p>
                <p class="excerpt">${item.content || ''}</p>
            </div>
        `).join('')}
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

// フィルター変更
function setFilter(filter) {
    currentFilter = filter;
    
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.filter === filter);
    });
    
    const query = document.getElementById('search-input').value;
    performSearch(query);
}

// 初期化
document.addEventListener('DOMContentLoaded', async () => {
    await loadSearchData();
    
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            performSearch(e.target.value);
        });
        
        // 初期表示
        performSearch('');
    }
    
    // フィルターボタン
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            setFilter(btn.dataset.filter);
        });
    });
});
