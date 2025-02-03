package LearningContents.FlowControl.Random;

import java.util.Random;

public class Random2 {
    public static void main(String[] args) {

        Random bar = new Random(23);
        // Seed 값이 있으면, 난수를 발생하는 패턴이 동일

        for (int i = 0 ; i < 5 ; i++) {
            System.out.println(bar.nextInt());
        }

        // Seed 값을 고정해 놓으면

    }
}
