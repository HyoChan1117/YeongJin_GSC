package LearningContents.FlowControl.Selection;

public class Switch {
    public static void main(String[] args) {

        String myTeam = "samsung";

        switch (myTeam) {
            case "samsung":
                System.out.println("최강 삼성");
                break;

            case "lg":
                System.out.println("엘쥐 미안");
                break;

            default:
                System.out.println("이외 팀");
        }

    }
}