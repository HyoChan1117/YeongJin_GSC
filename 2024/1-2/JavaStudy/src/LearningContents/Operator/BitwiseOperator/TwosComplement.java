package LearningContents.Operator.BitwiseOperator;

public class TwosComplement {
    public static void main(String[] args) {
        // 4비트에서 13과 10
        int a = 3;  // 13 in binary
        int b = 5;  // 10 in binary

        // 10의 1의 보수 계산
        int onesComplementB = ~b & 0b1111; // b의 1의 보수, 4비트 유지

        // 덧셈 수행 (13 + (~10))
        int result = a + onesComplementB + 1; // 1의 보수 계산 후 1 더함

        // 결과 출력 (오버플로우 처리)
        result = result & 0b1111; // 4비트 결과 유지
        System.out.println("Result (in 4 bits): " + Integer.toBinaryString(result));
    }
}
