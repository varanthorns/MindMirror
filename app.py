import streamlit as st

st.set_page_config(layout="wide")  # ตั้งค่าหน้าจอให้กว้างเพื่อความสวยงาม

st.title("แสดงหน้าเว็บใน Streamlit")

# ใส่ URL ที่ต้องการแสดง
url = "https://prehistoric-mind-mirror-core.base44.app"

# แสดงผลผ่าน iframe (สามารถปรับความกว้าง width และความสูง height ได้ตามต้องการ)
st.components.v1.iframe(url, width=1000, height=800, scrolling=True)
