import java.io.FileInputStream;
import java.util.logging.FileHandler;

class Outer {
    int outer_val = 1;

    void doSomething() {
        int local_var = 2;

        class Bar {
            void prt() {
                System.out.println(local_var);  // 캡쳐
                System.out.println(outer_val);  // 참조
//            ==System.out.println(Outer.this.outer_val);  13번 코드와 동일
            }
        }

        Bar bar = new Bar();
    }
}

public class MainTest1 {
    public static void main(String[] args) {
        new Outer().doSomething();
    }
}
