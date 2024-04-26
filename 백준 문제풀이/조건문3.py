# 사용자로부터 자연수 N을 입력 받아, 1부터 N까지 합을 구하는 프로그램 작성

# 자연수 N을 입력 받는다.
inputValue = int(input())

# 1부터 N까지의 합을 출력한다.
num = 0
for sum in range(1, inputValue + 1):
    num = num + sum
    
print(num)
    
