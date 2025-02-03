# [ expression for item in item_list if conditional expression ]
# bar = [ value for value in range(1, 21) if value % 3 == 0 ]    # value의 값이 3의 배수
# print(bar)

# 아래 리스트 중 'c'가 포함된 단어만 선택해서 리스트로 구성하라
# foo = ["abc", "dcd", "ef", "gh"]

# list_c = [ value for value in foo if "c" in value ]  # value 에 "c"가 있을 때
# print(list_c)

# 아래 리스트 중 글자 개수가 3개 이상인 단어만 선택하여 리스트로 생성하라.
# foo = ["abc", "dcd", "ef", "gh"]

# list_num = [ word for word in foo if len(word) >= 3 ]
# print(list_num)

# 아래 리스트 중 글자 개수가 3개 이상인 단어만 선택하여 리스트로 생성하라.
# foo = ["abc", "dcd", "ef", "gh"]

# 1에서 10 사이 정수 중, 홀수는 10을 곱하고, 짝수는 20을 곱한 리스트를 생성하라
# bar = [ num * 10 if num % 2 != 0 else num * 20 for num in range(1, 11) ]
# print(bar)

# 조건식 and 조건식 -> 두 개의 조건식 둘 다 만족 시켜야 함
s_list = [ value for value in range(1, 21) if value % 3 == 0 if value % 4 == 0]
