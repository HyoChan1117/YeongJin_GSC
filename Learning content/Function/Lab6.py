def wrap_in_tag(arg1, arg2):
    print(f"<{arg1}>{arg2}</{arg1}>")
    
    
print(wrap_in_tag('p', 'hello'))
print(wrap_in_tag('b', 'world'))