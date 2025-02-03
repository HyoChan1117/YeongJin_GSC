package LearningContents.FlowControl.Random;

public class MathRandom {
    public static void main(String[] args) {

        for (int i = 0; i < 10; i++) {
            double bar = (int)(Math.random() * 45) + 1;
            System.out.println(bar);
        }

    }
}
