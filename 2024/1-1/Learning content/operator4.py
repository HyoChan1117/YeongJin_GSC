# 산술연산자
# +, -, *, /

bar = 4
foo = 2

print(bar + foo) # 6
print(bar - foo) # 2
print(bar * foo) # 8
print(bar / foo) # 2.0
print(float(bar) / float(foo))  # 2.0
# 나누기 연산을 하면 파이썬이 print(float(bar) / float(foo))
# 으로 정수형을 자동적으로 실수형으로 바꿔준다.

print(3 / 2)  # 1.5 -> 몫과 나머지
print(3 % 2)  # 1   -> 나머지
print(3 // 2) # 1   -> 몫

print(2**3)   # 2^3 -> 2*2*2