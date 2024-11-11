package Prep.Lab.StarPrint;

import java.util.Scanner;

public class Lab1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Lab1
        // 사용자로부터 M, N 정수를 입력 받아, M x N Matrix를 출력하세요.
        // 예) M : 3, N : 2
        // * *
        // * *
        // * *

        // 사용자로부터 M, N 정수를 입력 받는다.
        System.out.println("M, N 정수를 입력하세요: ");
        int M = sc.nextInt();
        int N = sc.nextInt();

        // Matrix
        // Record
        for (int i = 0 ; i < M ; i++) {
            // Field
            for (int j = 0 ; j < N ; j++) {
                System.out.print('*');
            }
            System.out.println();
        }
    }
}
