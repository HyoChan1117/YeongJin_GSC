# 학생 성적 처리 프로그램
# 학생들의 성적을 키보드로부터 입력 받아 리스트에 저장하고 입력 값을 출력하는
# 프로그램을 함수를 이용하여 작성하라.

# 학생들의 정보를 저장하기 위한 딕셔너리를 생성한다.
dict_stu_info = {}

# 1. 학생 성적 입력 함수 정의
def stu_grade_input():
    global stu_num, count, total_avg
    
    # 학생들의 정보를 입력한다.
    stu_num = int(input("학번을 입력하세요: "))
    name = input("이름을 입력하세요: ")
    kor = int(input("국어 성적을 입력하세요: "))
    eng = int(input("영어 성적을 입력하세요: "))
    math = int(input("수학 성적을 입력하세요: "))

    # 입력 받은 값을 기준으로 총점과 평균을 구한다.
    total_sum = kor + eng + math
    avg = total_sum / 3
    
    # 정보 입력이 끝나면 현 입력 데이터 개수를 1씩 증가시키고,
    # 평균값을 매 입력마다 더 해서 전체 학생 평균 값을 구한다.
    count += 1
    total_avg = (total_avg + avg) / count
    
    # Dictionary를 사용하여 학번을 key 값으로 나머지 정보들은 1차원 리스트에
    # 담아 value 값으로 저장한다.
    dict_stu_info[stu_num] = [ name, kor, eng, math, total_sum, avg ]
    

# 2. 학생 목록 출력 함수 정의
def stu_list_output():
    while True:
        stu_num = int(input("학번을 입력하세요(0 입력 시 검색 종료): "))
        if stu_num in list(dict_stu_info.keys()):
            print(f"[ id : {stu_num} name : {dict_stu_info[stu_num][0]} \
kor : {dict_stu_info[stu_num][1]} eng : {dict_stu_info[stu_num][2]} \
math : {dict_stu_info[stu_num][3]} sum : {dict_stu_info[stu_num][4]} \
avg : {dict_stu_info[stu_num][5]} ]")
        elif stu_num == 0:
            break
        else:
            print("유효하지 않는 숫자입니다. 다시 입력해 주세요.")
    
# 3. 학생 목록 전체 출력 함수 정의
def total_stu_list_output():
    for key in dict_stu_info.keys():
        print(f"[ id : {key} name : {dict_stu_info[key][0]} \
kor : {dict_stu_info[key][1]} eng : {dict_stu_info[key][2]} \
math : {dict_stu_info[key][3]} sum : {dict_stu_info[key][4]} \
avg : {dict_stu_info[key][5]} ]")

count = 0
total_avg = 0
# 무한 루프를 통해 프로그램을 종료할 때까지 무한 반복
while True:
    # 메뉴 출력
    menu = f"""=========================
1. 학생 성적 입력
2. 학생 목록 출력
3. 학생 목록 전체 출력
4. 프로그램 종료

현 입력데이터 갯수 : {count}
전체 학생 평균 값 : {total_avg}
========================="""
    print(menu)
    
    # 메뉴 선택
    input_menu = int(input("메뉴를 선택하세요: "))
    
    # 1번을 입력 받았을 경우
    if input_menu == 1:
        stu_grade_input()
    
    # 2번을 입력 받았을 경우
    elif input_menu == 2:
        stu_list_output()
    
    # 3번을 입력 받았을 경우
    elif input_menu == 3:
        total_stu_list_output()
    
    # 4번을 입력 받았을 경우
    elif input_menu == 4:
        print("프로그램 종료")
        break
    
    # 1~4번 이외에 다른 번호를 입력 받았을 경우에는 오류 메시지 출력과 함께
    # 다시 메뉴를 입력 받는다.
    else:
        print("1에서 4까지의 숫자만 입력 하세요.")
    

