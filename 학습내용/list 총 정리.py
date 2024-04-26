# 리스트를 사용하기 위해서는 리스트를 생성
bar = []
foo = list()

# CRUD

# Create : 원소 삽입
bar.append(10) # bar -> [10]
bar.append(20) # bar -> [10, 20]

# index 0     1
# bar[ 10,    20  ]
#     index, value
bar.insert(1, 100)   # [10, 100, 20]

# Read
# bar [10, 100, 20]
print(bar[1])  # 100
print(bar)  # [10, 100, 20]


for index in range(0,len(bar)):  # 0, 3 : len(리스트) -> 리스트의 원소 개수
    print(bar[index])  # index 0 -> 2
    
# 단일 원소 읽기    
bar[2]

# slicing : 하나의 리스트에서 특정 구간에 있는 원소들을 여러 개 지정해서 복사를 해서 가져오는 것
bar = [value for value in range(10, 20)]

# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# slicing
# 참조변수 [start : stop : step]

foo = bar[0:4:1]