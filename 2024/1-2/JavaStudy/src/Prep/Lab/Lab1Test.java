package Prep.Lab;

import java.util.Scanner;

public class Lab1Test {
    // 메뉴를 출력하는 매서드
    static void menuPrint() {
        System.out.println("메뉴");
        System.out.println("1. 학생 성적 입력");
        System.out.println("2. 입력된 학생 목록 출력");
        System.out.println("3. 학생 삭제하기");
        System.out.println("4. 종료");
    }

    // 입력된 학생 목록 출력 매서드
    static void prtMatrix(float[][] argMatrix, int argNumOfStd) {
        for (int i = 0; i < argNumOfStd; i++) {
            for (int j = 0; j < argMatrix[i].length; j++) {
            }
            // 만약 학번이 0으로 초기화 됐을 경우 출력하지 않는다.
            if (argMatrix[i][0] == 0){
            }
            // 학번이 0이 아닌 경우
            else {
                System.out.println("[학번: " + (int)argMatrix[i][0] + "]" + " 국어: " + argMatrix[i][1] + ", 영어: " + argMatrix[i][2] + ", 수학: " + argMatrix[i][3] + ", 합계: " + argMatrix[i][4] + ", 평균: " + argMatrix[i][5]);
            }
        }
    }

    public static void main(String[] args) {
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

        Scanner sc = new Scanner(System.in);

        // 변수 초기화
        int inputValue = 0; // 메뉴 입력 변수
        float studentID = 0; // 학번 변수

        final int NUM_OF_STUDENTS = 3;
        final int NUM_OF_FIELDS = 6;

        int numOfStudent = 0; // 학생 수 변수

        boolean isRunning = true;

        // 입력된 학생 성적을 저장하는 배열 생성
        float[][] stuTable = new float[NUM_OF_STUDENTS][NUM_OF_FIELDS];

        // 무한루프 -> 동작이 이루어질 때마다 메뉴가 계속 출력됨
        while (isRunning) {
            // 메뉴판 출력
            menuPrint();

            // 메뉴판 선택
            System.out.print("선택: ");
            inputValue = sc.nextInt();

            // switch
            switch (inputValue) {
                case 1:
                    // 1. 학생 성적 입력
                    // 학번과 국어, 영어, 수학 성적을 차례대로 입력 받는다.
                    System.out.print("학번을 입력하세요: "); // 학번을 실수로 입력
                    studentID = sc.nextFloat();
                    stuTable[numOfStudent][0] = studentID;
                    System.out.print("국어 성적: "); // 국어 성적을 실수로 입력
                    stuTable[numOfStudent][1] = sc.nextFloat();
                    System.out.print("영어 성적: "); // 영어 성적을 실수로 입력
                    stuTable[numOfStudent][2] = sc.nextFloat();
                    System.out.print("수학 성적: "); // 수학 성적을 실수로 입력
                    stuTable[numOfStudent][3] = sc.nextFloat();
                    System.out.println("입력이 완료되었습니다."); // 입력이 완료 되었다는 문구 출력

                    // 합계 계산
                    stuTable[numOfStudent][4] = stuTable[numOfStudent][1] + stuTable[numOfStudent][2] + stuTable[numOfStudent][3];

                    // 평균 계산
                    stuTable[numOfStudent][5] = stuTable[numOfStudent][4] / 3.0f;
                    numOfStudent++; // 학생 수 변수 ++
                    break;

                case 2:
                    // 2. 입력된 학생 목록 출력
                    // 출력 형식: [학번] 국어: xx, 영어: xx, 수학: xx, 합계: xx, 평균: xx.xx
                    // 만약 0 < numOfStudent <= NUM_OF_STUDENTS
                    if (numOfStudent > 0 && numOfStudent <= NUM_OF_STUDENTS) {
                        // 현재 입력된 학생들의 성적 목록을 출력
                        System.out.println("학생 목록: ");
                        prtMatrix(stuTable, numOfStudent);
                    }
                    // 데이터가 없는 경우 "입력된 학생 정보가 없습니다." 출력
                    // 출력 후 메뉴로 복귀
                    else {
                        System.out.println("입력된 학생 정보가 없습니다.");
                    }
                    break;
                case 3:
                    // 3. 학생 삭제하기
                    // 무한루프 -> -1 입력 시 이전 메뉴로, 범위 외 값 입력 시 재입력

                    if (numOfStudent <= 0) {
                        System.out.println("삭제할 학생이 없습니다.");
                        break;
                    }

                    while (true) {
                        // 학생 정보 출력하기
                        System.out.println("학생 목록: ");
                        // 출력 형식: [학번] 국어: xx, 영어: xx, 수학: xx, 합계: xx, 평균: xx.xx
                        prtMatrix(stuTable, numOfStudent);

                        // 삭제할 학생의 학번을 입력 받음
                        System.out.println("삭제할 학생의 학번을 입력하세요 (-1: 이전 메뉴로): ");
                        int delStuID = sc.nextInt();

                        // 만약 studentID가 0이거나 범위 외 값 입력 시
                        if (delStuID <= -1) {
                            if (delStuID == -1){
                                System.out.println("이전 메뉴로 돌아갑니다.");
                                break;
                            } else {
                                System.out.println("학번은 음수일 수 없습니다.");
                            }
                        }
                        else {
                            // 학생 삭제
                            // 삭제하려는 학번의 인덱스 번호를 찾는다.


                            // 행 이동: 삭제할 행 이후의 행들을 위로 이동
                            for (int i =  ; i < numOfStudent ; i++) {
                                for (int j = 0; j < stuTable[i].length; j++) {
                                    stuTable[i][j] = stuTable[i + 1][j];
                                }
                            }

                            // 마지막 행을 0으로 초기화한다.
                            for (int j = 0 ; j < stuTable[stuTable.length - 1].length; j++) {
                                stuTable[numOfStudent - 1][j] = 0;
                            }

                            System.out.println("삭제가 완료되었습니다.");
                            numOfStudent--; // 삭제하면 학생 숫자 1 감소
                        }
                    }
                    break;
                case 4:
                    // 4. 종료
                    // 프로그램 종료
                    System.out.println("프로그램 종료");
                    isRunning = false; // false로 하면 무한루프 종료 -> 게임 종료
                    break;
                default:
                    // 메뉴에 없는 정수를 입력했을 경우 재입력 문구
                    System.out.println("잘못된 입력입니다. 다시 선택해주세요.");
                    break;
            }
        }
    }
}
