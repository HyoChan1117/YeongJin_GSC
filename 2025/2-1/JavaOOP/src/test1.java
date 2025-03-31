class Foo1 {
    // 1) 멤버변수
    //     A. 인스턴스 멤버 변수
    //     B. 클래스 멤버 변수
    // 2) 지역변수 -> 메서드 내 선언된 변수
}

class Bar1 {
    int x;
    String y;
    boolean z;

    void prtB(int argB) {
        System.out.println("prtB is invoked!");
    }

    void prtA(int argA) {
        System.out.println("prtA is invoked!");
        prtB(argA);
    }

}

public class test1 {
    public static void main(String[] args) {
    }
}
