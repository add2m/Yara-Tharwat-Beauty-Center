import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# 3. عرض اللوجو والجملة الترحيبية
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

st.markdown("<h3 style='text-align: center; color: #D4AF37;'>❤️ اهلا بكم في بيوتي سنتر يارا ثروت ❤️</h3>", unsafe_allow_html=True)

# 4. الشريط الجانبي (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل")
    st.info("01055901090\n\n01055907095")
    
    st.markdown("### 📍 العنوان")
    st.success("منيه النصر - الدقهلية\n\nشارع البحر - مقابل ستار مول\n\nأعلى يونيكورن - الدور الخامس")

# 5. فورم إدخال البيانات
st.markdown("<h2 style='text-align: right;'>بيانات الحجز</h2>", unsafe_allow_html=True)

with st.form("booking_form"):
    u_name = st.text_input("الاسم بالكامل")
    u_age = st.text_input("السن")
    u_address = st.text_input("العنوان بالتفصيل")
    u_phone = st.text_input("رقم الهاتف")
    
    submit = st.form_submit_button("إرسال البيانات")
    
    if submit:
        if u_name and u_address and u_phone:
            # تعديل تنسيق الرسالة عشان تظهر مظبوطة في واتساب
            # شيلنا النقط والرموز اللي بتبوظ الترتيب العربي
            raw_msg = (
                f"حجز جديد من الموقع\n"
                f"الاسم: {u_name}\n"
                f"السن: {u_age}\n"
                f"العنوان: {u_address}\n"
                f"الهاتف: {u_phone}"
            )
            encoded_msg = urllib.parse.quote(raw_msg)
            wa_link = f"https://wa.me/{whatsapp_num}?text={encoded_msg}"
            
            st.success("تمام! بياناتك جاهزة.")
            
            # زرار الواتساب
            st.markdown(f'<a href="{wa_link}" target="_blank" style="background-color: #25D366; color: white; padding: 15px 25px; text-decoration: none; border-radius: 10px; font-weight: bold; display: block; text-align: center;">اضغط هنا لفتح واتساب وتأكيد الحجز</a>', unsafe_allow_html=True)
        else:
            st.error("من فضلك، املأ الاسم والعنوان والتليفون عشان الحجز يكمل.")

# 6. تذييل الصفحة
st.markdown("<br><hr><p style='text-align: center; color: gray;'>❤️ شكراً لاختياركم بيوتي سنتر يارا ثروت ❤️</p>", unsafe_allow_html=True)
