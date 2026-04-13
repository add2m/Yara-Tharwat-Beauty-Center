import streamlit as st
import urllib.parse
import os
from datetime import datetime
import pytz # مكتبة لضبط التوقيت

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered")

# --- وظيفة حساب حالة العمل (مفتوح/مغلق) ---
def get_business_status():
    # ضبط التوقيت على توقيت مصر
    egypt_tz = pytz.timezone('Africa/Cairo')
    now = datetime.now(egypt_tz)
    current_hour = now.hour
    
    # المواعيد من 11 صباحاً (11) حتى 10 مساءً (22)
    start_hour = 11
    end_hour = 22
    
    if start_hour <= current_hour < end_hour:
        return "🟢 نحن متاحون الآن.. أهلاً بكِ", "rgba(40, 167, 69, 0.1)", "#28a745"
    else:
        return "🔴 المركز مغلق حالياً", "rgba(220, 53, 69, 0.1)", "#dc3545"

status_msg, bg_color, text_color = get_business_status()

# --- باقي الوظائف (الآراء) ---
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

# 3. إدارة التنقل
query_params = st.query_params
current_page = query_params.get("p", "home")

# 4. محتوى الصفحات (الحجز، الأسعار، الآراء، المعرض)
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم")
        u_phone = st.text_input("رقم الهاتف")
        if st.form_submit_button("إرسال البيانات", use_container_width=True):
            if u_name and u_phone:
                msg = urllib.parse.quote(f"حجز جديد:\nالاسم: {u_name}\nالهاتف: {u_phone}")
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center;">تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "prices":
    st.markdown("### 💰 قائمة الأسعار")
    st.info("سيتم إضافة قائمة الأسعار قريباً")

elif current_page == "reviews":
    st.markdown("### ✨ رأي عملائنا")
    all_revs = handle_reviews()
    for rev in reversed(all_revs):
        if "|" in rev:
            text, name = rev.strip().split("|")
            st.markdown(f'<div style="padding:15px; border:1px solid rgba(49,51,63,0.2); border-radius:10px; margin-bottom:10px;">"{text}"<br><small style="color:#D4AF37;">- {name}</small></div>', unsafe_allow_html=True)

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in ["1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi"]:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)

else:
    # الصفحة الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    st.markdown('<a href="./?p=booking" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49, 51, 63, 0.2); border-radius:8px; text-align:center; margin-bottom:12px;">📅 للحجز</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=prices" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49, 51, 63, 0.2); border-radius:8px; text-align:center; margin-bottom:12px;">💰 قائمة الأسعار</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=reviews" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px;">⭐ رأي عملائنا</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=gallery" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px;">✨ صور لشغلنا</div></a>', unsafe_allow_html=True)

# 5. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    
    # عرض حالة العمل (مفتوح/مغلق)
    st.markdown(f'''
        <div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; border: 1px solid {text_color};">
            {status_msg}
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">🔗 إرسال الموقع لصديقتك</div></a>', unsafe_allow_html=True)
    st.markdown(f'<div style="padding:10px; border:1px solid rgba(49,51,63,0.1); border-radius:5px;">📱 {phone_1}<br>📱 {phone_2}</div>', unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 📍 العنوان\nمنيه النصر - شارع البحر\nأعلى يونيكورن الدور الخامس")
