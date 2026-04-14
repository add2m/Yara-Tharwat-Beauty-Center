import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="✨اهلا بكم في بيوتي سنتر يارا ثروت✨", layout="centered")

# --- إضافة: خلفية متحركة (Icons للسنتر) في الفراغات ---
st.markdown("""
<style>
/* تعيين خلفية غامقة للصفحة بالكامل */
.stApp {
    background-color: #121212;
    overflow: hidden; /* عشان الرسومات متعملش Scrollbar */
}

/* حاوية الخلفية المتحركة */
.beauty-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none; /* عشان متوقفش الكليك على الزراير */
    z-index: 0; /* خلف الكحتوى */
}

/* تصميم الأيقونات */
.beauty-bg span {
    position: absolute;
    display: block;
    width: 25px; /* حجم الأيقونة */
    height: 25px;
    background-repeat: no-repeat;
    background-size: contain;
    opacity: 0.15; /* شفافة جداً عشان متشتتش الانتباه */
    animation: moveBeauty 15s linear infinite; /* حركة مستمرة */
}

/* حركة الأيقونات (بتطلع لفوق وتلف) */
@keyframes moveBeauty {
    0% {
        transform: translateY(110vh) rotate(0deg);
    }
    100% {
        transform: translateY(-10vh) rotate(360deg);
    }
}

/* توزيع الأيقونات بأماكن وأوقات مختلفة (باستخدام nth-child) */
/* الروابط دي لرسومات Icons جاهزة (SVG) للسنتر */
.beauty-bg span:nth-child(1) { left: 10%; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="%23D4AF37"><path d="M384 192a32 32 0 1 0 0-64 32 32 0 1 0 0 64zM240 224a16 16 0 1 0 0-32 16 16 0 1 0 0 32zm0-96c-17.7 0-32 14.3-32 32s14.3 32 32 32 32-14.3 32-32-14.3-32-32-32zm208 64c-35.3 0-64-28.7-64-64S412.7 64 448 64c8.8 0 16 7.2 16 16v16h16c8.8 0 16 7.2 16 16 0 35.3-28.7 64-64 64zm-224 32c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16s-7.2 16-16 16H240c-8.8 0-16-7.2-16-16z"/></svg>'); animation-delay: 0s; animation-duration: 20s; }
.beauty-bg span:nth-child(2) { left: 25%; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="%23D4AF37"><path d="M416 32v64h-32V32h-32v64h-32V32h-32v64h-32V32h-32v64h-32V32H32v160h64v288c0 17.7 14.3 32 32 32h192c17.7 0 32-14.3 32-32V192h64V32H416z"/></svg>'); animation-delay: 2s; animation-duration: 18s; }
.beauty-bg span:nth-child(3) { left: 45%; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="%23D4AF37"><path d="M448 64h-64v64h-64V64H256v64h-64V64H128v64H64V64H32v384h32v32h384v-32h32V64z"/></svg>'); animation-delay: 5s; animation-duration: 16s; }
.beauty-bg span:nth-child(4) { left: 65%; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="%23D4AF37"><path d="M496 384H352V144c0-26.5-21.5-48-48-48s-48 21.5-48 48v240H112c-26.5 0-48 21.5-48 48 0 26.5 21.5 48 48 48h384c26.5 0 48-21.5 48-48 0-26.5-21.5-48-48-48z"/></svg>'); animation-delay: 8s; animation-duration: 14s; }
.beauty-bg span:nth-child(5) { left: 80%; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="%23D4AF37"><path d="M480 224h-16c-35.3 0-64-28.7-64-64S428.7 96 464 96c8.8 0 16 7.2 16 16s-7.2 16-16 16-16-7.2-16-16v-16h-16s-16 7.2-16 16 16 16 16 16h16c8.8 0 16 7.2 16 16 0 35.3-28.7 64-64 64h-32v32h32c17.7 0 32 14.3 32 32s-14.3 32-32 32h-32c-17.7 0-32-14.3-32-32s14.3-32 32-32h32v-32h-32c-35.3 0-64 28.7-64 64s28.7 64 64 64h16c8.8 0 16-7.2 16-16s7.2-16-16-16h-16s-16-7.2-16-16 16-16 16-16h16c35.3 0 64 28.7 64 64S496.7 480 464 480c-8.8 0-16-7.2-16-16s7.2-16 16-16h16v-16c0-17.7 14.3-32 32-32s32 14.3 32 32-14.3 32-32 32H480v16c0 35.3-28.7 64-64 64h-16s-16-7.2-16-16 16-16 16-16h16c8.8 0 16-7.2 16-16s-7.2-16-16-16v16h-16c-35.3 0-64-28.7-64-64S404.7 288 440 288c8.8 0 16 7.2 16 16s-7.2 16-16 16H440c-17.7 0-32-14.3-32-32s14.3-32 32-32H440v32h16z"/></svg>'); animation-delay: 11s; animation-duration: 12s; }
.beauty-bg span:nth-child(6) { left: 95%; background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="%23D4AF37"><path d="M128 32C92.7 32 64 60.7 64 96c0 35.3 28.7 64 64 64s64-28.7 64-64C192 60.7 163.3 32 128 32zM32 160V128H96V160H32zm160 0V128h64V160h-64zm160 0V128h64V160h-64zM32 32h64V64H32V32zm160 0h64V64h-64V32zm160 0h64V64h-64V32zm64 128c17.7 0 32 14.3 32 32v256c0 17.7-14.3 32-32 32h-32c-17.7 0-32-14.3-32-32v-32h-64v32c0 17.7-14.3 32-32 32h-32c-17.7 0-32-14.3-32-32v-32h-64v32c0 17.7-14.3 32-32 32H32c-17.7 0-32-14.3-32-32V192c0-17.7 14.3-32 32-32s32 14.3 32 32v224h64V192c0-17.7 14.3-32 32-32s32 14.3 32 32v224h64V192c0-17.7 14.3-32 32-32s32 14.3 32 32v224h64V192c0-17.7 14.3-32 32-32h32zM32 96h64V128H32V96zm160 0h64V128h-64V96zm160 0h64V128h-64V96zm128 0h32V128H480V96zm-96-64h64V64H384V32zm0 160h64V160H384V192zM128 64h64V96H128V64zm160 0h64V96h-64V64zm160 0h64V96h-64V64zm-32 160h32v32H448v-32zM32 224H64v32H32v-32z"/></svg>'); animation-delay: 14s; animation-duration: 22s; }

/* تأكيد إن المحتوى نفسه ظاهر فوق الخلفية */
.element-container {
    z-index: 10;
    position: relative;
}
</style>

<div class="beauty-bg">
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
</div>
""", unsafe_allow_html=True)

