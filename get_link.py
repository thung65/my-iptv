from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time

# Cấu hình trình duyệt ẩn danh
chrome_options = Options()
chrome_options.add_argument("--headless") # Chạy ngầm không giao diện
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Truy cập trang gốc bạn vừa gửi
    driver.get("https://tvmienphi.org/live-tv/xem-kenh-sctv5-truc-tuyen.html")
    
    # Đợi 10 giây để Javascript tải xong luồng video
    time.sleep(10)
    
    # Lấy toàn bộ nội dung sau khi đã load xong link
    page_source = driver.page_source
    
    # Tìm link CDN (2, 3, 4, 5...) kèm token
    match = re.search(r'https://cdn\d+\.tvmienphi\.xyz/[^"\']+\.m3u8\?token=[^"\']+', page_source)
    
    if match:
        link_video = match.group(0)
        content = f"#EXTM3U\n#EXTINF:-1,SCTV5 HD\n{link_video}"
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write(content)
        print("Thành công: Đã dùng trình duyệt ảo lấy được link!")
    else:
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write("# Error: Khong tim thay link ngay ca khi dung Selenium.")
finally:
    driver.quit()
