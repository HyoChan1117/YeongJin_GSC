# 가변 인자값: 튜플 형태로 가져옴
# 가변 위치기반 매개변수
def prt(a, *arg):
    print(a, arg)
    
prt(1)
prt(1, 2)
prt(1, 2, 3)