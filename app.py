import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered")

# --- التنسيق الجمالي: الفريم الأبيض فقط ---
st.markdown("""
    <style>
    /* إضافة فريم أبيض حول الروابط دون إخفاء محتواها */
    .stMarkdown div a div {
        border: 2px solid #FFFFFF !important; /* فريم أبيض واضح */
        border-radius: 12px !important;      /* حواف دائرية */
        padding: 10px !important;           /* مسافة داخلية */
        margin-bottom: 10px !important;      /* مسافة بين الزراير */
        display: flex;
        justify-content: center;
        align-items: center;
        transition: 0.3s;
    }
    
    /* تغيير لون الفريم للذهبي عند التمرير */
    .stMarkdown div a div:hover {
        border-color: #D4AF37 !important;
        background-color: rgba(212, 175, 55, 0.1) !important;
    }

    /* الحفاظ على لون أيقونة المنيو ذهبي */
    [data-testid="stSidebarCollapseIcon"] svg {
        fill: #D4AF37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- وظيفة حالة العمل ---
def get_business_status():
    now = datetime.utcnow() + timedelta(hours=3) # توقيت مصر
    current_hour = now.hour
    if 13 <= current_hour < 22:
        return "🟢 نحن متاحون الآن.. أهلاً بكِ", "rgba(40, 167, 69, 0.1)", "#28a745"
    else:
        return "🔴 المركز مغلق حالياً", "rgba(220, 53, 69, 0.1)", "#dc3545"

status_msg, bg_color, text_color = get_business_status()

# --- وظيفة الآراء (لضمان عمل خانة العملاء) ---
def handle_reviews(action="read", data=None):
    file_path = "reviews.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f: f.write("شغل ممتاز!|سارة")
    with open(file_path, "r", encoding="utf-8") as f:
        reviews = f.readlines()
    if action == "add" and data:
        with open(file_path, "a", encoding="utf-8") as f: f.write(f"\n{data}")
    return reviews

# 2. البيانات الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
phone_2 = "01055907095"
site_url = "https://yara-tharwat.streamlit.app"
share_msg = urllib.parse.quote(f"شوفي بيوتي سنتر يارا ثروت: {site_url}")

# 3. إدارة التنقل
query_params = st.query_params
current_page = query_params.get("p", "home")

# 4. محتوى الصفحات
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم")
        u_age = st.text_input("السن")
        u_phone = st.text_input("رقم الهاتف")
        u_address = st.text_input("العنوان")
        if st.form_submit_button("إرسال البيانات", use_container_width=True):
            if u_name and u_phone:
                msg = urllib.parse.quote(f"حجز جديد:\nالاسم: {u_name}\nالسن: {u_age}\nالهاتف: {u_phone}\nالعنوان: {u_address}")
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">تأكيد عبر واتساب ✅</a>', unsafe_allow_html=True)
    if st.button("العودة"): st.query_params.clear(); st.rerun()

elif current_page == "reviews":
    st.markdown("### ⭐ رأي عملائنا")
    all_revs = handle_reviews()
    for rev in reversed(all_revs):
        if "|" in rev:
            t, n = rev.strip().split("|")
            st.markdown(f'<div style="padding:10px; border:1px solid #ddd; border-radius:10px; margin-bottom:5px;">"{t}" - <b>{n}</b></div>', unsafe_allow_html=True)
    if st.button("العودة"): st.query_params.clear(); st.rerun()

else:
    # الصفحة الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    
    # القائمة الرئيسية مع الفريم الأبيض
    menu = [("📅 للحجز الآن", "booking"), ("💰 قائمة الأسعار", "prices"), ("⭐ رأي عملائنا", "reviews"), ("✨ فيديوهات لشغلنا", "gallery")]
    for title, p in menu:
        st.markdown(f'<a href="./?p={p}" target="_blank" style="text-decoration:none;color:white;"><div style="font-weight: bold;">{title}</div></a>', unsafe_allow_html=True)

# 5. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px; font-weight: bold;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px; font-weight: bold;">🔗 إرسال الموقع لصديقتك</div></a>', unsafe_allow_html=True)
    st.markdown(f"📱 {phone_1} | {phone_2}")
    st.markdown("---")
    st.markdown("### 📍 العنوان\nمنيه النصر - شارع البحر")
