package Prep.Lab.Array;

import java.util.Scanner;

public class Lab1_1 {
    // 2차원 배열 활용 학생 성적 계산기

    // 총 학생 수 : 3명
    // 입력: 학번, 국어, 영어, 수학 / 자동 계산: 합계, 평균
    // 3 x 6 Matrix(float)

    // 메뉴 출력
    // 메뉴
    // 1. 학생 성적 입력
    // 2. 입력된 학생 목록 출력
    // 3. 학생 삭제하기
    // 4. 종료

    // 메뉴를 출력하는 매서드
    static void menuPrint() {
        System.out.println("메뉴");
        System.out.println("1. 학생 성적 입력");
        System.out.println("2. 입력된 학생 목록 출력");
        System.out.println("3. 학생 삭제하기");
        System.out.println("4. 종료");
    }

    // 입력된 학생 목록 출력 매서드
    static void prtMatrix(float[][] argMatrix, int argNumOfStudent) {

        // 만약 학번이 0일 경우 출력하지 않는다. -> 건너뛰기
        if (argNumOfStudent <= 0) {
            System.out.println("입력된 학생 정보가 없습니다.");
            return;
        }

        for (int i = 0; i < argNumOfStudent; i++) {
            // 학번이 0이 아닌 경우 해당 학번 정보 출력
            System.out.println("[학번: " + (int) argMatrix[i][0] + "]" +
                    " 국어: " + argMatrix[i][1] +
                    ", 영어: " + argMatrix[i][2] +
                    ", 수학: " + argMatrix[i][3] +
                    ", 합계: " + argMatrix[i][4] +
                    ", 평균: " + argMatrix[i][5]);
        }
    }

    // 학생 정보 입력 및 계산 메서드
    static boolean addStdToMatrix(float[][] argStdMatrix, int argNumOfStudent) {

        Scanner sc = new Scanner(System.in);

        // stuTable의 행의 원소의 개수가 현재 학생의 수보다 작거나 같을 때
        if (argStdMatrix.length <= argNumOfStudent) {
            System.out.println("Matrix 크기 초과, Matrix 크기를 확장 하세요!");
            return false; // false 반환
        }

        System.out.print("학번을 입력하세요: ");
        argStdMatrix[argNumOfStudent][0] = sc.nextFloat(); // 학번 성적을 실수로 입력
        System.out.print("국어 성적: ");
        argStdMatrix[argNumOfStudent][1] = sc.nextFloat(); // 국어 성적을 실수로 입력
        System.out.print("영어 성적: ");
        argStdMatrix[argNumOfStudent][2] = sc.nextFloat(); // 영어 성적을 실수로 입력
        System.out.print("수학 성적: ");
        argStdMatrix[argNumOfStudent][3] = sc.nextFloat(); // 수학 성적을 실수로 입력
        System.out.println("입력이 완료되었습니다.");

        // 합계 계산
        argStdMatrix[argNumOfStudent][4] = argStdMatrix[argNumOfStudent][1] + argStdMatrix[argNumOfStudent][2] + argStdMatrix[argNumOfStudent][3];

        // 평균 계산
        argStdMatrix[argNumOfStudent][5] = argStdMatrix[argNumOfStudent][4] / 3.0f;

        return true; // true 반환
    }

    // 삭제하려는 학번의 인덱스 번호를 반환하는 메서드
    static int getRowIndexByStdId(int argStdId, float[][] argStdMatrix, int argNumOfStudent) {
        // 삭제하려는 학번이 배열 내에 있을 경우, 그 인덱스 번호를 반환
        for (int i = 0; i < argNumOfStudent; i++) {
            if ((int) argStdMatrix[i][0] == argStdId) {
                return i;
            }
        }

        // 삭제하려는 학번이 배열 내에 없을 경우, '-1' 반환
        return -1;
    }

