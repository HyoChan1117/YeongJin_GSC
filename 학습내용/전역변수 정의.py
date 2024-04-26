# 전역변수 정의
global_variable = "전역변수입니다."

def demo_function():
    # 지역변수 정의
    local_variable = "지역변수입니다."
    
    # 지역변수 출력
    print(local_variable)
    # 전역변수 출력
    print(global_variable)

# 함수 호출
demo_function()

# 함수 외부에서 지역변수에 접근하려고 시도
# 아래 Error 발생
print(local_variable) # 지역변수는 함수 밖에서 접근할 수 없습니다.
    

# 전역변수는 어디서든 접근 가능
print(global_variable)