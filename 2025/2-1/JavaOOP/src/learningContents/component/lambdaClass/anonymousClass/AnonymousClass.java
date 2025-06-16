package learningContents.component.lambdaClass.anonymousClass;

interface Test1 {
    void print();
}

public class AnonymousClass {
    public static void main(String[] args) {

        // 클래스를 한 번만 사용할 때 익명 클래스를 사용
        Test1 test = new Test1() {
            public void print() {
                System.out.println("Hello World");
            }
        };

        test.print();

    }
}
