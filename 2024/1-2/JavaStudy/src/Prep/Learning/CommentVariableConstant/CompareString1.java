package Prep.Learning.CommentVariableConstant;

import java.util.Scanner;

public class CompareString1 {
    public static void main(String[] args) {


        // 문자 두 개를 각각 키보드로부터 입력 받아
        // 문자열 값이 같으면 "참" 아니면 "거짓"을 출력
        // 예시1 : "hello", "hello" -> "참"
        // 예시2 : "hello", "world" -> "거짓"

        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        if (str.equals("hello")) {
            System.out.println("참");
        }
        else {
            System.out.println("거짓");
        }
    }

}
