package learningContents.component.classObjectInstance;

class Bar {
    // 멤버변수 -> 클래스 내 선언 된 변수
    //            객체 생성 시 객체마다 독립된 값을 유지
    String name;

    // 멤버 메서드 -> 함수처럼 .. 생겼으니깐!
    // 생성자 : 이름이 클래스명과 동일, 반환형이 없다.
    Bar(String argName) {
        name = argName;
    }

    // 멤버 메서드 -> 클래스 내 선언 된 함수
    //              해당 클래스에 필요한 함수를 구현
    void printInfo() {
        System.out.println(name);
    }
}

public class study5 {
    public static void main(String[] args) {
        Bar b1 = new Bar("Richard");
        b1.printInfo();
    }
}
