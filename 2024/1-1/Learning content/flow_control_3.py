model = input("자동차 모델을 입력하세요: ")

# M3, M5, M7 -> BMW
# Y, X       -> Tesla
# ES, LS     -> Lexus
# G80, G90   -> Hyundai
# 이외 모델   -> "알 수 없는 모델입니다."
list_bmw = ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9"]
list_tesla = ["Y", "X"]
list_lexus = ["ES", "LS"]
list_genesis = ["G80", "G90"]

maker = "알 수 없는 모델입니다"

# 모델에 따른 메이커 선택
for i in list_bmw:
    if model == i:
        maker = "BMW"
        break

if maker == "":
    for i in list_tesla:
        if model == i:
            maker = "Tesla"

if maker == "":                
    for i in list_lexus:
        if model == i:
            maker = "lexus"
        break

if maker == "":    
    for i in list_genesis:
        if model == i:
            maker = "Hyundai"
        break

print(maker)
