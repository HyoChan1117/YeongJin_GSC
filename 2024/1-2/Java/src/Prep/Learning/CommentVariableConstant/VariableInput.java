package Prep.Learning.CommentVariableConstant;

import java.util.Scanner;

public class VariableInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 내가 입력 받으려는 변수의 자료형에 따라 메서드의 형태가 달라짐

        // short
        short barShort = sc.nextShort();

        // int
        int barInt = sc.nextInt();

        // long
        long barLong = sc.nextLong();

        // float
        float barFloat = sc.nextFloat();

        // double
        double barDouble = sc.nextDouble();

        // char
        char barChar = sc.next().charAt(0);  // -> next = String, charAt은 next()로 반환된 문자열에서 첫 번째 문자를 가져오기 위해 사용함

        // String
        String barString = sc.nextLine();

        // boolean
        boolean barBoolean = sc.nextBoolean();


        // 화면 출력
        System.out.print("world");
        System.out.println("hello");

        // next
        String bar = sc.next();

        // nextline
        String foo = sc.nextLine();
        System.out.print(foo);


    }

}
