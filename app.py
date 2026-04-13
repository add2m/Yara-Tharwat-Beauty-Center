elif current_page == "gallery":
    st.markdown("### ✨ فيديوهات من شغلنا")
    
    # الحصول على رقم الفيديو الحالي من الرابط، ولو مش موجود نبدأ بأول واحد (0)
    video_index = int(query_params.get("vid", 0))
    
    # عرض الفيديو الحالي فقط
    if video_index < len(video_ids):
        st.components.v1.iframe(f"https://drive.google.com/file/d/{video_ids[video_index]}/preview", height=480)
        
        # أزرار التنقل بين الفيديوهات
        col1, col2 = st.columns(2)
        with col1:
            if video_index < len(video_ids) - 1:
                if st.button("الفيديو التالي ⬅️"):
                    st.query_params.update(p="gallery", vid=video_index + 1)
                    st.rerun()
        with col2:
            if video_index > 0:
                if st.button("➡️ الفيديو السابق"):
                    st.query_params.update(p="gallery", vid=video_index - 1)
                    st.rerun()
    
    st.write("---")
    if st.button("العودة للرئيسية"):
        st.query_params.clear()
        st.rerun()
