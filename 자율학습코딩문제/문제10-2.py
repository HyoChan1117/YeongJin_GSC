# 사용자로부터 인덱스 번호를 입력 받아, 인덱스의 메뉴를 출력하는 프로그램 작성

# 미리 정의된 메뉴 리스트
menus = ["피자", "파스타", "샐러드", "스시", "버거"]

# 사용자로부터 인덱스를 입력 받는다.
index = int(input("메뉴의 인덱스를 선택하세요 (0부터 시작): "))

# 선택된 인덱스 메뉴를 출력한다.
if index == 0:
    menus[index]
    print(f"선택된 메뉴: {menus[index]}")
elif index == 1:
    menus[index]
    print(f"선택된 메뉴: {menus[index]}")
elif index == 2:
    menus[index]
    print(f"선택된 메뉴: {menus[index]}")
elif index == 3:
    menus[index]
    print(f"선택된 메뉴: {menus[index]}")
elif index == 4:
    menus[index]
    print(f"선택된 메뉴: {menus[index]}")

# 유효하지 않은 인덱스에 대해서는 오류 메시지를 출력한다.
else:
    print("유효하지 않은 선택입니다.")

