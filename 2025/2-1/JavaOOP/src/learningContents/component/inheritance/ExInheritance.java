package learningContents.component.inheritance;

// Inheritance(상속) - 부모 클래스로부터 멤버들을 물려 받는다.
// OOP의 꽃 -> 상속
// 1. 다형성
// 2. 추상클래스
// 3. 인터페이스

// 상속에서 객체 생성 순서 : 최상위 부모 클래스의 객체부터 생성되고, 순차적으로 생성

// 상속 종류
// 1. 다중상속: 부모 클래스가 2개 이상  -> Java에서는 없는 개념
// 다른 부모로부터 같은 이름의 멤버를 물려 받을 때, 충돌 문제가 발생하기 때문에 없어짐

// 2. 단일상속: 부모 클래스가 반드시 1개 -> Java에서는 단일상속만 지원


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

public class ExInheritance {
    public static void main(String[] args) {
        GscStudent s = new GscStudent();
    }
}
