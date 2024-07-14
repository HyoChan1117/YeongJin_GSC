
# Dictionary : Mutable, Sequential, key만 Unique elements only
# variable = { key : value, key1 : value1, ... }
# 장점 : 탐색이 필요없음(데이터의 개수가 많아도 검증시간은 동일함)

# Dictionary는 왜 사용할까?
# 1. 데이터 검색과 접근이 빈번할 때  ex) 인터넷 쇼핑 검색할 때 Key값은 의류, 생필품, 식품, value값은 해당 key에 대한 값
# 2. 데이터를 구조화하여 저장할 때
# 3. 데이터를 계층화 형태로 만들 수 있음

# List
# 단점 : 탐색이 필요하기 때문에 데이터의 개수가 많아지면 검증시간이 길어짐

import random

bar = {}  # -> {}(블레이스)는 Dictionary를 만듦

print(type(bar))

bar["ycj"] = "정영철"

print(bar["ycj"])


# key값은 학번
# 이름, 국어, 영어, 수학, 총점, 평균은 1차원 리스트로 생성