package lab.FlowControl;

import java.util.Scanner;

public class Lab2 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // 1부터 7까지의 정수를 입력 받아 해당 숫자에 맞는 요일을 출력하는 프로그램 작성
        // 정수 day를 초기화한다.
        int day = 0;

        // 1~7 사이의 숫자를 입력 받을 때까지 무한 반복
        while (true) {
            // 숫자를 입력 받는다.
            System.out.print("1에서 7 사이의 숫자를 입력하세요: ");
            day = scanner.nextInt();

            // 1~7의 숫자가 아닌 경우 무한 반복
            if (day < 1 || day > 7) {
                System.out.println("유효하지 않은 숫자입니다. 1~7 사이의 숫자를 입력하세요.");
            }
            // 1~7의 숫자인 경우 반복문 종료
            else {
                break;
            }
        }

        // 토, 일은 "주말", 그 외 요일은 "주중"으로 구분하여 출력
        switch (day) {
            case 1:
                System.out.println("월요일, 주중");
                break;
            case 2:
                System.out.println("화요일, 주중");
                break;
            case 3:
                System.out.println("수요일, 주중");
                break;
            case 4:
                System.out.println("목요일, 주중");
                break;
            case 5:
                System.out.println("금요일, 주중");
                break;
            case 6:
                System.out.println("토요일, 주말");
                break;
            case 7:
                System.out.println("일요일, 주말");
                break;
        }
    }
}