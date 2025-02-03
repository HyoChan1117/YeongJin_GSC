# 쇼핑을 준비하는 중, 구매해야 할 품목들의 리스트를 작성하고자 한다.
# 쇼핑 품목들을 관리하는 간단한 프로그램 작성

# 빈 리스트를 생성한다.
shopping_list = []

# 쇼핑 리스트에 품목을 추가한다.
shopping_list.extend(['milk', 'bread', 'eggs', 'apple'])

# 현재 쇼핑 리스트의 내용을 출력한다.
print(f"현재 쇼핑 리스트: {shopping_list}")

# 쇼핑을 시작하기 전에 'toilet paper'가 빠져 있는 것을 발견하고 리스트의 맨 앞에 추가한다.
shopping_list.insert(0, 'toilet paper')

# 'orange juice'를 리스트의 두 번째 위치에 추가한다.
shopping_list.insert(1, 'orange juice')

# 'chicken', 'rice'를 한 번의 연산으로 리스트에 추가한다.
# extend() 또는 '+' 연산 사용
shopping_list.extend(['chicken', 'rice'])

# 각 단계 후, 쇼핑 리스트를 출력하여, 추가된 품목들을 확인한다.
print(f"최종 쇼핑 리스트: {shopping_list}")