import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# 3. إدارة التنقل (Session State)
# ده الجزء اللي بيخلي البرنامج يعرف إحنا في أنهي صفحة
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def change_page(page_name):
    st.session_state.page = page_name

# 4. الشريط الجانبي الثابت (العنوان والتليفون فقط)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل")
    st.info("01055901090\n\n01055907095")
    st.markdown("### 📍 العنوان")
    st.success("منيه النصر - الدقهلية\n\nشارع البحر - مقابل ستار مول\n\nأعلى يونيكورن - الدور الخامس")
    
    # زرار للرجوع للرئيسية من الجنب برضه احتياطي
    if st.button("🏠 العودة للرئيسية"):
        change_page('home')

# --- محتوى الصفحات ---

# أ. الصفحة الرئيسية (الواجهة اللي فيها الأزرار)
if st.session_state.page == 'home':
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo_url, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>مرحباً بكم في بيوتي سنتر يارا ثروت</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>اختار القسم اللي حابب تدخله:</p>", unsafe_allow_html=True)
    
    # إنشاء الأزرار الكبيرة
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        if st.button("📅 احجز الآن", use_container_width=True):
            change_page('booking')
            
    with col_b:
        if st.button("💰 قائمة الأسعار", use_container_width=True):
            change_page('prices')
            
    with col_c:
        if st.button("✨ معرض الأعمال", use_container_width=True):
            change_page('gallery')

# ب. صفحة الحجز
elif st.session_state.page == 'booking':
    st.markdown("<h2 style='text-align: right;'>بيانات الحجز</h2>", unsafe_allow_html=True)
    with st.form("booking_form"):
        u_name = st.text_input("الاسم بالكامل")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان بالتفصيل")
        u_phone = st.text_input("رقم الهاتف")
        submit = st.form_submit_button("إرسال البيانات")
        
        if submit:
            if u_name and u_address and u_phone:
                raw_msg = f"حجز جديد من الموقع\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}"
                encoded_msg = urllib.parse.quote(raw_msg)
                wa_link = f"https://wa.me/{whatsapp_num}?text={encoded_msg}"
                st.success("تمام! بياناتك جاهزة.")
                st.markdown(f'<a href="{wa_link}" target="_blank" style="background-color: #25D366; color: white; padding: 15px 25px; text-decoration: none; border-radius: 10px; font-weight: bold; display: block; text-align: center;">اضغط هنا لفتح واتساب وتأكيد الحجز</a>', unsafe_allow_html=True)

# ج. صفحة الأسعار (مكان فاضي للصور)
elif st.session_state.page == 'prices':
    st.button("⬅️ رجوع", on_click=change_page, args=('home',))
    st.header("💰 قائمة الأسعار")
    st.info("ابعت لي صور المنيو عشان نحطها هنا")

# د. صفحة المعرض (مكان فاضي للصور)
elif st.session_state.page == 'gallery':
    st.button("⬅️
