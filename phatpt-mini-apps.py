import streamlit as st
import streamlit.components.v1 as components

# 1. Cấu hình trang cơ bản
st.set_page_config(
    page_title="App Portal | Phát Phan",
    page_icon="🌌",
    layout="wide"
)

# 2. CSS Tùy chỉnh làm đẹp thẻ Card
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
        min-height: 45px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Khởi tạo Session State (Quản lý trạng thái xem app)
if "current_app" not in st.session_state:
    st.session_state["current_app"] = None

# 4. KHO DỮ LIỆU CÁC ỨNG DỤNG (Chỉ đúng 6 app của bạn)
PORTAL_DATA = {
    "📚 Ngoại Ngữ - Đại học Mở Hà Nội (EHOU)": [
        {
            "title": "Listening EHOU", 
            "url": "https://listening-ehou.streamlit.app/", 
            "desc": "Luyện kỹ năng nghe tiếng Anh qua các bài tập chuyên sâu."
        },
        {
            "title": "Lý thuyết Reading", 
            "url": "https://lythuyet-reading.streamlit.app/", 
            "desc": "Hệ thống lý thuyết đọc hiểu và phân tích ngữ pháp."
        },
        {
            "title": "Reading EHOU", 
            "url": "https://reading-ehou.streamlit.app/", 
            "desc": "Thực hành bài tập đọc hiểu sát với chương trình học."
        }
    ],
    "🇨🇳 Tiếng Trung": [
        {
            "title": "Chinese Learning", 
            "url": "https://chinese-learning-phatpt.streamlit.app/", 
            "desc": "Hệ thống học từ vựng và ngữ pháp tiếng Trung cơ bản."
        },
        {
            "title": "Chinese Writing", 
            "url": "https://chinese-learning-writing.streamlit.app/", 
            "desc": "Luyện viết, nhận diện chữ Hán và thứ tự nét bút."
        }
    ],
    "💻 Công Nghệ Thông Tin - Đại Học CNTT (UIT)": [
        {
            "title": "Dinh dưỡng Crawler", 
            "url": "https://dinhduong-crawler.streamlit.app/", 
            "desc": "Thu thập, phân tích và thống kê dữ liệu dinh dưỡng tự động."
        }
    ]
}

# 5. XỬ LÝ GIAO DIỆN
if st.session_state["current_app"] is not None:
    # --- CHẾ ĐỘ XEM MINI APP NỘI BỘ ---
    app_info = st.session_state["current_app"]
    
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ Quay lại Portal", type="primary", use_container_width=True):
            st.session_state["current_app"] = None
            st.rerun()
            
    with col_title:
        st.subheader(f"📲 Đang chạy: {app_info['title']}")
        
    st.divider()
    
    # Nhúng trực tiếp mini app vào khung nhìn của Portal mà không hề đổi URL
    components.iframe(app_info['url'], height=850, scrolling=True)

else:
    # --- CHẾ ĐỘ TRANG CHỦ PORTAL ---
    st.title("🌟 Hệ Thống Ứng Dụng Học Tập & Quản Trị")
    st.markdown("**Author:** Phát Phan - Network Engineer TAH")
    st.divider()

    for category, apps in PORTAL_DATA.items():
        st.subheader(category)
        cols = st.columns(3)
        
        for index, app in enumerate(apps):
            col = cols[index % 3]
            
            with col:
                # Hiển thị Card thông tin
                st.markdown(f"""
                <div class="portal-card">
                    <div class="portal-title">{app['title']}</div>
                    <div class="portal-desc">{app['desc']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Nút bấm chuyển trạng thái mở App trực tiếp
                if st.button(f"Mở {app['title']} 🚀", key=f"btn_{category}_{index}", use_container_width=True):
                    st.session_state["current_app"] = app
                    st.rerun()
                st.markdown("<br>", unsafe_allow_html=True)
