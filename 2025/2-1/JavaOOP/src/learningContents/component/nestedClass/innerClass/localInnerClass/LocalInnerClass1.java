package learningContents.component.nestedClass.innerClass.localInnerClass;

interface Test1 {
    void print();
}

class Outer1{

    int outer_val = 1;

    Test1 prt() {
        // 캡처링이 일어나는 경우 : Inner Class에서 Outer Class에 있는 지역변수를 참조할 경우
        // 1. Effectively constant  2. constant
        int local_val = 2;
        class Inner implements Test1 {
            public void print() {
                System.out.println(outer_val);
                System.out.println(local_val);
            }
        }
        return new Inner();
    }

}

public class LocalInnerClass1 {
    public static void main(String[] args) {
        Outer1 outer = new Outer1();
        Test1 test = outer.prt();
        test.print();
    }
}
