import sys
import os

# 비표준 경로 추가 : 개인 환경에 맞게 수정
module_path = r"C:\Users\USER\OneDrive - yjc.ac.kr\바탕 화면\학습자료\프로그래밍(1)\My project\2024\summer_vacation\Lab\2_Module_and_package\Lab2\bar"

if module_path not in sys.path:
    sys.path.append(module_path)
    
# 모듈 임포트
import external_module

def main():
    greeting = external_module.greet("Kim")
    
if __name__ == '__main__':
    main()