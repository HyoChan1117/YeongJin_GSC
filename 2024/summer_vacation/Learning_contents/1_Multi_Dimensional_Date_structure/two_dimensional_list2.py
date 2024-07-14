bar = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]

# 'bar' Matrix의 모든 원소를 순회
for col in bar:  # 각 'row'는 'bar'의 한 행을 나타낸다.
    for item in col:  # 'row'의 각 요소(즉, 각 열의 값)를 'item'으로 순회
        # 현재 'item'을 출력하고, 같은 행의 다음 아이템과 공백으로 구분
        print(item, end='')
    print()