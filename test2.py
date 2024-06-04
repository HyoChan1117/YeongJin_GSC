# 1에서 20까지 정수로 구성된 리스트를 생성하세요.

# bar = []

# for value in range(1, 21):
#     bar.append(value)
    
# print(bar)
# list comprehension (리스트 컴플리헨션)
# -> list 안의 원소들을 for문을 이용해서 동적으로 생성
# [expression for item in item_list if conditional expression]
# 프로그램에서는 동적, 정적을 많이 사용
# 동적 : 프로그램이 실행되고 속성들이 결정이 됨 
# 정적 : 프로그램이 

bar = [ value for value in range(1, 21) ]

print(bar)