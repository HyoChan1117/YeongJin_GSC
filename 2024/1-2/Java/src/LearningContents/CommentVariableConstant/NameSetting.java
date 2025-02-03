package LearningContents.CommentVariableConstant;

import java.util.Scanner;

public class NameSetting {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("첫 번째 정수를 입력하세요: ");
        int firstNumber = scanner.nextInt();

        System.out.print("두 번째 정수를 입력하세요: ");
        int secondNumber = scanner.nextInt();

        int sum = firstNumber + secondNumber;

        System.out.println("두 값의 합은 " + sum + "입니다.");
    }
}
