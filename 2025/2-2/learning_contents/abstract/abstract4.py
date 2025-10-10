# 동적 타이핑 언어가 좋지만, 코드의 규모가 커질수록 관리의 어려움이 있다.
# Type hinting: 동적 타이핑 언어의 단점을 보완하기 위한 장치
# -> 변수, 매개변수, 반환값에 타입을 명시
def sum(a, b):
    return a + b

print(sum(1, 1))
print(sum(1, 1.0))
print(sum("1", "1"))