# 1. 반복이 정상적으로 종료되었나? 아니면 중간에 break문을
# 사용해서 정지 되었나?
done_break = False  # 플래그 변수
for value in range(3):
    
    input_value = int(input("입력 값: "))
    
    if input_value <= 0:
        done_break = True  # 플래그 변수
        break
    
    print(value)
    
msg = "break 사용" if done_break else "break 미사용"
print(msg)

# 위와 똑같은 결과가 나오고 for else를 사용하면
# 플래그 변수를 따로 사용하지 않아도 됨
for value in range(3):
    
    input_value = int(input("입력 값: "))
    
    if input_value <= 0:
        msg = "break 사용"
        break
    
    print(value)
    
else: # 반복문 종료 and break 미사용
    msg = "break 미사용"