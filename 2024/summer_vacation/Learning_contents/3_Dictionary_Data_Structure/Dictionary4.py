# Dictionary에서 [](브라켓)의 개수는 층을 나타냄
# 리스트로 생각하지만 인덱스 값이 key값이라고 생각하면 됨

bar = {
    "ycj" : {"name" : "정영철", "age" : 20}, 
    "lny" : {"name" : "이나영", "age" : 30}
}

for item in bar.values():
    for e in item.values():
        print(e)
        
print(bar["ycj"]["name"])