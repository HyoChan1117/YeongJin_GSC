package Prep;

import java.util.Scanner;

public class Prep1Lab1 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 사용자의 나이를 입력 받는다. => 0과 음수는 없음. 양수만 입력
        System.out.print("사용자의 나이를 입력해주세요: ");
        int age = sc.nextInt();

        //

        // 이용권 판별 후 출력한다.
        // 어린이 이용권: 12세 이하 어린이 대상
        String grade = "";
        if (age <= 12) {
            grade = "어린이";
        }

        // 청소년 이용권: 13세 이상 18세 이하 청소년 대상
        else if (age >= 13 && age <= 18) {
            grade = "청소년";
        }

        // 성인 이용권: 19세 이상 성인 대상
        else {
            grade = "성인";
        }

        System.out.println(grade + "이용권을 사용할 수 있습니다.");

    }
}
