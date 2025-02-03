# 사용자로부터 세 개의 정수를 입력 받아 세 수의 관계에 따라 결과를 출력하는 프로그램 작성

# 세 개의 정수를 입력 받는다.
inputValue1 = int(input("첫 번째 수 입력: "))
inputValue2 = int(input("두 번째 수 입력: "))
inputValue3 = int(input("세 번째 수 입력: "))

# 모든 수가 같을 경우, "모든 수가 같습니다." 문구를 출력한다.
if inputValue1 == inputValue2 and inputValue2 == inputValue3 and inputValue1 == inputValue3 :
    print("모든 수가 같습니다.")

# 두 수가 같으면, "두 수가 같습니다." 문구를 출력하고 같은 두 수도 출력한다.
elif inputValue1 == inputValue2 or inputValue2 == inputValue3 or inputValue1 == inputValue3 :
    if inputValue1 == inputValue2 :
        print(f"두 수가 같습니다. ({inputValue1}와 {inputValue2})")
    elif inputValue2 == inputValue3 :
        print(f"두 수가 같습니다. ({inputValue2}와 {inputValue3})")
    elif inputValue1 == inputValue3 :
        print(f"두 수가 같습니다. ({inputValue1}와 {inputValue3})")

# 모든 수가 다를 경우, "모든 수가 다릅니다. 가장 큰 수는 x입니다." 문구를 출력한다.
elif inputValue1 != inputValue2 and inputValue2 != inputValue3 and inputValue1 != inputValue3 :
    if inputValue2 < inputValue3 < inputValue1 or inputValue3 < inputValue2 < inputValue1 :
        print(f"모든 수가 다릅니다. 가장 큰 수는 {inputValue1}입니다.")
    elif inputValue1 < inputValue3 < inputValue2 or inputValue3 < inputValue1 < inputValue2 :
        print(f"모든 수가 다릅니다. 가장 큰 수는 {inputValue2}입니다.")
    elif inputValue1 < inputValue2 < inputValue3 or inputValue2 < inputValue1 < inputValue3 :
        print(f"모든 수가 다릅니다. 가장 큰 수는 {inputValue3}입니다.")

