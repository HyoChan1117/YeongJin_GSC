def bar():
    print("Hello")
    
def foo(arg_name):
    arg_name()
    
foo(bar)