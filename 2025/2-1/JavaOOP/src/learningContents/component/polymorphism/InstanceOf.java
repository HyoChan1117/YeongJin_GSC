package learningContents.component.polymorphism;

class A {
    int x = 2;
}

class B extends A {
    int y = 3;
}

class C extends A {
    int z = 4;
}

public class InstanceOf {
    public static void main(String[] args) {

        A bar = new B();

        if (bar instanceof C) {
            System.out.println("This is a learningContents.component.polymorphism.C");
        }
        else {
            System.out.println(((B)bar).y);
        }
    }
}