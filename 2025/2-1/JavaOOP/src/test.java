import java.util.Scanner;

class StuInfo {
    Scanner sc = new Scanner(System.in);

    // 멤버 변수
    int id;         // 학번
    int scoreKor;   // 국어 점수
    int scoreEng;   // 영어 점수
    int scoreMat;   // 수학 점수
    int sum;        // 합계 점수
    double avg;     // 평균 점수 (소수점 포함)

    // 학생 정보 입력 및 계산
    void inputInfo() {
        System.out.print("학번을 입력하세요: ");
        id = sc.nextInt();
        System.out.print("국어 점수를 입력하세요: ");
        scoreKor = sc.nextInt();
        System.out.print("영어 점수를 입력하세요: ");
        scoreEng = sc.nextInt();
        System.out.print("수학 점수를 입력하세요: ");
        scoreMat = sc.nextInt();

        sum = scoreKor + scoreEng + scoreMat;
        avg = sum / 3.0; // 평균은 소수점 포함
    }

    // 학생 정보 출력
    void prtInfo() {
        System.out.println("학번: " + id);
        System.out.println("국어: " + scoreKor + ", 영어: " + scoreEng + ", 수학: " + scoreMat);
        System.out.println("총점: " + sum + ", 평균: " + avg);
        System.out.println("---------------------------------");
    }
}

public class test {
    public static void main(String[] args) {
        // 학생 정보를 담을 배열 생성
        StuInfo[] students = new StuInfo[10];

        for (int i = 0; i < students.length; i++) {
            students[i] = new StuInfo(); // 새로운 객체 생성
            students[i].inputInfo();     // 정보 입력
        }

        System.out.println("\n학생 정보 출력:");
        for (StuInfo student : students) {
            student.prtInfo();
        }
    }
}
