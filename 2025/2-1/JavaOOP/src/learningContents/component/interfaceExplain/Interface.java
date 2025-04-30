package learningContents.component.interfaceExplain;

interface  KL {
    public abstract void print();
}

class T {
    KL obj;
    T(KL obj) {
        this.obj = obj;
    }
    void prt() {
        obj.print();
    }
}

class P implements KL {
    public void print() {
        System.out.println("learningContents.component.interfaceExplain.P");
    }
}

class Q implements KL {
    public void print() {
        System.out.println("learningContents.component.interfaceExplain.Q");
    }
}

class Z implements KL {
    public void print() {
        System.out.println("learningContents.component.interfaceExplain.Z");
    }
}

public class Interface {
    public static void main(String[] args) {
        (new T(new P())).prt();
        (new T(new Q())).prt();
        (new T(new Z())).prt();
    }
}
