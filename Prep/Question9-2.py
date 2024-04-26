# 사용자로부터 주민번호 13자리(앞 6자리, 뒤 7자리)를 입력 받아 주민번호의 유효성을
# 검사하는 프로그램 작성

# 주민번호를 입력 받는다.(OOOOOO-OOOOOOO)
text = list(input("주민번호를 입력하세요: "))

# 입력 받은 문자열에서 '-' 빼기
text.remove("-")

# 문자열의 각 문자를 한 글자씩 가져와서 출력한다.
for character in text:
    print(character)

check = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
for mul_result in check:
    