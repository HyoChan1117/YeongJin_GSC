package Lab.FlowControl;

import java.util.*;

public class Lab1 {
    public static void main(String[] args) {

        // 사용자가 입력한 나이를 기준으로 여러 연령대에 맞는 메시지를 출력하는 프로그램 작성
        Scanner sc = new Scanner(System.in);

        // 정수 age 초기화
        int age = 0;

        // 양수를 입력 받을 때까지 무한반복
        while (true) {
            // 나이를 입력 받는다.
            System.out.print("나이를 입력하세요: ");
            age = sc.nextInt();

            // 음수를 입력 받으면 무한반복
            if (age < 0) {
                System.out.println("나이는 음수가 될 수 없습니다. 다시 입력하세요.");
            } else {
                break;
            }
        }

        // 조건에 따라 메시지 출력
        // 0세 이상 12세 이하는 어린이
        if (age >= 0 && age <= 12) {
            System.out.println("어린이");
        }
        // 13세 이상 17세 이하는 청소년
        else if (age >= 13 && age <= 17) {
            System.out.println("청소년");
        }
        // 18세 이상 64세 이하는 성인
        else if (age >= 18 && age <= 64) {
            System.out.println("성인");
        }
        // 65세 이상은 노인
        else {
            System.out.println("노인");
        }

    }
}