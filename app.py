import streamlit as st
import urllib.parse

st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# رابط اللوجو الذهبي
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"

# عرض اللوجو في نص الصفحة
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

# الجملة الترحيبية اللي طلبتها تحت اللوجو علطول
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h3>", unsafe_allow_html=True)

# الشريط الجانبي (Sidebar) فيه بياناتك كاملة
with st.sidebar:
    st.image(logo_url, width=150)
    st.title("تواصل معنا")
    st.markdown("---")
    st.markdown("### 📞 الأرقام:")
    st.write("01055901090")
    st.write("01055907095")
    st.markdown("---")
    st.markdown("### 📍 العنوان:")
    st.write("منيه النصر - شارع البحر - مقابل ستار مول - اعلي يونيكورن - الدور الخامس")

if 'confirmed' not in st.session_state:
    st.session_state.confirmed = False

if not st.session_state.confirmed:
    st.header("برجاء إدخال البيانات التالية للحجز")
