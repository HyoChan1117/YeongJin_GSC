package Lab;

import java.util.Scanner;

public class Lab1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 사용자로부터 int형으로 나이를 입력받는다.
        System.out.print("첫 번째 값(나이 - 정수형): ");
        int age = scanner.nextInt();

        // 사용자로부터 float형으로 키를 입력받는다.
        System.out.print("두 번째 값(키 - 소수점 포함): ");
        float height = scanner.nextFloat();

        // 사용자로부터 int형으로 신용점수를 입력받는다.
        System.out.print("세 번째 값(신용점수 - 정수형): ");
        int score = scanner.nextInt();

        // 나이, 키, 신용점수의 합계와 이것을 3으로 나눈 평균값을 출력한다.
        System.out.println("합계: " + (age + height + score));

        System.out.printf("평균: %.2f\n", ((age + height + score) / 3));


    }
}
