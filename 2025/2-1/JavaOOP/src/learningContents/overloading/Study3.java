package learningContents.overloading;

class Bar2 {
    // Overloading
    // 동일한 이름을 가지는 메소드 생성
    int prtMsg(String argMsg1, int argMsg2) {
        System.out.println(1);

        return 0;
    }

    void prtMsg(String argMsg1) {
        System.out.println(2);
    }

    double prtMsg(String argMsg1, double argMsg2) {
        System.out.println(3);

        return 0.0;
    }
}

public class Study3 {
    public static void main(String[] args) {
        // 객체 생성
        Bar2 bar = new Bar2();

        // 이들을 호출할 때 매개변수의 개수와 자료형을 구분해서 호출
        bar.prtMsg("h",1);  // 매개변수가 1개이고, String 자료형을 가지는 메소드 찾기
        bar.prtMsg("e"); // 매개변수가 1개이고, int 자료형을 가지는 메소드 찾기
        bar.prtMsg("l", 3.0); // 매개변수가 1개이고, float 자료형을 가지는 메소드 찾기
    }
}
