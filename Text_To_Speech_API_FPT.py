import json
import requests
import urllib

#Sử dụng API của FPT
url_fpt = 'https://api.fpt.ai/hmi/tts/v5'

payload = input('Nhập nội dung cần chuyển: ')
headers = {
    'api-key': 'Thay thế bằng API key của bạn', #API key đăng ký tại https://id.fptcloud.com/auth/realms/FptSmartCloud/login-actions/registration?client_id=fptai_console&tab_id=JNPiE8agIFo
    'speed': '0', #Tốc độ đọc
    'voice': 'thuminh'
}
#Giọng: banmai, thuminh, myan, giahuy, ngoclam, leminh, minhquang, linhsan, lannhi

#Lấy url từ API cảu FPT
response = requests.request('POST', url_fpt, data=payload.encode('utf-8'), headers=headers)
#print(response.text)
url=response.text

#Tách lày url mới từ url của API  
new_url=url[10:100]

#Tải xuống file âm thanh
r = requests.get(new_url, allow_redirects = True)
open('audio.mp3','wb').write(r.content)

