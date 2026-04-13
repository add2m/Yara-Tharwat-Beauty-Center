import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="بيوتي سنتر يارا ثروت", layout="centered")

# 2. روابط البيانات الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# 3. نظام التنقل (Navigation) في الشريط الجانبي أو الصفحة الرئيسية
# هنستخدم راديو بوتون بشكل شيك عشان نختار بين الأقسام
st.sidebar.image(logo_url, width=150)
choice = st.sidebar.radio("اختار من القائمة:", ["الصفحة الرئيسية", "حجز موعد", "قائمة الأسعار", "معرض الأعمال"])

# --- الصفحة الرئيسية ---
if choice == "الصفحة الرئيسية":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo_url, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>مرحباً بكم في بيوتي سنتر يارا ثروت</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>نحن هنا لنجعل جمالك يتألق. اختاري ما تبحثين عنه من القائمة الجانبية:</p>", unsafe_allow_html=True)
    
    # زراير توضيحية في الصفحة الرئيسية
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("📅 **حجز سريع**\n\nسجلي بياناتك وهنتواصل معاكي فوراً.")
    with c2:
        st.warning("💰 **الأسعار**\n\nتعرفي على خدماتنا وأسعارنا المميزة.")
    with c3:
        st.success("✨ **أعمالنا**\n\nشوفي صور وفيديوهات من شغلنا.")

# --- صفحة الحجز (نفس اللي عملناها قبل كدة) ---
elif choice == "حجز موعد":
    st.markdown("<h2 style='text-align: right;'>بيانات الحجز</h2>", unsafe_allow_html=True)
    with st.form("booking_form"):
        u_name = st.text_input("الاسم بالكامل")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان بالتفصيل")
        u_phone = st.text_input("رقم الهاتف")
        
        submit = st.form_submit_button("إرسال البيانات")
        
        if submit:
            if u_name and u_address and u_phone:
                raw_msg = f"حجز جديد من الموقع:\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}"
                encoded_msg = urllib.parse.quote(raw_msg)
                wa_link = f"https://wa.me/{whatsapp_num}?text={encoded_msg}"
                st.success("تمام! بياناتك جاهزة.")
                st.markdown(f'<a href="{wa_link}" target="_blank" style="background-color: #25D366; color: white; padding: 15px 25px; text-decoration: none; border-radius: 10px; font-weight: bold; display: block; text-align: center;">اضغط هنا لفتح واتساب وتأكيد الحجز</a>', unsafe_allow_html=True)
            else:
                st.error("من فضلك، املأ البيانات الأساسية.")

# --- صفحة الأسعار (فاضية مؤقتاً) ---
elif choice == "قائمة الأسعار":
    st.markdown("<h2 style='text-align: center;'>قائمة الخدمات والأسعار</h2>", unsafe_allow_html=True)
    st.info("سيتم إضافة قائمة الأسعار هنا قريباً...")
    # هنا هنحط الجدول لما تبعت الأسعار

# --- معرض الأعمال (فاضي مؤقتاً) ---
elif choice == "معرض الأعمال":
    st.markdown("<h2 style='text-align: center;'>معرض أعمالنا ✨</h2>", unsafe_allow_html=True)
    st.success("سيتم إضافة صور الشغل هنا قريباً...")
    # هنا هنحط الصور لما تبعتها

# 6. تذييل الصفحة الثابت
st.markdown("<br><hr><p style='text-align: center; color: gray;'>مركز منيه النصر - الدقهلية | ❤️ يارا ثروت</p>", unsafe_allow_html=True)
