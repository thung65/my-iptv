import requests
import re
import base64

url = "https://xemtv.icu/xem-kenh-sctv5-truc-tuyen/"

# Giả lập trình duyệt cực kỳ chi tiết
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://xemtv.icu/",
    "Accept-Language": "vi-VN,vi;q=0.9"
}

try:
    # Bước 1: Truy cập trang để lấy nội dung
    session = requests.Session()
    response = session.get(url, headers=headers, timeout=20)
    response.encoding = 'utf-8'
    html_content = response.text

    # Bước 2: Tìm link theo nhiều cách khác nhau (Regex linh hoạt)
    # Tìm link cdn trực tiếp
    match = re.search(r'https://cdn\d+\.tvmienphi\.xyz/[^"\']+\.m3u8\?token=[^"\']+', html_content)
    
    # Nếu không thấy, tìm link đã bị mã hóa Base64 (một số trang dùng cách này để giấu link)
    if not match:
        base64_links = re.findall(r'atob\(["\']([a-zA-Z0-9+/=]+)["\']\)', html_content)
        for b64 in base64_links:
            try:
                decoded = base64.b64decode(b64).decode('utf-8')
                if "m3u8" in decoded:
                    match = re.search(r'https://cdn\d+\.tvmienphi\.xyz/.*?\.m3u8\?token=.*', decoded)
                    if match: break
            except: continue

    if match:
        link_video = match.group(0).split('\\')[0] # Xử lý nếu có ký tự thoát
        content = f"#EXTM3U\n#EXTINF:-1,SCTV5 HD\n{link_video}"
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write(content)
        print("Thành công: Đã lấy được link mới!")
    else:
        # Nếu vẫn không thấy, lưu lại một phần HTML để chúng ta kiểm tra lỗi sau
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write("# Error: Server web nguon dang chan bot GitHub. Hay thu lai sau.")
        print("Lỗi: Không tìm thấy link trong mã nguồn.")
        
except Exception as e:
    with open("sctv5.m3u", "w", encoding="utf-8") as f:
        f.write(f"# Loi ket noi: {str(e)}")
