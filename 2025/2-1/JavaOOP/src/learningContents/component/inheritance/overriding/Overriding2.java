package learningContents.component.inheritance.overriding;

class Parent {
    void prt() {
        System.out.println("Parent prt");
    }
}

class Child extends Parent {
    public void prt() {
        super.prt();
        System.out.println("Child prt");
    }
}

public class Overriding2 {
    public static void main(String[] args) {
        new Child().prt();
    }
}
