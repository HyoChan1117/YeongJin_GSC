package learningContents.component.nestedClass.staticNestedClass;

class A {
    static int x = 10;
    static class B {
        void prt() {
            System.out.println(x);
        }
    }
}

public class Study {
    public static void main(String[] args) {
        // B 클래스는 Static Nested Class 이기 때문에 A 클래스의 객체 없이 바로 생성 가능
        A.B b = new A.B();
//        A.B b = new A().new B();
    }
}
