import requests
import re

# Trang web nguồn
url = "https://xemtv.icu/xem-kenh-sctv5-truc-tuyen/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    response = requests.get(url, headers=headers)
    # Tìm link có token (tự động bắt cdn2, 3, 4, 5...)
    match = re.search(r'https://cdn\d+\.tvmienphi\.xyz/.*?\.m3u8\?token=.*?&e=\d+', response.text)
    
    if match:
        link = match.group(0)
        # Tạo nội dung file M3U8
        m3u_content = f"#EXTM3U\n#EXTINF:-1,SCTV5 HD\n{link}"
        with open("sctv5.m3u", "w") as f:
            f.write(m3u_content)
        print("Đã cập nhật link mới!")
except Exception as e:
    print(f"Lỗi rồi: {e}")
