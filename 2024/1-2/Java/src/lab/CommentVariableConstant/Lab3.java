package lab.CommentVariableConstant;

public class Lab3 {
    public static void main(String[] args) {

        // 원의 반지름을 저장하는 double형의 변수를 선언하고, 값을 5.0으로 초기화
        double radius = 5.0;

        // 원주율을 상수로 선언하고, 그 값을 3.14159로 초기화
        final double PI = 3.14159;

        // 원의 반지름과 원주율을 사용하여 원 면적 구하기
        System.out.printf("원의 면적: %.2f", PI * radius * radius);

    }
}
