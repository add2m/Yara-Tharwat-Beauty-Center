import streamlit as st
import urllib.parse
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️", layout="centered")

# --- وظيفة الآراء (قاعدة بيانات بسيطة) ---
def handle_reviews(action="read", new_review=None):
    file_path = "reviews.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f: f.write("شغل ممتاز وتسلم إيديكم!|سارة")
    
    if action == "add" and new_review:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"\n{new_review}")
    
    elif action == "delete_all":
        with open(file_path, "w", encoding="utf-8") as f: f.write("") # يمسح المحتوى
            
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()

# 2. البيانات الأساسية
logo_url = "https://i.postimg.cc/43LvfZ27/Screenshot-2026-04-11-005540.png"
whatsapp_num = "201055901090"
phone_1 = "01055901090"
ADMIN_PASSWORD = "1234"  # <--- غير الباسوورد بتاعك من هنا

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
        if st.form_submit_button("إرسال البيانات", use_container_width=True):
            if u_name and u_phone:
                msg = urllib.parse.quote(f"حجز جديد:\nالاسم: {u_name}\nالسن: {u_age}\nالعنوان: {u_address}\nالهاتف: {u_phone}")
                st.markdown(f'<a href="https://wa.me/{whatsapp_num}?text={msg}" target="_blank" style="background-color: #25D366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center;">تأكيد عبر واتساب</a>', unsafe_allow_html=True)

elif current_page == "reviews":
    st.markdown("### ✨ رأي عملائنا")
    
    with st.expander("اضف رأيك هنا"):
        with st.form("review_form"):
            r_name = st.text_input("الاسم")
            r_text = st.text_area("رأيك في الخدمة")
            if st.form_submit_button("نشر الرأي"):
                if r_name and r_text:
                    handle_reviews("add", f"{r_text}|{r_name}")
                    st.success("تم النشر بنجاح!")
                    st.rerun()

    # عرض الآراء
    reviews = handle_reviews()
    for rev in reversed(reviews):
        if "|" in rev:
            text, name = rev.strip().split("|")
            st.markdown(f'<div style="padding:15px; border:1px solid rgba(49,51,63,0.2); border-radius:10px; margin-bottom:10px;">"{text}"<br><small style="color:#D4AF37;">- {name}</small></div>', unsafe_allow_html=True)

    # --- لوحة التحكم السرية للمسح ---
    st.write("---")
    with st.expander("إدارة التعليقات (لصاحب الموقع فقط)"):
        pwd = st.text_input("أدخل كلمة المرور للمسح", type="password")
        if pwd == ADMIN_PASSWORD:
            if st.button("🗑️ مسح جميع الآراء"):
                handle_reviews("delete_all")
                st.warning("تم مسح جميع الآراء!")
                st.rerun()

elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    for vid in ["1eC2Vhnj9ON69lKyMPWtrXENQiDA8QnBL", "1w1PWV3eQaXAz1Cdz5WBJrtX3lDSi4hzi", "1SuxPy8-LsRE4iizxcR531sTXPeZdY-n0"]:
        st.components.v1.iframe(f"https://drive.google.com/file/d/{vid}/preview", height=480)
        st.write("---")

else:
    # الرئيسية
    st.image(logo_url, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>❤️اهلا بكم في بيوتي سنتر يارا ثروت❤️</h2>", unsafe_allow_html=True)
    st.markdown('<a href="./?p=booking" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49,51,63,0.2); border-radius:8px; text-align:center; margin-bottom:12px;">📅 للحجز</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=reviews" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49,51,63,0.2); border-radius:8px; text-align:center; margin-bottom:12px;">⭐ رأي عملائنا</div></a>', unsafe_allow_html=True)
    st.markdown('<a href="./?p=gallery" target="_blank" style="text-decoration:none;color:inherit;"><div style="padding:12px; border:1px solid rgba(49,51,63,0.2); border-radius:8px; text-align:center; margin-bottom:12px;">✨ صور لشغلنا</div></a>', unsafe_allow_html=True)

# 5. Sidebar
with st.sidebar:
    st.image(logo_url, width=150)
    st.markdown(f'<a href="tel:{phone_1}" style="text-decoration:none;"><div style="background-color:#007bff; color:white; padding:10px; border-radius:8px; text-align:center; margin-bottom:10px;">📞 اتصل بنا الآن</div></a>', unsafe_allow_html=True)
    st.markdown('<div style="padding:10px; border:1px solid rgba(49,51,63,0.1); border-radius:5px;">📱 01055901090<br>📱 01055907095</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📍 العنوان\nمنيه النصر - شارع البحر\nأعلى يونيكورن الدور الخامس")
