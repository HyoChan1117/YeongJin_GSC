package LearningContents.Operator.BitwiseOperator;

public class BitwiseOperator4 {
    public static void main(String[] args) {

        int bar = 0b010010101110001000000000010111011;

        // Get : 특정 자리의 비트 값 읽기
        //     - 비트 자리 수

        int bitPosition = 30; // bit 범위는 31 ~ 0
        int mask = 0b01000000000000000000000000000000;

        boolean result = (bar & mask) != 0;

        System.out.println(result);

    }
}
