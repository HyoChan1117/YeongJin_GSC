package learningContents.component.classObjectInstance;

//1. Class 정의 -> 틀 정의
// 틀을 정의하는 이유 : 객체를 찍어내기 위해
// Class의 이름을 정의할 때 첫 글자는 대문자로 함
class Car1{
    // Data + Function
    // Data -> Member variable(멤버 변수)
    // 멤버 변수란 클래스 안에 속해 있는 변수 라는 것
    String name;

    // Function -> Member method(멤버 메서드)
    void prtName() {
        System.out.println(name);
    }
}

public class study2 {
    public static void main(String[] args) {
        // new;
        // 복습
        // 1. heap영역 즉, 프로그램이 종료되거나 참조를 하지 않을 때까지 생명주기
        // 2. 메모리 공간은 코드가 실행되면서 할당

        // 2개의 차이
        // bar는 heap에 저장된다.
        int bar[] = new int[5];

        // car1은 stack에 저장된다.
        Car1 car1 = new Car1();
        Car1 car2 = new Car1();

        car2.name = "tesla";
        car2.prtName();

        // JAVA는 object 클래스 안에서 상속을 한다.
        // . 연산자 옆에 이외의 값들은 상속을 받은 것

    }
}