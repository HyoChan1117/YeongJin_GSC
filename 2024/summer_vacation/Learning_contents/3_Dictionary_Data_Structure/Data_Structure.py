# 자료구조 : 자료를 어떤 식으로 보관할 것인지에 대한 학문
# Computer Program = Algorithm + Data Structure

# Primitive Data Structure(기본형): 변수가 하나  -> 문제점: 알고리즘이 복잡해짐
# Composite Primitive Data Structure(복합형): 원시형 값이 2개 이상
# Abstract Data types(추상형): 복합형 + 알고리즘 -> 변수들을 2개 이상 어떤 식으로 묶을 것인지 논하는 것

# 자료구조 : 이론 또는 방법
# Collection : 이론을 기반으로 해서 구현해 놓은 것


bar = [10, 20]

foo = (30, 40)

print(bar[0], foo[0])

bar[0] = 100 # Mutable(가변성), Sequencial(순차적)
foo[0] = 200 # Immutable(불변성), Sequencial(순차적)

print(bar[0], foo[0])