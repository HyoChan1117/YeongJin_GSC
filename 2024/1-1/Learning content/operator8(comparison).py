
value = int(input("정수 입력"))


# 입력 값이 3이면
if value == 3:
    print("참")
else:
    print("거짓")

# 입력 값이 3이 아니면
if value != 3:
    print("참")
else:
    print("거짓")
    
# 입력 값이 3 초과이면
if value > 3:
    print("참")
else:
    print("거짓")

# 입력 값이 3 이상이면
if value >= 3:
    print("참")
else:
    print("거짓")
    
# 입력 값이 3 미만이면
if value < 3:
    print("참")
else:
    print("거짓")
    
# 입력 값이 3 이하이면
if value <= 3:
    print("참")
else:
    print("거짓")
    
# 입력 값이 3.0 이면  -> 입력값은 정수지만 실수로 형변환
if value == 3.0:
    print("참")
else:
    print("거짓")