import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 頁面標題與風格
st.set_page_config(page_title="府城漫遊：台南觀光懶人包", layout="wide")

st.title("🏯 台南旅遊觀光小幫手")
st.markdown("---")

# 1. 準備資料庫 (美食與娛樂)
data = {
    '名稱': ['國華街美食區', '赤崁樓', '安平古堡', '神農街', '奇美博物館', '文章牛肉湯'],
    '類型': ['美食', '娛樂/古蹟', '娛樂/古蹟', '娛樂/文創', '娛樂/藝術', '美食'],
    '緯度': [22.9934, 22.9975, 23.0018, 22.9972, 22.9348, 23.0006],
    '經度': [120.1969, 120.2025, 120.1610, 120.1965, 120.2260, 120.1654],
    '描述': ['必吃：肉燥飯、春捲、割包', '荷蘭時期至今的古蹟', '台灣歷史最悠久的城堡', '台南最老街區，適合拍網美照', '絕美的純白建築與藝術收藏', '台南必吃招牌溫體牛肉湯']
}
df = pd.DataFrame(data)

# 2. 側邊欄過濾器
st.sidebar.header("🗺️ 我想去哪裡？")
category = st.sidebar.multiselect("選擇類型：", options=['美食', '娛樂/古蹟', '娛樂/文創', '娛樂/藝術'], default=['美食', '娛樂/古蹟'])

# 根據選擇過濾資料
filtered_df = df[df['類型'].isin(category)]

# 3. 網頁內容佈局
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 熱門景點清單")
    for index, row in filtered_df.iterrows():
        with st.expander(f"**{row['名稱']}**"):
            st.write(f"🏷️ 分類: {row['類型']}")
            st.write(f"📝 {row['描述']}")

with col2:
    st.subheader("🗺️ 互動地圖")
    # 初始化地圖 (中心點設在台南市區)
    m = folium.Map(location=[22.997, 120.200], zoom_start=13)
    
    # 加入標記
    for index, row in filtered_df.iterrows():
        icon_color = 'red' if '美食' in row['類型'] else 'blue'
        folium.Marker(
            [row['緯度'], row['經度']],
            popup=row['名稱'],
            tooltip=row['名稱'],
            icon=folium.Icon(color=icon_color, icon='info-sign')
        ).add_to(m)
    
    # 顯示地圖
    st_folium(m, width=700, height=500)

# 4. 實用小撇步
st.markdown("---")
st.info("💡 **給第一次來台南的觀光客：** 台南的大部分美食都在中西區（國華街、海安路附近），建議租借機車或搭乘市區公車，步行距離可能比想像中遠喔！")