# --- باقي الكود الأساسي بدون أي تغيير ---

# --- وظيفة حساب حالة العمل (توقيت مصر UTC+3) ---
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

# رابط الموقع الأصلي
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
                full_msg = f"حجز جديد من الموقع:\n- الاسم: {u_name}\n- الهاتف: {u_phone}\n- السن: {u_age}\n- العنوان: {u_address}"
                msg = urllib.parse.quote(full_msg)
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center;">تأكيد عبر واتساب</a>', unsafe_allow_html=True)

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
        st.markdown(f'<a href="./?p={p}" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49, 51, 63, 0.2); border-radius:8px; text-align:center; margin-bottom:12px;">{title}</div></a>', unsafe_allow_html=True)

# 5. Sidebar
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<div style="background-color: {bg_color}; color: {text_color}; padding: 10px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 15px; border: 1px solid {text_color};">{status_msg}</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">🔗 إرسال الموقع لصديقتك</div></a>', unsafe_allow_html=True)
    st.markdown(f'<div style="padding:10px; border:1px solid rgba(49,51,63,0.1); border-radius:5px;">📞 {phone_1}<br>📞 {phone_2}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📍 العنوان\n الدقهليه - منيه النصر - \n شارع البحر - امام استار مول - \n اعلى يونيكورن - الدور الخامس")
