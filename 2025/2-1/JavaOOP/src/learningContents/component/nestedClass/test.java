package learningContents.component.nestedClass;

class A {
    static int x = 10;
    static class B {
        void prt() {
            System.out.println(x);
        }
    }
}

public class test {
    public static void main(String[] args) {
        A.B b = new A.B();
//        A.B b = new A().new B();
    }
}
