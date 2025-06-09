package learningContents.component.nestedClass.innerClass.memberInnerClass;

class Outer {
    int outer_val = 1;
    void prt() {
        // Inner 클래스가 생성되었는지 생성되지 않았는지 모르기 때문에 inner_val을 사용할 수 없음
        // System.out.println(inner_val);
    }

    class Inner {
        int inner_val = 2;

        void prt() {
            System.out.println(outer_val);
        }

        void set_val(int val) {
            Outer.this.outer_val = val;  // Outer class의 this 사용
            System.out.println(outer_val);
        }
    }
}


public class Study {
    public static void main(String[] args) {

        Outer outer = new Outer();
        Outer.Inner inner1 = outer.new Inner();
        Outer.Inner inner2 = outer.new Inner();

        inner1.set_val(3);
        inner2.prt();

        System.out.println(outer.outer_val);

        // outer가 더 이상 Outer 클래스의 객체를 가리키지 않음
        // 하지만 Outer 클래스의 객체를 내부적으로 참조하고 있는 Inner 클래스가 존재하기 때문에
        // Outer 클래스의 객체가 메모리 상에서 사라진 것은 아님 -> 내부 참조 있기 때문에 GC 대상 아님
        outer = null;

        inner1.prt();
    }
}
