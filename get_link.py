import requests
import re

# Trang web gốc bạn vừa gửi
url = "https://tvmienphi.org/live-tv/xem-kenh-sctv5-truc-tuyen.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://tvmienphi.org/", # Cực kỳ quan trọng để lách bảo mật
    "Origin": "https://tvmienphi.org"
}

try:
    response = requests.get(url, headers=headers, timeout=20)
    response.encoding = 'utf-8'
    
    # Tìm link m3u8 có chứa token và CDN (2, 3, 4, 5...)
    match = re.search(r'https://cdn\d+\.tvmienphi\.xyz/[^"\']+\.m3u8\?token=[^"\']+', response.text)
    
    if match:
        link_video = match.group(0)
        # Tạo file M3U chuẩn cho Smart TV Q70B
        content = f"#EXTM3U\n#EXTINF:-1,SCTV5 HD\n#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer=https://tvmienphi.org/\n{link_video}"
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write(content)
        print("Đã lấy được link từ server gốc!")
    else:
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write("# Khong tim thay link. Co the trang web dung Javascript de an link.")
except Exception as e:
    print(f"Lỗi kết nối: {e}")
