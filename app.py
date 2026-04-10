import streamlit as st

st.set_page_config(page_title="بوابة خدمة العملاء", layout="centered")

image_url = "https://raw.githubusercontent.com/add2m/my-first-app/master/logo.png"

try:
    st.image(image_url, width=300)
except:
    pass

st.title("أهلاً بك في خدمتنا")

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
            st.session_state.confirmed = True
            st.rerun()
        if col2.button("لا، أريد التعديل"):
            st.session_state.review = False
            st.rerun()

else:
    st.success("تم حفظ البيانات بنجاح!")
    st.subheader("إزاي نقدر نساعدك النهاردة؟")
    
    choice = st.radio("اختر من الخيارات التالية:", ["شراء", "تواصل مع خدمة العملاء"])
    
    if st.button("تأكيد الاختيار"):
        if choice == "شراء":
            st.info("شكراً لك! سيتم التواصل معك خلال لحظات.")
            st.balloons() 
        else:
            st.info("سيتم التواصل معك خلال 24 ساعة.")

    if st.button("البدء من جديد"):
        st.session_state.confirmed = False
        st.rerun()

st.write("\n" * 3) 
st.markdown("<h3 style='text-align: center;'>❤️شكراً لتعاملك معنا❤️</h3>", unsafe_allow_html=True)
