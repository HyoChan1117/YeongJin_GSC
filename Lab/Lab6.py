# 나이를 입력받는다.
age = int(input("나이를 입력하세요: "))

# 입력된 나이에 따라 "청소년(Teenager), 성인(Adult), 노년(Senior)" 중 하나로 분류한다.
# 13세에서 19세 사이는 "Teenager"를 출력한다.
if 13 <= age <= 19 :
    print("You are in the 'Teenager' age group.")

# 20세에서 64세 사이는 "Adult"를 출력한다.
elif 20 <= age <= 64 :
    print("You are in the 'Adult' age group.")

# 65세 이상은 "Senior"를 출력한다.
elif age >= 65 :
    print("You are in the 'Senior' age group.")

# 범위에 맞지 않는 입력값은 "Unknown age group"을 출력한다.
else :
    print("You are in the 'Unknown age group' age group.")
