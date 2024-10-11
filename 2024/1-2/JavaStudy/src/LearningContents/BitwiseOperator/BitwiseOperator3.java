package LearningContents.BitwiseOperator;

public class BitwiseOperator3 {
    public static void main(String[] args) {

        int bar = 0b01001010111000100000000011111111;
        int mask = 0x00ff0000;

        int result = bar & mask;
        System.out.println(result);

    }
}
