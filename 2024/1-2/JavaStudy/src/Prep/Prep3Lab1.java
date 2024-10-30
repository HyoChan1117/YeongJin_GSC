package Prep;

import java.util.Scanner;

public class Prep3Lab1 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 사용자로부터 나이, 예약하려는 이벤트 코드, 예약을 원하는 날짜를 입력받는다.
        int age = sc.nextInt(); // 나이
        String eventCode = sc.nextLine(); // 이벤트 코드
        int reservedDate = sc.nextInt(); // 예약날짜

        if (reservedDate < 1 || reservedDate > 30) {
            System.out.println("잘못된 입력 입니다");
            return;
        }

        switch (eventCode) {
            case "E1":
                if (age < 18) {
                    System.out.println("나이 제한으로 예약할 수 없습니다");
                } else {
                    System.out.println("예약이 완료 되었습니다");
                }
                break;
            case "E2":
                if (reservedDate % 2 != 0) {
                    System.out.println("선택하신 날짜에는 예약 할 수 없습니다");
                } else {
                    System.out.println("예약이 완료 되었습니다");
                }
                break;
            case "E3":
                if (age < 16) {
                    System.out.println("나이 제한으로 예약할 수 없습니다");
                } else if (reservedDate % 7 != 0) {
                    System.out.println("선택하신 날짜에는 예약 할 수 없습니다");
                } else {
                    System.out.println("예약이 완료 되었습니다");
                }
                break;
            default:
                System.out.println("잘못된 입력 입니다");
        }
    }
}