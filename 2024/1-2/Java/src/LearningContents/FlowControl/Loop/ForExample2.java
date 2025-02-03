package LearningContents.FlowControl.Loop;

public class ForExample2 {
    public static void main(String[] args) {
        // 1 이상 20 이하의 7의 배수를 출력하라.
        for (int num = 1; num <= 20; num++) {

            if (num % 7 == 0) {
                System.out.println(num);
            }
        }
    }
}
