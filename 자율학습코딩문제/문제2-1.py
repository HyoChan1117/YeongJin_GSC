# 사용자가 제곱미터(㎡) 단위로 입력한 토지의 면적을 평방피트와 에이커 단위로 변환해주는 프로그램 작성

# 토지의 면적을 제곱미터(㎡) 단위로 입력 받는다.
square_meters = float(input("토지의 면적을 제곱미터(㎡) 단위로 입력하세요: "))

# 단위를 변환해 주는 함수를 선언한다.
def convert_to_square_feet(square_meters) :
    square_feet = square_meters * 10.7639
    return square_feet

def convert_to_acres(square_meters) :
    acres = square_meters / 4046.86
    return acres

# 입력 받은 면적이 양수일 경우, 함수를 호출하여 결과를 출력한다.
if square_meters > 0 :
    print(f"{square_meters} 제곱미터는 {float(convert_to_square_feet(square_meters))} 평방피트입니다.")
    print(f"{square_meters} 제곱미터는 {float(convert_to_acres(square_meters))} 에이커입니다.")

# 입력 받은 면적이 음수일 경우, "잘못된 입력입니다."를 출력한다.
else :
    print("잘못된 입력입니다.")

