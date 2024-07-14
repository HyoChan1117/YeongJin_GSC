
# List는 Mutable, Sequential
bar = []

for _ in range(5):
    bar.append(input("값: "))
    
print(bar)


# set은 Sequential 하지 않음, Unique elements only(중복값 없음)
foo = set()  # set의 내부적 알고리즘으로 지정되어 있기 때문에 순차적이지 않음

for _ in range(5):
    foo.add(input("값: "))
    
print(foo)