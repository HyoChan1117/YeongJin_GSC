# 3개의 수를 입력 받아 평균을 계산해줘
inputValue1 = int(input("첫 번째 숫자를 입력하세요: "))
inputValue2 = int(input("두 번째 숫자를 입력하세요: "))
inputValue3 = int(input("세 번째 숫자를 입력하세요: "))

def getAvg(argA, argB, argC) :
    sum = argA + argB + argC
    avg = sum / 3
    return avg

average = getAvg(inputValue1, inputValue2, inputValue3)
print("세 정수의 평균값은?:", round(float(average), 2))