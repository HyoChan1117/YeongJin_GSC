package Baekjoon;

import java.util.Scanner;

public class Baekjoon1_3 {
    public static void main(String[] args) {
        // 스캐너 객체 생성
        Scanner sc = new Scanner(System.in);

        // 두 정수를 띄어쓰기로 입력 받기
        int A = sc.nextInt();
        int B = sc.nextInt();

        // 두 수의 합 출력
        System.out.println(A - B);

    }
}
