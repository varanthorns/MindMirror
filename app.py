import streamlit as st

# 1. ตั้งค่าพื้นฐานเปิดโหมดจอกว้าง
st.set_page_config(layout="wide", page_title="MindMirror", page_icon="👁️")

# 2. ใช้ CSS ขั้นสูงเพื่อทำลายขอบขาว (Padding/Margin) ทั้งหมดของ Streamlit ให้เป็น 0
# และสั่งให้ตัวแอปยืดตัวเต็มพื้นที่หน้าจอพิกเซลต่อพิกเซล
st.markdown("""
    <style>
    /* ลบ padding ของกล่องครอบทั้งหมด */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* ซ่อน Header แถบสีขาวด้านบนสุดของ Streamlit */
    header {
        visibility: hidden !important;
        height: 0px !important;
    }
    
    /* ซ่อน Footer ด้านล่าง (ยกเว้นปุ่ม Manage app ที่ระบบบังคับไว้ แต่อย่างน้อยจะช่วยลดระยะเบียด) */
    footer {
        visibility: hidden !important;
        height: 0px !important;
    }
    
    /* สั่งให้กล่องเนื้อหาหลักขยายตัวเต็มความสูงหน้าจอทิวทัศน์ (Viewport Height) */
    .stApp {
        margin: 0px !important;
        padding: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

url = "https://prehistoric-mind-mirror-core.base44.app"

# 3. ใช้สไตล์ใน iframe บังคับความสูงเต็มหน้าจอ 100vh (100% ของความสูงหน้าจอผู้ใช้แต่ละคน)
iframe_html = f"""
    <iframe src="{url}" style="width:100%; height:100vh; border:none; margin:0; padding:0; overflow:hidden;"></iframe>
""", unsafe_allow_html=True)

st.markdown(iframe_html, unsafe_allow_html=True)
