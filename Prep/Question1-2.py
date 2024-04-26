# 삼각형 유형 판별 프로그램 작성

# 세 변의 길이를 각각 입력 받는다.
length1 = int(input("첫 번째 변의 길이를 입력하세요: "))
length2 = int(input("두 번째 변의 길이를 입력하세요: "))
length3 = int(input("세 번째 변의 길이를 입력하세요: "))

# 삼각형을 형성할 수 없는 경우
if length1 + length2 <= length3 or length2 + length3 <= length1 or length1 + length3 <= length2 :
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.")
    print("삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")

# 세 변의 길이가 모두 같은 경우
elif length1 == length2 == length3 :
    print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다.")

# 세 변 중 두 변의 길이가 같은 경우
elif length1 == length2 or length2 == length3 or length1 == length3 :
    print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다.")

# 세 변의 길이가 모두 다른 경우
elif length1 != length2 != length3 :
    print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다.")
