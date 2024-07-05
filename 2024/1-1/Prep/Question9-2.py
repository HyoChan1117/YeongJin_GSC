#################
input_number = input("주민번호를 입력하세요: ")
check_number = [2,3,4,5,6,7,8,9,2,3,4,5]

# 유효성 검사

sum = 0  # 변수를 선언을 먼저 해주자
count = 0
for num in input_number:
    if num != "-" and count < 12:
        # 현재 num이 "-" 아니고 주민번호의 마지막 자리가 아닐 때
        sum += int(num) * check_number[count]
        count += 1
        

# 주민번호 12자리를 체크 값과 곱한 후 더한다.
# 주민번호 12자리 : 0번째 index -> 11번째 index

 
# 체크값을 계산하다 : (11 - (sum % 11)) % 10
check_value = (11 - (sum % 11)) % 10

# 판별 결과 값을 출력한다.
if check_value == int(input_number[-1]):
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호")