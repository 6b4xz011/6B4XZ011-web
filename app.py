import streamlit as st

# --- 頁面設定 ---
st.set_page_config(page_title="欣玫戴 | Executive Profile", page_icon="🏢", layout="wide")

# --- 注入自定義 CSS (Vibe Control) ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b4b;
        color: white;
    }
    .service-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 10px;
    }
    .hero-text {
        text-align: center;
        padding: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 側邊欄：聯絡資訊 ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="欣玫戴 Hsin-Mei Tai") # 建議替換為實際頭像
    st.title("聯絡資訊")
    st.write("📧 [6b4xz011@stust.edu.tw](mailto:6b4xz011@stust.edu.tw)")
    st.write("📞 080-0779779")
    st.write("📍 台南市永康區 (南台娛樂)")
    
    st.divider()
    
    # 社群連結
    st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-欣玫戴-1877F2?style=for-the-badge&logo=facebook)](https://www.facebook.com/keepbusytsai)")

# --- 主視覺區域 ---
st.markdown("""
    <div class="hero-text">
        <h1 style='font-size: 3rem;'>欣玫戴 <span style='color: #ff4b4b;'>Hsin-Mei Tai</span></h1>
        <h3 style='opacity: 0.8;'>南台娯樂有限公司 | 執行長 (CEO)</h3>
        <p style='font-size: 1.2rem; font-style: italic; color: #a0a0a0;'>
            「引領數位潮流，創造娛樂新標竿。」
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 核心服務內容 ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("💡 核心服務項目")
    services = [
        ("🌐 數位轉型顧問", "為企業量身打造雲端架構與自動化流程。"),
        ("📱 跨平台 App 開發", "極致性能與流暢 UI/UX 的完美結合。"),
        ("🔍 數據分析與 SEO", "精準定位客群，提升品牌網路曝光率。"),
        ("⚡ 網路資安防護", "全方位的資訊安全監測與防禦系統。")
    ]
    
    for title, desc in services:
        st.markdown(f"""
            <div class="service-card">
                <strong>{title}</strong><br>
                <small>{desc}</small>
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.subheader("🎯 品牌宣傳標語")
    st.info("**「南台娛樂，讓世界看見您的不凡。」**")
    st.success("**「用科技驅動娛樂，用專業定義未來。」**")
    st.warning("**「您的數位願景，由我們實踐。」**")
    
    st.subheader("📈 經營理念")
    st.write("""
    身為南台娯樂有限公司的執行長，欣玫致力於將最前衛的網路技術與娛樂產業深度結合。
    我們不只提供服務，我們提供的是轉型與成長的動力。
    """)

# --- 底部呼籲 ---
st.divider()
st.button("點擊與我聯繫 / 預約諮詢")

st.markdown("<center style='opacity: 0.5;'>© 2024 南台娯樂有限公司. All Rights Reserved.</center>", unsafe_allow_html=True)