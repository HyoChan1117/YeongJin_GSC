package LearningContents.FlowControl.Loop;

public class ForExample {
    public static void main(String[] args) {

        char bar = 33;

        System.out.println(bar);  // 출력: !

        // Z ~ A를 출력 하시오
        for (char chValue = 'Z'; chValue >= 'A'; chValue--) {
            System.out.print(chValue);
        }

        // 출력 값을 다른 줄에 띄우기 위해
        System.out.println();

        // Z ~ A를 출력 하시오
        // 하나씩 건너 뛰어서 출력
        for (char chValue = 'Z'; chValue >= 'A'; chValue -= 2){
            System.out.print(chValue);
        }

    }
}
