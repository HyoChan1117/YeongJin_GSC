package learningContents.component.accessModifier.protectedStudy.gsc;

class UserInfo {
    protected int x = 3;

    int getX() {
        return x;
    }
}

public class GscStudent extends UserInfo {
    public GscStudent() {}
    void print() {
        System.out.println(getX());
        System.out.println(x);
    }
}
