package LearningContents.Operator.PrePostOperator;

public class PrePostOperator1 {
    public static void main(String[] args) {

        int bar = 2;

        System.out.println(bar++);
        System.out.println(++bar);


    //    bar++; // bar = bar + 1, 후위(Post) 연산
    //    System.out.println(bar); // 3

    //    bar--; // bar = bar - 1, 후위(Post) 연산
    //    System.out.println(bar); // 2

    //    ++bar; // bar = bar + 1, 전위(Prep.Pre) 연산
    //    System.out.println(bar); // 3

    //    --bar; // bar = bar - 1, 전위(Prep.Pre) 연산
    //    System.out.println(bar); // 2

    }
}
