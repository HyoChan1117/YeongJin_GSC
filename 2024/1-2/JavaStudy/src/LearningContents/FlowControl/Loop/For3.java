package LearningContents.FlowControl.Loop;

public class For3 {
    public static void main(String[] args) {

        // i 라는 변수는 반복문이 종료되는 순간 사라짐
        for(int i = 0 ; i < 10 ; i++){
            System.out.println(i);
        }

        // i 라는 변수를 다시 선언할 수 있는 이유 : 반복문이 종료되는 순간 i 변수는 사라지기 때문
        for(int i = 0 ; i < 10 ; i++){
            System.out.println(i);
        }
    }
}
