package learningContents.component.polymorphism.variableHiding;

class A {
    int a = 1;
    void prt() {
        System.out.println(a);
    }
}

class B extends A {
    int a = 2;
    void prt() {
        System.out.println(a);
    }
}

class C extends B {
    int a = 3;
    void prt() {
        System.out.println(a);
    }
}

public class VariableHiding2 {
    public static void main(String[] args) {
        C c = new C();  // C 클래스로 c 객체 생성
        System.out.println(c.a);  //
        System.out.println(((B)c).a);  // C 클래스로 생성된 c 객체는 \
        // A 클래스의 객체와 B 클래스의 객체 모두 포함하기 때문에 클래스명으로 형변환 가능
        System.out.println(((A)c).a);
    }
}