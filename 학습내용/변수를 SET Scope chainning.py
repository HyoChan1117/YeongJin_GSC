# 변수를 SET 할 경우 Scope chainning => 원천적으로 불가

def foo():
    global msg     # global 함수를 가져와서 전역변수를 가져옴
    
    msg = "hello"  # 전역 변수 msg에 "hello"를 SET하고 싶을 때
    
msg = ""
    
foo()

print(msg)