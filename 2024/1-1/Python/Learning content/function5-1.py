
# 함수에 인자 값 4개를 입력 받아 합계와 평균을 반환하는
# 함수를 작성하라.
# 그리고 반환된 합계와 평균을 화면에 출력하라.

def sum_avg(arg1, arg2, arg3, arg4):
    num = [arg1, arg2, arg3, arg4]
    
    sum = 0
    for _ in num:
        sum += _
        avg = sum / len(num)
    
    return sum, avg

sum, avg = sum_avg(1, 2, 3, 4)

print(f"합계: {sum}")
print(f"평균: {avg}")