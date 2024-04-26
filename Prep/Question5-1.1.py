# 정수 3개를 입력 받는다.
# a, b, c
a = int(input("첫 번째 입력 값 : "))
b = int(input("두 번째 입력 값 : "))
c = int(input("세 번째 입력 값 : "))

# 입력 값이 모두 같으면, "모든 수가 같습니다." 출력
# 조건 : a == b and b == c and c == a
if a == b and b == c and c == a :
    print("모든 수가 같습니다.")

# 입력 값이 두 개가 같으면,
# 조건 : a == b or b == c or c == a
elif a == b or b == c or c == a :
    
# 1) "두 수가 같습니다." 출력
    print("두 수가 같습니다.")
# 2) 두 수도 출력
#   조건 : a == b -> a:b
#   조건 : b == c -> b:c
#   조건 : c == a -> c:a
    if a == b :
        print(a, ":", b)
    elif a == b :
        print(b, ":", c)
    elif a == b :
        print(c, ":", a)
        
# 입력 값이 모두 다르면,
# 1) "모든 수가 다릅니다."
# 2) 가장 큰 값을 출력한다.
