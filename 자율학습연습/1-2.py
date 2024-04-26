# 사용자로부터 입력 받은 세 개의 수를 변의 길이로 하는 삼각형이 형성될 수 있는지, 그리고 가능하다면
# 어떤 유형의 삼각형인지 판별하는 프로그램 작성

# 세 개의 수를 입력 받는다.
inputValue1 = int(input("첫 번째 변의 길이를 입력하세요: "))
inputValue2 = int(input("두 번째 변의 길이를 입력하세요: "))
inputValue3 = int(input("세 번째 변의 길이를 입력하세요: "))

# 어떤 유형의 삼각형인지 판별한다.
# 세 변의 길이가 모두 같은 경우, "정삼각형"
if inputValue1 == inputValue2 and inputValue2 == inputValue3 and inputValue1 == inputValue3:
    print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다.")

# 어느 두 변의 길이 합이 나머지 한 변의 길이보다 작거나 같다면, 삼각형을 형성할 수 없습니다.
elif inputValue1 + inputValue2 <= inputValue3 or inputValue2 + inputValue3 <= inputValue1 or inputValue1 + inputValue3 <= inputValue2:
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.")
    print("삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")

# 세 변 중 두 변의 길이가 같다면, "이등변삼각형"
elif inputValue1 == inputValue2 or inputValue2 == inputValue3 or inputValue1 == inputValue3:
    print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다.")

# 세 변의 길이가 모두 다르다면, "부등변삼각형"
elif inputValue1 != inputValue2 and inputValue2 != inputValue3 and inputValue1 != inputValue3:
    print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다.")

