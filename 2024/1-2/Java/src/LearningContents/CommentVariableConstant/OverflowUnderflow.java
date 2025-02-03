package LearningContents.CommentVariableConstant;

public class OverflowUnderflow {
    public static void main(String[] args) {

        // byte -> 1 byte -> 8 bits -> 2^8
        // -> 256 -> -128 ~ 127
        // 최대값 : 127
        // 최소값 : -128
        byte bar = 127; // overflow
        bar++;  // bar = bar + 1
        System.out.println(bar);

        bar = -128; // underflow
        bar--;  // bar = bar - 1
        System.out.println(bar);

        long pos = 2147483647 + 2; // -> 2147483647 + 2 => int형 + int형 : int형 출력 -> Overflow 발생
        System.out.println(pos);

        pos = 2147483647L + 2L;  // -> 2147483647L + 2L => long형 + long형 : long형 출력
        System.out.println(pos);

        pos = (long)(2147483647 + 2); // -> (long)(2147483647 + 2) => 이미 Overflow 발생한 것에 long으로 자료형이 바뀜
        System.out.println(pos);


    }
}
