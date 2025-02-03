package LearningContents.FlowControl.Loop;

import java.util.Scanner;

public class SwitchExample1 {
    public static void main(String[] args) {

        // switch 문을 이용하여 아래 프로그램 작성
        // 키보드로부터 정수를 입력
        // 1 이면 Python 출력
        // 2 이면 Java 출력
        // 3 이면 C++ 출력
        // 4 이면 JavaScript 출력

        Scanner sc = new Scanner(System.in);

        // 정수 N을 초기화
        int N = 0;

        // 키보드로부터 정수 N을 입력 받는다.
        System.out.print("정수 N을 입력하세요: ");
        N = sc.nextInt();


        String result = "";

        // Switch문을 이용하여 값을 출력한다.
        switch (N) {
            case 1:
                result = "Python";
                break;
            case 2:
                result = "Java";
                break;
            case 3:
                result = "C++";
                break;
            case 4:
                result = "C#";
                break;
        }
        System.out.println(result);
    }
}
