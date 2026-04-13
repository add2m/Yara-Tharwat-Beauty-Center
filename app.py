import streamlit as st
import urllib.parse
import re

# 1. إعدادات الصفحة
st.set_page_config(page_title="❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️", layout="centered")

# 2. الروابط الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"

# فيديوهات درايف اللي بعتها
video_links = [
    "https://drive.google.com/file/d/1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL/view?usp=sharing",
    "https://drive.google.com/file/d/1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi/view?usp=sharing",
    "https://drive.google.com/file/d/1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0/view?usp=sharing",
    "https://drive.google.com/file/d/1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1/view?usp=sharing",
    "https://drive.google.com/file/d/1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU/view?usp=sharing"
]

# وظيفة لتحويل رابط درايف لرابط تشغيل مباشر
def get_direct_link(url):
    file_id = re.search(r'/d/([^/]+)', url)
    if file_id:
        return f"https://drive.google.com/uc?export=download&id={file_id.group(1)}"
    return url

# 3. قراءة التوجه من الرابط (Query Params)
query_params = st.query_params
current_page = query_params.get("p", "home")

# 4. محتوى الصفحات
# ------------------------------

if current_page == "booking":
    st.markdown("### 📅 بيانات الحجز")
    with st.form("booking_form"):
        u_name = st.text_input("الاسم")
        u_age = st.text_input("السن")
        u_address = st.text_input("العنوان")
        u_phone = st.text_input("رقم الهاتف")
        submit = st.form_submit_button("إرسال البيانات", use_container_width=True)
        if submit and u_name and u_phone:
            msg = urllib.parse.quote(f"حجز جديد:\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}")
            st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center;">تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "prices":
    st.markdown("### 💰 قائمة الأسعار")
    st.info("قريباً سيتم عرض الأسعار هنا")

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for link in video_links:
        direct_link = get_direct_link(link)
        st.video(direct_link)
        st.write("---")

else:
    # الصفحة الرئيسية (أزرار شفافة)
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h2>", unsafe_allow_html=True)
    
    st.markdown('<a href="./?p=booking" target="_blank" style="text-decoration: none; color: inherit;"><div style="padding: 12px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px; font-size: 16px;">📅 للحجز</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=prices" target="_blank" style="text-decoration: none; color: inherit;"><div style="padding: 12px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px; font-size: 16px;">💰 قائمة الأسعار</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=gallery" target="_blank" style="text-decoration: none; color: inherit;"><div style="padding: 12px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 8px; text-align: center; margin-bottom: 12px; font-size: 16px;">✨ صور لشغلنا</div></a>', unsafe_allow_html=True)

# تذييل ثابت
st.write("---")
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown("### 📞 للتواصل\n01055901090\n\n01055907095")
    st.markdown("### 📍 العنوان\nالدقهليه - منيه النصر - شارع البحر\nمقابل استار مول - الدور الخامس")
    st.caption("شكرا لاختياركم بيوتي سنتر يارا ثروت💕")
