package Exam.Midterm.test;

import java.util.Scanner;

public class myTest {
    // 연속된 연산자에 대한 점수 계산 함수
    public static int calculateScore(int comboCount, char operator) {
        int score = 0;
        if (comboCount == 2) {
            if (operator == '+') {
                score = 1; // 연속된 2개의 '+' 연산자: 1점 추가
            } else if (operator == '-') {
                score = -1; // 연속된 2개의 '-' 연산자: 1점 감점
            } else if (operator == '*') {
                score = 2; // 연속된 2개의 '*' 연산자: 2점 추가
            }
        } else if (comboCount == 3) {
            if (operator == '+') {
                score = 3; // 연속된 3개의 '+' 연산자: 3점 추가
            } else if (operator == '-') {
                score = -3; // 연속된 3개의 '-' 연산자: 3점 감점
            } else if (operator == '*') {
                score = 5; // 연속된 3개의 '*' 연산자: 5점 추가
            }
        }
        return score;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 변수 초기화
        int inputValue = 0; // 슬롯머신 개수 입력 변수
        String gameResult = ""; // 게임 결과 변수
        int totalScore = 0; // 전체 점수 변수
        int roundScore = 0; // 그룹 점수 변수
        int count = 1; // 현재 라운드 변수 -> 1라운드부터 시작
        int combo = 0; // 연속된 연산자 콤보 변수
        int slotItem = 0; // 연속된 연산자 저장 변수

        // 연산자 배열 생성
        // 세 가지 연산자(+, -, *)를 포함하는 char type 1차원 배열 생성
        char operator[] = { '+', '-', '*' };

        // 무한루프 -> 반복 한 번 당 게임 한 판
        while (true) {
            // 슬롯 개수 입력
            // 무한루프 -> 유효하지 않은 값을 입력 받았을 경우 재입력
            while (true) {
                // 사용자로부터 3~7 사이의 정수를 입력 받는다.
                System.out.print("Enter the number of slots (3~7): ");
                inputValue = sc.nextInt();

                // 유효한 입력값을 받으면 반복문 종료 -> break
                if (inputValue >= 3 && inputValue <= 7) {
                    break;
                }
                // 입력값이 유효하지 않으면 오류 메시지를 출력하고 재입력 메시지 출력
                else {
                    System.out.println("Invalid input. Please enter a number between 3 and 7.");
                }

            }
            // 연산자를 무작위로 선택하여 저장하는 배열 생성
            char slotItems[] = new char[inputValue];

            // 랜덤 슬롯 결과 생성
            // 설정된 슬롯 개수만큼 연산자를 무작위로 선택하여 결과 배열 생성
            // 반복의 횟수는 슬롯의 개수(배열의 원소 개수)만큼! -> for문
            for (int i = 0 ; i < slotItems.length ; i++ ) {
                // 0 <= R < 3 -> 0, 1, 2 : 랜덤값 받기
                int randNum = (int)(Math.random() * 3);

                // 랜덤으로 선택된 연산자를 저장하는 배열에 값 저장
                slotItems[i] = operator[randNum];
            }

            // 출력 형식
            // 현재 라운드 출력
            // 설정된 슬롯 개수만큼 연산자를 무작위로 선택하여 결과 배열 생성
            System.out.println("--- Round " + count + " ---");
            System.out.print("Result: [");
            for (int i = 0; i < slotItems.length ; i++) {
                System.out.print(slotItems[i] + ", ");
            }
            System.out.println("]");

            // 점수 규칙:
            // 연속된 연산자 체크
            int comboCount = 1; // 연속된 동일 연산자 개수
            for (int i = 0; i < slotItems.length - 1; i++) {
                if (slotItems[i] == slotItems[i + 1]) {
                    comboCount++; // 연속된 동일 연산자 개수 증가
                }
                else {
                    // 연속된 동일 연산자가 끝났을 때 점수 계산
                    roundScore += calculateScore(comboCount, slotItems[i]);
                    comboCount = 1; // 연속된 연산자 초기화
                }
            }
            // 마지막 연속된 연산자 처리
            roundScore += calculateScore(comboCount, slotItems[slotItems.length - 1]);

            // 라운드 점수 출력
            System.out.println("Round score: " + roundScore);
            System.out.println("totol score: " + totalScore);
            totalScore += roundScore;

            // 승리/패배 조건
            // 총점이 5점 이상이면 승리, 총점이 -5점 이하이면 패배
            if (totalScore >= 5 || totalScore <= -5) {
                gameResult = (totalScore >= 5) ? "Congratulations, you win!" : "Too bad, you lose!";
                break;
            }

            // 결과 출력
            System.out.println(gameResult);


            // 게임 카운트 +1
            count++;
            roundScore = 0; // roundScore 초기화
        }
    }
}
