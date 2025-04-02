import java.util.Scanner;

class SubjectInfo {
    String title;
    int score;
    SubjectInfo(String argTitle, int argScore) {
        title = argTitle;
        score = argScore;
    }
    SubjectInfo() {}
}

class Student1 {
    Scanner sc = new Scanner(System.in);

    int id;
    String name;
    private static String university = "영진";
    SubjectInfo[] subList;
    int sum;
    float avg;

    Student1(int subNum, String argName, int argId) {
        subList = new SubjectInfo[subNum];
        for(int i = 0; i < subNum; i++) {

            subList[i] = new SubjectInfo();
        }

        name = argName;
        id = argId;
    }

    int getSum() {
        sum = 0;
        for(SubjectInfo temp:subList){
            sum += temp.score;
        }
        return sum;
    }

    float getAvg() {
        avg = getSum() / subList.length;
        return avg;
    }
    static void prtUniversity() {
        System.out.println(university);
    }
    void setName(String argName) {
        name = argName;
    }
}

public class test3 {
    public static void main(String[] args) {

    }
}
