package learningContents.component;

interface MyInterface {
    void prt(String s);
}

public class FunctionalInterface {
    public static void main(String[] args) {

        MyInterface obj = (msg) -> System.out.println(msg);

        obj.prt("Hello");

    }
}
