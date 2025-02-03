package LearningContents.Operator;

public class LogicalOperator {
    public static void main(String[] args) {

        boolean isOpened = false;

        // 방문이 열려있다.
        isOpened = true;

        // 방문이 닫혀있다.
        isOpened = false;

        // 방문이 닫혀 있으면... 실행
        if (!isOpened) {
            System.out.println("Do something");
        }

    }
}
