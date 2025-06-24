package learningContents.component.lambdaClass;

interface FunctionalInterface {
    float calculate(int a, int b);
}

public class LambdaExpress1 {
    public static void main(String[] args) {
        FunctionalInterface add = (a, b) -> a + b;
        FunctionalInterface sub = (a, b) -> a - b;
        FunctionalInterface mul = (a, b) -> a * b;
        FunctionalInterface div = (a, b) -> a / b;

        System.out.println(add.calculate(3, 4));
        System.out.println(sub.calculate(3, 4));
        System.out.println(mul.calculate(3, 4));
        System.out.println(div.calculate(6, 3));
    }
}