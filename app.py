import streamlit as st

# 1. บังคับให้หน้าเว็บขยายเต็มจอซ้าย-ขวา
st.set_page_config(layout="wide")

# 2. ปรับความกว้าง (width) และความสูง (height) ให้ใหญ่ขึ้น
# การใช้ use_container_width=True จะช่วยให้มันยืดตามขนาดหน้าจอคอมพิวเตอร์
url = "https://prehistoric-mind-mirror-core.base44.app"
st.components.v1.iframe(url, height=900, scrolling=True)
