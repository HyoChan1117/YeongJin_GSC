def bar():
    local_variable = "지역변수"
    print(local_variable)
    
global_variable = "전역변수"

bar()

print(local_variable)