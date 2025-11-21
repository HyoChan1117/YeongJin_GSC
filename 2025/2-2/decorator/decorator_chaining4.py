
from functools import wraps

def test(func):
    def wrapper():
        func()
        
    wrapper.__name__ = func.__name__
    
    return wrapper
    
@test
def bar():
    ...
    
print(bar.__name__)  # 출력: wrapper