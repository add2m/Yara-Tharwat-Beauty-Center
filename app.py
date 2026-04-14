import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered")

# --- خلفية "تموجات الشفق القطبي الذهبية" فائقة الدهشة والمضمونة 100% ---
# تم استخدام كود CSS نقي لإنشاء تأثير حركة أمواج متدرجة بالأسود والذهبي.
st.markdown("""
<style>
/* تعيين خلفية سوداء أساسية */
.stApp {
    background: #000;
    overflow: hidden;
}

/* حاوية الخلفية المتحركة */
.stApp::before {
    content: "";
    position: fixed;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    
    /* المتدرج اللوني المدهش: أسود ودرجات ذهبية خافتة */
    background: radial-gradient(circle at center, rgba(15, 15, 15, 0) 0%, #000 100%),
                linear-gradient(135deg, 
                                #000 0%, 
                                #111 25%, 
                                rgba(212, 175, 55, 0.08) 50%, 
                                #111 75%, 
                                #000 100%);
    
    background-size: 400% 400%;
    
    /* حركة تموجات بطيئة وناعمة */
    animation: goldAuroraWaves 30s ease infinite;
    z-index: 0;
    pointer-events: none;
    opacity: 0.7; /* درجة شفافية عشان متغطيش على الكلام */
}

@keyframes goldAuroraWaves {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* تأكيد إن المحتوى نفسه ظاهر فوق الخلفية وواضح */
.element-container, .stMarkdown, .stImage, .stButton {
    position: relative;
    z-index: 10;
}

/* تنسيق المربعات لتكون منسجمة مع الفخامة والدهشة */
div[data-testid="stMarkdownContainer"] > div > a > div {
    border: 1px solid rgba(212, 175, 55, 0.2) !important;
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(5px);
    transition: 0.4s !important;
    color: #eee !important;
}

div[data-testid="stMarkdownContainer"] > div > a > div:hover {
    border: 1px solid rgba(212, 175, 55, 0.8) !important;
    background: rgba(212, 175, 55, 0.05) !important;
    transform: translateY(-3px);
    box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1);
}
</style>
""", unsafe_allow_html=True)

# --- باقي الكود الأساسي كما هو تماماً ---

# --- وظيفة حساب حالة العمل ---
def get_business_status():
    now = datetime.utcnow() + timedelta(hours=3)
    current_hour = now.hour
    start_hour = 13
    end_hour = 22
    if start_hour <= current_hour < end_hour:
        return "🟢 نحن متاحون الآن.. أهلاً بكِ", "rgba(40, 167, 69, 0.1)", "#28a745"
    else:
        return "🔴 السنتر مغلق حالياً", "rgba(220, 53, 69, 0.1)", "#dc3545"

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
share_msg = urllib.parse.quote(f" شوفت بيوتي سنتر يارا ثروت وشغله عجبني جداً، شوفي موقعهم من هنا: {site_url}")

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
        u_name = st.text_input("الاسم بالكامل")
        u_phone = st.text_input("رقم الهاتف")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان")
        if st.form_submit_button("إرسال البيانات", use_container_width=True):
            if u_name and u_phone:
                lines = ["✨ حجز جديد من الموقع ✨", f"👤 الاسم: {u_name}", f"📱 الهاتف: {u_phone}", f"🎂 السن: {u_age}", f"📍 العنوان: {u_address}"]
                full_msg = "\n".join(lines)
                msg = urllib.parse.quote(full_msg)
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">✅ تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "prices":
    st.markdown("### 💵 قائمة الأسعار")
    st.info("سيتم إضافة قائمة الأسعار قريباً")

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
            st.markdown(f'<div style="padding:15px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; margin-bottom:10px; background: rgba(255,255,255,0.02);">"{t}"<br><small style="color:#D4AF37;">- {n}</small></div>', unsafe_allow_html=True)

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in video_ids:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)
        st.write("---")

else:
    # الصفحة الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    for title, p in [("📆 للحجز والاستفسار", "booking"), ("💵 قائمة الأسعار", "prices"), ("🌟 رأي عملائنا", "reviews"), ("✨ صور لشغلنا", "gallery")]:
        st.markdown(f'<a href="./?p={p}" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:15px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; text-align:center; margin-bottom:12px;">{title}</div></a>', unsafe_allow_html=True)

# 5. Sidebar
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">🔗 إرسال الموقع لصديقتك</div></a>', unsafe_allow_html=True)
    st.markdown(f'<div style="padding:10px; border:1px solid rgba(212,175,55,0.1); border-radius:5px;">📞 {phone_1}<br>📞 {phone_2}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📍 العنوان\n الدقهليه - منيه النصر - \n شارع البحر - امام استار مول - \n اعلى يونيكورن - الدور الخامس")
