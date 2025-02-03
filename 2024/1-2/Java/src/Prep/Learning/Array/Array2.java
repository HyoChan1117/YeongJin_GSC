package Prep.Learning.Array;

import java.util.Scanner;

public class Array2 {
    public static void main(String[] args) {

        // 키보드로부터 정수 N을 입력 받아 N개의 int 원소를 가지는 1차원 배열을 생성하라.
        // 만약 N 값이 0 이하 또는 10 초과일 경우 재입력
        // 만약 N 값이 0이하 또는 10 초과일 경우 재입력
        // 생성된 1차원 배열에 사용자로부터 값을 입력 받아 배열에 순차적으로 저장하라.
        // 만약 음의 정수 또는 0이 입력 될 경우 재입력
        // 현재 1차원 배열에 입력된 값을 역순으로 출력하라.

        Scanner sc = new Scanner(System.in);

        // 정수 N을 초기화
        int N = 0;

        // 키보드로부터 정수 N을 입력 받을 때, N의 값이 0 이하 또는 10 초과일 경우 무한루프
        while (true) {
            // 키보드로부터 정수 N을 입력 받는다.
            System.out.print("정수 N을 입력하세요: ");
            N = sc.nextInt();

            // N의 값이 0 이하 또는 10 초과일 경우 값을 재입력한다.
            if (N <= 0 || N > 10){
                System.out.println("값을 재입력하세요");
            }

            // 그 밖의 경우 반복문 종료
            else {
                break;
            }
        }

        // N개의 int 원소를 가지는 1차원 배열을 생성한다.
        int bar[] = new int[N];

        // 생성된 1차원 배열에 사용자로부터 값을 입력 받아 배열에 순차적으로 저장한다.
        for (int i = 0; i < bar.length; i++) {
            // 무한루프 -> 값으로 음의 정수 또는 0이 입력될 경우
            while(true) {
                System.out.print(i+1 + "번째 원소를 입력하세요: ");
                bar[i] = sc.nextInt();
                // 만약 음의 정수 또는 0이 입력 될 경우 재입력을 받는다.
                if (bar[i] <= 0){
                    System.out.println("값을 재입력하세요");
                }
                // 양의 정수일 경우 값을 저장하고 반복문 종료
                else {
                    break;
                }
            }
        }
        // 현재 1차원 배열에 입력된 값을 역순으로 출력
        for (int i = bar.length - 1 ; i >= 0; i--) {
            System.out.print(bar[i] + " ");
        }
    }
}