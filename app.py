import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️", layout="centered")

# 2. الروابط الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# --- ستايل الأزرار لتظهر بشكل احترافي ---
st.markdown("""
    <style>
    .nav-btn {
        display: block;
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        text-align: center;
        background-color: #D4AF37;
        color: white !important;
        text-decoration: none;
        border-radius: 10px;
        font-weight: bold;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. قراءة "علامة الصفحة" من الرابط (URL Query Params)
# دي اللي بتعرفنا إحنا في أي صفحة لما نفتح تاب جديد
query_params = st.query_params
current_page = query_params.get("p", "home")

# 4. محتوى الصفحات بناءً على الرابط
# ------------------------------

# أ. صفحة الحجز
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان")
        u_phone = st.text_input("رقم الهاتف")
        submit = st.form_submit_button("إرسال البيانات", use_container_width=True)
        if submit and u_name and u_phone:
            msg = urllib.parse.quote(f"حجز جديد:\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}")
            st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" class="nav-btn" style="background-
