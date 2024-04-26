# 사용자로부터 성적을 입력 받는다.
input_value = int(input("성적 입력: "))
    
score = ""
# 90점 이상이면 A
if input_value >= 90:   # 90 <= input_value
    score = "A"
    
# 80점 이상이면 B
elif input_value >= 80:   # 80 <= input_value < 90
    score = "B"
    
# 70점 이상이면 C
elif input_value >= 70:   # 70 <= input_value < 80
    score = "C"
    
# 60점 이상이면 D
elif input_value >= 60:   # 60 <= input_value < 70
    score = "D"
    
# 60점 미만이면 F   # 60 > input_value
else:
    score = "F"

# 조건 구간이 연속적으로 이어져 있을 때는 위에 조건에서 만족하지 않은 수가 포함되어 있을 수 있음
    
# 90점 이상이면 A
if input_value >= 90:
    print("A")
    
# 80점 이상이면 B
elif input_value >= 80:
    print("B")
    
# 70점 이상이면 C
elif input_value >= 70:
    print("C")
    
# 60점 이상이면 D
elif input_value >= 60:
    print("D")
    
# 60점 미만이면 F
else:
    print("F")