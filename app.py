import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️", layout="centered")

# 2. البيانات والروابط الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
phone_2 = "01055907095"

video_ids = [
    "1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL",
    "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi",
    "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0",
    "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1",
    "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"
]

# 3. إدارة التنقل
query_params = st.query_params
current_page = query_params.get("p", "home")

# 4. محتوى الصفحات
if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان")
        u_phone = st.text_input("رقم الهاتف")
        submit = st.form_submit_button("إرسال البيانات", use_container_width=True)
        if submit and u_name and u_phone:
            msg_text = f"حجز جديد:\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}"
            msg = urllib.parse.quote(msg_text)
            st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center;">تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "prices":
    st.markdown("### 💰 قائمة الأسعار")
    st.info("سيتم إضافة قائمة الأسعار التفصيلية هنا قريباً")

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in video_ids:
        video_embed_url = f"https://drive.google.com/file/d/{vid}/preview"
        st.components.v1.iframe(video_embed_url, height=480)
        st.write("---")

else:
    # الصفحة الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h2>", unsafe_allow_html=True)
    
    st.markdown('<a href="./?p=booking" target="_blank" style="text-decoration: none; color: inherit;"><div style="padding: 12px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px;">📅 للحجز</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=prices" target="_blank" style="text-decoration: none; color: inherit;"><div style="padding: 12px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px;">💰 قائمة الأسعار</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=gallery" target="_blank" style="text-decoration: none; color: inherit;"><div style="padding: 12px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px;">✨ صور لشغلنا</div></a>', unsafe_allow_html=True)

# 5. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    
    st.markdown("### 📞 أرقام التواصل")
    # زر الاتصال المباشر
    st.markdown(f'''
        <a href="tel:{phone_1}" style="text-decoration: none;">
            <div style="background-color: #007bff; color: white; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 10px;">
                📞 اتصل بنا الآن
            </div>
        </a>
    ''', unsafe_allow_html=True)
    
    # الأرقام والعنوان بتصميم شفاف ومنسق
    st.markdown(f'''
        <div style="padding: 10px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 5px;">
            📱 {phone_1}<br>
            📱 {phone_2}
        </div>
        <br>
        <div style="padding: 10px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 5px;">
            <b>📍 العنوان:</b><br>
            الدقهليه - منيه النصر - شارع البحر<br>
            (أعلى يونيكورن - الدور الخامس)
        </div>
    ''', unsafe_allow_html=True)
    
    st.write("---")
    st.caption("شكراً لاختياركم بيوتي سنتر يارا ثروت 💕")
