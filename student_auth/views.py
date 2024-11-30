from django.shortcuts import render
from django.http import HttpResponse
from .cku_login_macro import cku_login
import json
from django.http import JsonResponse
from django.middleware.csrf import get_token


def main(request):

    if request.method == 'POST':
        # JSON 형식으로 데이터를 받음
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            # cku_login 함수 호출하여 값 받기
            try:
                CrawlUserID, CrawlUserName, CrawlUserMajor = cku_login(username, password)
                
                # 받은 데이터를 JsonResponse로 반환
                return JsonResponse({
                    '학번': CrawlUserID,
                    '이름': CrawlUserName,
                    '전공': CrawlUserMajor
                })
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': '아이디와 비밀번호를 입력해주세요.'}, status=400)

    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
# from django.shortcuts import render
# from django.http import HttpResponse
# from .cku_login_macro import cku_login
# import json
# from django.http import JsonResponse
# from django.middleware.csrf import get_token
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# import base64
# import hashlib

# # Function to decrypt the AES encrypted data
# def decrypt_data(encrypted_data, secret_key):
#     # Decode the encrypted data from base64
#     encrypted_data_bytes = base64.b64decode(encrypted_data)
    
#     # Create AES cipher using the secret key (key must be 16, 24, or 32 bytes long)
#     secret_key_bytes = hashlib.sha256(secret_key.encode()).digest()  # Ensure the key is 32 bytes long for AES-256
#     cipher = AES.new(secret_key_bytes, AES.MODE_CBC, iv=encrypted_data_bytes[:16])  # Use the IV from the first 16 bytes

#     # Decrypt and remove padding
#     decrypted_data = unpad(cipher.decrypt(encrypted_data_bytes[16:]), AES.block_size)
    
#     # Convert bytes to string (assuming UTF-8 encoding)
#     return decrypted_data.decode('utf-8')

# def main(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)  # 데이터 파싱
#             encrypted_data = data.get('data')
#             if not encrypted_data:
#                 return JsonResponse({'error': '암호화된 데이터가 없습니다.'}, status=400)
            
#             secret_key = 'yoursecretkey1234'
#             decrypted_data = decrypt_data(encrypted_data, secret_key)

#             decrypted_json = json.loads(decrypted_data)
#             username = decrypted_json.get('username')
#             password = decrypted_json.get('password')

#             if not username or not password:
#                 return JsonResponse({'error': '아이디와 비밀번호가 잘못되었습니다.'}, status=400)

#             # 로그인 처리 (예시)
#             CrawlUserID, CrawlUserName, CrawlUserMajor = cku_login(username, password)
#             return JsonResponse({
#                 '학번': CrawlUserID,
#                 '이름': CrawlUserName,
#                 '전공': CrawlUserMajor
#             })

#         except json.JSONDecodeError:
#             return JsonResponse({'error': '잘못된 JSON 데이터입니다.'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': f'서버 오류: {str(e)}'}, status=400)
#     return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)


