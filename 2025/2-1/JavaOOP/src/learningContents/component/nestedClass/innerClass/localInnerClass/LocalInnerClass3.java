package learningContents.component.nestedClass.innerClass.localInnerClass;

class Outer2 {
    int outer_val = 1;

    void doSomething() {
        int local_var = 2;

        class Bar {
            void prt() {
                System.out.println(local_var);  // 캡쳐
                System.out.println(outer_val);  // 참조
//            ==System.out.println(learningContents.component.nestedClass.innerClass.localInnerClass.Outer.this.outer_val);  13번 코드와 동일
            }
        }

        Bar bar = new Bar();
        bar.prt();
    }
}

public class LocalInnerClass3 {
    public static void main(String[] args) {
        new Outer2().doSomething();
    }
}
