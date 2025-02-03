package LearningContents.Operator.BitwiseOperator;

public class BitwiseOperator5 {
    public static void main(String[] args) {

        int bar = 0b10010101110001000000000010111011;

        // Set
        int setPosition = 31;
        boolean value = false;

        int mask = 1 << 30;

        int result = bar | mask;

        System.out.println(Integer.toBinaryString(result));
    }
}