package LearningContents.Operator;

import java.util.Scanner;

public class RelationalOperator {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int inputValue = sc.nextInt();

        if (inputValue >= 1 && inputValue <= 10) {
            System.out.println("Do something");
        } else {
            System.out.println("잘못된 입력 값 입니다.");
        }

    }
}
