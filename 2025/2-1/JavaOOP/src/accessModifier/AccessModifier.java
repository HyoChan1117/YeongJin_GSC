package accessModifier;

class A {
    public int x;
}

class B extends A {
    void prt() {
        System.out.println(x);
    }
}

public class AccessModifier {
    public static void main(String[] args) {
        new B().prt();
    }
}

// public : 마음씨 좋은 사람 - 모든 곳에서 접근할 수 있게 하는 좋은 놈
// private : 속 좁은 사람 - 외부에서 접근하지 못하게 하는 나쁜 놈