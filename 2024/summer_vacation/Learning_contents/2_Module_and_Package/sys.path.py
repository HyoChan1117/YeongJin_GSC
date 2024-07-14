
import sys # 파이썬 인터프리터와 상호작용 기능 제공

# sys.path 변수의 자료형 출력
print(type(sys.path))

# sys.path 리스트에 있는 각 경로를 출력
for path in sys.path:
    print(path)
    

# import 시 모듈 검색 순서
# 1. 현재 파일이 있는 폴더(Working Directory)
# 2. 파이썬의 내장 모듈
# 3. pip 명령어를 통해 설치했던 Third-party 패키지 디렉토리 : site_packages

# sys.path : 현재 모듈을 찾는 순서