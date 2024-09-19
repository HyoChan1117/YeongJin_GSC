package Baekjoon;

import java.util.Scanner;

public class Baekjoon1_8 {
    public static void main(String[] args) {

        // 스캐너 생성
        Scanner sc = new Scanner(System.in);

        // 사용자로부터 불기연도를 입력 받는다.
        int year = sc.nextInt();

        // 입력 받은 불기연도를 서기연도로 출력한다.
        System.out.println(year - 543);


    }
}
