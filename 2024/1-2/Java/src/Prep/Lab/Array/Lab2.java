package Prep.Lab.Array;

import java.util.Scanner;

public class Lab2 {

    // 메뉴를 출력하는 메서드
    static void menuPrint() {
        System.out.println("메뉴");
        System.out.println("1. 학생 성적 입력");
        System.out.println("2. 입력된 학생 목록 출력");
        System.out.println("3. 학생 삭제하기");
        System.out.println("4. 종료");
    }

    // 중복 학번 검증 시 사용자 선택 메서드
    static void InputStuGrade() {
        Scanner sc = new Scanner(System.in);

        // 'Y'나 'q' 입력 시 반복문 탈출 / 그 외 값 입력 시 재입력 요구
        while (true) {
            System.out.println("중복된 입력이 있습니다.");
            System.out.print("덮어쓰기를 희망합니까? (Y: 덮어쓰기 진행, q: 메뉴로 돌아가기): ");
            char overlapInput = sc.next().charAt(0);

            // 'Y' 또는 'q' 입력 시 반복문 탈출
            if (overlapInput == 'Y' || overlapInput == 'q') {
                break;
            }
            else {
                System.out.println("재입력하세요. 잘못된 입력입니다.");
            }
        }

    }

    public static void main(String[] args) {

        // 2차원 배열 활용 학생 성적 계산기 확장버전

        Scanner sc = new Scanner(System.in);

        // 변수 초기화
        final int NUM_OF_STUDENTS = 3;
        final int NUM_OF_FIELDS = 6;

        int inputValue = 0; // 메뉴 선택 변수
        int numOfStudents = 0; // 현재 입력된 학생 수 변수

        // 학생 데이터는 2차원 배열에 저장
        // 초기 배열의 크기는 3행 6열로 설정
        float[][] stuTable = new float[NUM_OF_STUDENTS][NUM_OF_FIELDS];

        // 무한루프 -> 종료할 때까지 계속 반복
        while (true) {
            // 메뉴 출력 및 선택
            menuPrint();
            System.out.print("선택: ");
            inputValue = sc.nextInt();

            // switch문을 사용하여 각 메뉴 알고리즘 실행
            switch (inputValue) {
                // 1. 학생 성적 입력
                case 1:
                    // 학번, 국어, 영어, 수학 성적을 입력 받아 배열에 저장
                    // 국어, 영어, 수학의 합계와 평균 값도 계산한 후 배열에 저장
                    System.out.print("학번을 입력하세요: ");
                    int stuID = sc.nextInt(); // 학번 입력

                    // 중복 학번 검증
                    // 입력된 학번이 이미 존재하는 경우, (Y: 덮어쓰기 진행, q: 메뉴로 돌아가기) -> 그 외의 입력값은 재입력
                    InputStuGrade();

                    stuTable[numOfStudents][0] = stuID; // 학번 입력
                    System.out.print("국어 성적: ");
                    stuTable[numOfStudents][1] = sc.nextFloat(); // 국어 성적 입력
                    System.out.print("영어 성적: ");
                    stuTable[numOfStudents][2] = sc.nextFloat(); // 영어 성적 입력
                    System.out.print("수학 성적: ");
                    stuTable[numOfStudents][3] = sc.nextFloat(); // 수학 성적 입력

                    // 합계
                    stuTable[numOfStudents][4] = stuTable[numOfStudents][1] + stuTable[numOfStudents][2] + stuTable[numOfStudents][3];

                    // 평균
                    stuTable[numOfStudents][5] = (stuTable[numOfStudents][1] + stuTable[numOfStudents][2] + stuTable[numOfStudents][3]) / 3.0f;

                    numOfStudents++; // 현재 학생 수 1 증가

                // 2. 입력된 학생 목록 출력


                // 3. 학생 삭제하기


                // 4. 종료

            }

        }





    }
}
