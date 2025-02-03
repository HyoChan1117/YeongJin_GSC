package LearningContents.FlowControl.Random;

public class Random {
    public static void main(String[] args) {

        java.util.Random random1 = new java.util.Random(12345);
        java.util.Random random2 = new java.util.Random(12345);

        System.out.println("random1: " + random1.nextInt());
        System.out.println("random2: " + random2.nextInt());

        // 두 출력은 같은 시드 때문에 동일한 값을 출력

    }
}
