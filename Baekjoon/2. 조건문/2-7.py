a, b, c = map(int, input().split())

if a == b and b == c and c == a:
    print(10000 + a * 1000)
elif a == b and a != c and b != c:
    print(1000 + a * 100)
elif b == c and b != a and c != a:
    print(1000 + b * 100)
elif c == a and c != b and a != b:
    print(1000 + c * 100)
else:
    print(max(a, b, c) * 100)