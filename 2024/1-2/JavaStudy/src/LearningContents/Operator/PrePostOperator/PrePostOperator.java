package LearningContents.Operator.PrePostOperator;

public class PrePostOperator {
    public static void main(String[] args) {

        int[] numbers = {1, 2, 3, 4, 5, 6};
        int index = 0;

        // 1. 후위 증감 연산자 활용 예: 배열 요소 탐색(인덱스를 처리할 때)
        System.out.println("후위 증감 연산자 활용 예:");

        // 배열을 순차적으로 탐색하면서 값을 출력
        while (index < numbers.length) {
            System.out.println("현재 요소(후위): " + numbers[index++]);
        }
    }
}
