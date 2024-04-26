# 사용자로부터 문자열 입력 받기
text = input("문자열을 입력하세요: ")


# 문자열의 각 문자를 한 글자씩 가져와서 출력하기
for _ in range(2, 10):
    for character in text:
        mul = character * _
        print(mul)
