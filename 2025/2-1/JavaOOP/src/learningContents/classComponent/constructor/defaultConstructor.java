package learningContents.classComponent.constructor;

import java.util.Scanner;

// 클래스 생성
class Test {

    Scanner sc = new Scanner(System.in);

    // 멤버 변수 -> 클래스 내에서 정의한 변수
    // 객체의 상태를 나타냄
    String name;
    int age;

    // 생성자 -> 객체 생성 시 객체의 초기값 설정
    // 멤버 변수 초기화
    Test () {
    }

    // 멤버 메서드 -> 클래스 내에서 정의한 메서드
    // 객체의 동작을 정의
    void prtinf() {
        System.out.print("이름을 입력하세요: ");
        name = sc.nextLine();

        System.out.print("나이를 입력하세요: ");
        age = sc.nextInt();

        System.out.println("이름 : " + name + ", 나이 : " + age);
    }

}


public class defaultConstructor {
    public static void main(String[] args) {

        // 객체 생성
        Test test1 = new Test();

        // 객체 접근 -> '참조변수 + dot(.) + 멤버'를 사용해 특정 객체의 멤버에 접근할 수 있음
        test1.prtinf();

    }
}
