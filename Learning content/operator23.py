# 바다코끼리 연산자 :=
# 대입(Assignment)과 평가(Evaluation) -> 사용

msg = "hello"

for char in msg:
    print(msg)
    
for char in (msg := "hello"):  # 코드가 
    print(msg)