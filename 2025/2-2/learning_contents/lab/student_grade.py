# 학생 클래스
class Student:
    # 생성된 객체의 학생 수를 저장하는 변수 (count)
    # 클래스 멤버 변수
    count = 0
    
    # 생성자
    # id, student_id, name, eng, kor, math, total, average
    def __init__(self, student_id, name, eng, kor, math):
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math
        Student.count += 1
        self.id = Student.count
    
    # 합계 계산 메서드
    def calc_total(self):
        self.total = self.eng + self.kor + self.math
    
    # 평균 계산 메서드
    def calc_average(self):
        self.average = self.total / 3
    
    # Getter메서드
    def get_eng(self):
        print("영어 점수: ", self.eng)
    
    def get_kor(self):
        print("국어 점수: ", self.kor)
        
    def get_math(self):
        print("수학 점수: ", self.math)
    
    # Setter메서드
    def set_eng(self, eng):
        self.eng = eng
        
    def set_kor(self, kor):
        self.kor = kor
        
    def set_math(self, math):
        self.math = math
    
# 학생 객체 생성
s1 = Student("2025011", "Kim", 90, 80, 25)
s2 = Student("2025002", "Lee", 70, 75, 80)

# 합계 및 평균 계산
s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()

# 결과 출력
print(s1.id, s1.name, s1.total, s1.average)
print(s2.id, s2.name, s2.total, s2.average)

# 학생 객체 개수 확인
print("총 학생 수: ", Student.count)