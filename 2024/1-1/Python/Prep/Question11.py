# 사용자로부터 길이를 입력 받아 해당 길이의 무작위 패스워드를 생성하는 프로그램 작성

import random

def generate_password(length):
    # 대문자, 소문자, 숫자를 포함한 문자열 정의
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower() # 대문자를 소문자로 변환
    digits = '0123456789'
    # 모든 가능한 문자를 하나의 문자열로 결합
    all_characters = uppercase_letters + lowercase_letters + digits
    
    # 패스워드 초기화
    password = ""
    
    # 지정된 길이만큼 랜덤 문자 선택
    for _ in range(length):
        password += random.choice(all_characters)   # 랜덤 문자를 패스워드에 추가
        
    # 생성된 패스워드 반환
    return password

# 함수 호출하여 패스워드 생성
generated_password = generate_password(8)
print(generated_password)

