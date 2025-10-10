class Student:
    count = 0
    
    def __init__(self):
        Student.count += 1
        self.id = Student.count
        self.name = "Kim"
        self.kor = 90
        self.math = 100
        self.eng = 95
        self.sum = self.kor + self.math + self.eng