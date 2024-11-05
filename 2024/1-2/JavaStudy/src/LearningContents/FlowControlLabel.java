package LearningContents;

public class FlowControlLabel {
    public static void main(String[] args) {

        int img[][][] = {
                {{100, 200}, {1, 78}},
                {{-1, -2}, {300, 0}},
                {{50, 70}, {7, 90}}
        };

        // Flag variable
        boolean isFound = false;

        bar:
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    System.out.print(img[i][j][k] + "\t");

                    if(img[i][j][k] == 78) {
                        isFound = true;
                        break bar;
                    }
                }
                System.out.println();
            }
            System.out.println("-----------------");

        }

        if(isFound) {
            System.out.println("78을 찾았습니다.");
        }
        else {
            System.out.println("78이 존재하지 않습니다.");
        }
    }
}
