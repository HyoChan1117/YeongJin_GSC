# 사용자로부터 초기 자본금, 주식의 구매 가격, 구매할 주식의 수, 판매할 때의 주식 가격을
# 입력 받아, 구매 후 남은 자본금과 예상 이익(또는 손실)을 출력하는 프로그램 작성

# 주식 구매 비용을 계산하는 함수를 정의한다.
def calculate(arg1, arg2, arg3, arg4):
    purchase_cost = arg2 * arg3
    remain_capital = arg1 - purchase_cost
    expect_profit = arg4 * arg3 - purchase_cost
    return purchase_cost, remain_capital, expect_profit

# 초기 자본금, 주식의 구매 가격, 구매할 주식의 수, 판매할 떄의 주식 가격을 입력 받는다.
capital = int(input("초기 자본금을 입력하세요: "))
cost = int(input("주식 가격을 입력하세요: "))
purchase_num = int(input("구매할 주식 수를 입력하세요: "))
sales_price = int(input("판매할 때의 주식 가격을 입력하세요: "))

# 계산 함수들을 호출하여 구매 후 남은 자본금, 예상 이익을 출력하고, "예상되는 ()입니다."
# 문구를 출력한다.
result1, result2, result3 = calculate(capital, cost, purchase_num, sales_price)

print(f"구매 후 남은 자본금: {float(result2):.2f}")
print(f"예상 이익: {float(result3):.2f}")

# 예상 이익이 0보다 크면, "예상되는 이익입니다."를 출력한다.
if result3 > 0:
    print("예상되는 이익입니다.")

# 예상 이익이 0보다 작으면, "예상되는 손실입니다."를 출력한다.
elif result3 < 0:
    print("예상되는 손실입니다.")
