bar = [10, 20, 30, 40]

for item in bar:
    print(item)
    
print("-" * 30)

for index in range(-1, -5, -1):
    print(bar[index])
    
# 원소(Element) 30을 100으로 변경
# bar[좌표] = 100
bar[2] = 100