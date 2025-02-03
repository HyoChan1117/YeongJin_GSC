package Prep.Learning.CommentVariableConstant;

import java.util.Scanner;

public class ASCIICode {
    public static void main(String[] args) {

        // 문자 A ~ z 문자 한 개를 입력 받아,
        // 대문자는 소문자로, 소문자는 대문자로 출력하는 프로그램을 작성
        // 예시1 : 'a' -> 'A'
        // 예시2 : 'D' -> 'd'
        Scanner sc = new Scanner(System.in);

        char charValue = sc.next().charAt(0);  // 입력 받은 문자열 중 0번째를 선택

        if (charValue >= 'A' && charValue <= 'Z'){
            charValue = (char)(charValue + 32);
        } else if (charValue >= 'a' && charValue <= 'z'){
            charValue = (char)(charValue - 32);

        System.out.println(charValue);

        }
    }

}
