package LearningContents.FlowControl.Random;

public class MathRandom1 {
    public static void main(String[] args) {

        // Math.random() -> 0.0 <= rand value < 1.0
        // 0이상 1미만의 double형 랜덤값

        // 1 ~ 10 사이의 정수 중 난수값 5개를 출력하라.
        // 1.0 <= rand value <= 10.0
        // 랜덤 함수
//        for (int i = 0 ; i < 10 ; i++) {
//            double randValue = (int)(Math.random() * 11);
//
//            System.out.println(randValue);
//
//        }

        // 1이상 10 이하의 정수
        for (int i = 0 ; i < 10 ; i++) {
            int randValue = (int)(Math.random() * 10) + 1;

            System.out.println(randValue);

        }

    }
}