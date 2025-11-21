
def upper(func):
    def wrapper(msg:str):
        return func(msg.upper())
    
    return wrapper

@upper   # bar = upper(bar)
def bar(msg:str):
    return msg
print(bar("Hello"))

print(bar.__name__)