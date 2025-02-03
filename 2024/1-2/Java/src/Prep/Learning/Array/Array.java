package Prep.Learning.Array;

import java.util.Scanner;

public class Array {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // 키보드로부터 정수 N을 입력 받아,
        // N개의 int형 원소를 가지는 1차원 배열을 작성하시오.
        // 단 N 값은 1이상 10이하이며, 이외 값이 입력 될 경우 재입력 실시

        // 정수 N값 초기화
        int N = 0;

        // N이 1에서 10 사이일 때까지 반복한다.
        while (true) {
            // N값 입력
            System.out.print("정수 N 값을 입력 받는다.: ");
            N = scanner.nextInt();

            // 입력된 N이 1 이상 10 이하인지 검사한다.
            if (N >= 1 && N <= 10) {
                break;
            }
        }

        // N개의 배열을 생성한다.
        int[] array = new int[N];

        // 배열의 각 요소에 값을 입력 받는다.
        for (int i = 0 ; i < array.length ; i++) {
            System.out.println("배열 안에 넣을 원소를 입력 받는다: ");
            array[i] = scanner.nextInt();
        }

        // 입력된 배열 출력한다.
        for (int i : array) {
            System.out.print(i + " ");
        }
    }
}