    // 배열로부터 학생의 학번을 삭제하기 위한 메서드
    static boolean delStdFromMatrix(int argIndexNum, float[][] argMatrix, int argNumOfStudent) {

        // 삭제하려는 학번의 인덱스 번호가 현재 학생 수보다 많거나 같을 경우
        if (argIndexNum >= argNumOfStudent) {
            System.out.println("잘못된 인덱스 번호 입력: At  boolean delStdFromMatrix() ");
            return false; // 조건문을 false로 만들어 numOfStudens의 수를 감소 시키지 않기 위해
        }

        // 삭제하려는 학번의 인덱스 번호로 행을 하나씩 올린다.
        for (int i = argIndexNum; i < argNumOfStudent - 1; i++) {
            for (int j = 0 ; j < argMatrix[0].length ; j++) {
                argMatrix[i][j] = argMatrix[i + 1][j];
            }
        }

        // 마지막 행은 '0.0f'로 초기화
        for (int i = 0; i < argMatrix[0].length; i++) {
            argMatrix[argNumOfStudent - 1][i] = 0.0f;
        }

        return true; // 조건문을 true로 만들어 numOfStudents의 수를 감소 시키기 위해
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 변수 초기화
        final int NUM_OF_STUDENTS = 3;
        final int NUM_OF_FIELDS = 6;

        int inputValue = 0; // 메뉴 입력 변수
        float studentID = 0; // 학번 변수
        int numOfStudent = 0; // 현재 학생 수 변수
        int delIndex = 0; // 삭제할 인덱스 변수

        boolean isRunning = true; // 게임 플래그 변수

        // 입력된 학생 성적을 저장하는 배열 생성
        float[][] stuTable = new float[NUM_OF_STUDENTS][NUM_OF_FIELDS];

        // 무한루프 -> 동작이 이루어질 때마다 메뉴가 계속 출력됨
        while (isRunning) {
            // 메뉴판 출력
            menuPrint();

            // 메뉴판 선택
            System.out.print("선택: ");
            inputValue = sc.nextInt(); // 메뉴판 입력

            if (inputValue == 4) {
                // 4. 종료
                System.out.println("프로그램을 종료합니다.");
                break;
            }

            // switch문을 사용하여 입력 받은 메뉴의 번호 알고리즘 실행
            switch (inputValue) {
                case 1:
                    // 1. 학생 성적 입력
                    // 학번과 국어, 영어, 수학 성적을 차례대로 입력 받는다.
                    if (addStdToMatrix(stuTable, numOfStudent)) {
                        numOfStudent++; // 학생 수 변수 ++
                    }
                    break;
                case 2:
                    // 2. 입력된 학생 목록 출력
                    // 출력 형식: [학번] 국어: xx, 영어: xx, 수학: xx, 합계: xx, 평균: xx.xx
                    // 만약 0 < numOfStudent <= NUM_OF_STUDENTS
                    System.out.println("학생 목록: ");
                    prtMatrix(stuTable, numOfStudent);
                    break;
                case 3:
                    // 3. 학생 삭제하기
                    // 무한루프 -> 삭제할 학생 목록을 출력하고 '-1' 입력 전까지 계속 출력

                    System.out.println("학생 목록: ");
                    prtMatrix(stuTable, numOfStudent);

                    // 무한루프 -> 학생의 학번을 삭제하고, 메뉴판 출력 / 해당 학번이 없을 경우 재입력 / -1 입력 시 메뉴판 출력
                    while (true) {
                        // 플래그 변수 선언
                        boolean flagDelID = false;

                        // 삭제할 학생의 학번을 입력 받는다. (-1 입력 시 메뉴 출력으로 돌아감)
                        System.out.println("삭제할 학생의 학번을 입력하세요 (-1: 이전 메뉴로): ");
                        int delStuID = sc.nextInt();

                        // '-1'을 입력할 경우, 반복문 탈출 -> 이전 메뉴로 돌아감
                        if (delStuID == -1) {
                            break;
                        }

                        // 삭제하려는 학번이 배열 내에 있을 경우, 해당 인덱스 번호를 / 배열 내에 없을 경우, '-1' 저장
                        int indexNum = getRowIndexByStdId(delStuID, stuTable, numOfStudent);

                        // 삭제하려는 학번의 인덱스 번호가 있을 경우 -> '-1'이 아닌 경우
                        if (indexNum != -1) {
                            // 삭제하려는 학번의 인덱스 번호가 현재의 학생 수보다 적을 경우
                            if (delStdFromMatrix(indexNum, stuTable, numOfStudent)) {
                                numOfStudent--;
                            }
                            // 현재 학생 목록을 출력한 후, 반복문 종료
                            prtMatrix(stuTable, numOfStudent);
                            break;
                        }

                        // indexNum == -1이면 flagDelID는 true
                        if (indexNum == -1) {
                            flagDelID = true;
                        }

                        // 해당 학번이 없을 경우, 재입력
                        if (flagDelID) {
                            System.out.println("해당 학번이 존재하지 않습니다. 다시 입력해주세요.");
                        }
                    }
                    break;
                // 1~4의 정수를 입력 받지 못한 경우 재입력 요구
                default:
                    System.out.println("잘못된 입력입니다. 다시 선택해주세요.");
                    break;
            }
        }
    }
}
