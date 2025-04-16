package learningContents.component.accessModifier.encapsulation;

class Bar {
    private int x;  // 캡슐화 : 클래스 외부에서는 int x에 접근할 수 없음

    void prt() {
        System.out.println(x);
    }
}

public class Encapsulation {
    public static void main(String[] args) {
        Bar b = new Bar();
        b.prt();
    }
}
