package LearningContents.FlowControl.Selection;

public class Switch2 {
    public static void main(String[] args) {

        // case의 실행문이 동일하다면 이런 식으로 사용 가능
        // if - else와 비슷

        String day = "월요일";
        switch (day) {
            case "토요일":
            case "일요일":
                System.out.println("주말");
                break;
            // case "월요일": case "화요일": case "수요일": case "목요일": case "금요일":
            default:
                System.out.println("평일");
        }

        // switch문에서 {}를 사용하는 이유: Switch문의 시작과 끝을 명확하게 하기 위해
        // switch문에서 사용할 수 있는 자료형: int, String, char(0과 양의 정수이기 때문에 가능)
    }
}