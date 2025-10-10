# type hinting을 활용하여 sum 함수의 매개변수와 반환값에 타입을 명시
# 실제 출력되는 결과에는 영향 없음
# 하지만 json, orm 등 외부 라이브러리와 연동할 때 도움이 될 수 있음
# 에러 검출에 도움을 줄 수 있음

# 그럼 왜 사용하는가?

from typing import Union

def sum(a : Union[int, float], b : Union[int, float]) -> int | float:
    return a + b

print(sum(1, 1))
print(sum(1, 1.0))
print(sum("1", "1"))