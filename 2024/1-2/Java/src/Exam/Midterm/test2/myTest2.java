package Exam.Midterm.test2;

import java.util.Scanner;

public class myTest2 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 슬롯머신 게임 구현하기 프로그램 만들기
        // 변수 초기화
        int inputValue = 0; // 슬롯 개수 입력 변수
        int count = 1; // 게임 라운드 카운트 변수
        int totalScore = 0; // 전체 점수 변수
        int groupScore = 0; // 라운드 점수 변수
        String result = ""; // 결과 변수
        int combo = 1; // 콤보 변수

        // char type 연산자 배열 생성 ( +, -, * )
        char operator[] = {'+', '-', '*'};

        // 슬롯 개수 입력 -> 무한 루프(범위 외 정수 입력 시 재입력)
        while (true) {
            // 사용자로부터 3~7 사이의 정수를 입력받는다. -> 슬롯 개수 설정
            System.out.print("Enter the number of slots (3~7): ");
            inputValue = sc.nextInt();
            // 입력값이 유효하면 반복문 종료
            if (inputValue >= 3 && inputValue <= 7) {
                break;
            }
            // 입력값이 유효하지 않으면 오류 메시지를 출력하고 재입력 요구
            else {
                System.out.println("Invalid input. Please enter a number between 3 and 7.");
            }
        }

        // 무한 루프 -> 한 라운드 당 반복 한 번
        while (true) {
            // 랜덤으로 선택된 연산자를 저장하는 배열
            char slotItems[] = new char[inputValue];

            // 랜덤 연산자 선택
            // 각 라운드에서 슬롯머신을 돌리면 +, -, * 문자 중 3개가 무작위로 선택
            // 선택된 3개의 연산자를 1차원 Array에 저장
            for (int i = 0; i < slotItems.length; i++) {
                int randnum = (int) (Math.random() * 3);
                slotItems[i] = operator[randnum];
            }

            // 라운드 출력
            // 아무 키 입력 시 라운드 시작
            System.out.println("--- Round " + count + " ---");
            System.out.print("Press Enter to spin the slot machine: ");
            sc.nextLine();
            System.out.println();
            System.out.print("Result: [");
            for (int i = 0; i < slotItems.length; i++) {
                System.out.print(slotItems[i] + ((i < slotItems.length - 1) ? ", " : "]"));
            }
            System.out.println(); // 결과 출력 구분

            // 콤보 점수 계산
            // 동일한 연산자의 개수를 계산하여, 아래 규칙에 따라 보너스 점수 부여
            // A. 연속된 연산자가 두 개일 경우
            // B. 연속된 연산자가 세 개일 경우
            // 점수 계산
            for (int i = 0; i < slotItems.length; i++) {
                // 연산자가 연속되는 경우
                if (i < slotItems.length - 1 && slotItems[i] == slotItems[i + 1]) {
                    combo++;
                }
                // 연속이 끝났을 경우 계산
                else {
                    // 연속된 문자 수 -> 2나 3
                    if (combo == 2 || combo >= 3) {
                        switch (slotItems[i]) {
                            case '+':
                                groupScore += (combo == 2) ? 1 : 3;
                                break;
                            case '-':
                                groupScore -= (combo == 2) ? 1 : 3;
                                break;
                            case '*':
                                groupScore += (combo == 2) ? 2 : 5;
                                break;
                        }
                    }
                    combo = 1; // combo 변수 초기화
                }
            }

            // 그룹 점수 계산
            // 현재 라운드 점수를 계산하여 출력
            System.out.println("Group Scores: " + groupScore);

            // 전체 점수 계산
            // 각 그룹별 점수를 합산하여 라운드 점수 계산
            totalScore += groupScore; // 라운드가 끝날 때마다 점수 합산
            System.out.println("Total Score: " + totalScore);

            // 승리, 패배 조건
            // 총점이 5점 이상이면 승리, -5점 이하이면 패배
            if (totalScore >= 5 || groupScore <= -5) {
                result = (totalScore >= 5) ? "Congratulations, you win!" : "Too bad, you lose!";
                // 결과 출력
                System.out.println(result);
                break;
            }

            // groupScore 초기화
            groupScore = 0;

            // count +1
            count++;

        }
    }
}
