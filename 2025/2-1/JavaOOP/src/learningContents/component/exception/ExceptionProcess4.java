package learningContents.component.exception;

class A {
    void prt() throws Exception {

    }
}

class B extends A {
    @Override
    void prt() throws RuntimeException {

    }
}

public class ExceptionProcess4 {
    public static void main(String[] args) throws Exception {
        A a = new B();
    }
}
