import requests
import re

# Chúng ta sẽ dùng một dịch vụ Proxy miễn phí để giả vờ như đang ở vùng khác
# Hoặc thử lấy trực tiếp với một bộ Header (đầu đề) cực kỳ chi tiết
url = "https://tvnet.gov.vn/kenh-truyen-hinh/1011/sctv5" # Thử nguồn này trước vì nó ít chặn IP GitHub hơn

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://tvnet.gov.vn/",
    "Accept-Language": "vi-VN,vi;q=0.9"
}

try:
    response = requests.get(url, headers=headers, timeout=20)
    # Tìm link .m3u8 có token
    match = re.search(r'https://[^"\']+\.m3u8\?token=[^"\']+', response.text)
    
    if not match:
        # Nếu nguồn 1 lỗi, thử lại nguồn tvmienphi nhưng với tham số lách luật
        url2 = "https://tvmienphi.org/live-tv/xem-kenh-sctv5-truc-tuyen.html"
        res2 = requests.get(url2, headers=headers, timeout=20)
        match = re.search(r'https://cdn\d+\.tvmienphi\.xyz/[^"\']+\.m3u8\?token=[^"\']+', res2.text)

    if match:
        link_video = match.group(0)
        content = f"#EXTM3U\n#EXTINF:-1,SCTV5 HD\n{link_video}"
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write(content)
        print("Success!")
    else:
        # Nếu vẫn không được, chúng ta sẽ ghi lại nội dung để kiểm tra
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write("# Server dang bao tri hoac chan IP. Hay thu lai sau 30 phut.")
except Exception as e:
    print(f"Error: {e}")
