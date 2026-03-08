import requests
import re
import os

url = "https://xemtv.icu/xem-kenh-sctv5-truc-tuyen/"
# Thêm User-Agent thật hơn để không bị chặn
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://xemtv.icu/"
}

try:
    response = requests.get(url, headers=headers, timeout=15)
    # Tìm link CDN (từ cdn2 đến cdn5)
    match = re.search(r'https://cdn\d+\.tvmienphi\.xyz/[^\s"\']+\.m3u8\?token=[^\s"\'&]+&e=\d+', response.text)
    
    if match:
        link = match.group(0)
        content = f"#EXTM3U\n#EXTINF:-1,SCTV5 HD\n{link}"
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write(content)
        print("Success: File sctv5.m3u has been created!")
    else:
        print("Error: Could not find the stream link in HTML.")
        # Tạo file trống để tránh lỗi "pathspec" nếu muốn
        with open("sctv5.m3u", "w") as f: f.write("# Error finding link")
except Exception as e:
    print(f"Request failed: {e}")
