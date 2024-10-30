package Prep;

import java.util.Scanner;

public class test1 {
    public static void main(String[] args) {
        // 키보드로부터 정수 N을 입력 받아,
        // N개의 int형 원소를 가지는 1차원 배열을 작성하시오.
        // 단 N 값은 1이상 10이하이며, 이외 값이 입력 될 경우 재입력 실시
        Scanner sc = new Scanner(System.in);

        // 정수 N 초기화
        int N = 0;

        // step1
        // 정수 N을 입력 받아, N의 범위가 1이상 10이하일 때까지 반복
        while (true) {
            System.out.print("정수 N값을 입력하세요: ");
            N = sc.nextInt();

            // N의 범위가 1이상 10이하이면 반복 종료
            if (N >= 1 && N <= 10) {
                break;
            }
        }


        // step2
        // N개의 int형 원소를 가지는 1차원 배열 생성
        int bar[] = new int[N];

        // 생성된 배열에 원소를 입력 받는다.
        for (int i = 0; i < bar.length; i++) {
            System.out.println("배열의 원소를 입력받는다: ");
            bar[i] = sc.nextInt();
        }

        // 만들어진 배열을 출력한다.
        for (int i : bar) {
            System.out.print(i + " ");
        }

        // 배열 내 전체 원소 중 최대값과 최소값을 출력하고,
        // 평균 값을 출력하라.
        // [3, 10, 100, 0]
        // 최대값 : 100, 최소값 : 0
        // 평균값 : (3 + 10 + 100 + 0)/4
        int minValue = bar[0];
        int maxValue = bar[0];
        int sum = 0;

        for(int value : bar){
            // 최대값
            if (value > maxValue) {
                maxValue = value;
            }

            // 최소값
            if (value < minValue) {
                minValue = value;
            }

            // 누적값
            sum += value;
        }

        // 평균 계산
        float avg = ((float)sum) / bar.length;

        // 출력
        System.out.println("최대값 : " + maxValue);
        System.out.println("최소값 : " + minValue);
        System.out.printf("평균 : %.2f", avg);


    }
}
