# 10 ~ 20 사이 정수 중 짝수의 합을 계산하라.

sum = 0

for value in range(10, 21, 2):
    sum += value
    
print(sum)