def getCalcValues(argA, argB):
    # argA와 argB의 +, -, *, / 값을 변환하는 함수 작성
    # 값 반환 시 tuple 자료형으로...
    sum = argA + argB
    sub = argA - argB
    mul = argA * argB
    div = argA / argB
    return sum, sub, mul, div

sum, substract, multiply, division = getCalcValues(2, 3)

print(f"{sum}, {substract}, {multiply}, {division}")