# 1에서 1000 사이의 정수 중 3의 배수 합 구하기
# While문을 사용하여 1~1000까지의 정수 중 3의 배수의 총합을 구하라
integer = 1
total_sum = 0

# 반복문을 이용하여 1~1000까지의 정수 중 3의 배수의 총합을 구한다.
while 1 <= integer <= 1000:
    if integer % 3 == 0:
        total_sum += integer
    integer += 1

print(f"1~1000 사이 정수 중 3의 배수의 총 합은 : {total_sum}")