package Prep.Lab.StarPrint;

import java.util.Scanner;

public class starMatrix {
    public static void main(String[] args) {
        // 메뉴를 선택하세요
        // 1번째 실행 // 게임 실행 횟수 출력
        // 1. M X N Matrix를 출력
        // 2. 좌상단->우하단 대각선 삭제 후 M X N Matrix 출력
        // 3. 좌상단->우하단 + 우상단->좌하단 대각선 삭제 후 M X N Matrix 출력
        // 4. 종료

        // 메뉴를 입력 받아 해당 프로그램 실행 후 다시 메뉴 출력
        // 1~4 이외 값 입력 시 에러메시지 출력 후 재입력 : 메뉴 출력 X
        // - 번호 입력만 새롭게 받기

        // 1번 : 사용자로부터 M, N 정수를 입력 받아, M X N Matrix를 출력하세요
        // 예) M : 3, N : 2
        //   * *
        //   * *
        //   * *
        //  예외처리 : M과 N이 0 또는 음의 정수인 경우, 재입력

        // 2번: 좌상단->우하단 대각선 삭제 후 M X N Matrix 출력
        // 예) M : 3, N : 3
        //     * *
        //   *   *
        //   * *
        //  예외처리 : M과 N이 0 또는 음의 정수인 경우, 재입력


        // 3번: 좌상단->우하단 + 우상단->좌하단 대각선 삭제 후 M X N Matrix 출력
        // 예) M : 3, N : 3
        //     *
        //   *   *
        //     *
        //  예외처리 : M과 N이 0 또는 음의 정수인 경우, 재입력

        Scanner sc = new Scanner(System.in);

        // 게임 횟수 카운트 변수 초기화
        int count = 0;

        // 메뉴 입력 변수 초기화 -> 최초 실행 시 메뉴 출력해야 하기 때문에 1로 초기화
        int inputValue = 1;

        // 무한루프 -> 게임 종료할 때까지 무한 반복
        while (true) {
            // inputValue가 1이상 4이하일 경우 메뉴를 출력한다.
            // 게임 실행 횟수 출력
            // 1. M X col Matrix를 출력
            // 2. 좌상단->우하단 대각선 삭제 후 M X col Matrix 출력
            // 3. 좌상단->우하단 + 우상단->좌하단 대각선 삭제 후 M X col Matrix 출력
            // 4. 종료
            System.out.println("----------------------------------------------------------------");
            System.out.println("게임 실행 횟수: " + count + "회");
            System.out.println("1. M X col Matrix를 출력");
            System.out.println("2. 좌상단->우하단 대각선 삭제 후 M X col Matrix 출력");
            System.out.println("3. 좌상단->우하단 + 우상단->좌하단 대각선 삭제 후 M X col Matrix 출력");
            System.out.println("4. 게임 종료");
            System.out.println("----------------------------------------------------------------");

            // 사용자로부터 메뉴를 입력 받는다.
            while(true) {
                System.out.println("메뉴를 선택하세요(1~4 이외의 값 입력 시 재입력)");
                inputValue = sc.nextInt();
                if(inputValue >= 1 && inputValue <= 4) {
                    break;
                }
                System.out.println("1~4 범위 내 정수 값을 입력하세요");
            }

            // 게임 종료 및 재입력
            // 만약 4를 선택했을 경우
            // 게임 종료 -> break
            if (inputValue == 4) {
                System.out.println("게임을 종료합니다.");
                break;
            }

            // 정수 M, col 초기화
            int row = 0;
            int col = 0;

            //  정수 M, N이 0 또는 음의 정수일 경우 계속 반복 -> 무한루프
            while (true) {
                // 정수 M과 N을 입력 받는다.(M, N이 0 또는 음의 정수일 경우 재입력)
                System.out.println("정수 M, N을 입력하세요(M, N이 0 또는 음의 정수일 경우 재입력): ");
                row = sc.nextInt();
                col = sc.nextInt();

                // M, N이 양의 정수일 경우 반복문 탈출
                if (row > 0 && col > 0) {
                    break;
                }
                // M, N이 0 또는 음의 정수일 경우 재입력
                else {
                    System.out.println("재입력하세요. M, N을 양의 정수로 입력하세요.");
                }
            }

            // Matrix 출력 메뉴(1, 2, 3)
            // 만약 1을 선택했을 경우
            // M X col Matrix를 출력한다.
            if (inputValue == 1) {
                for (int i = 0; i < row; i++) {
                    for (int j = 0; j < col; j++) {
                        System.out.print('*');
                    }
                    System.out.println();
                }
            }
            // 만약 2를 선택했을 경우
            // 좌상단->우하단 대각선 삭제 후 M X col Matrix 출력
            else if (inputValue == 2) {
                for (int i = 0; i < row; i++) {
                    for (int j = 0; j < col; j++) {
                        if (i == j) {
                            System.out.print(' ');
                        } else {
                            System.out.print('*');
                        }
                    }
                    System.out.println();
                }
            }
            // 만약 3을 선택했을 경우
            // 좌상단->우하단 + 우상단->좌하단 대각선 삭제 후 M X col Matrix 출력
            else {
                for (int i = 0; i < row; i++) {
                    for (int j = 0; j < col; j++) {
                        if (i == j || i + j == col - 1) {
                            System.out.print(' ');
                        } else {
                            System.out.print('*');
                        }
                    }
                    System.out.println();
                }
            }

            // 게임 한판 카운트 +1
            count++;
        }
    }
}