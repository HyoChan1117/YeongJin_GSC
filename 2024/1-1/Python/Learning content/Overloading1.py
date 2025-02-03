# Overloading
# 함수와 메서드에 적용이 된다.
# 사용 목적은? 프로그래머에게 코드 작성의 편리성을 제공하기 위해

def bar(arg_fnc):
    arg_fnc()
    
def foo():
    print("안녕하세요: ")
    
bar(foo)