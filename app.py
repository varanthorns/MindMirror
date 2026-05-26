import streamlit as st

# 1. บังคับให้ Streamlit เปิดโหมดหน้าจอกว้างพิเศษ (ลบขอบขาวซ้ายขวา)
st.set_page_config(layout="wide", page_title="MindMirror", page_icon="👁️")

# ซ่อนขอบขาวด้านบนของ Streamlit (Padding) เพื่อให้หน้าเว็บชิดขอบสุดๆ
st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    </style>
""", unsafe_allow_html=True)

url = "https://prehistoric-mind-mirror-core.base44.app"

# 2. ปรับความสูง (height) เป็น 950px เพื่อให้เห็นฟอร์ม Login ทั้งหมดรวมถึงปุ่มด้านล่าง
iframe_html = f"""
    <iframe src="{url}" style="width:100%; height:950px; border:none;"></iframe>
"""

st.markdown(iframe_html, unsafe_allow_html=True)
