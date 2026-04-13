import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered")

# --- تنسيق "الشرطتين" والأزرار (CSS) - التعديل الجديد هنا ---
st.markdown("""
    <style>
    /* تمييز أيقونة المنيو بتوهج ذهبي راقي */
    [data-testid="stSidebarCollapseIcon"], [data-testid="sidebar-button"] svg {
        color: #D4AF37 !important;
        fill: #D4AF37 !important;
        filter: drop-shadow(0 0 8px rgba(212, 175, 55, 0.8));
    }
    
    /* --- الفريم الأبيض حوالين أزرار الصفحة الرئيسية --- */
    .stMarkdown div a div {
        /* إطار أبيض واضح وسماكة متوسطة */
        border: 2px solid #FFFFFF !important;
        /* حواف دائرية شيك */
        border-radius: 10px !important;
        /* خلفية شفافة عشان يبان إن الكلام جوه الإطار */
        background-color: transparent !important;
        transition: 0.3s ease-in-out;
        /* مسافة جوه الإطار */
        padding: 15px !important;
    }
    
    /* تأثير عند تمرير الماوس فوق الزرار */
    .stMarkdown div a div:hover {
        /* تغيير لون الإطار للذهبي عند التمرير */
        border-color: #D4AF37 !important;
        /* خلفية ذهبية خفيفة جداً */
        background-color: rgba(212, 175, 55, 0.1) !important;
        transform: scale(1.02);
    }
    
    /* جعل النص جوه الإطار لونه أبيض واضح */
    .stMarkdown div a div {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- وظيفة حالة العمل ---
def get_business_status():
    now = datetime.utcnow() + timedelta(hours=3)
    current_hour = now.hour
    if 13 <= current_hour < 22:
        return "🟢 نحن متاحون الآن.. أهلاً بكِ", "rgba(40, 167, 69, 0.1)", "#28a745"
    else:
        return "🔴 المركز مغلق حالياً", "rgba(220, 53, 69, 0.1)", "#dc3545"

status_msg, bg_color, text_color = get_business_status()

# --- البيانات والروابط ---
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
phone_2 = "01055907095"
ADMIN_PASSWORD = "9811"
site_url = "https://yara-tharwat.streamlit.app"
share_msg = urllib.parse.quote(f"بصي يا جميلة، شوفت بيوتي سنتر يارا ثروت وشغله عجبني، شوفي موقعهم: {site_url}")

video_ids = ["1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi", 
             "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0", "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1", 
             "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"]

query_params = st.query_params
current_page = query_params.get("p", "home")

# 4. محتوى الصفحات
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    # (هنا كود الحجز اللي انت عارفه بالسن والعنوان..)
    if st.button("العودة للرئيسية"): st.query_params.clear(); st.rerun()

elif current_page == "prices":
    st.markdown("### 💰 قائمة الأسعار")
    st.info("سيتم إضافة قائمة الأسعار التفصيلية قريباً..")
    if st.button("العودة للرئيسية"): st.query_params.clear(); st.rerun()

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in video_ids:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)
        st.write("---")
    if st.button("العودة للرئيسية"): st.query_params.clear(); st.rerun()

elif current_page == "reviews":
    st.markdown("### ⭐ رأي عملائنا")
    # (هنا كود الآراء اللي انت عارفه..)
    if st.button("العودة للرئيسية"): st.query_params.clear(); st.rerun()

else:
    # الصفحة الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    
    menu = [("📅 للحجز الآن", "booking"), ("💰 قائمة الأسعار", "prices"), ("⭐ رأي عملائنا", "reviews"), ("✨ فيديوهات لشغلنا", "gallery")]
    for title, p in menu:
        # هنا غيرنا target ليكون _blank عشان يفتح في صفحة تانية زي ما كنت طالب في الكود القديم
        st.markdown(f'<a href="./?p={p}" target="_blank" style="text-decoration:none;color:inherit;"><div style="text-align:center; font-weight: bold; font-size: 18px;">{title}</div></a>', unsafe_allow_html=True)

# 5. Sidebar
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"📱 **للتواصل:**\n{phone_1}\n{phone_2}")
    st.markdown(f"📍 **العنوان:**\nمنيه النصر - شارع البحر - أعلى يونيكورن")
