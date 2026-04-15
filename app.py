import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# ============================================================
# 1. إعدادات الصفحة
# ============================================================
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- وظيفة التعامل مع ملف الآراء ---
def handle_reviews(action="read", data=None):
    file_path = "reviews.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f: 
            f.write("شغل ممتاز وتسلم إيديكم!|سارة")
            
    with open(file_path, "r", encoding="utf-8") as f:
        reviews = f.readlines()
        
    if action == "add" and data:
        with open(file_path, "a", encoding="utf-8") as f: 
            f.write(f"\n{data}")
    elif action == "delete_one" and data is not None:
        if 0 <= data < len(reviews):
            reviews.pop(data)
            with open(file_path, "w", encoding="utf-8") as f: 
                f.writelines(reviews)
    return reviews

# ============================================================
# 2. كود الـ CSS المتقدم (حل مشكلة اليمين واليسار والموبايل)
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* ضبط الخط والاتجاه العام */
    html, body, [data-testid="stSidebar"], .stMarkdown {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* إجبار السايدبار على جهة اليسار تماماً */
    [data-testid="stSidebar"] {
        left: 0 !important;
        right: auto !important;
        background-color: #080808 !important;
        border-right: 1px solid #D4AF37;
        border-left: none !important;
    }

    /* تعديل مكان زر السايدبار (السهم) ليكون في اليسار */
    [data-testid="stSidebarCollapsedControl"] {
        left: 20px !important;
        right: auto !important;
        background-color: rgba(212, 175, 55, 0.2);
        border-radius: 50%;
    }

    /* تحسين شكل السايدبار في الموبايل */
    @media (max-width: 768px) {
        [data-testid="stSidebar"] {
            width: 250px !important;
        }
    }

    .stApp {
        background: #000000;
        background-image: 
            radial-gradient(at 0% 100%, rgba(212, 175, 55, 0.1) 0, transparent 50%), 
            linear-gradient(180deg, #000000 0%, #050505 100%);
        background-attachment: fixed;
        color: #ffffff !important;
    }

    /* أزرار القائمة الرئيسية */
    .nav-btn {
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 18px;
        text-align: center;
        margin-bottom: 12px;
        transition: all 0.3s ease;
        text-decoration: none !important;
        display: block;
        color: #D4AF37 !important;
        font-weight: bold;
        font-size: 1.1rem;
    }

    .nav-btn:hover {
        background: #D4AF37 !important;
        color: #000 !important;
        transform: translateY(-2px);
    }

    /* إخفاء الهيدر الافتراضي المزعج */
    header { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }

    /* أنيميشن المقص */
    @keyframes scissors-swing {
        0% { transform: rotate(0deg); opacity: 0.1; }
        50% { transform: rotate(-10deg); opacity: 0.2; }
        100% { transform: rotate(0deg); opacity: 0.1; }
    }
    .scissors-container {
        position: fixed;
        bottom: 5%;
        left: 5%; 
        width: 150px;
        z-index: 0;
        pointer-events: none;
        animation: scissors-swing 6s infinite;
    }
</style>

<div class="scissors-container">
    <svg viewBox="0 0 512 512" fill="#D4AF37"><path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9z"/></svg>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 3. الثوابت والبيانات
# ============================================================
LOGO = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
WA_NUM = "201055901090"
PHONES = ["01055901090", "01055907095"]
ADDR = "الدقهلية - منية النصر - شارع البحر - أمام ستار مول - أعلى يونيكورن - الدور الخامس"
ADMIN_PWD = "9811"

VIDS = ["1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi"]

# ============================================================
# 4. السايدبار (الجهة اليسرى)
# ============================================================
with st.sidebar:
    st.image(LOGO)
    now = datetime.utcnow() + timedelta(hours=3)
    is_open = 13 <= now.hour < 22
    st.markdown(f"""<div style="background:{'rgba(40,167,69,0.1)' if is_open else 'rgba(220,53,69,0.1)'}; color:{'#28a745' if is_open else '#dc3545'}; padding:10px; border-radius:10px; text-align:center; font-weight:bold; border:1px solid;">{'🟢 نتشرف بكم الآن' if is_open else '🔴 السنتر مغلق'}</div>""", unsafe_allow_html=True)
    
    st.write(" ")
    # أزرار الاتصال والمشاركة
    st.markdown(f'<a href="tel:{PHONES[0]}" class="nav-btn" style="padding:10px; font-size:14px; background:#007bff !important; color:white !important;">📞 اتصلي بنا</a>', unsafe_allow_html=True)
    
    share_text = "شوفت بيوتي سنتر يارا ثروت وعجبني ادخلي شوفيه انتي كمان من اللينك ده"
    wa_share_url = f"https://wa.me/?text={urllib.parse.quote(share_text)}https://yara-tharwat.streamlit.app/"
    st.markdown(f'<a href="{wa_share_url}" class="nav-btn" style="padding:10px; font-size:14px; background:#25D366 !important; color:white !important;">🟢 مشاركة الموقع</a>', unsafe_allow_html=True)

    st.markdown(f"""<div style="padding:10px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; font-size:12px;"><b>📍 العنوان:</b><br>{ADDR}</div>""", unsafe_allow_html=True)

# ============================================================
# 5. الصفحات والمحتوى
# ============================================================
p = st.query_params.get("p", "home")

if p == "home":
    st.image(LOGO)
    st.markdown("<h2 style='text-align: center; color:#D4AF37;'>✨ بيوتي سنتر يارا ثروت ✨</h2>", unsafe_allow_html=True)
    menu = [
        ("📅 للحجز والاستفسار ✨💄", "booking"), 
        ("💰 قائمة الأسعار والعروض 💸", "prices"),
        ("🎥 صور لشغلنا 🎬", "gallery"), 
        ("⭐ آراء العملاء 💖", "reviews")
    ]
    for text, target in menu:
        st.markdown(f'<a href="./?p={target}" target="_self" class="nav-btn">{text}</a>', unsafe_allow_html=True)

elif p == "booking":
    st.markdown("### 📅 حجز موعد جديد ✨")
    # محتوى صفحة الحجز (الاسم، السن، إلخ)
    name = st.text_input("الاسم 👤")
    phone = st.text_input("رقم الموبايل 📱")
    if st.button("🚀 إرسال الطلب عبر واتساب"):
        if name and phone:
            msg = f"✨ حجز جديد ✨\nالاسم: {name}\nالهاتف: {phone}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url=https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}">', unsafe_allow_html=True)
    st.markdown('<a href="./?p=home" target="_self" style="color:#D4AF37;">⬅️ العودة للرئيسية</a>', unsafe_allow_html=True)

elif p == "gallery":
    st.markdown("### 🎥 صور لشغلنا 🎬")
    # إضافة الصور أو الفيديوهات هنا
    st.markdown('<a href="./?p=home" target="_self" style="color:#D4AF37;">⬅️ العودة للرئيسية</a>', unsafe_allow_html=True)

elif p == "prices":
    st.markdown("### 💰 قائمة الأسعار والعروض")
    st.info("سيتم عرض الأسعار هنا قريباً...")
    st.markdown('<a href="./?p=home" target="_self" style="color:#D4AF37;">⬅️ العودة للرئيسية</a>', unsafe_allow_html=True)

elif p == "reviews":
    st.markdown("### ⭐ آراء العملاء 💖")
    # نظام التعليقات
    st.markdown('<a href="./?p=home" target="_self" style="color:#D4AF37;">⬅️ العودة للرئيسية</a>', unsafe_allow_html=True)
