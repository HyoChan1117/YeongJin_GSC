package LearningContents.FlowControl;

import java.util.Scanner;

public class FlowControlExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. 사용자 입력 받기
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        // 2. 선택적 실행 (조건문 사용)
        if (number % 2 == 0) {
            System.out.println(number + " is even.");
        } else {
            System.out.println(number + " is odd.");
        }

        // 3. 반복 실행 (반복문 사용)
        System.out.print("Counting down from " + number + " to 1:");
        for (int i = number; i > 0; i--) {
            System.out.print(i);
        }

        scanner.close();


    }
}
