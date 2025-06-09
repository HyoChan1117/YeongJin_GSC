package learningContents.component.nestedClass.cohesion;

class Poo {
    // Poo 클래스(Outer class)의 멤버 영역에서 선언된 변수는 Inner class에서 사용 가능
    int x = 2;

    class Foo {
        // Foo 클래스는 Poo 클래스의 멤버 변수 x에 자유롭게 접근 가능
        void prt() {
            System.out.println(x);
        }
    }
}

public class cohesion {
}
