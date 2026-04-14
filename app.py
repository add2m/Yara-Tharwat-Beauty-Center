import streamlit as st
import urllib.parse
import os
import time
from datetime import datetime, timedelta

# ============================================================
# 1. إعدادات الصفحة المتقدمة (Streamlit Configuration)
# ============================================================
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. كود الـ CSS الاحترافي (Advanced UI/UX)
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"], .stMarkdown {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* السايدبار جهة اليمين */
    [data-testid="stSidebar"] {
        position: fixed;
        right: 0 !important;
        left: auto !important;
        background-color: #0d0d0d !important;
        border-right: 2px solid #D4AF37;
        z-index: 100;
    }
    
    section[data-testid="stSidebar"] > div { direction: rtl; }

    /* الخلفية الغامقة الملكية */
    .stApp {
        background: #050505;
        background-image: 
            radial-gradient(at 0% 100%, rgba(212, 175, 55, 0.12) 0, transparent 50%), 
            linear-gradient(180deg, #000000 0%, #080808 100%);
        background-attachment: fixed;
        color: #ffffff !important;
    }

    /* أنيميشن المقص الذهبي (جهة اليسار) */
    @keyframes scissors-float {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.2; }
        50% { transform: translateY(-20px) rotate(-10deg); opacity: 0.4; }
        100% { transform: translateY(0px) rotate(0deg); opacity: 0.2; }
    }

    .scissors-art {
        position: fixed;
        bottom: 5%;
        left: 3%; 
        width: 280px;
        height: 280px;
        z-index: 0;
        pointer-events: none;
        animation: scissors-float 7s ease-in-out infinite;
    }

    /* تنسيق الأزرار (فتح في تاب جديد) */
    .nav-link-custom {
        border: 1px solid rgba(212, 175, 55, 0.5) !important;
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(12px);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
        transition: 0.4s all;
        text-decoration: none !important;
        display: block;
        color: #D4AF37 !important;
        font-weight: bold;
        font-size: 1.1rem;
    }

    .nav-link-custom:hover {
        background: #D4AF37 !important;
        color: #000 !important;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
    }

    /* إخفاء شعارات Streamlit */
    #MainMenu, footer, header { visibility: hidden; }
</style>

<div class="scissors-art">
    <svg viewBox="0 0 512 512" fill="#D4AF37" xmlns="http://www.w3.org/2000/svg">
        <path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9zM152.7 465.1c-10.6 10.6-27.7 10.6-38.3 0s-10.6-27.7 0-38.3l103.5-103.5 38.3 38.3-103.5 103.5zm244-38.3c10.6 10.6 10.6 27.7 0 38.3s-27.7 10.6-38.3 0l-103.5-103.5 38.3-38.3 103.5 103.5z"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 3. البيانات والثوابت (Business Data)
# ============================================================
LOGO = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
WA_NUM = "201055901090"
PHONES = ["01055901090", "01055907095"]
MAP_URL = "http://googleusercontent.com/maps.google.com/5"
ADDR = "الدقهلية - منية النصر - شارع البحر - أمام ستار مول - أعلى يونيكورن - الدور الخامس"

# قائمة الفيديوهات (التي قمت بإرسالها)
VIDEO_URLS = [
    "https://www.w3schools.com/html/mov_bbb.mp4", # فيديو تجريبي 1 (استبدله بروابط فيديوهاتك)
    "https://www.w3schools.com/html/movie.mp4"    # فيديو تجريبي 2 (استبدله بروابط فيديوهاتك)
]

# ============================================================
# 4. السايدبار (جهة اليمين - الأرقام واللوكيشن)
# ============================================================
with st.sidebar:
    st.image(LOGO, use_container_width=True)
    
    # الحالة المباشرة
    now = datetime.utcnow() + timedelta(hours=3)
    is_open = 13 <= now.hour < 22
    st.markdown(f"""
        <div style="background:{'rgba(40,167,69,0.1)' if is_open else 'rgba(220,53,69,0.1)'}; 
        color:{'#28a745' if is_open else '#dc3545'}; padding:10px; border-radius:10px; 
        text-align:center; font-weight:bold; border:1px solid;">
            {'🟢 متاحون لخدمتكم الآن' if is_open else '🔴 السنتر مغلق حالياً'}
        </div>
    """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # أزرار الاتصال (تفتح في تاب جديد)
    st.markdown(f'<a href="tel:{PHONES[0]}" target="_blank" style="text-decoration:none;"><div style="background:#007bff; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📞 اتصلي بنا</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{MAP_URL}" target="_blank" style="text-decoration:none;"><div style="background:#6c757d; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📍 موقعنا بالخريطة</div></a>', unsafe_allow_html=True)
    
    # تفاصيل الأرقام والعنوان
    st.markdown(f"""
        <div style="padding:15px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; background:rgba(255,255,255,0.03); font-size:14px;">
            <b>📱 الأرقام:</b><br>{PHONES[0]}<br>{PHONES[1]}<br>
            <hr style="margin:10px 0; border-color:rgba(212,175,55,0.1);">
            <b>📍 العنوان:</b><br>{ADDR}
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# 5. إدارة المحتوى (Main Content & Navigation)
# ============================================================
p = st.query_params.get("p", "home")

if p == "home":
    st.image(LOGO, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color:#D4AF37;'>✨ بيوتي سنتر يارا ثروت ✨</h2>", unsafe_allow_html=True)
    
    # قائمة الأزرار الرئيسية
    links = [
        ("📅 للحجز والاستفسار", "booking"),
        ("💰 قائمة الأسعار والعروض", "prices"),
        ("🎥 فيديو لشغلنا (المعرض)", "gallery"),
        ("⭐ رأي عملائنا", "reviews")
    ]
    
    for text, target in links:
        st.markdown(f'<a href="./?p={target}" target="_blank" class="nav-link-custom">{text}</a>', unsafe_allow_html=True)

elif p == "booking":
    st.markdown("### 📅 طلب حجز سريع")
    # تصميم انسيابي بدون فواصل
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("الاسم")
        age = st.text_input("السن")
    with c2:
        phone = st.text_input("رقم الموبايل")
        service = st.selectbox("الخدمة", ["ميك أب", "بروتين", "بشرة", "أخرى"])
    
    if st.button("إرسال الطلب عبر واتساب", use_container_width=True):
        if name and phone:
            msg = f"✨ حجز جديد ✨\nالاسم: {name}\nالهاتف: {phone}\nالسن: {age}\nالخدمة: {service}"
            link = f"https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={link}">', unsafe_allow_html=True)
            st.success("تم التوجيه للواتساب..")

elif p == "gallery":
    st.markdown("### 🎥 معرض فيديوهاتنا")
    st.write("استمتعي بمشاهدة أحدث أعمالنا:")
    
    # عرض الفيديوهات ورا بعضها بتنسيق فخم
    for i, vid in enumerate(VIDEO_URLS):
        with st.container():
            st.video(vid)
            st.markdown(f"<p style='text-align:center; color:#D4AF37;'>فيديو رقم {i+1} ✨</p>", unsafe_allow_html=True)
            st.write("---")

elif p == "prices":
    st.markdown("### 💰 الأسعار والعروض")
    st.info("انتظروا أقوى عروض الموسم قريباً جداً..")

elif p == "reviews":
    st.markdown("### ⭐ آراء الجميلات")
    st.success("المكان يجنن والشغل احترافي جداً ❤️")
    st.success("تسلم إيدك يا يارا، ميك أب روعة بجد!")
