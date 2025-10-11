# Student 클래스 생성
class Student:
    # 클래스 멤버 변수
    # __id_count: 현재까지 생성된 객체 수를 저장. 초기값 0
    __id_count = 0
    
    # 인스턴스 멤버 변수
    # name, id, gender, age, grade_korean, grade_math, grade_english, total, avg
    # 생성자
    # 매개변수: name, id, gender
    # 객체 생성 시 id에 __id_count 값을 부여하고, __id_count를 1 증가 시키기
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        Student.__id_count += 1
        self.id = Student.__id_count
    
    # 인스턴스 메서드
    # set_score(korean, math, english): 국어, 영어, 수학 점수를 입력 받아
    # 멤버 변수에 저장하고, total과 avg를 계산하여 멤버 변수에 저장
    def set_score(self, korean, math, english):
        self.grade_korean = korean
        self.grade_math = math
        self.grade_english = english
        
        self.total = self.grade_korean + self.grade_math + self.grade_english
        self.avg = self.total / 3
    
    # get_total_avg(): 총점(total)과 평균(avg)을 튜플로 반환할 것
    def get_total_avg(self):
        return self.total, self.avg
    
    # 클래스 메서드
    # get_id_count(): 현재 생성된 객체 수(__id_count)를 반환
    @classmethod
    def get_id_count(cls):
        return Student.__id_count
    
    # 정적 메서드
    # get_avg(arg1, arg2, arg3): 세 과목 점수를 인자로 받아 평균을 반환
    @staticmethod
    def get_avg(arg1, arg2, arg3):
        total = arg1 + arg2 + arg3
        avg = total / 3
        return avg

# 객체 생성
s1 = Student("Alice", 15, "F")
s2 = Student("Bob", 20, "M")

# 점수 입력
s1.set_score(90, 85, 92)
s2.set_score(75, 80, 78)

# 총점과 평균 출력
print(s1.get_total_avg())  # (267, 89.0)
print(s2.get_total_avg())  # (233, 77.67...)

# 클래스 메서드 호출 (현재 생성된 객체 수)
print(Student.get_id_count())   # 2

# 정적 메서드 호출 (별도의 객체 없이 평균 계산)
print(Student.get_avg(100, 90, 80))   # 90.0

print(f"이름: {s1.name} 번호: {s1.id} 성별: {s1.gender} 나이: {s1.age}세")
print(f"이름: {s2.name} 번호: {s2.id} 성별: {s2.gender} 나이: {s2.age}세")