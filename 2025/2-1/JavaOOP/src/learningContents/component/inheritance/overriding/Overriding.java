package learningContents.component.inheritance.overriding;

class A {
    void prt() {
        System.out.println("안녕하세요");
    }
}

class B extends A {
    // Overriding : 부모로부터 물려받은 멤버
    // 완전 재정의 - 부모로부터 물려받은 알고리즘 리셋하고 재정의
    // ex) prt() {}
    // 부분 재정의 - 부모로부터 물려받은 알고리즘에서 더 추가하는 것
    // ex) super.prt() {}

    // 다음과 같은 요소들이 모두 동일해야 함
    // 1. 이름
    // 2. 매개 변수
    // 3. 반환형

    void prt() {
        super.prt();
        System.out.println("Hello");
    }
}

public class Overriding {
    public static void main(String[] args) {
        new B().prt();

    }
}
