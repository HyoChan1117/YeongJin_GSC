package learningContents.inheritance;

// Inheritance(상속) - 부모 클래스로부터 멤버들을 물려 받는다.
// OOP의 꽃 -> 상속
// 1. 다형성
// 2. 추상클래스
// 3. 인터페이스

// 상속에서 객체 생성 순서 : 최상위 부모 클래스의 객체부터 생성되고, 순차적으로 생성

// 학생 클래스
class Student {
    int id = 2;
    String name = "Student";
    int age = 30;
}

// 글로벌시스템융합과 학생 클래스 - 학생 클래스의 멤버들을 물려 받음
class GscStudent extends Student {
    int id = 20;
    String name = "GscStudent";
    GscStudent() {
        System.out.println("id: " + this.id + ", name: " + super.name + ", age: " + age);
    }
}

public class test {
    public static void main(String[] args) {
        GscStudent s = new GscStudent();
    }
}
