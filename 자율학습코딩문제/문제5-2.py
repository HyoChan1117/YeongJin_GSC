# 사용자로부터 자연수 N을 입력 받아, 지정된 패턴으로 별(*)을 출력하는 프로그램 작성

# 자연수 N을 입력 받는다.
N = int(input("N 입력: "))

# 첫 번째 줄부터 N번째 줄까지 별의 개수를 1씩 증가시키면서 출력한다.
for count in range(1, N+1):
    num1 = "*" * count
    print(num1)

# N번째 줄 이후부터는 별의 개수를 감소시켜 마지막 줄에는 별 1개를 출력한다.
for count in range(N-1, 0, -1):
    num2 = "*" * count
    print(num2)

