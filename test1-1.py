# 키보드로부터 정수를 입력 받고,
# 입력 받은 정수 개수의 가로 X 세로 바둑판 출력
# 예) 입력 정수 : 3
# 결과) ***
input_value = int(input("입력 값: "))

for _ in range(0, input_value):  # 세로축 반복
    for count in range(0, input_value):   # 가로축 반복
        print("*", end = "")
    print()  # 매 세로축의 반복이 실행될 때마다 실행

# 13번의 for문이 끝났다는 것은 가로에 대한 반복이
# 끝났다는 것
        
# 중첩 반복문 : 반복문 안에 반복문
# () 안에 아무것도 없으면 개행문자 \n가 자동으로 붙음
# for _ in range(0, input_value):  # 세로 반복
    
#     for _ in range(0, input_value):   # 가로 반복
#         print("*", end = "")   # end = ""으로 붙이기
        
#     print()  # 공백을 출력하면 \n이 자동 붙어서 출력