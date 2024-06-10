
# 함수에 인자 값 4개를 입력 받아 합계와 평균을 반환하는
# 함수를 작성하라.
# 그리고 반환된 합계와 평균을 화면에 출력하라.

def sum_avg(arg1, arg2, arg3, arg4):
    sum = arg1 + arg2 + arg3 + arg4
    avg = sum / 4
    
    return sum, avg  # 반환값이 두 개 이상이면 tuple로
                     # 변환 후 반환한다.

# print(type(sum_avg(1, 2, 3, 4)))
sum, avg = sum_avg(1, 2, 3, 4)  # -> sum, avg = (10, 2.5)
print(f"합계: {sum}")
print(f"평균: {avg}")
# collection unpacking이 일어남
# collection : list, tuple, hash map, ...

value = sum_avg(1, 2, 3, 4)
print(f"합계: {value[0]}")
print(f"평균: {value[1]}")