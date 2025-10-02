# / : 위치기반 매개변수 전용
# -> / 앞까지의 모든 매개변수는 위치기반 인자값으로 할당되어야 됨
def calculate(x, y, /, op = "+"):
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    else:
        print("error")
        
calculate(2, 3)  # 5
calculate(10, 20, "-")  # -10