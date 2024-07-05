# 대한민국 주민번호 유효성 검사기(1)
# 대한민국 주민번호는 총 13자리 숫자로 구성되어 있습니다.
# 앞의 6자리는 생년월일을 나타내며, 뒤의 7자리는 성별, 출생등록지, 일련번호 및
# 검증번호로 구성됨
# 이 문제에서는 사용자로부터 주민번호를 입력 받아, 주민번호의 유효성을 검사하는
# 프로그램 작성

# 사용자로부터 주민번호를 입력 받는다.
input_value = "790608-2552416"

# 입력 받은 주민번호의 앞 12자리를 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5
# 곱한다.
mul_input = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

sum = 0
count = 0
for i in input_value:
    # "-"이 아니고 count가 12 미만일 경우
    if i != "-" and count < 12:
        num = int(i)
        sum += num * mul_input[count]
        count += 1

# 체크 계산
check_calculate = (11 - (sum % 11)) % 10 == input_value[-1]

if check_calculate == input_value[-1]:
    print("유효한 주민번호입니다.")
else:
    print("유효하지 않은 주민번호입니다.")