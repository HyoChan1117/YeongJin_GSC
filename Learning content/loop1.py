# while

# while 조건식:
#   참 일때 실행되는 문장

# 키보드로부터 정수를 입력 받고, 양수일 경우 출력,
# 음수 또는 0인 경우 재입력 -> 양수가 입력 될 때까지

# while True:
#     input_value = int(input("키보드로부터 정수를 입력 받는다: "))
#     if input_value > 0:
#         print(input_value)
#         break
#     else:
#         print("재입력 하세요.")

# while 문을 이용하여 1에서 10까지 출력하는 프로그램을 작성
# num = 1
# while num <= 10:
#     print(num)
#     num += 1   # 증감식을 missing 하는 경우가 있으니깐 주의

bar = ["hello", "world", "Richard"]
# found_word = False  # Flag 변수 -> 깃발 : Boolean

for word in bar:
    
    if word == "world":
        print("단어를 찾았음")
#        found_word = True
        break

# 정상적으로 반복을 마쳤을 때 else를 사용
else:
    print("단어를 찾지 못했음")

# if not found_word:
#     print("단어를 찾지 못했음.")

# 반복문이 종료
# 1. 반복문이 횟수가 다 되거나 조건식이 종료가 된 경우
# 2. 반복의 횟수가 종료 됐음
# 2-1. 반복문이 정상적으로 종료될 때만 else 선택
# else를 사용하면 플래그 변수를 사용할 필요가 없음
# while문에도 else 사용 가능

