package lab.CommentVariableConstant;

import java.util.Scanner;

public class Lab4 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // 사용자로부터 나이를 입력받고, 이를 int형 변수에 저장
        System.out.print("나이를 입력하세요: ");
        int age = sc.nextInt();

        // 사용자에게 몸무게를 입력받고, 이를 double형 변수에 저장
        System.out.print("몸무게를 입력하세요: ");
        double weight = sc.nextDouble();

        // 나이를 double로 명시적 형변환하여 몸무게와 더한 결과를 출력
        System.out.println("나이를 double로 변환한 후 몸무게와 더한 결과: " + ((double) age + weight));

        // 몸무게를 int로 명시적 형변환하여 나이와 더한 결과를 출력
        System.out.println("몸무게를 int로 변환한 후 나이와 더한 결과: " + ((int) weight + age));

    }
}
