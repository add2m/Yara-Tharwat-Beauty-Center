import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_number = "201055901090"

# 3. عرض اللوجو
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

# 4. الجملة الترحيبية
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>❤️ اهلا بكم في بيوتي سنتر يارا ثروت ❤️</h3>", unsafe_allow_html=True)

# 5. الشريط الجانبي (Sidebar) - العنوان متقسم عشان يظهر كامل وميتقصش
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل")
    st.info("01055901090\n\n01055907095")
    
    st.markdown("### 📍 العنوان")
    # تقسيم العنوان لسطور واضحة
    st.success("منيه النصر - الدقهلية\n\nشارع البحر - مقابل ستار مول\n\nأعلى يونيكورن - الدور الخامس")

# 6. عنوان فورم الحجز
st.markdown("<h2 style='text-align: right;'>بيانات الحجز</h2>", unsafe_allow_html=True)

# 7. فورم إدخال البيانات
with st.form("booking_form"):
    u_name = st.text_input("الاسم بالكامل")
