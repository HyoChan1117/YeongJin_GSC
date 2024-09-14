package Baekjoon;

import java.util.Scanner;

public class Baekjoon1_6 {
    public static void main(String[] args) {

        // 스캐너 생성
        Scanner sc = new Scanner(System.in);

        // 두 자연수를 입력 받는다.
        int n = sc.nextInt();
        int m = sc.nextInt();

        // 두 자연수의 덧셈, 뺄셈, 곱셈, 나눗셈 값을 출력한다.
        System.out.println(n + m);
        System.out.println(n - m);
        System.out.println(n * m);
        System.out.println(n / m);
        System.out.println(n % m);
    }
}
