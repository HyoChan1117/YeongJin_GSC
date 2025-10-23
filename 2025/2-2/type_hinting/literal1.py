from typing import NoReturn, Optional, Union, Literal

# 리터럴 상수로 올 수 있는 자료형과 값을 알려줌
def move(direction: Literal["forward", "backward", "left", "right"]) -> None:
    ...
    
move("forward")
move("backward")
move("left")
move("right")