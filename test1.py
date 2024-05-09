# 키보드로부터 정수를 입력 받고, 입력 받은 정수 개수만큼
# *을 출력하세요. * 연산자 사용 금지
# 예) 입력 정수 : 3
# 결과) ***
input_value = int(input("입력 값: "))

for count in range(1, input_value + 1):
    sum = "*" * count

print(sum)