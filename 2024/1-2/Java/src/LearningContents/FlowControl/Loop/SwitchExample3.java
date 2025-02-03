package LearningContents.FlowControl.Loop;

import java.util.Scanner;

public class SwitchExample3 {
    public static void main(String[] args) {

        // 성적 [ A, B, C ], 출석 [ PASS, FAIL ]
        // 성적 A이고, 출석 PASS -> 전액 + 추가 장학금 출력
        // 성적 A이고, 출석 FAIL -> 전액
        // 성적 B이고, 출석 PASS -> 반액
        // 나머지는 장학금 없음

        String grade = "A";
        String attendance = "PASS";


        // 성적이 장학금을 선택하는데 중요한 요소이기 때문에 switch 안에는 grade 변수가 들어간다.
        String schilarship = switch (grade) {
            case "A" -> {
                // 성적 A이고, 출석 PASS -> 전액 + 추가 장학금 출력
                // 성적 A이고, 출석 FAIL -> 전액
                if (attendance.equals("PASS")) {
                    yield "전액 + 추가 장학금";
                }
                else {
                    yield "전액";
                }
            }
            case "B" -> {
                // 성적 B이고, 출석 PASS -> 반액
                if (attendance.equals("PASS")) {
                    yield "반액";
                }
                else {
                    yield "장학금 없음";
                }
            }
            case "C" -> "장학금 없음";  // 장학금 없음과 unknown을 구분하기 위해 했음
            default -> "unknown";
        };


    }
}