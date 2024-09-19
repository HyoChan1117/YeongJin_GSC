package Baekjoon;

import java.util.Scanner;

public class Baekjoon1_9 {
    public static void main(String[] args) {

        // 스캐너 생성
        Scanner sc = new Scanner(System.in);

        // 사용자로부터 3개의 정수를 입력 받는다.
        byte A = sc.nextByte();
        byte B = sc.nextByte();
        byte C = sc.nextByte();

        // 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
        System.out.println((A + B) % C);
        System.out.println(((A % C) + (B % C)) % C);
        System.out.println((A * B) % C);
        System.out.println(((A%C) * (B%C)) % C);

        sc.close();

    }
}
