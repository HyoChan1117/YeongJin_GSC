package Prep.Lab;

import java.util.Scanner;

public class Lab3_2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 입력받기
        System.out.print("주당 수업 시간(시수/주): ");
        int weeklyHours = scanner.nextInt();

        System.out.print("결석한 총 시간: ");
        int absenceHours = scanner.nextInt();

        System.out.print("지각 횟수: ");
        int tardyCount = scanner.nextInt();

        // 총 수업 시간 계산
        int totalHours = weeklyHours * 15;

        // 지각 3회를 결석 1시간으로 처리
        int totalAbsenceHours = absenceHours + (tardyCount / 3);

        // 결석 시간이 총 수업 시간의 1/4을 초과하는지 확인
        if (totalAbsenceHours > totalHours / 4) {
            System.out.println("F (학점 미부여)");
        } else {
            // 출석 점수 계산
            double attendanceScore = 20 - (20.0 * totalAbsenceHours / totalHours);
            System.out.printf("출석 점수: %.2f점\n", attendanceScore);
        }

        scanner.close();
    }
}