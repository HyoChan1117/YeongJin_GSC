
# 3번 코드를 실행하면 bar.py의 코드가 실행되고 다시 돌아옴
from bar import file_name as b_name  # bar.py로부터 file_name이라는 변수를 'b_name'이라는 이름으로 지정해 줌
from foo import print_name

print_name(b_name)