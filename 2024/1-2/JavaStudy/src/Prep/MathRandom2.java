package Prep;

import java.util.Scanner;

public class MathRandom2 {
    public static void main(String[] args) {

        // 가위, 바위, 보 게임 만들기
        // 사용자로부터 Scissors, Rock, Paper
        // - Scissors, Rock, Paper 중 하나를 입력 하세요.
        // 컴퓨터가 난수를 이용해서 가위-바위-보 중 하나 선택
        // 결과 출력
        // 예 1) 승리: 사용자 - 가위, 컴퓨터 - 보
        // 예 2) 패배: 사용자 - 가위, 컴퓨터 - 바위
        // 예 3) 무승부: 사용자 - 가위, 컴퓨터 - 가위
        // 그리고 게임 재실행

        // 사용자로부터 Scissors, Rock, Paper 입력 예외 처리
        // - Scissors, Rock, Paper 이외의 값이 입력 될 경우
        // "잘못된 입력 값 입니다, Scissors, Rock, Paper 중 하나를 입력 하세요."
        // 출력 후 재입력
        // "quit"를 입력하면 프로그램 종료

        Scanner sc = new Scanner(System.in);

        // 무한루프 - 한번의 반복은 게임 한판
        while(true) {
            // 사용자로부터 Scissors, Rock, Paper 중 하나를 입력 받는다.
            System.out.println("Scissors, Rock, Paper 중 하나를 입력하세요: ");
            String userInput = sc.nextLine();

            int inputValue = switch (userInput){
                case "Scissors" -> 0;
                case "Rock" -> 1;
                case "Paper" -> 2;
                case "Quit" -> 3;
                default -> -1;
            };

            // 예외 처리
            // 1: Quit 이면 -> 프로그램 종료 -> break
            if (inputValue == 3) {
                break;
            }

            // 2: 잘못된 입력 -> 재입력 -> continue
            if (inputValue == -1) {
                System.out.println("잘못된 입력입니다. Scissors, Rock, Paper 중 하나를 입력하세요.");
                continue;
            }

            // 컴퓨터 선택 : 가위, 바위, 보 중 하나 선택
            // 난수 이용 : 0 ~ 2 사이 난수 발생 후 "가위, 바위, 보"에 매칭
            String sciRockPaper[] = {"Scissors", "Rock", "Papers"};
            int computerNum = (int)(Math.random() * 3);
            String computerInput = sciRockPaper[computerNum];


            // 승패 계산
            // 사용자가 가위를 내는 경우
            if (inputValue == 0) {
                // 컴퓨터가 가위를 내는 경우 -> 무승부
                if (computerInput == "Scissors") {
                    System.out.println("컴퓨터: " + computerInput + " 무승부");
                }

                // 컴퓨터가 바위를 내는 경우 -> 패배
                else if (computerInput == "Rock") {
                    System.out.println("컴퓨터: " + computerInput + " 패배");
                }

                // 컴퓨터가 보를 내는 경우 -> 승리
                else {
                    System.out.println("컴퓨터: " + computerInput + " 승리");
                }

            }

            // 사용자가 바위를 내는 경우
            else if (inputValue == 1) {
                // 컴퓨터가 가위를 내는 경우 -> 승리
                if (computerInput == "Scissors") {
                    System.out.println("컴퓨터: " + computerInput + " 승리");
                }

                // 컴퓨터가 바위를 내는 경우 -> 무승부
                else if (computerInput == "Rock") {
                    System.out.println("컴퓨터: " + computerInput + " 무승부");
                }

                // 컴퓨터가 보를 내는 경우 -> 패배
                else {
                    System.out.println("컴퓨터: " + computerInput + " 패배");
                }

            }

            // 사용자가 보를 내는 경우
            else if (inputValue == 2) {
                // 컴퓨터가 가위를 내는 경우 -> 패배
                if (computerInput == "Scissors") {
                    System.out.println("컴퓨터: " + computerInput + " 패배");
                }

                // 컴퓨터가 바위를 내는 경우 -> 승리
                else if (computerInput == "Rock") {
                    System.out.println("컴퓨터: " + computerInput + " 승리");
                }

                // 컴퓨터가 보를 내는 경우 -> 무승부
                else {
                    System.out.println("컴퓨터: " + computerInput + " 무승부");
                }

            }
        }

    }
}