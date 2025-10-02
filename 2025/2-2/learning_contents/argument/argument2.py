# def prt(positional, variable prositional, keyword, \
#         variable keywords):
#     ...

# keyword(키워드 기반) parameter가 선언된 이후에는 
# positional(위치 기반) parameter가 올 수 없음
# 이 값은 무조건 받아야 해 -> keyword

# def prt(a, b = 2, c = 3, d):
#     print(a, b, c)
    
# prt(1) # 1, 2, 3
# prt(10, 20) # 10, 20, 3
# prt(2, 3)  # 2, 3, 3