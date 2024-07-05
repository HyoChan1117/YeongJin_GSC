# bar 리스트를 만드는 방법
bar = [10, 20, 30, 40]

print(bar)
# 10, 20, 30, 40
#  1,  2,  3,  4

# = del bar[2]
bar.pop(2)  # pop의 기능: pop을 사용하면 해당 인덱스의 원소가 반환되면서 삭제

# 10, 20, 40
#  1,  2,  3

# del로 삭제할 때마다 원소의 개수가 줄어 듦