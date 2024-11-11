package Prep.Lab.StarPrint;

import java.util.Scanner;

public class Lab2 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Lab2
        // 문제는 동일, 출력값 변경
        // 예) M : 3, N : 3
        //  **
        // * *
        // **

        // 사용자로부터 M, N 정수를 입력 받는다.
        System.out.println("M, N 정수를 입력하세요: ");
        int M = sc.nextInt();
        int N = sc.nextInt();

        // Matrix
        // Record
        for (int i = 0 ; i < M ; i++) {
            // Field
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    System.out.print(' ');
                }
                else {
                    System.out.print('*');
                }
            }
            System.out.println();
        }
    }
}
