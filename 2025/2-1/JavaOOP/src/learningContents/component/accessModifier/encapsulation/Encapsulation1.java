package learningContents.component.accessModifier.encapsulation;

class Foo {
    private int score;
    void prt() {
        System.out.println(score);
    }

    // Getter, Setter Method
    int getScore() {
        return score;
    }
    boolean setScore(int newScore) {
        if (newScore >= 0 && newScore <= 100) {
            score = newScore;
            return true;
        }
        return false;
    }
}

public class Encapsulation1 {
    public static void main(String[] args) {
        Foo f = new Foo();
    }
}
