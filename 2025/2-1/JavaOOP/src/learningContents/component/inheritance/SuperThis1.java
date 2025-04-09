package learningContents.component.inheritance;

// super() -> 부모 클래스의 객체 주소
// this() -> 현재 클래스의 객체 주소

class bar extends Object {  // Object는 객체를 생성할 때 상속받는 최상위 객체
    bar () {
        System.out.println("A 생성자 호출");
    }
}

class foo extends bar {
    foo (int m) {
        this();
        // super(); -> 생략됨 (컴파일러가 자동 삽입)
        System.out.println("B Parameter 생성자 호출");
    }
    foo () {
        System.out.println("B Default 생성자 호출");
    }
}

class pos extends foo {
    pos() {
        super(2);
        System.out.println("C 생성자 호출");
    }

    pos (int m) {
        this();
        System.out.println("C (int m) 생성자 호출");
    }

    pos (int m, int n) {
        this();
        System.out.println("C (int m, int n) 생성자 호출");
    }
}

public class SuperThis1 {
    public static void main(String[] args) {
        pos p1 = new pos();
    }
}
