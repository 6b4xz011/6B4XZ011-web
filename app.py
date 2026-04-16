import streamlit as st
import folium
from streamlit_folium import st_folium

# --- 頁面配置 ---
st.set_page_config(page_title="Tainan Élégance | 台南優雅漫步", page_icon="🍷", layout="wide")

# --- 側邊欄：優雅的聯絡方式 ---
with st.sidebar:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### 🕊️ *L'Explorateur*")
    st.write("---")
    st.markdown("**聯絡諮詢**")
    st.write("📧 6b4xz011@stust.edu.tw")
    st.markdown("[![FB](https://img.shields.io/badge/Facebook-KeepbusyTsai-9A8C98?style=for-the-badge)](https://www.facebook.com/keepbusytsai)")
    st.write("---")
    st.markdown("### *Philosophie*")
    st.markdown("*「旅行不是尋找新的風景，而是擁有新的眼光。」*")

# --- 主視覺區域 ---
st.markdown('<div class="main-header">TAINAN · ÉLÉGANCE</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-family: serif; font-size: 1.1rem; color: #9A8C98;'>一場關於莫蘭迪色調與府城記憶的溫柔對話</p>", unsafe_allow_html=True)

# --- 整合地圖與視覺亮點 ---
m_col, d_col = st.columns([1.5, 1])

with m_col:
    # 使用莫蘭迪色調的地圖樣式
    m = folium.Map(location=[22.9975, 120.18], zoom_start=13, tiles="CartoDB Positron")
    
    # 景點標註
    points = [
        {"name": "奇美博物館", "pos": [22.9348, 120.2260], "color": "#D4B2A7"},
        {"name": "國華街美食", "pos": [22.9961, 120.1979], "color": "#84A59D"},
        {"name": "神農街", "pos": [22.9972, 120.1966], "color": "#9A8C98"}
    ]
    for p in points:
        folium.CircleMarker(
            location=p["pos"], radius=8, color=p["color"], fill=True, popup=p["name"]
        ).add_to(m)
    
    st_folium(m, width="100%", height=400)

with d_col:
    st.markdown("### *Sélection d'Art* 必訪清單")
    st.markdown("""
    - **國華街美食**：味覺的極致優雅
    - **安平古堡**：歷史遺留的溫潤紅磚
    - **奇美博物館**：台南的凡爾賽宮
    """)
    st.image("https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=400&q=80", caption="Gourmet Tainan")

# --- 行程區 (法式排版) ---
st.markdown("<br><h2 style='text-align: center;'>ITINÉRAIRE · 行程設計</h2>", unsafe_allow_html=True)

t1, t2, t3 = st.tabs(["L'Essentiel 一日", "La Culture 二日", "La Vie 三日"])

with t1:
    st.markdown("""
    <div class="vibe-card">
        <h3>時光靜好 · 一日輕旅行</h3>
        <p><span class="time-tag">Matin</span> 於老宅享用牛肉湯，感受府城的甦醒</p>
        <p><span class="time-tag">Après-midi</span> 散步於神農街，在工藝小店尋寶</p>
        <p><span class="time-tag">Soirée</span> 觀夕平台，看夕陽沒入溫柔的海面</p>
        <div class="quote-box">
            「台南的步調，適合用來讀一本好書，或談一場無事的戀愛。」— <em>旅人 A推薦</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="vibe-card">
        <h3>藝術陶冶 · 二日深旅</h3>
        <p><strong>Premier Jour:</strong> 走訪孔廟園區，品嚐莉莉水果冰的清甜。</p>
        <p><strong>Deuxième Jour:</strong> 沉浸於奇美博物館的西洋藝術收藏。</p>
        <div class="quote-box">
            「在這裡，時間彷彿被調慢了速度。」— <em>藝術評論家 B</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
    <div class="vibe-card">
        <h3>漫活府城 · 三日漫遊</h3>
        <p><strong>完整導覽:</strong> 從市區的小巷、安平的潮汐，到北門的鹽田。每一處都是莫蘭迪色調的完美體現。</p>
        <div class="quote-box">
            「這不是一場觀光，而是一場靈魂的洗滌。」— <em>生活風格家 C</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("<center style='opacity: 0.6; font-family: serif;'>C'est la vie. 南台娛樂 | 執行長 欣玫戴 監製</center>", unsafe_allow_html=True)