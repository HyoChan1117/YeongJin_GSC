# 구구단을 출력하는 프로그램 작성하시오 : 2단 ~ 9단
# 함수로 작성
# 1) 2단과 3단을 출력
# 2) 3단만 출력
def printMulTable(arg_a, arg_b = None):
    if arg_b == None:
        for dan in range(arg_a, arg_a + 1):
            for num in range(1, 10):
                print(f"{dan} X {num} = {dan * num}")
    else:
        for dan in range(arg_a, arg_b + 1):
            for num in range(1, 10):
                print(f"{dan} X {num} = {dan * num}")

printMulTable(2, 3)
printMulTable(3)