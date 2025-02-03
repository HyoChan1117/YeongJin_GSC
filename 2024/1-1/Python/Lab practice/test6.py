# 사용자 나이대를 영어로 표현하는 프로그램을 작성

# 나이를 입력받는다.
age = int(input("나이를 입력하세요: "))

# 13세에서 19세 사이는 "Teenager"을 출력한다.
if 13 <= age <= 19 :
    print("You are in the 'Teenager' age group.")

# 20세에서 64세 사이는 "Adult"을 출력한다.
elif 20 <= age <= 64 :
    print("You are in the 'Adult' age group.")

# 65세 이상은 "Senior"을 출력한다.
elif 65 <= age :
    print("You are in the 'Senior' age group.")

# 범위에 맞지 않는 입력값은 "Unknown age group"을 출력한다.
else :
    print("You are in the 'Unknown age group'")