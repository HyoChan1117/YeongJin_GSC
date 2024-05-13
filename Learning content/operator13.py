bar = [2, 3, 4, 5]  # list
foo = (6, 7, 8, 9)  # tuple

print(bar[0])  # list의 0번째 원소 2가 출력
print(foo[0])  # tuple의 0번째 원소 6이 출력

bar[0] = 20  # Mutable : list의 0번째 원소가 20으로 바뀜
foo[0] = 60  # Immutable : tuple은 원소를 바꿀 수 없기 때문에 error
