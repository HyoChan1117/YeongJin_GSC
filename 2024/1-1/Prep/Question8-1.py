# 사용자로부터 현재 온도(섭씨)를 입력 받고, 입력 받은 온도에 따라, 적합한 야외 활동을
# 추천하는 프로그램 작성

# 현재 온도를 섭씨 단위로 입력 받는다.
current_celcius = float(input("현재 온도(섭씨)를 입력하세요: "))

# 30도 이상일 경우, 현재 온도와 추천 활동을 출력한다.
if current_celcius >= 30 :
    print(f"현재 온도: {current_celcius}도")
    print("추천 활동: 수영")

# 20도 이상 30도 미만일 경우, 현재 온도와 추천 활동을 출력한다.
elif 20 <= current_celcius < 30 :
    print(f"현재 온도: {current_celcius}도")
    print("추천 활동: 등산")

# 10도 이상 20도 미만일 경우, 현재 온도와 추천 활동을 출력한다.
elif 10 <= current_celcius < 20 :
    print(f"현재 온도: {current_celcius}도")
    print("추천 활동: 자전거 타기")

# 10도 미만일 경우, 현재 온도와 추천 활동을 출력한다.
elif current_celcius < 10 :
    print(f"현재 온도: {current_celcius}도")
    print("추천 활동: 스키")

