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

list_model = [list_bmw, list_tesla, list_lexus, list_genesis]

# 회사별 자동차 목록을 가지고 온다. 반복 -> 4회 -> bmw, tesla, lexus, genesis
# 세로 반복
maker_name_list = ["bmw", "tesla", "lexus", "genesis"]
index_count = 0

for maker_list in list_model:
    # 회사별 자동차 모델을 가지고 온다. -> 반복 횟수? 회사별 모델 개수에 따라 다름
    # 가로 반복
    for model_in_list in maker_list:
        if model == model_in_list:
            maker = maker_name_list[index_count]
            break
        
    if maker != "":
        break
    
    index_count += 1
        
        
# 다음주 월요일 오후 11시 40분까지
# Lab1~10까지 풀어오기