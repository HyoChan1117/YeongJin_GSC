package learningContents.overloading;

class Bar {
    // Overloading
    // 동일한 이름을 가지는 메소드 생성
    void prtMsg(String argMsg) {
        System.out.println(argMsg);
    }

    void prtMsg(int argMsg) {
        System.out.println(argMsg);
    }

    void prtMsg(float argMsg) {
        System.out.println(argMsg);
    }
}

public class study1 {
    public static void main(String[] args) {
        // 객체 생성
        Bar bar = new Bar();

        // 이들을 호출할 때 매개변수의 개수와 자료형을 구분해서 호출
        bar.prtMsg("hello");  // 매개변수가 1개이고, String 자료형을 가지는 메소드 찾기
        bar.prtMsg(2); // 매개변수가 1개이고, int 자료형을 가지는 메소드 찾기
        bar.prtMsg(3.f); // 매개변수가 1개이고, float 자료형을 가지는 메소드 찾기
    }
}
