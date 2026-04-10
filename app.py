import streamlit as st
import urllib.parse

st.set_page_config(page_title="بوابة خدمة العملاء", layout="centered")

# رابط اللوجو
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"

# عرض اللوجو والبيانات الجانبية
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

with st.sidebar:
    st.image(logo_url, width=150)
    st.title("تواصل معنا")
    st.markdown("---")
    st.markdown("### 📞 الأرقام:")
    st.write("01055901090")
    st.write("01055907095")
    st.markdown("---")
    st.markdown("### 📍 العنوان:")
    st.write("منيه النصر - شارع البحر - مقابل ستار مول - اعلي يونيكورن - الدور الخامس")

if 'confirmed' not in st.session_state:
    st.session_state.confirmed = False

if not st.session_state.confirmed:
    st.header("برجاء إدخال البيانات التالية")
    with st.form("user_form"):
        name = st.text_input("الاسم بالكامل")
        age = st.number_input("السن", min_value=1, max_value=100)
        address = st.text_input("العنوان")
        phone = st.text_input("رقم الهاتف")
        email = st.text_input("البريد الإلكتروني")
        submit = st.form_submit_button("إرسال")
        
        if submit:
            if name and address and phone and email:
                st.session_state.user_data = {
                    "الاسم": name, "السن": age, "العنوان": address, 
                    "رقم الهاتف": phone, "البريد الإلكتروني": email
                }
                st.session_state.review = True
            else:
                st.error("برجاء ملء جميع الخانات.")

    if 'review' in st.session_state and st.session_state.review:
        st.write("---")
        st.subheader("مراجعة بياناتك")
        for key, value in st.session_state.user_data.items():
            st.write(f"**{key}:** {value}")
        
        col1, col2 = st.columns(2)
        if col1.button("أيوه، البيانات صحيحة"):
            # تجهيز رسالة الواتساب
            msg = f"طلب جديد من الموقع:\n\nالاسم: {st.session_state.user_data['الاسم']}\nالسن: {st.session_state.user_data['السن']}\nالعنوان: {st.session_state.user_data['العنوان']}\nالهاتف: {st.session_state.user_data['رقم الهاتف']}\nالإيميل: {st.session_state.user_data['البريد الإلكتروني']}"
            msg_encoded = urllib.parse.quote(msg)
            
            # رقم الواتساب بتاعك (تم استخدام الرقم الأول)
            whatsapp_url = f"https://wa.me/201055901090?text={msg_encoded}"
            
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{whatsapp_url}\' />', unsafe_allow_html=True)
            st.session_state.confirmed = True
            st.rerun()
            
        if col2.button("لا، أريد التعديل"):
            st.session_state.review = False
            st.rerun()

else:
    st.success("تم تحويلك للواتساب لإرسال البيانات!")
    st.balloons()
    if st.button("تسجيل مستخدم جديد"):
        st.session_state.confirmed = False
        st.rerun()

st.markdown("<br><hr><p style='text-align: center; color: gray;'>❤️ شكراً لتعاملك معنا ❤️</p>", unsafe_allow_html=True)
