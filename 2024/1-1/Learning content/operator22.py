# Identity Operator
# is, is not

bar = [2, 3, 4]

foo = [2, 3, 5]

if bar == foo:
    print("참")
else:
    print("거짓")
    
if bar is foo:
    print("참")
else:
    print("거짓")
    
pos = bar

if bar is pos:
    print("참")
else:
    print("거짓")
    
# walrus operator를 사용한 Identity operator의 예시
if bar == (foo := list((2, 3, 4))):
    print("참")
else:
    print("거짓")