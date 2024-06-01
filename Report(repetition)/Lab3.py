# 문자열 내 'h' 글자 개수 구하기
# for 문을 사용하여 아래 문자열 내 'h'의 개수를 출력하는
# 프로그램 작성

myString = "hello hyundai hoho"

count = 0

# 문장에서 "h"가 나오면 count에 1씩 추가한다.
for i in myString:
    if i == "h":
        count += 1

# count가 끝났으면 출력한다.
print("문자열 내 h 갯수 : ", count)