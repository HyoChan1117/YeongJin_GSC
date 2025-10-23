from typing import NoReturn, Optional, Union

# Optional: 해당 자료형 아니면 None
x: Optional[int] = 2
x: Optional[int] = None

y: Optional[float] = 2


# 
def add_user(name: str) -> Union[str, None]:
    ...
    
def add_user1(name: Optional[str]) -> Optional[str]:
    ...
    

# 
def add_user2(name: Optional[str]) -> Optional[NoReturn]:
    if name is None:
        raise ValueError("Name must be values")
    
    print(name)
  
    
# 
def add_user3(name: Optional[str]) -> NoReturn:
    raise ValueError("Name must be values")

def add_user4(name: Optional[str]) -> str | None:
    raise ValueError("Name must be values")