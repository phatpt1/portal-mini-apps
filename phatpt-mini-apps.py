import streamlit as st

# 1. Cấu hình trang cơ bản
st.set_page_config(
    page_title="App Portal | Phát Phan",
    page_icon="🌌",
    layout="wide"
)

# 2. Header và Tác giả
st.title("🌟 Hệ Thống Ứng Dụng Học Tập & Tiện Ích")
st.markdown("**Author:** Phát Phan")
st.divider()

# 3. KHO DỮ LIỆU CÁC ỨNG DỤNG (Bạn sẽ cập nhật thêm ở đây)
PORTAL_DATA = {
    "📚 Tiếng Anh - Đại học Mở Hà Nội (EHOU)": [
        {
            "title": "Listening EHOU", 
            "url": "https://listening-ehou.streamlit.app/", 
            "desc": "Luyện kỹ năng nghe tiếng Anh."
        },
        {
            "title": "Lý thuyết Reading", 
            "url": "https://lythuyet-reading.streamlit.app/", 
            "desc": "Hệ thống lý thuyết đọc hiểu."
        },
        {
            "title": "Reading EHOU", 
            "url": "https://reading-ehou.streamlit.app/", 
            "desc": "Thực hành bài tập đọc hiểu."
        }
    ],
    "🇨🇳 Tiếng Trung": [
        {
            "title": "Chinese Learning", 
            "url": "https://chinese-learning-phatpt.streamlit.app/", 
            "desc": "Học từ vựng và ngữ pháp tiếng Trung."
        },
        {
            "title": "Chinese Writing", 
            "url": "https://chinese-learning-writing.streamlit.app/", 
            "desc": "Luyện viết và nhận diện chữ Hán."
        }
    ],
    "🛠️ Công cụ & Tiện ích": [
        {
            "title": "Dinh dưỡng Crawler", 
            "url": "https://dinhduong-crawler.streamlit.app/", 
            "desc": "Công cụ tự động thu thập dữ liệu dinh dưỡng."
        }
    ]
}

# 4. Render giao diện tự động
for category, apps in PORTAL_DATA.items():
    st.subheader(category)
    
    # Chia làm 3 cột để giao diện dàn đều trên màn hình rộng
    cols = st.columns(3)
    
    for index, app in enumerate(apps):
        # Xác định app hiện tại sẽ nằm ở cột nào
        col = cols[index % 3]
        
        with col:
            # Tạo hiệu ứng thẻ (card) hiển thị thông tin
            st.info(f"**{app['title']}**\n\n{app['desc']}")
            # Nút bấm chuyển hướng sang app tương ứng
            st.link_button("Truy cập ứng dụng 🚀", app['url'], use_container_width=True)
            
    st.markdown("---")