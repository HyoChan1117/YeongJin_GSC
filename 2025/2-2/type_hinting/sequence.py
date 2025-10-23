from typing import Sequence

# Sequence -> Type Hinting -> list, tuple, range
x_seq_int: Sequence[int] = [1, 2, 3]
x_seq_int = (1, 2, 3)  # Sequence 타입은 tuple형을 사용할 때, 요소의 개수를 지정할 필요가 없다.
x_seq_int = {1, 2, 3}
x_seq_int = {1:2, 3:4}

