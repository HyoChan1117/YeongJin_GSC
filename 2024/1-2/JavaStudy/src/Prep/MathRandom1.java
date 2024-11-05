package Prep;

import java.util.Scanner;

public class MathRandom1 {
    public static void main(String[] args) {

        // 사용자로부터 배열 크기 N을 입력받아,
        // N개의 정수를 저장할 수 있는 1차원 배열을 생성하라.
        // 단, N이 0 또는 음수이면 재입력을 요구한다.

        // 사용자로부터 난수 범위를 지정할 start, end 값을 입력받아,
        // start <= 난수 값 <= end 범위의 난수를 생성하여 배열에 저장하라.
        // 단, (end - start + 1) 값이 배열의 크기 N보다 작을 경우
        // 다시 입력을 요구한다.
        // 예) N = 5 -> 5개의 원소를 가지는 1차원 배열 생성
        //     start = 10, end = 12 -> 배열 원소는 10, 11, 12 중 하나의 값이어야 함

        // 생성된 배열의 모든 원소 값을 출력하라.

        Scanner sc = new Scanner(System.in);

        // Step1
        // 정수 N을 초기화
        int N = 0;

        // N이 0 또는 음수이면 재입력을 받는다. -> 무한루프
        while (true){
            // 사용자로부터 배열의 크기 N을 입력 받는다.
            System.out.print("정수 N을 입력 받는다: ");
            N = sc.nextInt();

            // N이 양수이면 반복문을 종료한다.
            if (N > 0){
                break;
            }
        }

        // N개의 정수를 저장할 수 있는 1차원 배열을 생성한다.
        int bar[] = new int[N];

        // Step2
        // (end - start + 1)의 값이 배열의 크기 N보다 작을 경우 재입력을 받는다. -> 무한루프
        // 정수 start, end 값 초기화
        int start = 0;
        int end = 0;

        while (true) {
            // 사용자로부터 난수의 범위를 지정할 start, end 값을 입력 받는다.
            System.out.print("start 값을 입력하세요: ");
            start = sc.nextInt();

            System.out.print("end 값을 입력하세요: ");
            end = sc.nextInt();

            // (end - start + 1)의 값이 배열의 크기 N보다 크거나 같을 경우 반복문 종료
            if (end - start + 1 >= N) {
                break;
            }

            // 조건에 만족하지 못했을 경우
            System.out.println("배열의 크기보다 큰 범위를 입력하세요");
        }

        // N개의 정수를 저장할 수 있는 1차원 배열에 원소를 랜덤으로 받는다.
        for (int i = 0; i < bar.length ; i++) {
            int randValue = (int)((Math.random() * (end - start + 1)) + start);
            bar[i] = randValue;
        }


        // 생성된 배열의 모든 원소 값을 출력한다.
        for (int value : bar){
            System.out.print(value + " ");
        }
    }
}