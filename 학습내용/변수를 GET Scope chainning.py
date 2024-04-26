# 변수를 GET 할 경우 Scope chainning
# 1) 전역코드 -> 지역 변수 : 원천적 접근 불가
# 2) 지역코드 -> 전역 변수 : 접근 가능, scope chainning 규칙에 의거
# Local -> Enclosed -> Global -> Built-in (LEGB)
#   x                    x              x           ->  error


def foo():
    msg = "hello"
    print(greeting)
    
greeting = "안녕하세요"

foo()