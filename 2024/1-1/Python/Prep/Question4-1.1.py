# 사용자로부터 초기 자본금, 주식의 구매 가격, 구매할 주식의 수, 판매할 때의 주식 가격을
# 입력 받아 구매 후 남은 자본금과 예상 이익을 출력하는 프로그램 작성

# 초기 자본금, 주식의 구매 가격, 구매할 주식의 수, 판매할 때의 주식 가격을 입력 받는다.
inputValue1 = int(input("초기 자본금을 입력하세요: "))
inputValue2 = int(input("주식 가격을 입력하세요: "))
inputValue3 = int(input("구매할 주식 수를 입력하세요: "))
inputValue4 = int(input("판매할 때의 주식 가격을 입력하세요: "))

# 주식 구매 비용, 남은 자본금, 판매 예상 이익을 계산하는 변수를 선언한다.
purchase_cost = inputValue2 * inputValue3
remain_capital = inputValue1 - purchase_cost
expect_profit = inputValue4 * inputValue3 - purchase_cost

# 구매 후 남은 자본금과 예상 이익(또는 손실)을 출력한다. 이익과 손실 발생 여부에 따라
# "예상되는 ~입니다." 문구를 추가 출력한다.
print(f"구매 후 남은 자본금: {float(remain_capital):.2f}")
print(f"예상 이익: {float(expect_profit):.2f}")

if expect_profit > 0 :
    print("예상되는 이익입니다.")
    
elif expect_profit < 0 :
    print("예상되는 손실입니다.")