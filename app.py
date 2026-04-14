import streamlit as st
import urllib.parse
from datetime import datetime, timedelta

# ============================================================
# 1. إعدادات الصفحة المتقدمة (Streamlit Config)
# ============================================================
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. كود الـ CSS الاحترافي (Professional Dark Theme)
# ============================================================
st.markdown("""
<style>
    /* تحسين الخطوط والتنسيق العربي */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"], .stMarkdown {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* السايدبار جهة اليمين (تعديل ثابت) */
    [data-testid="stSidebar"] {
        position: fixed;
        right: 0 !important;
        left: auto !important;
        background-color: #0a0a0a !important;
        border-right: 2px solid #D4AF37;
        z-index: 100;
    }
    
    section[data-testid="stSidebar"] > div {
        direction: rtl;
    }

    /* الخلفية الغامقة الملكية (Deep Dark) */
    .stApp {
        background: #000000;
        background-image: 
            radial-gradient(at 0% 100%, rgba(212, 175, 55, 0.1) 0, transparent 50%), 
            linear-gradient(180deg, #000000 0%, #050505 100%);
        background-attachment: fixed;
        color: #ffffff !important;
    }

    /* أنيميشن المقص الذهبي (جهة اليسار) */
    @keyframes scissors-swing {
        0% { transform: rotate(0deg) scale(1); opacity: 0.15; }
        50% { transform: rotate(-15deg) scale(1.1); opacity: 0.3; }
        100% { transform: rotate(0deg) scale(1); opacity: 0.15; }
    }

    .scissors-container {
        position: fixed;
        bottom: 8%;
        left: 5%; 
        width: 260px;
        height: 260px;
        z-index: 0;
        pointer-events: none;
        animation: scissors-swing 8s ease-in-out infinite;
    }

    /* تنسيق الأزرار (فتح في نافذة جديدة) */
    .nav-button-custom {
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 22px;
        text-align: center;
        margin-bottom: 12px;
        transition: all 0.3s ease;
        text-decoration: none !important;
        display: block;
        color: #D4AF37 !important;
        font-weight: bold;
        font-size: 1.2rem;
    }

    .nav-button-custom:hover {
        background: #D4AF37 !important;
        color: #000 !important;
        transform: scale(1.02);
    }

    /* تحسين عرض الفيديوهات */
    iframe {
        border-radius: 15px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    /* إخفاء عناصر Streamlit غير الضرورية */
    #MainMenu, footer, header { visibility: hidden; }
</style>

<div class="scissors-container">
    <svg viewBox="0 0 512 512" fill="#D4AF37" xmlns="http://www.w3.org/2000/svg">
        <path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9zM152.7 465.1c-10.6 10.6-27.7 10.6-38.3 0s-10.6-27.7 0-38.3l103.5-103.5 38.3 38.3-103.5 103.5zm244-38.3c10.6 10.6 10.6 27.7 0 38.3s-27.7 10.6-38.3 0l-103.5-103.5 38.3-38.3 103.5 103.5z"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 3. الثوابت والبيانات (System Data)
# ============================================================
LOGO_URL = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
WHATSAPP = "201055901090"
PHONES = ["01055901090", "01055907095"]
MAPS = "http://googleusercontent.com/maps.google.com/6"
ADDRESS = "الدقهلية - منية النصر - شارع البحر - أمام ستار مول - أعلى يونيكورن - الدور الخامس"

# قائمة الفيديوهات الجديدة المطلوبة
VIDEOS_LIST = [
    "1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL",
    "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi",
    "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0",
    "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1",
    "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"
]

# ============================================================
# 4. السايدبار (جهة اليمين)
# ============================================================
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    
    # حالة العمل الحالية
    egypt_now = datetime.utcnow() + timedelta(hours=3)
    is_open = 13 <= egypt_now.hour < 22
    st.markdown(f"""
        <div style="background:{'rgba(40,167,69,0.1)' if is_open else 'rgba(220,53,69,0.1)'}; 
        color:{'#28a745' if is_open else '#dc3545'}; padding:12px; 
        border-radius:10px; text-align:center; font-weight:bold; border:1px solid;">
            {'🟢 نحن متاحون لخدمتكِ الآن' if is_open else '🔴 السنتر مغلق حالياً'}
        </div>
    """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # أزرار الاتصال واللوكيشن (تاب جديد)
    st.markdown(f'<a href="tel:{PHONES[0]}" target="_blank" style="text-decoration:none;"><div style="background:#007bff; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📞 اتصلي بنا</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{MAPS}" target="_blank" style="text-decoration:none;"><div style="background:#6c757d; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📍 موقعنا بالخريطة</div></a>', unsafe_allow_html=True)
    
    # تفاصيل الأرقام والعنوان
    st.markdown(f"""
        <div style="padding:15px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; background:rgba(255,255,255,0.02); font-size:14px;">
            <b>📱 أرقام التواصل:</b><br>{PHONES[0]}<br>{PHONES[1]}<br>
            <hr style="border-color:rgba(212,175,55,0.1);">
            <b>📍 العنوان:</b><br>{ADDRESS}
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# 5. محتوى الصفحات (Navigation & Content)
# ============================================================
current_p = st.query_params.get("p", "home")

if current_p == "home":
    st.image(LOGO_URL, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color:#D4AF37;'>✨ بيوتي سنتر يارا ثروت ✨</h2>", unsafe_allow_html=True)
    
    # أزرار التنقل الرئيسية
    menu = [
        ("📅 للحجز والاستفسار", "booking"),
        ("💰 الأسعار وأقوى العروض", "prices"),
        ("🎥 معرض فيديوهاتنا", "gallery"),
        ("⭐ آراء الجميلات", "reviews")
    ]
    
    st.write("<br>", unsafe_allow_html=True)
    for text, target in menu:
        # الفتح في نافذة جديدة كما هو مطلوب
        st.markdown(f'<a href="./?p={target}" target="_blank" class="nav-button-custom">{text}</a>', unsafe_allow_html=True)

elif current_p == "gallery":
    st.markdown("<h3 style='text-align: center;'>🎥 معرض فيديوهات السنتر</h3>", unsafe_allow_html=True)
    st.write("شاهدي أحدث أعمالنا من الفيديوهات المتميزة:")
    
    # عرض الفيديوهات الجديدة باستخدام IDs المطلوبة
    for vid_id in VIDEOS_LIST:
        video_embed_url = f"https://drive.google.com/file/d/{vid_id}/preview"
        st.markdown(f"""
            <div style="margin-bottom:20px;">
                <iframe src="{video_embed_url}" width="100%" height="450" allow="autoplay"></iframe>
            </div>
        """, unsafe_allow_html=True)
        st.write("---")

elif current_p == "booking":
    st.markdown("### 📅 حجز موعد جديد")
    st.write("يرجى ملء البيانات التالية:")
    
    col1, col2 = st.columns(2)
    with col1:
        u_name = st.text_input("الاسم")
        u_age = st.text_input("السن")
    with col2:
        u_phone = st.text_input("الموبايل")
        u_service = st.selectbox("الخدمة", ["ميك أب", "شعر", "عناية", "أخرى"])
    
    if st.button("🚀 إرسال الطلب عبر واتساب", use_container_width=True):
        if u_name and u_phone:
            full_msg = f"✨ طلب حجز ✨\nالاسم: {u_name}\nالهاتف: {u_phone}\nالسن: {u_age}\nالخدمة: {u_service}"
            wa_link = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(full_msg)}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url={wa_link}">', unsafe_allow_html=True)
            st.success("جاري تحويلك لواتساب...")

elif current_p == "prices":
    st.markdown("### 💰 قائمة الأسعار")
    st.info("سيتم إضافة أقوى العروض هنا قريباً!")

elif current_p == "reviews":
    st.markdown("### ⭐ آراء عملائنا")
    st.success("أحسن مكان في منية النصر بجد، معاملة وشغل فوق الوصف! 😍")
    st.success("تسلم إيدك يا يارا، الميك أب كان روعة وكل الناس سألتني عليه. ❤️")
