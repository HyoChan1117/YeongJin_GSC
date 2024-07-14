# 학생 성적 관리 프로그램
# 학생들의 성적을 키보드로부터 입력 받아 리스트에 저장하고 입력 값을 출력하는 프로그램을 함수로 이용하여 작성하라.

# 학생 성적 관리 테이블을 위한 리스트
list_grade = []

count = 0
score_average = 0
while True:
    # 메뉴 출력
    print("=" * 25)
    print("1. 학생 성적 입력\n2. 학생 목록 출력(입력 순)\n3. 프로그램 종료")
    print()
    print(f"현재 입력 데이터 개수 : {count}")
    print(f"전체 학생 평균 값 : {float(score_average)}")
    print("=" * 25)
    
    input_menu = int(input("메뉴를 선택해 주세요: "))
    
    # 1. 학생 성적 입력
    if input_menu == 1:
        list_student = []
        
        print("학번을 입력하세요")
        student_num = int(input())
        list_student.append(student_num)
        print("이름을 입력하세요")
        student_name = input()
        list_student.append(student_name)
        print("국어 성적을 입력하세요")
        kor_score = int(input())
        list_student.append(kor_score)
        print("영어 성적을 입력하세요")
        eng_score = int(input())
        list_student.append(eng_score)
        print("수학 성적을 입력하세요")
        math_score = int(input())
        list_student.append(math_score)
        
        sum = kor_score + eng_score + math_score
        list_student.append(sum)
        
        average = sum / 3
        list_student.append(average)
        
        list_grade.append(list_student)
        
        count += 1
        score_average = (score_average + average) / count
        
    elif input_menu == 2:
        for id in range(count):
            print(f"[ id : {list_grade[id][0]} name : {list_grade[id][1]} kor : {list_grade[id][2]} eng : {list_grade[id][3]} math : {list_grade[id][4]} sum : {list_grade[id][5]} avg : {list_grade[id][6]} ]")
            
    elif input_menu == 3:
        print("프로그램 종료")
        break