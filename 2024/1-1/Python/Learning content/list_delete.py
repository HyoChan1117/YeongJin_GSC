# CRUD : Delete
# 원소 삭제 : 원소 한 개 삭제, 리스트 내 전체 원소 삭제
# 원소 한 개 삭제 : 세 가지 방법
# 1) del 명령어를 사용해서 해당 index의 원소를 삭제
# 2) remove 함수를 이용해서 값을 이용해서 해당 원소를 삭제
# 3) pop 함수를 이용해서, 해당 index의 원소를 삭제하고, 삭제된 값을 반환

# 원소 한 개 삭제 1)
# bar = [10, 20, 30, 40, 50, 60]
# print("before : ", bar, len(bar))
# del bar[1]
# print("after : ", bar, len(bar))


# 원소 한 개 삭제 2) : 특정 값을 삭제할 때 remove 함수를 사용
bar = [10, 50, 30, 40, 50, 60]
print("before : ", bar, len(bar))   # [10, 50, 30, 40, 50, 60] 6개
bar. remove(50)
print("after : ", bar, len(bar))   # [10, 30, 40, 50, 60]  5개
# 50 중 앞에 있는 50을 삭제하고 뒤에는 사라지지 않음


# 원소 한 개 삭제 3)
print(bar.pop(2))  # 30
print("after : ", bar, len(bar))  # [10, 50, 40, 50, 60]  5개

print(bar.pop())  # 60  -> ()안에 아무것도 없으면 가장 마지막 원소가 반환되면서 삭제
print("after : ", bar, len(bar))   # [10, 50, 40, 50]  4개