package learningContents.component.inheritance;

// super() -> 부모 클래스의 객체 주소
// this() -> 현재 클래스의 객체 주소

class A extends Object {  // Object는 객체를 생성할 때 상속받는 최상위 객체
    A () {
        System.out.println("A 생성자 호출");
    }
}

class B extends A {
    B (int m) {
        // super(); -> 생략됨 (컴파일러가 자동 삽입)
        System.out.println("B Parameter 생성자 호출");
    }
    B () {
        System.out.println("B Default 생성자 호출");
    }
}

class C extends B {
    C() {
        super(); // -> 명시적으로 작성한 경우, 컴파일러는 삽입하지 않음
        System.out.println("C 생성자 호출");
    }
}

public class SuperThis {
    public static void main(String[] args) {
        C c = new C();
    }
}
