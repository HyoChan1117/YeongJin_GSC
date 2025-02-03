package LearningContents.FlowControl.Random;

import java.util.Random;

public class Random1 {
    public static void main(String[] args) {

        Random bar = new Random();
        // Seed 값이 없기 때문에, 실행 시 현재시간을 시드값으로 활용

        for (int i = 0 ; i < 5 ; i++) {
            System.out.println(bar.nextInt());
        }

    }
}
