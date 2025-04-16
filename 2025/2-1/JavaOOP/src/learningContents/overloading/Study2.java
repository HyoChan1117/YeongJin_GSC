package learningContents.overloading;

class Bar1 {
    // Overloading
    // 동일한 이름을 가지는 메소드 생성
    void prtMsg(String argMsg1, int argMsg2) {
        System.out.println(1);
    }

    void prtMsg(String argMsg1, float argMsg2) {
        System.out.println(2);
    }

    void prtMsg(String argMsg1, double argMsg2) {
        System.out.println(3);
    }
}

public class Study2 {
    public static void main(String[] args) {
        // 객체 생성
        Bar1 bar = new Bar1();

        // 이들을 호출할 때 매개변수의 개수와 자료형을 구분해서 호출
        bar.prtMsg("h",1);  // 매개변수가 1개이고, String 자료형을 가지는 메소드 찾기
        bar.prtMsg("e", 2.f); // 매개변수가 1개이고, int 자료형을 가지는 메소드 찾기
        bar.prtMsg("l", 3.0); // 매개변수가 1개이고, float 자료형을 가지는 메소드 찾기
    }
}
