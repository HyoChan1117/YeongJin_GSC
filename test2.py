
count = 1

for _ in range(3):
    for _ in range(2):
        print(count)
        count += 1
        
# 이중 for문이 있으면 바깥쪽부터 보지 말고 안쪽부터 봐라
for _ in range(3):
    for _ in range(3):
        print("*", end = "")
        
    print()