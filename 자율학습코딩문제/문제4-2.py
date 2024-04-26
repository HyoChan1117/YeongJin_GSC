# 사용자로부터 입력 받은 비밀번호가 안전한지를 검증하는 프로그램을 작성

# 비밀번호를 입력 받는다.
password = int(input("비밀번호를 입력하세요: "))

# 문자열 길이를 확인하고 길이가 충분한 경우와 짧은 경우 각각 출력한다.
if len(password) >= 8 :
    print("비밀번호 길이가 충분합니다.")
else :
    print("비밀번호가 너무 짧습니다.")
    
# 문자열에 숫자가 포함되어 있는지 확인한다.
has_number = False
for char in password :
    if char.isdigit():
        print(char)
        has_number = True
        break

# 문자열에 대문자가 포함되어 있는지 확인한다.


# 