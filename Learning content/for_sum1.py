# 10 ~ 20 사이 정수 중 짝수의 합을 계산하라.

sum = 0

for i in range(10, 21):
    if i % 2 == 0:
        sum += i
print(sum)