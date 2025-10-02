def foo(a, b, c):  # 위치 기반 매개변수는 반드시 값을 받아야 함
    pass

# foo(1, 2)  # Error

def pos(a, b, c=20):  # 키워드 기반 매개변수는 값을 받아도 되고 안 받아도 됨
    print(a, b, c)

pos(1, 2)