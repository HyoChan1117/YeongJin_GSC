package Prep.RockPaperScissors;

import LearningContents.FlowControl.Random.MathRandom;

import java.util.Scanner;

public class Game3 {
    public static void main(String[] args) {

        // 가위, 바위, 보 게임을 구현
        // 사용자로부터 "Scissors, Rock, Paper"를 입력 받아
        // 컴퓨터는 "Scissors, Rock, Paper" 중 하나를 랜덤하게 선택

        // 결과 값 출력:
        // 예 1) 승리 - 사용자 : 가위, 컴퓨터 : 보
        // 예 2) 패배 - 사용자 : 가위, 컴퓨터 : 바위
        // 예 3) 무승부 - 사용자 : 가위, 컴퓨터 : 가위

        // "Exit"를 입력하기 전까지 계속해서 게임 실행
        // 보너스 점수 구현
        // 사용자 승리 시 : 1점, 패배 시 : -1
        // 연속 승리 시 : 3점, 2 -> 3 -> 4...
        // 보너스 점수가 7점 이상 또는 -7점 이면 종료
        // - 사용자 승리 : 보너스 점수 XX점
        // - 사용자 패배 : 보너스 점수 XX점

        Scanner sc = new Scanner(System.in);

        // 보너스 점수 변수 및 연속 승리 변수 초기화
        int count = 0;
        int winwin = 0;

        // 결과 판별 변수
        String result = "";

        // 컴퓨터의 경우
        String cpuInput[] = { "Scissors", "Rock", "Paper" };

        // 무한루프 -> 한 번 반복은 게임 한판
        while (true) {
            // count >= 7 또는 count <= -7인 경우
            if (count >= 7 || count <= -7) {
                result = (count >= 7) ? "승리" : "패배";  // count >= 7이면 "승리", 아니면 "패배"
                // 결과 출력
                System.out.println("사용자 " + result + ": 보너스 점수 " + count + "점, 게임을 종료합니다.");
                break;
            }

            // 사용자로부터 "Scissors, Rock, Paper"를 입력 받는다.
            System.out.print("Scissors, Rock, Paper 중 하나를 입력하세요: ");
            String userInput = sc.nextLine();

            // 입력 받은 문자열을 정수형으로 받는다. -> switch expression
            // "Scissors" -> 0
            // "Rock" -> 1
            // "Paper" -> 2
            // "Quit" -> 3 => 게임 종료
            // default -> -1 => 재입력
            int inputValue = switch (userInput) {
                case "Scissors" -> 0;
                case "Rock" -> 1;
                case "Paper" -> 2;
                case "Exit" -> 3; // 게임 종료
                default -> -1; // 재입력
            };

            // inputValue == 3 -> 게임종료 -> break
            if (inputValue == 3) {
                System.out.println("게임을 종료합니다.");
                break;
            }

            // inputValue == -1 -> 재입력 -> continue
            if (inputValue == -1) {
                System.out.println("재입력하세요. Scissors, Rock, Paper 중 하나를 입력하세요.");
                continue;
            }

            // 컴퓨터 난수 생성
            int cpunum = (int)(Math.random() * 3);

            // 승패 결정
            // 무승부
            if (inputValue == cpunum) {
                result = "무승부";
                winwin = 0; // 무승부 했을 경우 winwin 초기화
            }
            // 승리
            else if (inputValue == 0 && cpunum == 2 ||
                     inputValue == 1 && cpunum == 0 ||
                     inputValue == 2 && cpunum == 1) {
                result = "승리";
                winwin++; // 승리 시 계속 1점 추가 -> 무승부, 패배 시 초기화

                // 연속 승리를 했을 경우 -> 보너스 점수 3점 추가
                count += winwin >= 2 ? 3 : 1; // winwin이 2보다 크거나 같으면 3, 같지 않으면 1
            }
            // 패배
            else {
                result = "패배";
                count--; // 패배 했을 경우 보너스 점수 1점 차감
                winwin = 0; // 패배 했을 경우 winwin 초기화
            }

            // 결과 출력
            System.out.println(result + "- 사용자 : " + userInput + ", 컴퓨터 : " + cpuInput[cpunum]);
            System.out.println("현재 점수 : " + count + "점");
        }
    }
}
