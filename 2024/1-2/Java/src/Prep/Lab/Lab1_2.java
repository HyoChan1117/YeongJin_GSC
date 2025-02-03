package Prep.Lab;

import java.util.Scanner;

public class Lab1_2 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        // 사용자로부터 세 변의 길이를 입력 받는다.
        System.out.println("세 변의 길이를 입력하세요:");
        int length1 = sc.nextInt();
        int length2 = sc.nextInt();
        int length3 = sc.nextInt();

        String triangle = "";
        // 삼각형을 만들 수 있다.
        if (length1 + length2 > length3 && length2 + length3 > length1 && length3 + length1 > length2) {
            // 세 변이 모두 같은 경우: 정삼각형
            if (length1 == length2 && length2 == length3) {
                triangle = "정삼각형";
            }
            // 두 변의 길이가 같은 경우: 이등변삼각형
            else if (length1 == length2 || length2 == length3 || length3 == length1) {
                triangle = "이등변삼각형";
            }
            // 세 변의 길이가 모두 다른 경우: 부등변삼각형
            else {
                triangle = "부등변삼각형";
            }
        }
        // 삼각형을 만들 수 없다.
        else {
            triangle = "삼각형을 형성할 수 없습니다.";
        }

        // 결과를 출력한다.
        System.out.println(triangle);
    }
}
