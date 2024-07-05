# 사용자로부터 토지의 면적을 제곱미터(m^2) 단위로 입력 받아, 평방피트(ft^2)와 에이커(ac) 단위로
# 변환해 주는 프로그램 작성

# 제곱미터(m^2)를 평방피트(ft^2)와 에이커(ac) 단위로 변환해 주는 함수를 정의한다.
def calculate_convert_to_square_feet(arg):
    square_feet = arg * 10.7639
    return square_feet

def calculate_convert_to_acres(arg):
    acres = arg / 4046.86
    return acres

# 토지의 면적을 제곱미터(m^2) 단위로 입력 받는다.
width = float(input("토지의 면적을 제곱미터(㎡) 단위로 입력하세요: "))

# 함수를 호출하여 결과를 출력한다.
if width > 0:
    print(f"{width} 제곱미터는 {calculate_convert_to_square_feet(width)} 평방피트입니다.")
    print(f"{width} 제곱미터는 {calculate_convert_to_acres(width)} 에이커입니다.")

else:
    print("잘못된 입력입니다.")