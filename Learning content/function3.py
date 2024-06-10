
def sum(arg_first, arg_second):
    sum = arg_first + arg_second
    
    if sum < 0:
        print("음수")
        return  # 1) 함수 종료  -> break와 비슷
    
    return sum  # 2) 값 반환 -> 함수를 호출한 쪽으로 반환

result = sum(2, 3)
print(result)  # result -> 5

result = sum(-2, -3)
print(result)  # result -> -5

# 함수 정의 시 return은 있어도 되고 없어도 됨 -> 옵션