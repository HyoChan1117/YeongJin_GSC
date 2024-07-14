bar = { "영어" : 20, "수학" : 30, "국어" : 40 }

# keys() : 키 값
# values() : 데이터 값
# items() : 키 + 데이터

# sum = 0

# for record in bar.values(): # value(데이터) 값에 관심 있을 때
#     sum += record
    
# print(sum)

print(sum(bar.values()))


for key, value in bar.items(): # key(키), value(데이터) 값 둘 다 튜플(tuple)로 묶어서 반납
    print(key, value)


for key in bar.keys(): # key(키) 값에 관심 있을 때
    print(key)
    
    
for key, value in bar.items():
    print(key, "\t", value)



for key in bar:
    print(key, "\t", bar[key])

# 25번 코드와 30번 코드는 동일한 결과가 나옴