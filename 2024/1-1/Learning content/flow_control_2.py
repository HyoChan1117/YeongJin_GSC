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

maker = ""

# 모델에 따른 메이커 선택
if model in list_bmw:
    maker = "bmw"
elif model in list_tesla:
    maker = "tesla"
elif model in list_lexus:
    maker = "lexus"
elif model in list_genesis:
    maker = "genesis"
else:
    maker = "Unknown model"
    
print(maker)