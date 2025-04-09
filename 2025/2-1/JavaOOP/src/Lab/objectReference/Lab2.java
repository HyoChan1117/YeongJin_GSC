package Lab.objectReference;

class Scv {
    int numOfScv;
    int id;
    Scv() {
        id = ++numOfScv;
    }

    public String toString() {
        return "SCV ID: " + id;
    }
}

public class Lab2 {
    public static void main(String[] args) {
        Scv s1 = new Scv();
        Scv s2 = new Scv();
        Scv s3 = new Scv();

        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
    }
}
