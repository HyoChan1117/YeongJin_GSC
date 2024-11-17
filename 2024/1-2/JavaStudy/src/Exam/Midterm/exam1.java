package Exam.Midterm;

import java.util.Scanner;

public class exam1 {
    public static void main(String[] args) {

        // 슬롯머신 게임 구현하기

        Scanner sc = new Scanner(System.in);

        // 변수 초기화
        int slotnum = 3; // 슬롯머신 개수 변수
        int count = 1; // 게임 횟수 카운트 변수
        int score = 0; // 게임 점수 카운트 변수
        int slotItem = 0; // 연속된 연산자 저장 변수

        // 연산자 배열 생성
        // 세 가지 연산자(+, -, *)를 포함하는 char type 1차원 배열 생성
        // 랜덤 연산자를 저장할 1차원 배열 생성
        char operator[] = { '+', '-', '*' };
        char slotItems[] = new char[slotnum];

        // 무한 루프 -> 게임 한 판 당 반복 한 번
        while (true) {
            // 랜덤으로 선택된 3개의 연산자를 1차원 배열에 저장 -> 3번 반복으로 랜덤값을 저장해야 하기 때문에 for문 사용
            for (int i = 0 ; i < slotnum ; i++) {
                // 랜덤으로 연산자 선택
                int randnum = (int)(Math.random() * 3);
                // slotItem 배열에 값 저장
                slotItems[i] = operator[randnum];
            }

            // 게임 진행 상황 출력
            // A. 게임 횟수 출력
            // B. "게임을 시작하려면 아무 값이나 입력하세요" 문구 출력
            // 입력
            System.out.println(count + "번째 게임");
            System.out.print("게임을 시작하려면 아무 값이나 입력하세요.");
            sc.next();

            // -----------------------------------------------
            // C. 랜덤으로 선택된 3개의 연산자 출력
            // -----------------------------------------------
            System.out.println("-----------------------------------");
            for (int i = 0 ; i < slotnum ; i++) {
                System.out.print(slotItems[i] + "\t:\t");
            }
            System.out.println();
            System.out.println("-----------------------------------");

            int combo = 0; // 연속된 연산자 카운트 변수
            String result = ""; // 게임 결과 변수

            // 콤보 점수 계산
            // 슬롯머신에서 심볼이 연속해서 나오면 콤보 점수가 올라감
            for (int i = 0; i < slotItems.length - 1; i++) {
                // 연속된 연산자가 생길 경우 combo++
                if (slotItems[i] == slotItems[i + 1]) {
                    combo++;
                    // 연속된 변수 저장
                    slotItem = slotItems[i];
                }
            }

            // 만약 연속된 연산자가 없을 경우
            if (combo == 0) {
                System.out.println(); // 연속된 연산자가 없을 경우 공백 출력
            }
            // 만약 연속된 연산자가 있을 경우
            else {
                switch(slotItem){
                    // 연속된 연산자가 1개면 true, 2개면 false
                    case '+':
                        result = (combo == 1) ? "+ 2 combo - 보너스 점수 1점 획득" : "+ 3 combo - 보너스 점수 3점 획득";
                        score += (combo == 1) ? 1 : 3;
                        break;
                    case '-':
                        result = (combo == 1) ? "- 2 combo - 보너스 점수 1점 감점" : "- 3 combo - 보너스 점수 3점 감점";
                        score -= (combo == 1) ? 1 : 3;
                        break;
                    case '*':
                        result = (combo == 1) ? "* 2 combo - 보너스 점수 2점 획득" : "* 3 combo - 보너스 점수 5점 획득";
                        score += (combo == 1) ? 2 : 5;
                        break;
                }
                System.out.println(result); // 반환된 결과 출력
            }

            // 현재 점수 출력
            System.out.println("현재 점수 : " + score);

            // 게임 종료 조건
            // 점수가 5 이상이면 "승리" 메시지를 출력하고 종료
            // 점수가 -5 이하이면 "패배" 메시지를 출력하고 종료
            if (score >= 5 || score <= -5) {
                result = (score >= 5) ? "승리!" : "패배!";
                System.out.println(result + " 최종 점수 : " + score);
                break;
            }

            // 게임 출력 띄우기
            System.out.println();

            // 게임 횟수 카운트 +1
            count++;
        }
    }
}
