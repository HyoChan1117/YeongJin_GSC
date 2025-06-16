package learningContents.component.lambdaClass.anonymousClass;

// 함수형 인터페이스는 메서드가 하나인 인터페이스
interface MathOperator {
    int operate(int a, int b);
}

public class LambdaExpress {
    public static void main(String[] args) {

        // 람다 표현식
        // 매개변수가 1개 있을 경우에는 ()가 생략될 수 있음
        // 매개변수 0개나 2개 이상 있을 경우에는 () 생략될 수 없음
        // 실행문이 1개 있을 경우에는 {}가 생략될 수 있음
        // 실행문이 2개 이상 있을 경우에는 {} 생략될 수 없음
        MathOperator opAdd = (a, b) -> a + b;
        MathOperator opMul = (a, b) -> a * b;

        System.out.println(opAdd.operate(1, 2));
        System.out.println(opMul.operate(1, 2));

    }
}