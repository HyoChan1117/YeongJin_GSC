# 현재 연도와 사용자의 태어난 연도를 입력받아 나이 계산하기

# 현재 연도를 입력받는다.
current_year = int(input("현재 연도를 입력하세요: "))

# 태어난 연도를 입력받는다.
born_year = int(input("태어난 연도를 입력하세요: "))

# "현재 연도 - 태어난 연도"의 식을 이용해 나이를 계산한다.
age = current_year - born_year

# 결과를 출력한다.
print("당신의 나이는", age, end="살 입니다.")

