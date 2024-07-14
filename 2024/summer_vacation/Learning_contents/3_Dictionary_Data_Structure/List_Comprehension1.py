# List Comprehension에서 반복문이 중첩되는 경우
# 가장 왼쪽 반복문은 가장 바깥쪽, 가장 오른쪽은 가장 안쪽 반복문
foo = [ [g for g in range(2)] for value in range(3) ]

print(foo)

for value in range(3):
    list = [g for g in range(2)]
    print(list)