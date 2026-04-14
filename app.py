import streamlit as st
import urllib.parse
import os
import base64
from datetime import datetime, timedelta

# ==========================================
# 1. إعدادات الصفحة والتهيئة (Page Config)
# ==========================================
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. كود الـ CSS المتقدم (Professional Styling)
# ==========================================
# تم دمج الخلفية الغامقة، المقص المتحرك، والتنسيقات الأصلية هنا
st.markdown("""
<style>
    /* الخطوط والتنسيق العام */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* الخلفية الغامقة الملكية (Dark Royal) */
    .stApp {
        background: #0a0a0a;
        background-image: 
            radial-gradient(at 0% 0%, rgba(212, 175, 55, 0.15) 0, transparent 50%), 
            radial-gradient(at 100% 100%, rgba(255, 255, 255, 0.05) 0, transparent 50%),
            linear-gradient(135deg, #000000 0%, #0a0a0a 100%);
        background-attachment: fixed;
        color: #ffffff !important;
    }

    /* أنيميشن المقص الذهبي (ملفت جداً) */
    @keyframes scissors-magic {
        0% { transform: rotate(0deg) scale(1) translate(0, 0); opacity: 0.2; }
        50% { transform: rotate(20deg) scale(1.1) translate(-10px, 10px); opacity: 0.4; }
        100% { transform: rotate(0deg) scale(1) translate(0, 0); opacity: 0.2; }
    }

    .scissors-container {
        position: fixed;
        top: 15%;
        right: 10%;
        width: 280px;
        height: 280px;
        z-index: 0;
        pointer-events: none;
        animation: scissors-magic 7s ease-in-out infinite;
    }

    /* تنسيق أزرار الصفحة الرئيسية (مربعات شفافة أصلية) */
    .nav-card {
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
        transition: all 0.3s ease;
        cursor: pointer;
        text-decoration: none !important;
        display: block;
        color: white !important;
    }

    .nav-card:hover {
        background: rgba(212, 175, 55, 0.1) !important;
        transform: translateY(-3px);
        border-color: #D4AF37 !important;
    }

    /* تنسيق السايدبار */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
        border-left: 1px solid #D4AF37;
    }

    /* تحسين العناوين */
    h1, h2, h3 {
        color: #D4AF37 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* إخفاء عناصر Streamlit الافتراضية للجمال */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>

<div class="scissors-container">
    <svg viewBox="0 0 512 512" fill="#D4AF37" xmlns="http://www.w3.org/2000/svg">
        <path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9zM152.7 465.1c-10.6 10.6-27.7 10.6-38.3 0s-10.6-27.7 0-38.3l103.5-103.5 38.3 38.3-103.5 103.5zm244-38.3c10.6 10.6 10.6 27.7 0 38.3s-27.7 10.6-38.3 0l-103.5-103.5 38.3-38.3 103.5 103.5z"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 3. الثوابت والبيانات (Constants & Data)
# ==========================================
LOGO_URL = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
WHATSAPP_NUM = "201055901090"
PHONE_1 = "01055901090"
PHONE_2 = "01055907095"
LOCATION_URL = "https://maps.google.com/?q=31.1895,31.7214" # إحداثيات منية النصر التقريبية
ADMIN_PASS = "9811"

# ==========================================
# 4. الوظائف المساعدة (Helper Functions)
# ==========================================
def check_status():
    """حساب حالة العمل بناءً على توقيت مصر (UTC+3)"""
    egypt_time = datetime.utcnow() + timedelta(hours=3)
    current_hour = egypt_time.hour
    if 13 <= current_hour < 22: # من 1 ظهراً لـ 10 مساءً
        return "🟢 السنتر متاح الآن.. أهلاً بكِ", "rgba(40, 167, 69, 0.2)", "#28a745"
    return "🔴 السنتر مغلق حالياً", "rgba(220, 53, 69, 0.2)", "#dc3545"

def save_review(review_text, reviewer_name):
    """حفظ المراجعات في ملف نصي"""
    with open("reviews.txt", "a", encoding="utf-8") as f:
        f.write(f"{review_text}|{reviewer_name}\n")

def load_reviews():
    """تحميل المراجعات من الملف"""
    if not os.path.exists("reviews.txt"):
        return []
    with open("reviews.txt", "r", encoding="utf-8") as f:
        return f.readlines()

# ==========================================
# 5. إدارة التنقل (Navigation Logic)
# ==========================================
query_params = st.query_params
page = query_params.get("p", "home")

# ==========================================
# 6. محتوى الصفحات (Page Content)
# ==========================================

# --- الصفحة الرئيسية ---
if page == "home":
    st.image(LOGO_URL, use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>✨اهلا بكم في بيوتي سنتر يارا ثروت✨</h2>", unsafe_allow_html=True)
    
    # شبكة الأزرار الاحترافية
    menu_items = [
        ("📆 للحجز والاستفسار", "booking"),
        ("💵 قائمة الأسعار", "prices"),
        ("🌟 رأي عملائنا", "reviews"),
        ("✨ صور لشغلنا", "gallery")
    ]
    
    for label, target in menu_items:
        st.markdown(f'<a href="./?p={target}" target="_self" class="nav-card"><div>{label}</div></a>', unsafe_allow_html=True)

# --- صفحة الحجز ---
elif page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        name = st.text_input("الاسم بالكامل")
        phone = st.text_input("رقم الهاتف")
        age = st.text_input("السن")
        address = st.text_input("العنوان")
        
        if st.form_submit_button("إرسال البيانات عبر واتساب", use_container_width=True):
            if name and phone:
                text = f"✨ حجز جديد من الموقع ✨\n👤 الاسم: {name}\n📱 الهاتف: {phone}\n🎂 السن: {age}\n📍 العنوان: {address}"
                link = f"https://wa.me/{WHATSAPP_NUM}?text={urllib.parse.quote(text)}"
                st.markdown(f'<a href="{link}" target="_blank" style="background:#25D366; color:white; padding:15px; border-radius:10px; display:block; text-align:center; text-decoration:none; font-weight:bold;">✅ اضغطي هنا لتأكيد الحجز</a>', unsafe_allow_html=True)
            else:
                st.error("يرجى ملء البيانات الأساسية")

# --- صفحة الآراء ---
elif page == "reviews":
    st.markdown("### 🌟 رأي عملائنا")
    with st.expander("📝 أضيفي رأيك هنا"):
        r_name = st.text_input("اسمك")
        r_text = st.text_area("رأيك في خدماتنا")
        if st.button("نشر الرأي"):
            if r_name and r_text:
                save_review(r_text, r_name)
                st.success("شكراً لرأيك الجميل!")
                st.rerun()

    revs = load_reviews()
    for r in reversed(revs):
        if "|" in r:
            msg, author = r.strip().split("|")
            st.markdown(f"""
            <div style="background: rgba(212,175,55,0.05); padding: 15px; border-radius: 10px; border-right: 4px solid #D4AF37; margin-bottom: 10px;">
                <p style="margin:0;">"{msg}"</p>
                <small style="color:#D4AF37;">— {author}</small>
            </div>
            """, unsafe_allow_html=True)

# --- صفحة الصور ---
elif page == "gallery":
    st.markdown("### ✨ معرض صور السنتر")
    st.info("جاري رفع أحدث الصور من أعمالنا المتميزة..")

# --- صفحة الأسعار ---
elif page == "prices":
    st.markdown("### 💵 قائمة الأسعار")
    st.info("سيتم تحديث قائمة الأسعار بأقوى العروض قريباً")

# ==========================================
# 7. الشريط الجانبي (Sidebar - Professional)
# ==========================================
with st.sidebar:
    st.image(LOGO_URL, width=150)
    
    # حالة السنتر
    msg, bg, txt = check_status()
    st.markdown(f'<div style="background:{bg}; color:{txt}; padding:10px; border-radius:8px; text-align:center; font-weight:bold; border:1px solid {txt};">{msg}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # أزرار الاتصال واللوكيشن الأصلية
    st.markdown(f'<a href="tel:{PHONE_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:12px; border-radius:8px; text-align:center; margin-bottom:10px; font-weight:bold;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{LOCATION_URL}" target="_blank" style="text-decoration:none;"><div style="background-color:#6c757d; color:white; padding:12px; border-radius:8px; text-align:center; margin-bottom:10px; font-weight:bold;">📍 موقعنا على الخريطة</div></a>', unsafe_allow_html=True)
    
    # الأرقام والعنوان الأصلي تماماً
    st.markdown(f"""
    <div style="padding:15px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; background:rgba(255,255,255,0.02);">
        <p style="margin:0; font-size:14px;">📱 {PHONE_1}</p>
        <p style="margin:0; font-size:14px;">📱 {PHONE_2}</p>
        <hr style="margin:10px 0; border-color:rgba(212,175,55,0.1);">
        <p style="font-size:13px; line-height:1.6;">📍 <b>العنوان:</b><br>الدقهلية - منية النصر - شارع البحر - أمام ستار مول - أعلى يونيكورن - الدور الخامس</p>
    </div>
    """, unsafe_allow_html=True)
