package learningContents.component.exception;

class Bar1 {
    void level1() {
        level2();
    }

    void level2() {
        level3();
    }

    void level3() {
        throw new RuntimeException("예외 발생 위치: level3()");
    }
}

public class test {
    public static void main(String[] args) {
        new Bar1().level1();

        System.out.println("이 코드는 실행되지 않습니다.");
    }
}
