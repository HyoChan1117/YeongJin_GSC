package Exam.Midterm;

public class test1 {
    public static void main(String[] args) {

        char slotItems[] = { '-', '-', '*'};
        int slotItem = 0; //
        int combo = 0; // 연속된 연산자 카운트 변수
        int score = 0; // 현재 점수 카운트 변수
        String result = "";

        // 콤보 점수 계산
        // 슬롯머신에서 심볼이 연속해서 나오면 콤보 점수가 올라감
        for (int i = 0; i < slotItems.length - 1; i++) {
            // 연속된 연산자가 생길 경우 combo++
            if (slotItems[i] == slotItems[i + 1]) {
                combo++;
                // 연속된 변수 저장
                slotItem = slotItems[i];
            }
        }
        // 만약 연속된 연산자가 2개일 경우
        if (combo == 1 || combo == 2) {
            switch(slotItem){
                // 연속된 연산자가 1개면 true, 2개면 false
                case '+':
                    result = (combo == 1) ? "+ 2 combo - 보너스 점수 1점 획득" : "+ 3 combo - 보너스 점수 3점 획득";
                    break;
                case '-':
                    result = (combo == 1) ? "- 2 combo - 보너스 점수 1점 감점" : "- 3 combo - 보너스 점수 3점 감점";
                    break;
                case '*':
                    result = (combo == 1) ? "* 2 combo - 보너스 점수 2점 획득" : "* 3 combo - 보너스 점수 5점 획득";
                    break;
                default:
                    System.out.println(); // 연속된 연산자가 없을 경우 공백 출력
            }
        }
        System.out.println(result); // 반환된 결과 출력
    }
}
