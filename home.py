import streamlit as st

# CSS Tùy chỉnh làm đẹp thẻ Card
st.markdown("""
<style>
    .portal-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        border: 1px solid #e0e0e0;
        border-left: 5px solid #1f77b4;
        margin-bottom: 10px;
        height: 120px;
    }
    .portal-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 8px;
    }
    .portal-desc {
        font-size: 0.9rem;
        color: #555555;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌟 Hệ Thống Ứng Dụng Học Tập & Quản Trị")
st.markdown("**Author:** Phát Phan - Network Engineer TAH")
st.divider()

# --- NHÓM EHOU ---
st.subheader("📚 Ngoại Ngữ - Đại học Mở Hà Nội (EHOU)")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class="portal-card"><div class="portal-title">Listening EHOU</div>
        <div class="portal-desc">Luyện kỹ năng nghe tiếng Anh qua các bài tập chuyên sâu.</div></div>""", unsafe_allow_html=True)
    if st.button("Truy cập ứng dụng 🚀", key="btn_listen", use_container_width=True):
        st.switch_page("listening.py")

with col2:
    st.markdown("""<div class="portal-card"><div class="portal-title">Lý thuyết Reading</div>
        <div class="portal-desc">Hệ thống lý thuyết đọc hiểu và phân tích ngữ pháp.</div></div>""", unsafe_allow_html=True)
    if st.button("Truy cập ứng dụng 🚀", key="btn_lythuyet", use_container_width=True):
        st.switch_page("lythuyet.py")

with col3:
    st.markdown("""<div class="portal-card"><div class="portal-title">Reading EHOU</div>
        <div class="portal-desc">Thực hành bài tập đọc hiểu sát với chương trình học.</div></div>""", unsafe_allow_html=True)
    if st.button("Truy cập ứng dụng 🚀", key="btn_read", use_container_width=True):
        st.switch_page("reading.py")

st.markdown("<br>", unsafe_allow_html=True)

# --- NHÓM TIẾNG TRUNG ---
st.subheader("🇨🇳 Tiếng Trung")
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""<div class="portal-card"><div class="portal-title">Chinese Learning</div>
        <div class="portal-desc">Hệ thống học từ vựng và ngữ pháp tiếng Trung cơ bản.</div></div>""", unsafe_allow_html=True)
    if st.button("Truy cập ứng dụng 🚀", key="btn_cn_learn", use_container_width=True):
        st.switch_page("chinese_learn.py")

with col5:
    st.markdown("""<div class="portal-card"><div class="portal-title">Chinese Writing</div>
        <div class="portal-desc">Luyện viết, nhận diện chữ Hán và thứ tự nét bút.</div></div>""", unsafe_allow_html=True)
    if st.button("Truy cập ứng dụng 🚀", key="btn_cn_write", use_container_width=True):
        st.switch_page("chinese_write.py")

st.markdown("<br>", unsafe_allow_html=True)

# --- NHÓM UIT ---
st.subheader("💻 Công Nghệ Thông Tin - Đại Học CNTT (UIT)")
col7, col8, col9 = st.columns(3)

with col7:
    st.markdown("""<div class="portal-card"><div class="portal-title">Dinh dưỡng Crawler</div>
        <div class="portal-desc">Thu thập, phân tích và thống kê dữ liệu dinh dưỡng tự động.</div></div>""", unsafe_allow_html=True)
    if st.button("Truy cập ứng dụng 🚀", key="btn_crawler", use_container_width=True):
        st.switch_page("nutrition.py")