# 사용자로부터 하나의 영문자를 입력받고, 해당 문자가 모음(a, e, i, o, u) 중 하나인지 아닌지를 판별하여 결과를 출력하는 프로그램을 작성
# 하나의 영문자를 입력받는다.
alphabet = input("한 문자를 입력하세요: ")

# 입력받은 문자가 모음인 경우의 결과를 출력한다.
if alphabet == "a" :
    print(alphabet, end="는 모음입니다.")

elif alphabet == "e" :
    print(alphabet, end="는 모음입니다.")

elif alphabet == "i" :
    print(alphabet, end="는 모음입니다.")

elif alphabet == "o" :
    print(alphabet, end="는 모음입니다.")

elif alphabet == "u" :
    print(alphabet, end="는 모음입니다.")

# 입력받은 문자가 자음인 경우의 결과를 출력한다.
else :
    print(alphabet, end="는 모음이 아닙니다.")

