package Lab.CommentVariableConstant;

public class Lab2 {
    public static void main(String[] args) {

        // byte 자료형의 최대값, 최소값을 나타내는 변수를 선언하고 초기화
        byte maxValue = 127;
        byte minValue = -128;

        // 최대값에는 1을 더하고, 최소값에는 1을 뺌
        maxValue++;  // -> maxValue에 1이 더해지면서 값이 128이 되고, 이 코드에서 overflow 발생
        minValue--;  // -> minValue에 1이 빼지면서 값이 -129가 되고, 이 코드에서 underflow 발생

        // 최대값에 1을 더한 변수와 최소값에 1을 뺀 변수를 출력
        System.out.println("오버플로우된 값: " + maxValue);
        System.out.println("언더플로우된 값: " + minValue);
    }
}
