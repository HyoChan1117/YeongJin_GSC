package Prep.RockPaperScissors;

import java.util.Scanner;

public class Game2 {
    public static void main(String[] args) {

        // 가위, 바위, 보 게임 만들기

        // 키보드로부타 Scissors, Rock, Paper를 입력받아,
        // 아래와 같이 결과를 출력하라
        // 예 1) 승리   - 사용자 : Scissors, 컴퓨터 : Paper
        // 예 2) 패배   - 사용자 : Scissors, 컴퓨터 : Rock
        // 예 3) 무승부  - 사용자 : Scissors, 컴퓨터 : Scissors

        // 고려사항
        // 1. 사용자로부터 입력 시 "Scissors, Rock, Paper" 이외 값은
        //    재입력 처리
        // 2. "Quit" 입력 전까지 계속해서 게임 실행
        // 3. 승리 시 보너스 포인트 1점 증가, 패배 시 보너스 포인트 1점 차감
        //    연속으로 승리 시 보너스 포인트 3점 추가
        // 4. 결과값 판별 후 현재 포인트 출력
        //    예) 현재포인트 : 1점
        // 5. 게임 종료 조건 추가
        //    사용자 포인트가 7점 이상 또는 -7점 이하이면 종료
        //     7점 이상이면 : "승리하였습니다. 축하합니다!"
        //     -7점 이하이면 : "패배하였습니다. 다음 기회에!"

        Scanner sc = new Scanner(System.in);

        // 포인트 count 변수 초기화
        int count = 0;
        int winwin = 0;

        // 연속 승리

        // 무한루프 -> 게임 한 판은 반복 한 번
        while (true){

            // 현재 포인트 출력
            System.out.println("현재 포인트: " + count + "점");

            // 포인트가 7점 이상이면 메세지 출력 후 승리
            if (count >= 7) {
                System.out.println("승리하였습니다. 축하합니다!");
                break;
            }
            // 포인트가 -7점 이하이면 메세지 출력 후 패배
            else if (count <= -7) {
                System.out.println("패배하였습니다. 다음 기회에!");
                break;
            }

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
                winwin = 0; // 무승부 시 초기화
            }

            // 승리
            else if ((inputValue == 0 && randCpu == 3) ||
                    (inputValue == 1 && randCpu == 0) ||
                    (inputValue == 2 && randCpu == 1)) {
                System.out.println("컴퓨터: " + cpuInput[randCpu] + " 승리입니다.");
                winwin++;

                // 연속 승리 했을 경우
                if (winwin >= 2){
                    count += 3;
                }
                // 1번 승리 했을 경우
                else {
                    count++;
                }
            }

            // 패배
            else {
                System.out.println("컴퓨터: " + cpuInput[randCpu] + " 패배입니다.");
                count--;
                winwin = 0; // 패배 시 초기화
            }

        }

    }
}
