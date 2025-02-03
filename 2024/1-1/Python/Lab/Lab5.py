# "남자" 또는 "여자"라는 문자를 입력받는다.
ManWoman = input("성별을 한글로 입력하세요 (남자/여자) : ")

# "남자"인 경우 "MAN"으로 출력한다.
if ManWoman == "남자" :
    print("MAN")
    
# "여자"인 경우 "WOMAN"으로 출력한다.
elif ManWoman == "여자" :
    print("WOMAN")

# 둘 다 아닌 경우 "잘못된 입력입니다."로 출력한다. 
else :
    print("잘못된 입력입니다.")