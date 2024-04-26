numbers = [4, 1, 3, 2]
print("원래 순서: ", numbers)

numbers.append(5)
print("요소 추가 후:", numbers)

numbers.remove(2)
print("요소 삭제 후:", numbers)

mixed_list = [1, "apple", 3.14, [2, 4, 6], True]
print("혼합 데이터 타입 리스트:", mixed_list)

squares = [x**2 for x in range(10)]
print("리스트 컴프리헨션:", squares)