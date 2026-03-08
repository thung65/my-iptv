import requests
import re

# Trang web nguồn phát SCTV5 free
url = "https://xemtv.icu/xem-kenh-sctv5-truc-tuyen/"

# Giả lập trình duyệt Chrome xịn để không bị chặn
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://xemtv.icu/",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
}

try:
    response = requests.get(url, headers=headers, timeout=20)
    response.encoding = 'utf-8' # Đảm bảo đọc đúng tiếng Việt
    
    # Tìm link CDN bất kỳ (cdn2, 3, 4, 5...) có chứa .m3u8 và token
    # Regex này quét rộng hơn để không bỏ sót link
    match = re.search(r'https://cdn\d+\.tvmienphi\.xyz/[^"\']+\.m3u8\?token=[^"\']+', response.text)
    
    if match:
        link_video = match.group(0)
        # Tạo nội dung file chuẩn M3U
        content = f"#EXTM3U\n#EXTINF:-1,SCTV5 HD\n{link_video}"
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write(content)
        print("Da tim thay link SCTV5!")
    else:
        # Nếu không tìm thấy, ghi rõ lỗi vào file để kiểm tra
        with open("sctv5.m3u", "w", encoding="utf-8") as f:
            f.write("# Khong tim thay link trong HTML. Co the trang web da doi giao dien.")
        print("Loi: Khong tim thay link trong ma nguon.")
        
except Exception as e:
    with open("sctv5.m3u", "w", encoding="utf-8") as f:
        f.write(f"# Loi ket noi: {str(e)}")
    print(f"Loi ket noi: {e}")
