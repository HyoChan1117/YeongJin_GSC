# walrus operator
# 변수 := 표현식
# 대입된 변수를 바로 평가
# 바다 코끼리 연산자

bar = "hello"

for char in bar:
    print(char, end = "")
    
print()

# 변수의 대입과 평가가 동시에 일어남
# walrus operator의 장점 : 코드가 간결하면서 직관적으로 보임
for char in (foo := "world"):
    print(char, end = "")