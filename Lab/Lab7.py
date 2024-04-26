# 사용자로부터 두 개의 정수를 입력 받고, 그 합, 차, 곱, 나눗셈의 결과를 출력하는 프로그램을 작성
# 첫 번째 숫자를 입력받는다.
inputValue1 = int(input("첫 번째 숫자를 입력하세요: "))

# 두 번째 숫자를 입력받는다.
inputValue2 = int(input("두 번째 숫자를 입력하세요: "))

# 입력 받은 숫자의 합, 차, 곱, 나눗셈을 구한다.
sum = inputValue1 + inputValue2
sub = inputValue1 - inputValue2
mul = inputValue1 * inputValue2
div = inputValue1 / inputValue2

# 결과를 출력한다.
print("합: ", float(sum))
print("차: ", float(sub))
print("곱: ", float(mul))
print("나눗셈: ", float(div))
