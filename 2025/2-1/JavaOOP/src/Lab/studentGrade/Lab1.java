package Lab.studentGrade;

import java.util.Scanner;

class Student {
    // ID, 이름, 국어, 영어, 수학, 합계점수, 평균
    int id;
    String name;
    private int scoreKorean;
    private int scoreEnglish;
    private int scoreMath;
    private int sum;
    private float avg;

    Student(int argId, String argName) {
        id = argId;
        name = argName;
    }

    boolean setScore(int argKorean, int argEnglish, int argMath) {
        if (argKorean < 0 || argEnglish < 0 || argMath < 0) {
            return false;
        }

        if (argKorean > 100 || argEnglish > 100 || argMath > 100) {
            return false;
        }

        scoreKorean = argKorean;
        scoreEnglish = argEnglish;
        scoreMath = argMath;

        return true;
    }

    int getScoreKorean() {
        return scoreKorean;
    }

    int getScoreEnglish() {
        return scoreEnglish;
    }

    public int getScoreMath() {
        return scoreMath;
    }

    int getSum() {
        sum = scoreKorean + scoreEnglish + scoreMath;
        return sum;
    }

    float getAvg() {
        avg = (float) getSum() / 3;
        return avg;
    }
}

class StdScoreMgr {
    Student[] stdList;
    int numOfStudents;

    StdScoreMgr(int argNumOfStudents) {
        stdList = new Student[argNumOfStudents];
        numOfStudents = argNumOfStudents;
    }

    void addStudent() {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < numOfStudents; i++) {

            System.out.println("ID 입력 : ");
            int stdId = sc.nextInt();

            System.out.println("이름 입력 : ");
            String stdName = sc.next();

            Student student = new Student(stdId, stdName);

            System.out.println("국어 성적 입력 : ");
            int scoreKorean = sc.nextInt();

            System.out.println("영어 성적 입력 : ");
            int scoreEnglish = sc.nextInt();

            System.out.println("수학 성적 입력 : ");
            int scoreMath = sc.nextInt();

            if (student.setScore(scoreKorean, scoreEnglish, scoreMath)) {
                stdList[i] = student;
            } else {
                System.out.println("점수가 유효하지 않습니다. 다시 입력하세요.");
                i--; // 다시 반복하도록 인덱스 감소
            }
        }
    }

    void printAllStudents() {
        System.out.println("\n--- 전체 학생 정보 ---");
        for (int i = 0; i < numOfStudents; i++) {
            Student s = stdList[i];
            if (s != null) {
                System.out.println("ID: " + s.id);
                System.out.println("이름: " + s.name);
                System.out.println("국어: " + s.getScoreKorean());
                System.out.println("영어: " + s.getScoreEnglish());
                System.out.println("수학: " + s.getScoreMath());
                System.out.println("합계: " + s.getSum());
                System.out.printf("평균: %.2f\n", s.getAvg());
                System.out.println("---------------------");
            }
        }
    }
}

public class Lab1 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("입력 학생 수: ");
        int stdNum = sc.nextInt();

        StdScoreMgr stdMgr = new StdScoreMgr(stdNum);
        stdMgr.addStudent();

        while (true) {
            System.out.println("\n--- 메뉴 선택 ---");
            System.out.println("1. 전체 학생 정보 출력");
            System.out.println("2. 종료");
            System.out.print("번호 선택: ");
            int choice = sc.nextInt();

            if (choice == 1) {
                stdMgr.printAllStudents();
            } else if (choice == 2) {
                System.out.println("프로그램을 종료합니다.");
                break;
            } else {
                System.out.println("잘못된 입력입니다. 다시 선택하세요.");
            }
        }

        sc.close();
    }
}
