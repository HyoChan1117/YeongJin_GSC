# 데코레이터 체이닝 (Decorator chaining)
# 함수에 데코레이터를 여러 개 겹쳐서 적용하는 것

def f_a(func):
    def wrapper():
        print(f"f_a: {func}")
        func()
        
    return wrapper
    
def f_b(func):
    def wrapper():
        print(f"f_b: {func}")
        func()
    
    return wrapper

@f_a
@f_b   # bar = f_a(f_b(bar))
def bar():
    print("bar")
    
bar()