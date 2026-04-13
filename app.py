import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered")

# --- تنسيق "الشرطتين" (Sidebar Icon) والأزرار (CSS) ---
st.markdown("""
    <style>
    /* جعل أيقونة المنيو ذهبية ومتوهجة بشكل شيك */
    [data-testid="stSidebarCollapseIcon"], [data-testid="sidebar-button"] svg {
        color: #D4AF37 !important;
        fill: #D4AF37 !important;
        filter: drop-shadow(0 0 5px rgba(212, 175, 55, 0.8));
    }
    
    /* تحسين شكل أزرار الصفحة الرئيسية */
    .stMarkdown div a div {
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        transition: 0.3s ease;
        background-color: rgba(255, 255, 255, 0.02);
    }
    .stMarkdown div a div:hover {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border-color: #D4AF37 !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# --- وظيفة حساب حالة العمل (توقيت مصر UTC+3) ---
def get_business_status():
    now = datetime.utcnow() + timedelta(hours=3)
    current_hour = now.hour
    start_hour = 13
    end_hour = 22
    if start_hour <= current_hour < end_hour:
        return "🟢 نحن متاحون الآن.. أهلاً بكِ", "rgba(40, 167, 69, 0.1)", "#28a745"
    else:
        return "🔴 المركز مغلق حالياً", "rgba(220, 53, 69, 0.1)", "#dc3545"

status_msg, bg_color, text_color = get_business_status()

# --- وظيفة الآراء ---
def handle_reviews(action="read", data=None):
    file_path = "reviews.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f: f.write("شغل ممتاز وتسلم إيديكم!|سارة")
    with open(file_path, "r", encoding="utf-8") as f:
        reviews = f.readlines()
    if action == "add" and data:
        with open(file_path, "a", encoding="utf-8") as f: f.write(f"\n{data}")
    elif action == "delete_one" and data is not None:
        if 0 <= data < len(reviews):
            reviews.pop(data)
            with open(file_path, "w", encoding="utf-8") as f: f.writelines(reviews)
    return reviews

# 2. البيانات والروابط
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
phone_2 = "01055907095"
ADMIN_PASSWORD = "9811" 

site_url = "https://yara-tharwat.streamlit.app" 
share_msg = urllib.parse.quote(f"بصي يا جميلة، شوفت بيوتي سنتر يارا ثروت وشغله عجبني جداً، شوفي موقعهم من هنا: {site_url}")

video_ids = ["1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi", 
             "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0", "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1", 
             "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"]

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
        
        if st.form_submit_button("إرسال البيانات وحجز موعد", use_container_width=True):
            if u_name and u_phone and u_age and u_address:
                msg_text = f"حجز جديد من الموقع:\n\n👤 الاسم: {u_name}\n🎂 السن: {u_age}\n📱 الهاتف: {u_phone}\n📍 العنوان: {u_address}"
                msg = urllib.parse.quote(msg_text)
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">تأكيد عبر واتساب ✅</a>', unsafe_allow_html=True)
            else:
                st.warning("رجاءً أكملي كافة البيانات")
    if st.button("العودة للرئيسية"): st.query_params.clear(); st.rerun()

elif current_page == "prices":
    st.markdown("### 💰 قائمة الأسعار")
    st.info("سيتم إضافة قائمة الأسعار قريباً")
    if st.button("العودة للرئيسية"): st.query_params.clear(); st.rerun()

elif current_page == "reviews":
    st.markdown("### ✨ رأي عملائنا")
    with st.expander("اضف رأيك هنا"):
        with st.form("review_form"):
            r_name = st.text_input("الاسم")
            r_text = st.text_area("رأيك")
            if st.form_submit_button("نشر"):
                if r_name and r_text:
                    handle_reviews("add", f"{r_text}|{r_name}")
                    st.rerun()
    all_revs = handle_reviews()
    for rev in reversed(all_revs):
        if "|" in rev:
            t, n = rev.strip().split("|")
            st.markdown(f'<div style="padding:15px; border:1px solid rgba(49,51,63,0.2); border-radius:10px; margin-bottom:10px;">"{t}"<br><small style="color:#D4AF37;">- {n}</small></div>', unsafe_allow_html=True)
    
    with st.expander("🔐 إدارة"):
        pwd = st.text_input("الباسورد", type="password")
        if pwd == ADMIN_PASSWORD:
            for i, rev in enumerate(all_revs):
                if "|" in rev:
                    content, sender = rev.strip().split("|")
                    if st.button(f"🗑️ حذف {sender}", key=f"del_{i}"):
                        handle_reviews("delete_one", i)
                        st.rerun()
    if st.button("العودة للرئيسية"): st.query_params.clear(); st.rerun()

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in video_ids:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)
        st.write("---")
    if st.button("العودة للرئيسية"): st.query_params.clear(); st.rerun()

else:
    # الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    
    # تم تعديل target ليكون _blank لفتح صفحات جديدة
    menu = [("📅 للحجز الآن", "booking"), ("💰 قائمة الأسعار", "prices"), ("⭐ رأي عملائنا", "reviews"), ("✨ فيديوهات لشغلنا", "gallery")]
    for title, p in menu:
        st.markdown(f'<a href="./?p={p}" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:15px; border-radius:10px; text-align:center; margin-bottom:12px; font-weight: bold; font-size: 18px;">{title}</div></a>', unsafe_allow_html=True)

# 5. Sidebar
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">🔗 إرسال الموقع لصديقتك</div></a>', unsafe_allow_html=True)
    st.markdown(f'<div style="padding:10px; border:1px solid rgba(49,51,63,0.1); border-radius:5px; text-align: center;">📱 {phone_1}<br>📱 {phone_2}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📍 العنوان\nمنيه النصر - شارع البحر\nأعلى يونيكورن الدور الخامس")
