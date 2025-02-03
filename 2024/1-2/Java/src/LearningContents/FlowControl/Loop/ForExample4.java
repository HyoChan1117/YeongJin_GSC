package LearningContents.FlowControl.Loop;

public class ForExample4 {
    public static void main(String[] args) {

        int bar[] = new int[3];

        for (int i = 0, j = 10; i < bar.length ; i++, j += 10) {
            bar[i] = j;

        }

        // bar 1차원 배열(Array) 내 원소 값을 출력하는 코드를 작성하시오.
        // 10, 20, 30
        for (int i = 0 ; i < bar.length ; i++)
            System.out.print(bar[i] + " ");  // 10 20 30

    }
}