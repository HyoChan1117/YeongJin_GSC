# 문자열 내 단어 개수 출력
# for 문을 사용하여 아래 문자열 내 단어 개수를 출력하는
# 프로그램 작성

myString = "It is a great weather with you"

count = 0

# 반복문을 통해 띄어쓰기의 개수를 count하여 단어의 개수를 구한다.
for i in myString:
    if i == " ":
        count += 1

# 띄어쓰기 개수에서 1을 더하여 단어의 개수를 찾는다.
count += 1

print("문자열 단어 갯수 : ", count)