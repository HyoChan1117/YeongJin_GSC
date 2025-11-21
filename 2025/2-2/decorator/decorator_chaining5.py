
from functools import wraps

def test(n):
    def factory(func):
        def wrapper():
            print(f"decorator arg n = {n}")
            func()
        return wrapper
    
    return factory
    
@test(1)  # test(1) -> factory()(bar) -> bar = factory((bar))
def bar():
    print("bar 호출")
    
bar()