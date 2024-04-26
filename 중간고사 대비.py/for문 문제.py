# for문을 사용하여 다섯 개의 정수를 키보드로부터 입력 받아, 합계와 평균을 출력하는 프로그램을 작성한다.

total_sum = 0
average = 0
for count in range(1, 6):
    num = int(input(f"{count}번째 값 입력"))
    total_sum += count

print(f"합계 : {total_sum}")
print(f"평균 : {total_sum / 5}")