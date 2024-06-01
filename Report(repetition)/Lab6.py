# 1부터 20까지의 정수 중 짝수의 합계 계산
# continue 문 연습 (홀수 합계 건너뛰기)
# for 문과 continue 문을 사용하여 1부터 20까지의 숫자 중
# 홀수를 건너뛰고 짝수의 합계를 계산하는 프로그램 작성
total_sum = 0

# 1부터 20까지의 숫자 중 2로 나눴을 때 나머지가 0이 아닌
# 숫자가 나오면 건너뛴다.
for i in range(1, 21):
    if i % 2 != 0:
        continue
    total_sum += i

print(f"1부터 20까지의 짝수 합계 (홀수 건너뜀): {total_sum}")