# 사용자로부터 첫째 줄에 현재 시간과 분, 둘째 줄에 요리하는 데 필요한 시간을 분 단위로
# 입력 받아, 요리가 완료되는 시간을 출력하는 프로그램 작성

# 첫째 줄에 현재 시간과 분, 둘째 줄에 요리하는 데 필요한 시간을 분 단위로 입력 받는다.
A, B = map(int,input().split())
C = int(input())

clock = (A + ((B + C) // 60))

if 0 <= clock <= 23 and 0 <= B <= 59 and 0 <= C <= 1000:
    print((clock), (B + C) % 60)
    
elif clock >= 24 and 0 <= B <= 59 and 0 <= C <= 1000:
    print((clock - 24), (B + C) % 60)