package Exam.Midterm.test2;

public class calculate {
    public static void main(String[] args) {

        // 변수 초기화
        char slotItems[] = { '-', '-', '+', '-', '-' };
        int combo = 1; // 콤보 변수
        int groupScore = 0; // 라운드 점수 카운트

        // 점수 계산
        for (int i = 0 ; i < slotItems.length ; i++) {
            // 연산자가 연속되는 경우
            if (i < slotItems.length - 1 && slotItems[i] == slotItems[i + 1]) {
                combo++;
            }
            // 연속이 끝났을 경우 계산
            else {
                // 연속된 문자 수 -> 2
                if (combo == 2) {
                    switch (slotItems[i]) {
                        case '+':
                            groupScore++;
                            break;
                        case '-':
                            groupScore--;
                            break;
                        case '*':
                            groupScore += 2;
                            break;
                    }
                }
                // 연속된 문자 수 -> 3
                else if (combo >= 3) {
                    switch (slotItems[i]) {
                        case '+':
                            groupScore += 3;
                            break;
                        case '-':
                            groupScore -= 3;
                            break;
                        case '*':
                            groupScore += 5;
                            break;
                    }
                }
                groupScore = 0; // groupScore 초기화
                combo = 1; // combo 변수 초기화
            }
        }
        System.out.println("GroupScore: " + groupScore);

    }
}
