package LearningContents.FlowControl.Loop;

public class ForExample1 {
    public static void main(String[] args) {

        // 1차원 배열(Array) 선언 -> 원소의 개수 5개
        int bar[] = new int[5];

        // bar 배열의 각 원소의 값을 초기화
        for(int iCount = 0, value = 1 ; iCount < bar.length ; iCount++, value *= 10) {
            bar[iCount] = value;
        }

        // bar 배열의 각 원소의 값을 출력
        for(int iCount = 0 ; iCount < bar.length ; iCount++) {
            System.out.println(bar[iCount]);
        }

    }
}
