import streamlit as st

# 1. Cấu hình trang cơ bản
st.set_page_config(
    page_title="App Portal | Phát Phan",
    page_icon="🌌",
    layout="wide"
)

# 2. CSS Tùy chỉnh (Giao diện bóng bẩy & Nút bấm mở cùng Tab)
st.markdown("""
<style>
    .portal-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        margin-bottom: 20px;
        border: 1px solid #e0e0e0;
        border-left: 5px solid #1f77b4;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .portal-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        border-color: #1f77b4;
    }
    .portal-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .portal-desc {
        font-size: 0.95rem;
        color: #555555;
        margin-bottom: 20px;
        flex-grow: 1;
    }
    .portal-btn {
        display: inline-block;
        text-align: center;
        padding: 10px 15px;
        background-color: #1f77b4;
        color: white !important;
        text-decoration: none;
        border-radius: 6px;
        font-weight: 600;
        transition: background-color 0.2s;
        width: 100%;
    }
    .portal-btn:hover {
        background-color: #155a8a;
    }
</style>
""", unsafe_allow_html=True)

# 3. Header và Tác giả
st.title("🌟 Hệ Thống Ứng Dụng Học Tập & Tiện Ích")
st.markdown("**Author:** Phát Phan - Network Engineer TAH")
st.divider()

# 4. KHO DỮ LIỆU CÁC ỨNG DỤNG
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
        },
        {
            "title": "English Phonetics", 
            "url": "#", 
            "desc": "Công cụ phân tích phiên âm IPA và luyện trọng âm."
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
            "title": "CS & Networking Fundamentals", 
            "url": "#", 
            "desc": "Tài liệu ôn tập kiến thức nền tảng Khoa học Máy tính và Mạng máy tính."
        },
        {
            "title": "CCNA / Routing & Switching", 
            "url": "#", 
            "desc": "Lab thực hành cấu hình kiến trúc L2/L3, mô phỏng mạng doanh nghiệp."
        }
    ],
    "🛠️ Công cụ & Tiện ích": [
        {
            "title": "Dinh dưỡng Crawler", 
            "url": "https://dinhduong-crawler.streamlit.app/", 
            "desc": "Thu thập, phân tích và thống kê dữ liệu dinh dưỡng tự động."
        },
        {
            "title": "Aquarium Bio-Tracker", 
            "url": "#", 
            "desc": "Công cụ theo dõi hệ vi sinh và thông số nước cho bể thủy sinh."
        }
    ]
}

# 5. Render giao diện bằng HTML
for category, apps in PORTAL_DATA.items():
    st.subheader(category)
    
    # Chia 3 cột
    cols = st.columns(3)
    
    for index, app in enumerate(apps):
        col = cols[index % 3]
        
        with col:
            # target="_self" mở liên kết ngay tại tab hiện tại
            card_html = f"""
            <div class="portal-card">
                <div class="portal-title">{app['title']}</div>
                <div class="portal-desc">{app['desc']}</div>
                <a href="{app['url']}" target="_self" class="portal-btn">Truy cập ứng dụng 🚀</a>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
            
    # Thêm khoảng trống giữa các danh mục
    st.markdown("<br>", unsafe_allow_html=True)
