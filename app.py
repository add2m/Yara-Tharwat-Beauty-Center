import streamlit as st
import urllib.parse
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️", layout="centered")

# --- وظيفة الآراء (حذف تعليق محدد) ---
def handle_reviews(action="read", data=None):
    file_path = "reviews.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f: f.write("شغل ممتاز وتسلم إيديكم!|سارة")
    with open(file_path, "r", encoding="utf-8") as f:
        reviews = f.readlines()
    if action == "add" and data:
        with open(file_path, "a", encoding="utf-8") as f: f.write(f"\n{data}")
    elif action == "delete_one" and data is not None:
        if 0 <= data < len(reviews):
            reviews.pop(data)
            with open(file_path, "w", encoding="utf-8") as f: f.writelines(reviews)
    return reviews

# 2. البيانات والروابط
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
phone_2 = "01055907095"
ADMIN_PASSWORD = "9811" 

video_ids = ["1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi", 
             "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0", "1wlMl0Mi7COStjKh1d8B9JxWqj7Cf-fD1", 
             "1mGeV2CQrYyJCwZkSGBrB2rhMqta8BlOU"]

# 3. إدارة التنقل
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
        if st.form_submit_button("إرسال البيانات", use_container_width=True):
            if u_name and u_phone:
                msg = urllib.parse.quote(f"حجز جديد:\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}")
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center;">تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "prices":
    st.markdown("### 💰 قائمة الأسعار")
    # هنا تقدر تضيف جدول أو نصوص للأسعار
    st.markdown('''
    <div style="padding: 20px; border: 1px solid rgba(49, 51, 63, 0.2); border-radius: 10px; text-align: center;">
        <h4>قائمة الخدمات</h4>
        <p>مكياج - عناية بالبشرة - قص شعر - وأكثر</p>
        <p style="color: #D4AF37;">(يرجى التواصل معنا لمعرفة العروض الحالية)</p>
    </div>
    ''', unsafe_allow_html=True)
    if st.button("العودة للرئيسية"):
        st.query_params.clear()
        st.rerun()

elif current_page == "reviews":
    st.markdown("### ✨ رأي عملائنا")
    with st.expander("اضف رأيك هنا"):
        with st.form("review_form"):
            r_name = st.text_input("الاسم")
            r_text = st.text_area("رأيك في الخدمة")
            if st.form_submit_button("نشر الرأي"):
                if r_name and r_text:
                    handle_reviews("add", f"{r_text}|{r_name}")
                    st.success("تم النشر!")
                    st.rerun()
    all_revs = handle_reviews()
    for rev in reversed(all_revs):
        if "|" in rev:
            text, name = rev.strip().split("|")
            st.markdown(f'<div style="padding:15px; border:1px solid rgba(49,51,63,0.2); border-radius:10px; margin-bottom:10px;">"{text}"<br><small style="color:#D4AF37;">- {name}</small></div>', unsafe_allow_html=True)
    
    st.write("---")
    with st.expander("🔐 إدارة التعليقات"):
        pwd = st.text_input("أدخل كلمة المرور", type="password")
        if pwd == ADMIN_PASSWORD:
            for i, rev in enumerate(all_revs):
                if "|" in rev:
                    content, sender = rev.strip().split("|")
                    if st.button(f"🗑️ حذف تعليق: {sender}", key=f"del_{i}"):
                        handle_reviews("delete_one", i)
                        st.rerun()

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in video_ids:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)
        st.write("---")

else:
    # الصفحة الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h2>", unsafe_allow_html=True)
    
    st.markdown('<a href="./?p=booking" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49,51,63,0.2); border-radius:8px; text-align:center; margin-bottom:12px;">📅 للحجز</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=prices" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49,51,63,0.2); border-radius:8px; text-align:center; margin-bottom:12px;">💰 قائمة الأسعار</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=reviews" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49,51,63,0.2); border-radius:8px; text-align:center; margin-bottom:12px;">⭐ رأي عملائنا</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=gallery" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49,51,63,0.2); border-radius:8px; text-align:center; margin-bottom:12px;">✨ صور لشغلنا</div></a>', unsafe_allow_html=True)

# 5. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown(f'<div style="padding:10px; border:1px solid rgba(49,51,63,0.1); border-radius:5px;">📱 {phone_1}<br>📱 {phone_2}</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📍 العنوان\nمنيه النصر - شارع البحر\nأعلى يونيكورن الدور الخامس")
    st.write("---")
    st.caption("شكراً لاختياركم بيوتي سنتر يارا ثروت 💕")
