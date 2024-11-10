package Prep.RockPaperScissors;

import java.util.Scanner;

public class Game1 {

    public static void main(String[] args) {

        // 가위, 바위, 보 게임 만들기

        // 키보드로부터 Scissors, Rock, Paper를 입력 받아,
        // 아래와 같이 결과를 출력하라
        // 예 1) 승리 - 사용자 : Scissors, 컴퓨터 : Paper
        // 예 2) 패배 - 사용자 : Scissors, 컴퓨터 : Rock
        // 예 3) 무승부 - 사용자 : Scissors, 컴퓨터 : Scissors

        // 고려사항
        // 1. 사용자로부터 키보드 입력 시 "Scissors, Rock, Paper" 이외 값은
        // 재입력 처리
        // 2. "Quit" 입력 전까지 계속해서 게임 실행

        Scanner sc = new Scanner(System.in);

        // 무한루프 -> 게임 한 판은 반복 한 번
        while (true){
            // 사용자로부터 키보드를 입력 받는다. "Scissors, Rock, Paper를 입력하세요: "
            System.out.print("Scissors, Rock, Paper를 입력하세요: ");
            String userInput = sc.nextLine();

            // switch expression을 사용하여 반환값을 정수화
            // 가위: "Scissors" -> 0
            // 바위: "Rock" -> 1
            // 보: "Paper" -> 2
            // 종료: "Quit" -> 3
            // 재입력: default -> -1
            int inputValue = switch (userInput) {
                case "Scissors" -> 0;
                case "Rock" -> 1;
                case "Paper" -> 2;
                case "Quit" -> 3;
                default -> -1;
            };

            // "Quit"를 입력하면 게임을 종료한다. -> break
            if (inputValue == 3) {
                System.out.println("게임을 종료합니다.");
                break;
            }

            // 잘못된 값을 입력하면 "Scissors, Rock, Paper 중 하나를 입력 하세요." 문구 출력 후 재입력 -> continue
            if (inputValue == -1) {
                System.out.println("재입력하세요. Scissors, Rock, Paper 중 하나를 입력 하세요.");
                continue;
            }

            // 컴퓨터 난수 발생
            String cpuInput[] = { "Scissors", "Rock", "Paper" };
            int randCpu = (int)(Math.random() * 3); // => 0 <= R < 3 => 0, 1, 2

            // 승패 결과
            // 무승부
            // inputValue == randCpu
            if (inputValue == randCpu) {
                System.out.println("컴퓨터: " + cpuInput[randCpu] + " 무승부입니다.");
            }

            // 승리
            else if ((inputValue == 0 && randCpu == 3) ||
                    (inputValue == 1 && randCpu == 0) ||
                    (inputValue == 2 && randCpu == 1)) {
                System.out.println("컴퓨터: " + cpuInput[randCpu] + " 승리입니다.");
            }
            // 패배
            else {
                System.out.println("컴퓨터: " + cpuInput[randCpu] + " 패배입니다.");
            }
        }

    }
}
