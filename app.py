import streamlit as st
import urllib.parse
from datetime import datetime, timedelta

# ============================================================
# 1. إعدادات الصفحة المتقدمة (Streamlit Page Config)
# ============================================================
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. التنسيق البرمجي المخصص (Professional CSS)
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

    /* السايدبار جهة اليمين (تعديل الطلب الأول) */
    [data-testid="stSidebar"] {
        position: fixed;
        right: 0 !important;
        left: auto !important;
        background-color: #080808 !important;
        border-right: 2px solid #D4AF37;
        z-index: 100;
    }
    
    section[data-testid="stSidebar"] > div {
        direction: rtl;
    }

    /* الخلفية الغامقة الملكية العميقة */
    .stApp {
        background: #000000;
        background-image: 
            radial-gradient(at 0% 100%, rgba(212, 175, 55, 0.08) 0, transparent 50%), 
            linear-gradient(180deg, #000000 0%, #050505 100%);
        background-attachment: fixed;
        color: #ffffff !important;
    }

    /* أنيميشن المقص الذهبي (جهة اليسار) */
    @keyframes scissors-swing {
        0% { transform: rotate(0deg) scale(1); opacity: 0.15; }
        50% { transform: rotate(-12deg) scale(1.05); opacity: 0.3; }
        100% { transform: rotate(0deg) scale(1); opacity: 0.15; }
    }

    .scissors-container {
        position: fixed;
        bottom: 5%;
        left: 5%; 
        width: 240px;
        height: 240px;
        z-index: 0;
        pointer-events: none;
        animation: scissors-swing 8s ease-in-out infinite;
    }

    /* تنسيق الأزرار الاحترافي (فتح في تاب جديد) */
    .nav-btn {
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 22px;
        text-align: center;
        margin-bottom: 15px;
        transition: all 0.3s ease;
        text-decoration: none !important;
        display: block;
        color: #D4AF37 !important;
        font-weight: bold;
        font-size: 1.15rem;
    }

    .nav-btn:hover {
        background: #D4AF37 !important;
        color: #000 !important;
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(212, 175, 55, 0.2);
    }

    /* تنسيق الحقول والمدخلات */
    .stTextInput input, .stTextArea textarea, .stSelectbox div {
        background-color: rgba(255,255,255,0.05) !important;
        color: white !important;
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
    }

    /* إخفاء شعارات Streamlit */
    #MainMenu, footer, header { visibility: hidden; }
</style>

<div class="scissors-container">
    <svg viewBox="0 0 512 512" fill="#D4AF37" xmlns="http://www.w3.org/2000/svg">
        <path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9zM152.7 465.1c-10.6 10.6-27.7 10.6-38.3 0s-10.6-27.7 0-38.3l103.5-103.5 38.3 38.3-103.5 103.5zm244-38.3c10.6 10.6 10.6 27.7 0 38.3s-27.7 10.6-38.3 0l-103.5-103.5 38.3-38.3 103.5 103.5z"/>
    </svg>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 3. الثوابت والبيانات الأساسية (Core Data)
# ============================================================
LOGO = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
WA_NUM = "201055901090"
PHONES = ["01055901090", "01055907095"]
ADDR = "الدقهلية - منية النصر - شارع البحر - أمام ستار مول - أعلى يونيكورن - الدور الخامس"

# الفيديوهات المطلوبة
VIDEOS = [
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
    st.image(LOGO, use_container_width=True)
    
    # حالة العمل الحالية
    now = datetime.utcnow() + timedelta(hours=3)
    is_open = 13 <= now.hour < 22
    st.markdown(f"""
        <div style="background:{'rgba(40,167,69,0.1)' if is_open else 'rgba(220,53,69,0.1)'}; 
        color:{'#28a745' if is_open else '#dc3545'}; padding:12px; 
        border-radius:10px; text-align:center; font-weight:bold; border:1px solid;">
            {'🟢 نستقبلكم الآن بكل حب' if is_open else '🔴 السنتر مغلق حالياً'}
        </div>
    """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # أزرار الاتصال (تاب جديد)
    st.markdown(f'<a href="tel:{PHONES[0]}" target="_blank" style="text-decoration:none;"><div style="background:#007bff; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📞 اتصلي بنا</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="http://googleusercontent.com/maps.google.com/7" target="_blank" style="text-decoration:none;"><div style="background:#6c757d; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📍 موقعنا بالخريطة</div></a>', unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="padding:15px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; background:rgba(255,255,255,0.02); font-size:14px;">
            <b>📱 أرقامنا:</b><br>{PHONES[0]}<br>{PHONES[1]}<br>
            <hr style="border-color:rgba(212,175,55,0.1);">
            <b>📍 العنوان:</b><br>{ADDR}
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# 5. إدارة المحتوى (Navigation & Pages)
# ============================================================
current_page = st.query_params.get("p", "home")

if current_page == "home":
    st.image(LOGO, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color:#D4AF37;'>✨ بيوتي سنتر يارا ثروت ✨</h2>", unsafe_allow_html=True)
    
    menu = [
        ("📅 للحجز والاستفسار", "booking"),
        ("💰 الأسعار وأقوى العروض", "prices"),
        ("🎥 معرض فيديوهاتنا", "gallery"),
        ("⭐ آراء الجميلات", "reviews")
    ]
    
    for text, target in menu:
        st.markdown(f'<a href="./?p={target}" target="_blank" class="nav-btn">{text}</a>', unsafe_allow_html=True)

elif current_page == "booking":
    st.markdown("<h3 style='text-align: center;'>🗓️ حجز موعد جديد</h3>", unsafe_allow_html=True)
    st.write("يرجى إدخال البيانات التالية لنتمكن من خدمتكِ:")
    
    col1, col2 = st.columns(2)
    with col1:
        u_name = st.text_input("الاسم بالكامل 👤")
        u_age = st.text_input("السن 🎂")
    with col2:
        u_phone = st.text_input("رقم الموبايل 📱")
        # تم إزالة "ميك أب" من الخيارات بناءً على طلبك
        u_service = st.selectbox("الخدمة المطلوبة ✨", ["شعر", "عناية بالبشرة", "حمام مغربي", "أخرى"])
    
    # إضافة خانة الملاحظات الجديدة
    u_notes = st.text_area("هل لديكِ أي ملاحظات إضافية؟ 📝 (اختياري)")
    
    if st.button("🚀 إرسال طلب الحجز عبر واتساب", use_container_width=True):
        if u_name and u_phone:
            full_msg = f"✨ طلب حجز جديد ✨\n━━━━━━━━━━━━\n👤 الاسم: {u_name}\n📱 الهاتف: {u_phone}\n🎂 السن: {u_age}\n💄 الخدمة: {u_service}\n📝 الملاحظات: {u_notes}"
            wa_link = f"https://wa.me/{WA_NUM}?text={urllib.parse.quote(full_msg)}"
            # التوجيه في تاب جديد
            st.markdown(f'<meta http-equiv="refresh" content="0; url={wa_link}">', unsafe_allow_html=True)
            st.success("جاري تحويلك لواتساب لتأكيد الحجز..")
        else:
            st.warning("رجاءً تأكدي من كتابة الاسم ورقم الهاتف.")

elif current_page == "gallery":
    st.markdown("<h3 style='text-align: center;'>🎥 معرض الفيديوهات</h3>", unsafe_allow_html=True)
    for v_id in VIDEOS:
        st.markdown(f'<iframe src="https://drive.google.com/file/d/{v_id}/preview" width="100%" height="450"></iframe>', unsafe_allow_html=True)
        st.write("---")

elif current_page == "prices":
    st.markdown("### 💰 الأسعار والعروض")
    st.info("انتظروا أقوى العروض الحصرية قريباً!")

elif current_page == "reviews":
    st.markdown("### ⭐ آراء عملائنا")
    st.success("المكان يجنن والشغل احترافي جداً، تسلم إيدك يا يارا! 😍")
