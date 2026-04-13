import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# 3. إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to(page_name):
    st.session_state.page = page_name

# 4. الشريط الجانبي الثابت (معلومات التواصل)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل")
    st.info("01055901090\n\n01055907095")
    st.markdown("### 📍 العنوان")
    st.success("منيه النصر - الدقهلية\n\nشارع البحر - مقابل ستار مول\n\nأعلى يونيكورن - الدور الخامس")
    if st.button("🏠 العودة للرئيسية"):
        go_to('home')

# --- محتوى الصفحات ---

# الصفحة الرئيسية
if st.session_state.page == 'home':
    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    with col_img2:
        st.image(logo_url, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>مرحباً بكم في بيوتي سنتر يارا ثروت</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>اختار القسم الذي تريده:</p>", unsafe_allow_html=True)
    
    # أزرار التنقل الكبيرة في وسط الصفحة
    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
        if st.button("📅 حجز موعد", use_container_width=True):
            go_to('booking')
    with btn_col2:
        if st.button("💰 الأسعار", use_container_width=True):
            go_to('prices')
    with btn_col3:
        if st.button("✨ أعمالنا", use_container_width=True):
            go_to('gallery')

# صفحة الحجز
elif st.session_state.page == 'booking':
    st.markdown("<h2 style='text-align: right;'>بيانات الحجز</h2>", unsafe_allow_html=True)
    with st.form("booking_form"):
        u_name = st.text_input("الاسم بالكامل")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان بالتفصيل")
        u_phone = st.text_input("رقم الهاتف")
        submit = st.form_submit_button("إرسال البيانات")
