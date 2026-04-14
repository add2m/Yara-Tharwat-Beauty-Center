import streamlit as st
import urllib.parse
import os
from datetime import datetime, timedelta

# ============================================================
# 1. إعدادات الصفحة والوظائف المتقدمة
# ============================================================
st.set_page_config(
    page_title="✨ بيوتي سنتر يارا ثروت ✨",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
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
# 2. كود الـ CSS الملكي (تم تعديل السايدبار ليكون في اليسار)
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"], .stMarkdown {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* السايدبار جهة اليسار (الوضع الافتراضي لستريمليت) */
    [data-testid="stSidebar"] {
        background-color: #080808 !important;
        border-left: 2px solid #D4AF37;
        z-index: 100;
    }
    
    /* ضبط اتجاه النصوص داخل السايدبار */
    section[data-testid="stSidebar"] > div { direction: rtl; }

    .stApp {
        background: #000000;
        background-image: 
            radial-gradient(at 0% 100%, rgba(212, 175, 55, 0.1) 0, transparent 50%), 
            linear-gradient(180deg, #000000 0%, #050505 100%);
        background-attachment: fixed;
        color: #ffffff !important;
    }

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
        transform: translateY(-3px);
    }

    .review-card {
        padding: 15px;
        border: 1px solid rgba(212, 175, 55, 0.2);
        border-radius: 12px;
        margin-bottom: 12px;
        background: rgba(255,255,255,0.02);
    }

    #MainMenu, footer, header { visibility: hidden; }
</style>

<div class="scissors-container">
    <svg viewBox="0 0 512 512" fill="#D4AF37" xmlns="http://www.w3.org/2000/svg">
        <path d="M490.5 35.8c-18.7-18.7-49.1-18.7-67.9 0L256 202.5 89.4 35.8c-18.7-18.7-49.1-18.7-67.9 0-18.7 18.7-18.7 49.1 0 67.9L188.2 270.3l-142.1 142c-29.4 29.4-29.4 77 0 106.4 29.4 29.4 77 29.4 106.4 0l103.5-103.5 103.5 103.5c29.4 29.4 77 29.4 106.4 0 29.4-29.4 29.4-77 0-106.4l-142.1-142 166.7-166.6c18.7-18.8 18.7-49.2 0-67.9zM152.7 465.1c-10.6 10.6-27.7 10.6-38.3 0s-10.6-27.7 0-38.3l103.5-103.5 38.3 38.3-103.5 103.5zm244-38.3c10.6 10.6 10.6 27.7 0 38.3s-27.7 10.6-38.3 0l-103.5-103.5 38.3-38.3 103.5 103.5z"/>
    </svg>
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

VIDS = [
    "1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi",
    "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0", "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1",
    "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"
]

# ============================================================
# 4. السايدبار (في جهة اليسار)
# ============================================================
with st.sidebar:
    st.image(LOGO, use_container_width=True)
    now = datetime.utcnow() + timedelta(hours=3)
    is_open = 13 <= now.hour < 22
    st.markdown(f"""<div style="background:{'rgba(40,167,69,0.1)' if is_open else 'rgba(220,53,69,0.1)'}; color:{'#28a745' if is_open else '#dc3545'}; padding:12px; border-radius:10px; text-align:center; font-weight:bold; border:1px solid;">{'🟢 نتشرف بكم الآن' if is_open else '🔴 السنتر مغلق'}</div>""", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    # أزرار الاتصال
    st.markdown(f'<a href="tel:{PHONES[0]}" target="_blank" style="text-decoration:none;"><div style="background:#007bff; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">📞 اتصلي بنا</div></a>', unsafe_allow_html=True)
    
    # زر المشاركة عبر الواتساب
    share_text = "شوفت بيوتي سنتر يارا ثروت وعجبني ادخلي شوفيه انتي كمان من اللينك ده"
    wa_share_url = f"https://wa.me/?text={urllib.parse.quote(share_text)}https://yara-tharwat.streamlit.app/"
    
    st.markdown(f"""
        <a href="{wa_share_url}" target="_blank" style="text-decoration:none;">
            <div style="background:#25D366; color:white; padding:12px; border-radius:10px; text-align:center; margin-bottom:10px; font-weight:bold;">
                🟢 مشاركة الموقع عبر واتساب
            </div>
        </a>
    """, unsafe_allow_html=True)

    st.markdown(f"""<div style="padding:15px; border:1px solid rgba(212,175,55,0.2); border-radius:10px; background:rgba(255,255,255,0.02); font-size:14px;"><b>📱 أرقامنا:</b><br>{PHONES[0]}<br>{PHONES[1]}<br><hr><b>📍 العنوان:</b><br>{ADDR}</div>""", unsafe_allow_html=True)

# ============================================================
# 5. الصفحات والمحتوى
# ============================================================
p = st.query_params.get("p", "home")

if p == "home":
    st.image(LOGO, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color:#D4AF37;'>✨ بيوتي سنتر يارا ثروت ✨</h2>", unsafe_allow_html=True)
    menu = [
        ("📅 للحجز والاستفسار ✨💄", "booking"), 
        ("💰 قائمة الأسعار والعروض 💸", "prices"),
        ("🎥 صور لشغلنا 🎬", "gallery"), 
        ("⭐ آراء العملاء 💖", "reviews")
    ]
    for text, target in menu:
        st.markdown(f'<a href="./?p={target}" target="_blank" class="nav-btn">{text}</a>', unsafe_allow_html=True)

elif p == "booking":
    st.markdown("### 📅 حجز موعد جديد ✨")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("الاسم 👤")
        age = st.text_input("السن 🎂")
    with col2:
        phone = st.text_input("رقم الموبايل 📱")
        service = st.selectbox("الخدمة المطلوبة ✨", ["شعر", "بشرة", "أخرى"])
    notes = st.text_area("ملاحظات إضافية 📝")
    if st.button("🚀 إرسال الطلب عبر واتساب", use_container_width=True):
        if name and phone:
            msg = f"✨ حجز جديد ✨\n-----------------------------------------------------\nالاسم: {name}\nالسن: {age}\nالهاتف: {phone}\nالخدمة: {service}\nملاحظات: {notes}"
            st.markdown(f'<meta http-equiv="refresh" content="0; url=https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}">', unsafe_allow_html=True)

elif p == "prices":
    st.markdown("### 💰 قائمة الأسعار والعروض 💸")
    st.info("سيتم عرض الاسعار هنا قريبا....")

elif p == "gallery":
    st.markdown("### 🎥 صور لشغلنا 🎬")
    for v_id in VIDS:
        st.markdown(f'<iframe src="https://drive.google.com/file/d/{v_id}/preview" width="100%" height="450"></iframe>', unsafe_allow_html=True)
        st.write("---")

elif p == "reviews":
    st.markdown("### ⭐ آراء العملاء 💖")
    with st.expander("اضف رأيك هنا ✨"):
        with st.form("review_form"):
            r_name = st.text_input("الاسم")
            r_text = st.text_area("رأيك")
            if st.form_submit_button("نشر"):
                if r_name and r_text:
                    handle_reviews("add", f"{r_text}|{r_name}")
                    st.success("تم نشر رأيك بنجاح!")
                    st.rerun()
    all_revs = handle_reviews()
    for rev in reversed(all_revs):
        if "|" in rev:
            try:
                t, n = rev.strip().split("|")
                st.markdown(f'<div class="review-card">"{t}"<br><small style="color:#D4AF37;">- {n}</small></div>', unsafe_allow_html=True)
            except: continue
    st.write("---")
    with st.expander("🔐 إدارة التعليقات"):
        pwd = st.text_input("كلمة المرور", type="password")
        if pwd == ADMIN_PWD:
            for i, rev in enumerate(all_revs):
                if "|" in rev:
                    content, sender = rev.strip().split("|")
                    if st.button(f"🗑️ حذف تعليق: {sender}", key=f"del_{i}"):
                        handle_reviews("delete_one", i)
                        st.rerun()
